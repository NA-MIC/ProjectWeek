Back to [Projects List](../../README.md#ProjectsList)

# PolySeg in the browser

## Key Investigators

- Steve Pieper (Isomics)
- Erik Ziegler (Radical Imaging / Open Health Imaging Foundation)
- Jean-Christophe Fillion-Robin (Kitware)
- Csaba Pinter (PerkLab)

# Project Description

Various data structures are available to represent segmentation results. Unfortunately none of them are optimal for storage, analysis, and real-time visualization at the same time, so a trade-off is typically made to choose one that is most suitable for the main purpose of the application.

[PolySeg](https://github.com/PerkLab/PolySeg) is a library for polymorph segmentation representation for medical image computing. PolySeg is integrated within the 3D Slicer open-source medical image analysis and visualization platform. Automatic conversion between various different segment representations (Contours, Ribbon, Surface, Binary Labelmap, Fractional Labelmap) is driven by a conversion graph.

As segmentation tools become available for the web browser through toolkits such as [Cornerstone Tools](https://github.com/cornerstonejs/cornerstoneTools) and [VTK.js](https://github.com/Kitware/vtk-js), demand is increasing for the same type of polymorphic segmentation representation in web applications. The goal of this project is to understand how the functionality in PolySeg can be most easily exploited inside the browser.

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Identify whether or not it is possible to cross-compile PolySeg (and its VTK dependencies) to WebAssembly.
1. Support automatic conversion between two segment representations (e.g. contour and binary labelmap) in the browser as a proof-of-concept.
1. Create examples using Cornerstone Tools and VTK.js which show how to create, convert, and display segments between their representations.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Csaba will explain how PolySeg works and what its dependencies are.
1. Investigators will discuss what the minimum viable product is for using PolySeg in the browser. e.g. Most end users will only need to convert between contours and binary labelmaps.
1. We will investigate how PolySeg & VTK could be cross-compiled for use inside the browser. We will also explore whether or not the functionality can be obtained through a port of PolySeg to JavaScript which depends on VTK.js.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

### Progress

1. Learned how to use [itk-js](https://github.com/InsightSoftwareConsortium/itk-js/) to build combined ITK/VTK pipelines which can run in the browser.
1. Added PolySeg as a build step in a fork of the `itk-js` Docker image which is used for cross-compilation (via [dockcross](https://github.com/dockcross/dockcross)).
1. Used combined Docker image to build PolySeg tests to JavaScript
1. Built PolySeg example conversion pipeline from Binary Labelmap to Closed Surface which runs in Node.js and in the Browser (WASM bundle around 6.2 MB, non-WASM JS bundle 10.2 MB)
1. Built example page which runs the conversion pipeline on an input labelmap file and displays it with VTK.js

Pull Request to PolySeg with the code: https://github.com/PerkLab/PolySeg/pull/4

### Next Steps
1. Deal with issues around VTK's multithreading (`pthread_attr_setscope`) breaking cross-compilation procedures in Emscripten. There is already an [open ticket for enabling multithreading at itk-js](https://github.com/InsightSoftwareConsortium/itk-js/issues/213) so for now we just [disabled it everywhere](https://github.com/swederik/VTK/commit/acd6ccd796c511acdafc9c2ff2f2135f1a8900cc). The next step is to settle on the proper approach to disable pthread usage without having a fork of VTK. The built-in environment variable (`CMAKE_USE_PTHREADS_INIT`) did not do the trick on third-party extensions such as vtkhdf5.
1. Deal with issues around library linking between PolySeg and VTK. If PolySeg uses `BUILD_SHARED_LIBS:BOOL=ON`, then everything works normally but duplicate links show up when building the pipeline (`symbol multiply defined!`).
If `BUILD_SHARED_LIBS:BOOL=OFF`, certain VTK functions are not accessible within PolySeg for some reason (e.g. `vtkImageStencil`, `vtkImageAccumulate`). This is the key remaining blocker before this project could be considered a success.
1. Once things are working properly, we should contribute back some examples to `itk-js`. Much of the knowledge needed for this project was present in `itk-js` already, but it was inside things like tests or source code.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- Pinter, C., Lasso, A., & Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. https://doi.org/10.1016/j.cmpb.2019.02.011
- [vtk-js](https://github.com/Kitware/vtk-js)
- [itk-js](https://github.com/InsightSoftwareConsortium/itk-js)
- [PolySeg](https://github.com/PerkLab/PolySeg)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
