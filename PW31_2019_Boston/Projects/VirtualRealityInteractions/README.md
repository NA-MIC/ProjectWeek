Back to [Projects List](../../README.md#ProjectsList)

# Virtual reality interactions

## Key Investigators

- Csaba Pinter (Queen's University)
- Nayra Pumar Carreras (Universidad de Las Palmas de Gran Canaria)
- Clement Mirabel (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->
The goal of the project is to make progress towards having an in-VR interaction widget that the user can use to drive Slicer features. A home widget gives access to typical VR settings, and provides access to modules (VR'ized version of much used modules from Slicer). The user uses the controller as a laser pointer, which acts as a mouse on the Qt widget shown on the VTK actor that appears in the VR scene. See full description ![here](https://github.com/KitwareMedical/SlicerVirtualReality/issues/43).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. vtkQWidgetWidget works with Slicer's new VTK widget event handling method
1. The widget can show the VR home widget in VR

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Add vtkQWidgetWidget support in Slicer using the new VTK widget event handling method
1. Bind controller menu button to show the home widget in front of the user
1. If the new laser pointer is ready by then, then start implementing Qt event translation

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![VR home widget prototype](https://user-images.githubusercontent.com/46090514/59448974-2bdd0900-8dd4-11e9-9191-610cfb5253dd.gif)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
