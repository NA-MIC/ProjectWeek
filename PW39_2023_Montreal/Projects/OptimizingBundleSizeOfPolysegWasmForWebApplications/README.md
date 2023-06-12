---
layout: pw39-project

permalink: /:path/

project_title: Optimizing Bundle Size of PolySeg-WASM for Web Applications
category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Alireza Sedghi
  affiliation: OHIF
  country: Canada

- name: Jaswant Panchumarti
  affiliation: Kitware
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The Institute of Cancer Research (ICR) has created PolySeg-WASM is an extended WASM wrapper for the [PerkLab/PolySeg](https://github.com/PerkLab/PolySeg) library, including C++ code repurposed from [Slicer](https://github.com/Slicer/Slicer) and [SlicerRT](https://github.com/SlicerRt/SlicerRT).

In the [previous year project](https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/OHIF_PolySeg/README.md) we created the contour segmentation representation for [Cornerstone3D library](https://www.cornerstonejs.org/live-examples/contourrendering), now this year we want to use the polySEG to convert the contours to closed surfaces.

The repo by ICR does the job However, the bundle is huge (3MB) which is not optimal for the web applications. This project aims to find out how to reduce the bundle size by choosing the VTK dependencies.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  **Analyze VTK dependencies**: dentify the specific VTK components used in the PolySeg-WASM library that contribute the most to the bundle size in order to determine areas for potential optimization.
2.  **Optimize VTK bundle size**: Reduce the bundle size of PolySeg-WASM by selectively choosing essential VTK dependencies, excluding or replacing components with lightweight alternatives, while maintaining the required functionality.
3.  **Evaluate performance and functionality**: Assess the performance and functionality of the optimized PolySeg-WASM library to ensure that the reduction in bundle size does not compromise accuracy or efficiency in converting contours to closed surfaces for web applications.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Perform a detailed code analysis to identify the specific VTK components used in PolySeg-WASM.
2.  Measure the size contribution of each VTK component to the overall bundle size of PolySeg-WASM.
3.  Document the findings, including a breakdown of the size contribution of each component.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![image](https://github.com/NA-MIC/ProjectWeek/assets/7490180/4f5dfd53-ffb1-41a3-9f17-85d64a47a30b)

![image](https://github.com/NA-MIC/ProjectWeek/assets/7490180/daf0cfd0-9aee-420b-a94e-6b93edbb5356)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[PolySEG repo ](https://github.com/PerkLab/PolySeg)
[ICR Wrapper](https://bitbucket.org/icrimaginginformatics/polyseg-wasm/src/master/)
