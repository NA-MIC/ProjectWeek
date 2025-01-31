---
layout: pw39-project

permalink: /:path/

project_title: 3D Slicer Undo/Redo
category: Infrastructure
presenter_location: In-person

key_investigators:
- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada
---

# Project Description

Global undo/redo is currently [the highest voted feature](https://discourse.slicer.org/t/is-it-possible-to-add-a-global-undo-button/16859) on the [3D Slicer Discourse feature requests board](https://discourse.slicer.org/c/support/feature-requests/9).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Gather feedback on the current state of Undo/Redo in Slicer.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

To test the undo/redo functionality currently available in Slicer, add the following code to '.slicerrc' to test undo/redo with Markups:

```python
slicer.mrmlScene.SetUndoOn()

undoEnabledNodeClassNames = [
  "vtkMRMLMarkupsFiducialNode",
  "vtkMRMLMarkupsLineNode",
  "vtkMRMLMarkupsAngleNode",
  "vtkMRMLMarkupsCurveNode",
  "vtkMRMLMarkupsClosedCurveNode",
  "vtkMRMLMarkupsPlaneNode",
  "vtkMRMLMarkupsROINode",
  ]
for className in undoEnabledNodeClassNames:
  node = slicer.mrmlScene.CreateNodeByClass(className)
  node.SetUndoEnabled(True)
  slicer.mrmlScene.AddDefaultNode(node)

def onRedo():
  slicer.mrmlScene.Redo()

def onUndo():
  slicer.mrmlScene.Undo()

redoShortcuts = []
redoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Redo)
for redoBinding in redoKeyBindings:
  redoShortcut = qt.QShortcut(slicer.util.mainWindow())
  redoShortcut.setKey(redoBinding)
  redoShortcut.connect("activated()", onRedo)
  redoShortcuts.append(redoShortcut)

undoShortcuts = []
undoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Undo)
for undoBinding in undoKeyBindings:
  undoShortcut = qt.QShortcut(slicer.util.mainWindow())
  undoShortcut.setKey(undoBinding)
  undoShortcut.connect("activated()", onUndo)
  undoShortcuts.append(undoShortcut)

toolBar = qt.QToolBar("Undo/Redo")
toolBar.addAction(qt.QIcon(":/Icons/Medium/SlicerUndo.png"), "Undo", onUndo)
toolBar.addAction(qt.QIcon(":/Icons/Medium/SlicerRedo.png"), "Redo", onRedo)
slicer.util.mainWindow().addToolBar(toolBar)
```

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Fixed issue with camera movements creating unnecessary undo states: [Slicer/5e460ad](https://github.com/Slicer/Slicer/commit/5e460add5b9163fb2f80e33037624c97f5b4d7f4).
2. Continue to receive feedback and bug reports on the current implementation.
3. Add option to enable/disable undo from application settings in Slicer.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![undo_redo](https://github.com/NA-MIC/ProjectWeek/assets/9222709/13bc6fc2-c93d-41b0-b25c-c24b996c867d)

# Background and References

- [Slicer global undo feature request](https://discourse.slicer.org/t/is-it-possible-to-add-a-global-undo-button/16859)
