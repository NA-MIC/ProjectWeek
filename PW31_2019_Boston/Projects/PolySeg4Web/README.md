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

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- Pinter, C., Lasso, A., & Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. https://doi.org/10.1016/j.cmpb.2019.02.011

- [vtk-js](https://github.com/Kitware/vtk-js)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
