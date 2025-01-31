Back to [Projects List](../../README.md#ProjectsList)

# Touch and pen interactions

## Key Investigators

- Kyle Sunderland (Queen's University)
- Jarett Rushmore (Boston University)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
Implement and integrate robust interactions using both touchscreen gestures and peripherals such as the [Microsoft Surface Pen](https://www.microsoft.com/en-us/p/surface-pen/8zl5c82qmg6b?rtc=1&source=lp&activetab=pivot:overviewtab), and [Microsoft Surface Dial](https://www.microsoft.com/en-us/p/surface-dial/925r551sktgn?activetab=pivot%3aoverviewtab).

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Demonstrate and receive feedback on the current state of gesture and peripheral interactions in 3D Slicer
1. Determine the requirements for the utilization of interactions during segmentation
1. Update interactions in VTK and Slicer based on feedback

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
- [VTK pull request for fixing touchscreen gestures](https://gitlab.kitware.com/vtk/vtk/merge_requests/5679)
  - [Video of touch interactions in VTK](https://youtu.be/fpnqsDmJ0Y8)
- [Slicer Pull request for adding touchscreen gestures](https://github.com/Slicer/Slicer/pull/1122)
- Added tablet mode to segment editor
  - Tablet mode rejects regular mouse events and instead only acknowledges tablet events within the segment editor
- Added interaction with button on surface pen to switch between the last active segment editor effect

### Feedback
  - Would be useful to have a button on the tablet that increments/deincrements through the slices

### Issues
  - For Microsoft Surface Pen, pen button events are sent as "Windows Key" + F18-F20, however Slicer is only currently detectinbg the "Windows Key" (Qt::Key_Meta)
  - Improvements have been added to Qt, starting with the currently Slicer incompatible version of 5.12 (https://bugreports.qt.io/browse/QTBUG-53739)

## Result

 [Segmentation using Surface Pen](https://youtu.be/ZE16nNRxEjw)

# Background and References

- [WIP Slicer branch](https://github.com/Sunderlandkyl/Slicer/tree/gesture_interaction4)
- [WIP VTK branch](https://github.com/Sunderlandkyl/VTK/tree/slicer_qt_gestures2)
