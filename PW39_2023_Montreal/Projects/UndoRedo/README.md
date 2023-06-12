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

To test the undo/redo functionality currently availiable in Slicer, add the following code to '.slicerrc' to test undo/redo with Markups:

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

toolBar = qt.QToolBar()
toolBar.addAction(qt.QIcon(":/Icons/Medium/SlicerUndo.png"), "Undo", onUndo)
toolBar.addAction(qt.QIcon(":/Icons/Medium/SlicerRedo.png"), "Redo", onRedo)
slicer.util.mainWindow().addToolBar(toolBar)
```

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- [Slicer global undo feature request](https://discourse.slicer.org/t/is-it-possible-to-add-a-global-undo-button/16859)
