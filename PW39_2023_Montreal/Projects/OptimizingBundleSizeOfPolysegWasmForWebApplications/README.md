---
layout: pw39-project

permalink: /:path/

project_title: Optimizing Bundle Size of PolySeg-WASM for Web Applications
category: Early Presenter
topic-category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Alireza Sedghi
  affiliation: OHIF
  country: Canada

- name: Kyle Sunderland
  affiliation: Queen's University
  coutnry: Canada

- name: Jaswant Panchumarti
  affiliation: Kitware, Inc.
  country: USA


---

# Project Description

The Institute of Cancer Research (ICR) has created PolySeg-WASM is an extended WASM wrapper for the [PerkLab/PolySeg](https://github.com/PerkLab/PolySeg) library, including C++ code repurposed from [Slicer](https://github.com/Slicer/Slicer) and [SlicerRT](https://github.com/SlicerRt/SlicerRT).

In the [previous year project](https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/OHIF_PolySeg/README.md) we created the contour segmentation representation for [Cornerstone3D library](https://www.cornerstonejs.org/live-examples/contourrendering), now this year we want to use the polySEG to convert the contours to closed surfaces.

The repo by ICR does the job However, the bundle is huge (3.6MB) which is not optimal for the web applications. This project aims to find out how to reduce the bundle size by choosing the VTK dependencies.

## Objective


1.  **Analyze VTK dependencies**: dentify the specific VTK components used in the PolySeg-WASM library that contribute the most to the bundle size in order to determine areas for potential optimization.
2.  **Optimize VTK bundle size**: Reduce the bundle size of PolySeg-WASM by selectively choosing essential VTK dependencies, excluding or replacing components with lightweight alternatives, while maintaining the required functionality.
3.  **Evaluate performance and functionality**: Assess the performance and functionality of the optimized PolySeg-WASM library to ensure that the reduction in bundle size does not compromise accuracy or efficiency in converting contours to closed surfaces for web applications.

## Approach and Plan


1.  Perform a detailed code analysis to identify the specific VTK components used in PolySeg-WASM.
2.  Measure the size contribution of each VTK component to the overall bundle size of PolySeg-WASM.
3.  Document the findings, including a breakdown of the size contribution of each component.

## Progress and Next Steps

0. Updated the vtk that polyseg-wasm is using to the one that slicer is using which is specified [here](https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_VTK.cmake#L136-L146), it was previously depending on latest vtk
1. We initially tried to reduce the final wasm size by disabling various modules in the vtk cmake. However, this approach didn't yield the desired results.
2. Next, we examined the polySEG-wasm's cmake to determine potential modifications for size reduction. We discovered that all vtk dependencies are included in ${VTK_LIBS}, set by cmake. By incrementally adding these dependencies, we pinpointed the minimum number of libraries needed, resulting in a 550 KB reduction in the final wasm size. The final set of included libraries was VTK::CommonDataModel VTK::CommonCore VTK::CommonExecutionModel VTK::FiltersCore VTK::FiltersExtraction VTK::ImagingStencil VTK::ImagingStatistics VTK::ImagingMorphological.
3. Furthermore, we observed that the browser gzips the loaded wasm, bringing the final resource size down to 800 KB - a significant improvement from before.
4. PR created [here ](https://bitbucket.org/icrimaginginformatics/polyseg-wasm/pull-requests/1)

### Next steps

1. We should look into if we can even narrow down even more the VTK::CommonDataModel and VTK::CommonCore to only include those sub libs that is necessary for the build


# Illustrations

![image](https://github.com/NA-MIC/ProjectWeek/assets/7490180/fe1091cc-32f5-4710-a605-8345ce399849)


![image](https://github.com/NA-MIC/ProjectWeek/assets/7490180/8ab133e7-aa73-4b02-8c1d-3dc807861b64)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[PolySEG repo ](https://github.com/PerkLab/PolySeg)
[ICR Wrapper](https://bitbucket.org/icrimaginginformatics/polyseg-wasm/src/master/)
