Back to [Projects List](../../README.md#ProjectsList)

## SlicerMitralValve

## Key Investigators
- Patrick Carnahan (Robarts) 

# Project Description
This extension contains a collection of tools for aiding in patient-specific mitral valve modelling. Currently consists of components for registering bi-plane colour ultrasound into 3D, and semi-automatically segmenting the mitral valve from 3D TEE data.

## Objective
1. Add functionality for registering both 2D and 2D bi-plane images.
1. Add section to automatically register 2D and bi-plane based on user defined MV annulus points.
1. Improve usability of interactive-automatic mitral valve segmentation module.
1. Integrate custom mold generation from segmentation.

## Approach and Plan

1. Identify and make necessary changes to generalize bi-plane registration to regular 2D images
1. Implement user defined annulus in 2D images
1. Initialize registration using annulus points

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
1. Working prototype of segmentation and registration modules already developed

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->
![BiPlaneRegistration Module screenshot](https://raw.githubusercontent.com/pcarnah/SlicerMitralValve/master/BiPlaneRegistration.png)

![Mitral Valve Segmenter Module screenshot](https://raw.githubusercontent.com/pcarnah/SlicerMitralValve/master/MitralValveSegmenter-Screenshot.png)

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/pcarnah/SlicerMitralValve
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data

