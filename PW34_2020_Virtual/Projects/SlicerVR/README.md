Back to [Projects List](../../README.md#ProjectsList)

# SlicerVR: interactive UI panel in the VR environment

## Key Investigators

- Csaba Pinter (Ebatinca, Pixel Medical)

# Project Description

<!-- Add a short paragraph describing the project. -->

A key infrastructural element that is still missing from SlicerVR is the ability to show and interact with arbitrary Qt widgets in the VR scene. Up until recently, a blocking issue was an incomplete implementation of the vtkQWidgetWidget class in the VTK version that Slicer was using. Now that Slicer is being migrated to VTK9, this issue can hopefully be fixed and the implementation of this in-VR widget continued. With this improvement, arbitrary UI elements of Slicer can be used from within VR, thus basically exposing the entire Slicer functionality within the VR environment.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Build SlicerVR against VTK9
1. Add interactive Qt panel to VR scene [SlicerVR#43](https://github.com/KitwareMedical/SlicerVirtualReality/issues/43)
1. Make use of the in-VR widget via laser pointer and VR-optimized widgets

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Update SlicerVR CMake files to build with VTK9
1. Try [vtkQWidgetWidget](https://vtk.org/doc/nightly/html/classvtkQWidgetWidget.html) in SlicerVR, confirm that it now works
1. Explore existing possibilities for using a laser pointer emanating from the controllers to control the Qt-based widget (press, click, drag&drop, etc)
1. Add the already implemented but dormant VR-optimized widgets in the SlicerVR user interface

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

![In-VR user interface](https://spie.org/Images/Graphics/Newsroom/2019articles/Crime-920.jpg)

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
