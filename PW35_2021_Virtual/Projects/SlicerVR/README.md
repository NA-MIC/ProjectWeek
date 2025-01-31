Back to [Projects List](../../README.md#ProjectsList)

# SlicerVR: interactive UI panel in the VR environment

## Key Investigators

- Csaba Pinter (Ebatinca, Pixel Medical)
- Adam Rankin (Robarts Research, Canada)
- Jean-Christophe Fillion-Robin (Kitware)
- Simon Drouin (ETS)

# Project Description

<!-- Add a short paragraph describing the project. -->

A key infrastructural element that is still missing from SlicerVR is the ability to show and interact with arbitrary Qt widgets in the VR scene. Up until recently, a blocking issue was an incomplete implementation of the vtkQWidgetWidget class in the VTK version that Slicer was using. Now that Slicer has been migrated to VTK9, the implementation of this in-VR widget continued.

A blocking issue for this to happen is the ability to build the SlicerVR extension against Slicer built with VTK9. Currently, build fails because the build system does not support building VTK remote modules externally (this issue breaks the build of other important extensions as well, such as SlicerVMTK).

Once build is fixed and the in-VR widget is added, arbitrary UI elements of Slicer can be used from within VR, thus basically exposing the entire Slicer functionality within the VR environment.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Build SlicerVR against VTK9
1. Add interactive Qt panel to VR scene [SlicerVR#43](https://github.com/KitwareMedical/SlicerVirtualReality/issues/43)
1. Make use of the in-VR widget via laser pointer and VR-optimized widgets

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Update SlicerVR CMake files to build with VTK9
    1. Utilize new VTKExternalModule infrastructure to build vtk openvr rendering
    3. Extract the said module from VTK proper with history (JC)
    4. Change main CMake file to use this instead of the VTK remote module approach (Adam?)
    5. Fix build issues arising from the switch to VTK9 in SlicerVR (Csaba?)
1. Try [vtkQWidgetWidget](https://vtk.org/doc/nightly/html/classvtkQWidgetWidget.html) in SlicerVR, confirm that it now works (Csaba)
1. Explore existing possibilities for using a laser pointer emanating from the controllers to control the Qt-based widget (press, click, drag&drop, etc) (?)
1. Add the already implemented but dormant VR-optimized widgets in the SlicerVR user interface (Csaba)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Build SlicerVR against VTK9 :heavy_check_mark:
    1. [KitwareMedical/SlicerVirtualReality#84](https://github.com/KitwareMedical/SlicerVirtualReality/pull/84): Update build system to support building against VTK9
    1. Created [KitwareMedical/VTKExternalModule](https://github.com/KitwareMedical/VTKExternalModule) for externally building any built-in or remote VTK module outside of the VTK source tree.
    1. [vtk/vtk#8123](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8123): vtkModule: Do not generate files in source tree when building module externally
1. In-VR UI widgets
   1. Rebased VR widgets branch to the latest master to a [new branch](https://github.com/cpinter/SlicerVirtualReality/tree/virtual-widget-2)
   1. Built the SlicerVR branch succesfully with VTK9
   1. The vtkQWidgetWidget test still crashes unfortunately
1. Proposed some hooks to enable customization of VR interaction from python code in Slicer. [Pull request here](https://github.com/KitwareMedical/SlicerVirtualReality/pull/83) for reference.

# Illustrations

![In-VR user interface](https://spie.org/Images/Graphics/Newsroom/2019articles/Crime-920.jpg)

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

1. Commit that broke 3rd party module build [here](https://gitlab.kitware.com/vtk/vtk/-/commit/140f8d8bcd85cedd7ac996c806f984add70bb11d)
2. Discussion on remote modules vs. external modules [here](https://discourse.vtk.org/t/remote-modules-vs-external-modules/2003)
3. How to make downstream VTK modules [here](https://discourse.vtk.org/t/example-of-vtk-module-built-after-vtk-is-built/6099)
    1. Links to example [here](https://gitlab.kitware.com/vtk/vtk/-/tree/master/Examples/Build/vtkMy)
4. [https://github.com/KitwareMedical/VTKExternalModule](https://github.com/KitwareMedical/VTKExternalModule)
5. VR virtual widget branch [here](https://github.com/cpinter/SlicerVirtualReality/tree/virtual-widget)
