# Display Proposal for `slicer.util.pip_install_with_progress`

## Overview

This proposal addresses the **display** problem: how to show users meaningful feedback during pip install operations. We introduce a new function `pip_install_with_progress()` that builds on the non-blocking infrastructure from the blocking-prevention proposal.

## Design Goals

1. **Visual feedback**: Users see that something is happening (progress bar, status text)
2. **Transparency**: Full pip output available in collapsible details section
3. **Consistent error handling**: Failed installations show the log before raising exception
4. **Backward compatible**: Existing `pip_install()` unchanged; new function is opt-in
5. **Testing-friendly**: Progress dialog skipped in testing mode

## Why a New Function (Not Extending `pip_install`)

We considered adding a `show_progress` parameter to `pip_install()` directly, but decided against it for these reasons:

1. **Separation of concerns**: `pip_install()` is the low-level building block (can be blocking or non-blocking, with callbacks). `pip_install_with_progress()` is the high-level user-facing wrapper that provides a complete UX.

2. **Different return semantics**:
   - `pip_install(blocking=False)` returns immediately (async)
   - `pip_install_with_progress()` always waits for completion (sync from caller's perspective, but UI stays responsive)

   Mixing these in one function with a `show_progress` flag would be confusing.

3. **Modal dialog implies different usage context**: When you want a progress dialog, you're in a "user-initiated action" context (like `onApplyButton`). When you just want to install quietly, you're in a different context. Different functions for different contexts.

4. **Follows existing Slicer patterns**: Slicer has `confirmOkCancelDisplay()` vs `messageBox()` - higher-level convenience functions built on lower-level ones.

5. **Keeps `pip_install` simple**: The low-level function stays focused on one job. Users who need custom progress UI can use `pip_install(blocking=False, logCallback=...)` directly.

---

## New Function: `slicer.util.pip_install_with_progress()`

### Signature

```python
def pip_install_with_progress(
    requirements,
    show_progress: bool = True,
    requester: str | None = None,
    parent=None,
):
    """Install Python packages with a progress dialog.

    This is a high-level wrapper around pip_install() that provides visual feedback
    during installation. The UI remains responsive while pip runs in the background.

    Args:
        requirements: Requirement specifier (string or list), same as pip_install().
        show_progress: If True (default), show modal progress dialog with status
            and collapsible log details. If False, just show busy cursor.
        requester: Name shown in dialog title (e.g., "MyExtension").
        parent: Parent widget for the dialog.

    Raises:
        subprocess.CalledProcessError: If pip installation fails. Before raising,
            an error dialog is shown with the full pip log in expandable details.

    When the application is running in testing mode (slicer.app.testingEnabled()),
    the progress dialog is skipped and installation proceeds with console output only.

    Example::

        # Simple usage
        slicer.util.pip_install_with_progress("pandas scipy")

        # With requester name in title
        slicer.util.pip_install_with_progress(
            "scikit-image>=0.21",
            requester="MyExtension"
        )

        # Quiet mode (busy cursor only)
        slicer.util.pip_install_with_progress("requests", show_progress=False)

    """
```

### Implementation

```python
def pip_install_with_progress(requirements, show_progress=True, requester=None, parent=None):
    """Install Python packages with a progress dialog."""
    import threading
    from subprocess import CalledProcessError

    import qt
    import slicer

    # In testing mode, skip UI and use simple blocking install
    if slicer.app.testingEnabled():
        import logging
        logging.info("Testing mode is enabled: skipping progress dialog for pip_install")
        pip_install(requirements)  # blocking mode, raises on failure
        return

    if not show_progress:
        # Simple case: just busy cursor with blocking install
        qt.QApplication.setOverrideCursor(qt.Qt.BusyCursor)
        try:
            pip_install(requirements)  # blocking mode
        finally:
            qt.QApplication.restoreOverrideCursor()
        return

    # Create the progress dialog
    dialog = _PipProgressDialog(requester=requester, parent=parent)
    dialog.show()
    slicer.app.processEvents()  # Ensure dialog is displayed

    completed = threading.Event()
    result = {"returnCode": None, "log": ""}

    def onLog(line):
        dialog.appendLog(line)
        dialog.updateStatus(line)
        print(line)  # Still log to console

    def onComplete(returnCode):
        result["returnCode"] = returnCode
        result["log"] = dialog.getFullLog()
        completed.set()

    pip_install(requirements, blocking=False, logCallback=onLog, completedCallback=onComplete)

    # Wait for completion while keeping UI responsive
    while not completed.is_set():
        slicer.app.processEvents()

    dialog.close()

    if result["returnCode"] != 0:
        slicer.util.errorDisplay(
            "Package installation failed.",
            windowTitle=f"{requester} - Installation Failed" if requester else "Installation Failed",
            detailedText=result["log"]
        )
        raise CalledProcessError(result["returnCode"], "pip install")
```

---

## New Internal Class: `_PipProgressDialog`

```python
class _PipProgressDialog(qt.QDialog):
    """Modal dialog showing pip installation progress with collapsible log details."""

    def __init__(self, requester=None, parent=None):
        import ctk
        import qt
        import slicer

        super().__init__(parent or slicer.util.mainWindow())
        self.setModal(True)
        self.setWindowTitle(
            f"{requester} - Installing Python Packages" if requester else "Installing Python Packages"
        )
        # Prevent closing via X button or Escape
        self.setWindowFlags(self.windowFlags() & ~qt.Qt.WindowCloseButtonHint)

        layout = qt.QVBoxLayout(self)

        # Status label
        self.statusLabel = qt.QLabel("Preparing installation...")
        layout.addWidget(self.statusLabel)

        # Indeterminate progress bar
        self.progressBar = qt.QProgressBar()
        self.progressBar.setRange(0, 0)  # Indeterminate mode
        layout.addWidget(self.progressBar)

        # Collapsible details section
        self.detailsButton = ctk.ctkCollapsibleButton()
        self.detailsButton.text = "Details"
        self.detailsButton.collapsed = True
        detailsLayout = qt.QVBoxLayout(self.detailsButton)

        self.logText = qt.QPlainTextEdit()
        self.logText.setReadOnly(True)
        self.logText.setMinimumHeight(150)
        self.logText.setMaximumHeight(300)
        # Use monospace font for log output
        font = qt.QFont("Monospace")
        font.setStyleHint(qt.QFont.TypeWriter)
        self.logText.setFont(font)
        detailsLayout.addWidget(self.logText)

        layout.addWidget(self.detailsButton)

        # Set reasonable default size
        self.resize(500, 120)

        # Store log lines for retrieval
        self._logLines = []

    def appendLog(self, line):
        """Append a line to the log display."""
        self._logLines.append(line)
        self.logText.appendPlainText(line)
        # Auto-scroll to bottom
        scrollBar = self.logText.verticalScrollBar()
        scrollBar.setValue(scrollBar.maximum())

    def getFullLog(self):
        """Return the complete log as a string."""
        return "\n".join(self._logLines)

    def updateStatus(self, line):
        """Parse pip output to show friendly status message."""
        line_lower = line.lower()
        if "collecting" in line_lower:
            # Extract package name if possible
            parts = line.split()
            if len(parts) >= 2:
                self.statusLabel.setText(f"Collecting {parts[1]}...")
            else:
                self.statusLabel.setText("Collecting packages...")
        elif "downloading" in line_lower:
            self.statusLabel.setText("Downloading...")
        elif "installing collected packages" in line_lower:
            self.statusLabel.setText("Installing packages...")
        elif "successfully installed" in line_lower:
            self.statusLabel.setText("Finalizing...")
        elif "requirement already satisfied" in line_lower:
            parts = line.split()
            if len(parts) >= 4:
                self.statusLabel.setText(f"Already installed: {parts[3]}")

    def reject(self):
        """Prevent dialog from being closed by Escape key."""
        pass  # Do nothing - installation cannot be cancelled
```

---

## Summary of All Changes

| Component | Type | Description |
|-----------|------|-------------|
| `pip_install_with_progress()` | New function | High-level wrapper with progress UI |
| `_PipProgressDialog` | New class | Modal dialog with progress bar and collapsible log |
| `pip_install()` | Modified | Add `blocking`, `logCallback`, `completedCallback` params (from blocking-prevention proposal) |
| `_executePythonModule()` | Modified | Pass through new params (from blocking-prevention proposal) |
| `launchConsoleProcess()` | Modified | Add non-blocking mode (from blocking-prevention proposal) |
| `_startAsyncProcessHandling()` | New function | QTimer-based async handling (from blocking-prevention proposal) |

---

## UI Behavior Summary

| Scenario | Progress Bar | Status Label | Details Panel | Busy Cursor | Console Output |
|----------|-------------|--------------|---------------|-------------|----------------|
| `show_progress=True` | Indeterminate | Updates with phase | Collapsible, shows full log | No (dialog is enough) | Yes |
| `show_progress=False` | No | No | No | Yes | Yes |
| Testing mode | No | No | No | No | Yes |
| On failure | N/A | N/A | Error dialog with full log | No | Yes |

---

## Comparison with Alternatives

### Alternative 1: Add `show_progress` to `pip_install()` directly

```python
pip_install(requirements, show_progress=True)
```

| Aspect | Assessment |
|--------|------------|
| **Simplicity for users** | Slightly simpler (one function to remember) |
| **API clarity** | Confusing - mixes low-level and high-level concerns |
| **Return semantics** | Problematic - `blocking=False` + `show_progress=True` unclear |
| **Backward compatibility** | Same |

**Rejected because**: Mixing async callbacks with modal dialogs in one function is confusing.

### Alternative 2: Context manager approach (like SlicerKonfAI)

```python
with pip_progress_dialog("Installing..."):
    pip_install(requirements)
```

| Aspect | Assessment |
|--------|------------|
| **Flexibility** | High - can wrap any code |
| **Log capture** | Difficult - pip_install blocks, no log streaming |
| **UI responsiveness** | Poor - still blocking |

**Rejected because**: Can't capture streaming log output or keep UI responsive.

### Alternative 3: Determinate progress bar (like SlicerNeuro)

Install packages one at a time to show X of Y progress.

| Aspect | Assessment |
|--------|------------|
| **Progress accuracy** | Better (shows package count) |
| **Performance** | Worse (can't batch installs, repeated pip invocations) |
| **Dependency resolution** | Problematic (pip resolves dependencies across all packages) |

**Rejected because**: Installing one package at a time breaks pip's dependency resolution and is slower.

### Chosen Approach: Separate function with indeterminate progress

| Aspect | Assessment |
|--------|------------|
| **API clarity** | Clear - separate function for separate concern |
| **Log capture** | Full streaming via `logCallback` |
| **UI responsiveness** | Excellent - QTimer-based async |
| **Progress accuracy** | Indeterminate (honest about not knowing %) |
| **Error handling** | Complete - shows log on failure |

---

## Dependencies

This proposal depends on the **blocking-prevention proposal** which adds:
- `blocking` parameter to `pip_install()`
- `logCallback` and `completedCallback` parameters
- QTimer-based async infrastructure

---

## Testing Considerations

1. **Unit tests**: Mock `pip_install` to test dialog behavior
2. **Integration tests**: Run in testing mode (dialog skipped, falls back to blocking)
3. **Manual testing**: Verify dialog appears, log streams, error dialog shows on failure

The testing mode bypass ensures automated tests don't hang on modal dialogs while still exercising the underlying installation logic.
