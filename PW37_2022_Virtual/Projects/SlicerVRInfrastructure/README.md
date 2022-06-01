Back to [Projects List](../../README.md#ProjectsList)

# SlicerVR infrastructure maintenance

## Key Investigators

- Csaba Pinter (EBATINCA)
- You!

# Project Description

<!-- Add a short paragraph describing the project. -->

SlicerVR has many great features that allow an efficient visualization of medical 3D data. However, recent updates in the infrastructure (mainly that of VTK) broke certain key features, which make SlicerVR basically unusable in its current form.

At the same time, a new project (Kitware/Robarts) has started to upgrade the rendering backend of SlicerVR from OpenVR to OpenXR. However, the initial scope of the project may not include making these essential fixes.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The goal of the project is, with coordination with Kitware/Robarts, to reach the previous usability state of the SlicerVR extension.

1. Fix volume rendering display in the virtual reality view. This may not be OpenVR-related, because the same thing happens using the Looking Glass extension, so would be a first candidate.
1. Depending on the progress of OpenXR integration into SlicerVR, either
    1. Help with the integration and do testing and fixes, OR
    2. Work with the OpenVR version to fix controller events and the errors that bog down the application while rendering

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
1. ...
1. ...

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

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

* https://github.com/KitwareMedical/SlicerVirtualReality/issues/91
