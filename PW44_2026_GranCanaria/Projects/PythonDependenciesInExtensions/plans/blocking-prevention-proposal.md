# Blocking Prevention Proposal for `slicer.util.pip_install`

## Overview

This proposal addresses the **blocking-prevention** problem: how to keep the Slicer UI responsive during pip install operations. We adopt a QTimer-based polling approach inspired by SlicerMONAIAuto3DSeg, modified to fit into Slicer's existing utility functions.

## Design Goals

1. **Backward compatible**: Existing code using `pip_install()` continues to work unchanged
2. **Fully non-blocking option**: Main thread is free, Qt event loop runs normally
3. **Output still captured**: All pip output is logged to Python console as before
4. **Flexible API**: Callers can provide callbacks for custom handling
5. **Opt-in complexity**: Simple use cases stay simple

## Functions to Modify

### 1. `slicer.util.launchConsoleProcess()` (lines 3879-3919)

**Current signature:**
```python
def launchConsoleProcess(args, useStartupEnvironment=True, updateEnvironment=None, cwd=None):
```

**Proposed signature:**
```python
def launchConsoleProcess(args, useStartupEnvironment=True, updateEnvironment=None, cwd=None,
                         blocking=True, logCallback=None, completedCallback=None):
```

**New parameters:**
- `blocking` (bool, default=True): If False, return immediately and process output asynchronously
- `logCallback` (callable, optional): Called with each line of output. Signature: `logCallback(line: str) -> None`
- `completedCallback` (callable, optional): Called when process completes. Signature: `completedCallback(returnCode: int) -> None`

**Proposed implementation:**

```python
def launchConsoleProcess(args, useStartupEnvironment=True, updateEnvironment=None, cwd=None,
                         blocking=True, logCallback=None, completedCallback=None):
    """Launch a process. Hiding the console and captures the process output.

    The console window is hidden when running on Windows.

    :param args: executable name, followed by command-line arguments
    :param useStartupEnvironment: launch the process in the original environment
    :param updateEnvironment: map containing optional additional environment variables
    :param cwd: current working directory
    :param blocking: If True (default), return the process object for use with logProcessOutput().
        If False, process output asynchronously using a background thread and QTimer polling.
        The main thread remains free and the Qt event loop runs normally.
    :param logCallback: When blocking=False, called with each line of output.
        If None, output is printed to console (same as blocking mode).
    :param completedCallback: When blocking=False, called when process completes.
        Receives the return code as argument. If the process failed (non-zero return code)
        and no completedCallback is provided, a CalledProcessError is logged.
    :return: process object.

    Blocking mode example (unchanged from before)::

      proc = slicer.util.launchConsoleProcess(args)
      slicer.util.logProcessOutput(proc)

    Non-blocking mode example::

      def onLog(line):
          print(f"[pip] {line}")

      def onComplete(returnCode):
          if returnCode == 0:
              print("Installation complete!")
          else:
              print(f"Installation failed with code {returnCode}")

      slicer.util.launchConsoleProcess(
          args,
          blocking=False,
          logCallback=onLog,
          completedCallback=onComplete
      )
      # Returns immediately, UI stays responsive

    """
    import subprocess
    import os

    # ... existing environment setup code unchanged ...

    if os.name == "nt":
        info = subprocess.STARTUPINFO()
        info.dwFlags = 1
        info.wShowWindow = 0
        proc = subprocess.Popen(args, env=startupEnv, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, universal_newlines=True,
                                startupinfo=info, cwd=cwd)
    else:
        proc = subprocess.Popen(args, env=startupEnv, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, universal_newlines=True, cwd=cwd)

    if blocking:
        return proc  # Caller will use logProcessOutput() as before

    # Non-blocking mode: start background thread and QTimer polling
    _startAsyncProcessHandling(proc, logCallback, completedCallback)
    return proc
```

### 2. New helper function `_startAsyncProcessHandling()` (new)

This is the core of the non-blocking implementation:

```python
def _startAsyncProcessHandling(proc, logCallback=None, completedCallback=None):
    """Start asynchronous handling of process output using a background thread and QTimer.

    Internal function used by launchConsoleProcess when blocking=False.

    :param proc: subprocess.Popen object
    :param logCallback: Called with each line of output, or None for default console printing
    :param completedCallback: Called when process completes with return code
    """
    import threading
    import queue
    from subprocess import CalledProcessError

    import qt

    outputQueue = queue.Queue()
    CHECK_INTERVAL_MS = 100  # Poll every 100ms for responsive UI

    def readOutputThread():
        """Background thread: read stdout and put lines into queue."""
        while True:
            try:
                line = proc.stdout.readline()
                if not line:
                    break
                outputQueue.put(("line", line.rstrip()))
            except UnicodeDecodeError:
                # Same handling as logProcessOutput - ignore decode errors
                pass
        proc.wait()
        outputQueue.put(("done", proc.returncode))

    def checkOutput():
        """Main thread: poll queue and process available output."""
        while True:
            try:
                msgType, data = outputQueue.get_nowait()
                if msgType == "line":
                    if logCallback:
                        logCallback(data)
                    else:
                        # Default behavior: print to console (matches blocking mode)
                        print(data)
                elif msgType == "done":
                    returnCode = data
                    if completedCallback:
                        completedCallback(returnCode)
                    elif returnCode != 0:
                        # No callback provided and process failed - log the error
                        import logging
                        logging.error(f"Process failed with return code {returnCode}: {proc.args}")
                    return  # Stop polling
            except queue.Empty:
                break

        # Process still running or output still being read - reschedule
        qt.QTimer.singleShot(CHECK_INTERVAL_MS, checkOutput)

    # Start background thread
    thread = threading.Thread(target=readOutputThread, daemon=True)
    thread.start()

    # Start polling from main thread
    qt.QTimer.singleShot(0, checkOutput)
```

