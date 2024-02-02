---
layout: pw40-project

permalink: /:path/

project_title: Automated Registration of Cone-Bean Computed Tomography scans - maintenance
category: Other
presenter_location: Online

key_investigators:

- name: Jeanne Claret
  affiliation: University of Michigan
  country: USA

- name: Gaëlle Leroux
  affiliation: UoM
  country: USA

- name: Eduardo Duarte Caleme
  affiliation: UoM
  country: USA

- name: Claudia Mattos
  affiliation: UoM
  country: USA

- name: Lucia Cevidanes
  affiliation: UoM
  country: USA

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The Automated Registration tool, AREG, was first presented at the NA-MIC project week #39.
It aims to reduce the sources of error in the 3D image processing workflow by automating the orientation and registration of 3D Cone-Beam Computed Tomography. These methods combine classical algorithmic approaches and AI-based models trained and tested on de-identified CBCT volumetric images.

The registration method is based on an automatic tool, AMASS, available in the extension SlicerAutomatedDentalTool, to perform a segmentation of the different regions of reference used for the regional voxel-based registration

The different methods for automatic orientation and registration of 3D CBCT scans rely on a combination of algorithmic and deep-learning techniques to perform both the orientation and the registration automatically. It also uses work that our group of researchers has already developed. Our Python-based algorithm and requires multiple libraries for the different image-processing tasks accomplished throughout the proposed method: SimpleITK, VTK, SimpleElastix. To implement these tools, we also used the Medical Open Network for Artificial Intelligence (MONAI) library, which is a PyTorch-based framework for medical image analysis. MONAI offers several advantages for our work, such as high performance, modularity, and interoperability with other libraries.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Maintain the code to make it work properly on the new version of Slicer

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Find the issue by testing
2.  Correct the problem

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. The module AREG is working inly with itk-elastix==0.17.1
2. In the last release of SlicerAutomatedDentalTools, users are asked if they agree to change the libraries versions of their Slicer environment.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![Screenshot from 2024-02-02 08-49-19](https://github.com/NA-MIC/ProjectWeek/assets/91120559/cca61e1d-e380-4acf-b904-cd9a78be8080)

![Workflow](https://github.com/lucanchling/ProjectWeek/assets/72148963/a6617e85-df6e-426f-ab4a-eef322453e7e)

![MaskComparison](https://github.com/lucanchling/ProjectWeek/assets/72148963/7312a43f-8b00-4513-bf75-0cf1a363b310)

![AREGCBCTExample](https://github.com/lucanchling/ProjectWeek/assets/72148963/66574b8d-a9b0-465a-a5ef-4206bb2d84dd)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [AMASS and AREG](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools)