### 3. `slicer.util._executePythonModule()` (lines 3957-3988)

**Current signature:**
```python
def _executePythonModule(module, args):
```

**Proposed signature:**
```python
def _executePythonModule(module, args, blocking=True, logCallback=None, completedCallback=None):
```

**Proposed implementation:**

```python
def _executePythonModule(module, args, blocking=True, logCallback=None, completedCallback=None):
    """Execute a Python module as a script in Slicer's Python environment.

    Internally python -m is called with the module name and additional arguments.

    :param module: Python module name to execute (e.g., "pip")
    :param args: command-line arguments to pass to the module
    :param blocking: If True (default), block until completion. If False, return immediately.
    :param logCallback: When blocking=False, called with each line of output.
    :param completedCallback: When blocking=False, called when process completes.
    :raises RuntimeError: if PythonSlicer executable not found
    :raises CalledProcessError: in blocking mode, if process fails
    """
    # ... existing pythonSlicerExecutablePath setup unchanged ...

    commandLine = [pythonSlicerExecutablePath, "-m", module, *args]

    if blocking:
        proc = launchConsoleProcess(commandLine, useStartupEnvironment=False)
        logProcessOutput(proc)
    else:
        launchConsoleProcess(
            commandLine,
            useStartupEnvironment=False,
            blocking=False,
            logCallback=logCallback,
            completedCallback=completedCallback
        )
```

### 4. `slicer.util.pip_install()` (lines 3991-4034)

**Current signature:**
```python
def pip_install(requirements):
```

**Proposed signature:**
```python
def pip_install(requirements, blocking=True, logCallback=None, completedCallback=None):
```

**Proposed implementation:**

```python
def pip_install(requirements, blocking=True, logCallback=None, completedCallback=None):
    """Install python packages.

    :param requirements: requirement specifier (string or list of arguments)
    :param blocking: If True (default), block until installation completes and raise
        CalledProcessError on failure. If False, return immediately and use callbacks.
    :param logCallback: When blocking=False, called with each line of pip output.
        If None, output is printed to Python console as usual.
    :param completedCallback: When blocking=False, called when pip completes.
        Receives return code (0 = success). Required when blocking=False to know
        when installation finished.

    .. warning::

        When using blocking=False without a modal progress dialog, the user can
        interact with the application while installation is in progress. This may
        lead to conflicts if the user triggers another operation that depends on
        or modifies the Python environment. Use with caution and consider showing
        a modal dialog or disabling relevant UI elements during installation.

    Example: blocking mode (unchanged)::

      pip_install("pandas scipy")  # Blocks until complete

    Example: non-blocking mode::

      def onComplete(returnCode):
          if returnCode == 0:
              import pandas  # Now safe to import
              # Continue with operation...
          else:
              slicer.util.errorDisplay("Failed to install packages")

      pip_install("pandas scipy", blocking=False, completedCallback=onComplete)
      # Returns immediately

    """
    if type(requirements) == str:
        import shlex
        args = "install", *(shlex.split(requirements))
    elif type(requirements) == list:
        args = "install", *requirements
    else:
        raise ValueError("pip_install requirement input must be string or list")

    _executePythonModule("pip", args, blocking=blocking,
                         logCallback=logCallback, completedCallback=completedCallback)
```

---

## Output Capturing and Logging

The proposal ensures output is captured and logged identically to the current blocking behavior:

| Mode | Output Destination | How |
|------|-------------------|-----|
| Blocking (current) | Python console via `print()` | `logProcessOutput()` reads and prints each line |
| Non-blocking, no callback | Python console via `print()` | `checkOutput()` prints each line (same behavior) |
| Non-blocking, with callback | Custom handling | Callback receives each line; caller decides |

**Key point:** If `logCallback=None` in non-blocking mode, the output still goes to the Python console exactly as before. The only difference is timing (lines appear as they're polled rather than immediately).

---

## Comparison with Other Approaches

### Approach 1: Current Semi-Blocking (logProcessOutput)

```python
while True:
    line = proc.stdout.readline()  # Blocks
    print(line)
    app.processEvents()  # Brief UI refresh
```

| Aspect | Assessment |
|--------|------------|
| **UI Responsiveness** | Poor - only refreshes between lines |
| **User Interaction** | Minimal - can see updates but not interact meaningfully |
| **Complexity** | Very low |
| **Cancel Support** | No |
| **Risk of Conflicts** | None - user can't do anything |

### Approach 2: Modal Wait Popup (SlicerKonfAI)

```python
with slicer_wait_popup("Installing..."):
    pip_install("package")  # Still blocks
```

| Aspect | Assessment |
|--------|------------|
| **UI Responsiveness** | Poor - blocked, but dialog shown |
| **User Interaction** | None |
| **Complexity** | Very low |
| **Cancel Support** | No |
| **Risk of Conflicts** | None |

### Approach 3: Busy-Wait Threading (SlicerNNInteractive)

```python
thread = threading.Thread(target=pip_install, args=(...,))
thread.start()
while not event.is_set():
    app.processEvents()
```

| Aspect | Assessment |
|--------|------------|
| **UI Responsiveness** | Good - processEvents runs continuously |
| **User Interaction** | Limited - main thread is in loop |
| **Complexity** | Medium |
| **Cancel Support** | Possible |
| **Risk of Conflicts** | Low - user can interact but loop continues |
| **CPU Usage** | High - busy-wait loop |

### Approach 4: QTimer Polling (This Proposal)

```python
# Background thread reads into queue
# QTimer polls queue from main thread
```

| Aspect | Assessment |
|--------|------------|
| **UI Responsiveness** | Excellent - event loop runs freely |
| **User Interaction** | Full - user can do anything |
| **Complexity** | Medium-High |
| **Cancel Support** | Yes |
| **Risk of Conflicts** | High if no modal dialog |
| **CPU Usage** | Low - timer-based |

---

## Pros and Cons of This Proposal

### Pros

1. **Truly non-blocking**: The Qt event loop runs freely. Animations work, other modules work, everything stays responsive.

2. **Backward compatible**: `blocking=True` is the default, so existing code works unchanged.

3. **Flexible**: Callers can:
   - Use blocking mode for simple cases
   - Use non-blocking with default logging
   - Use non-blocking with custom callbacks for full control

4. **Efficient**: QTimer-based polling uses minimal CPU compared to busy-wait loops.

5. **Output preserved**: All pip output is captured and logged, whether blocking or not.

6. **Cancel support possible**: Since main thread is free, a cancel button could kill the process.

7. **Foundation for progress display**: The `logCallback` can be used to parse pip output and update a progress bar.

### Cons

1. **More complex implementation**: ~50 lines of new code vs. the simple blocking approach.

2. **Risk of user conflicts**: Without a modal dialog, users might start conflicting operations. (Mitigated by documentation warning.)

3. **Async complexity for callers**: Non-blocking mode requires callback-based programming, which is more complex than linear code.

4. **Polling latency**: 100ms polling interval means output appears slightly delayed (imperceptible to users, but technically not instant).

5. **Thread safety considerations**: While the implementation is thread-safe (using Queue), callers must be careful not to modify shared state from callbacks.

---

## Summary of Changes

| Function | Change |
|----------|--------|
| `launchConsoleProcess()` | Add `blocking`, `logCallback`, `completedCallback` parameters |
| `_startAsyncProcessHandling()` | New internal function for QTimer-based async handling |
| `_executePythonModule()` | Pass through new parameters to `launchConsoleProcess()` |
| `pip_install()` | Add `blocking`, `logCallback`, `completedCallback` parameters with warning |
| `pip_uninstall()` | Same changes as `pip_install()` (for consistency) |

---

## Usage Example: Integration with Progress Display

This blocking-prevention infrastructure enables the progress display feature:

```python
def pip_install_with_progress(requirements, requester=None):
    """Install packages with a modal progress dialog."""
    import qt

    # Create modal progress dialog
    dialog = slicer.util.createProgressDialog(autoClose=False)
    dialog.setLabelText(f"Installing packages...")
    dialog.setWindowTitle(f"{requester} - Installing" if requester else "Installing")
    dialog.setCancelButton(None)  # Or enable for cancel support
    dialog.setModal(True)
    dialog.show()

    log_lines = []

    def onLog(line):
        log_lines.append(line)
        # Could parse line to update progress or show current package
        dialog.setLabelText(f"Installing...\n{line[:50]}")
        # Output still goes to console
        print(line)

    def onComplete(returnCode):
        dialog.close()
        if returnCode != 0:
            slicer.util.errorDisplay(
                "Installation failed",
                detailedText="\n".join(log_lines)
            )

    pip_install(requirements, blocking=False, logCallback=onLog, completedCallback=onComplete)
```

This separation of concerns means:
- `pip_install` handles the non-blocking execution
- The progress display is built on top using callbacks
- Users can choose to use the simple blocking mode or the advanced non-blocking mode
