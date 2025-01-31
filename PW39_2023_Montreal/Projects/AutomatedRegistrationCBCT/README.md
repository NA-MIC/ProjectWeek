---
layout: pw39-project

permalink: /:path/

project_title: Automated Registration of Cone-Beam Computed Tomography
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:
- name: Anchling Luc
  affiliation: University of Michigan

- name: Nathan Hutin
  affiliation: University of Michigan
  country: France

- name: Marcela Grugel
  affiliation: University of Michigan
  country: USA

- name: Selene Barone
  affiliation: University of Michigan
  country: USA

- name: Felicia Miranda
  affiliation: University of Michigan
  country: USA

- name: Sophie Roberts
  affiliation: University of Melbourne
  country: Australia

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

- name: Lucia Cevidanes
  affiliation: University of Michigan
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->
Automated clinical decision support systems rely on accurate analysis of three-dimensional (3D) medical and dental images to assist clinicians in diagnosis, treatment planning, intervention, and assessment of growth and treatment effects. However, analyzing 3D images requires orientation and registration, which are tedious and error-prone tasks.

This project proposes two novel tools that can automatically perform the orientation and registration of 3D Cone-Beam Computed Tomography (CBCT) scans with high accuracy. Our work aims to reduce the sources of error in the 3D image processing workflow by automating these operations. These methods combine classical algorithmic approaches and AI-based models trained and tested on de-identified CBCT volumetric images.

The registration method is based on an automatic tool [AMASSS](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools) to perform a segmentation of the different regions of reference (described [here](#illustrations)) used for the regional voxel-based registration

Our code is available [here](https://github.com/lucanchling/areg)

The different methods for automatic orientation and registration of 3D CBCT scans rely on a combination of algorithmic and deep-learning techniques to perform both the orientation and the registration automatically. It also uses work that our group of researchers has already developed. Our Python-based algorithm and requires multiple libraries for the different image-processing tasks accomplished throughout the proposed method: SimpleITK \cite{Lowekamp2013-jt}, VTK \cite{Schroeder2006-ab}, SimpleElastix \cite{SimpleElastix}. To implement these tools, we also used the Medical Open Network for Artificial Intelligence (MONAI) library, which is a PyTorch-based framework for medical image analysis. MONAI offers several advantages for our work, such as high performance, modularity, and interoperability with other libraries.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Continue to develop the Slicer tool
1. Deploy AREG CBCT in the Slicer extension *SlicerAutomatedDentalTools*

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Find a method to perform the Automatic Registration of CBCT
1. Implement this method with a python script
1. Use the previous work done on developing other Slicer Extensions to develop the AReg extension for Slicer

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Method and script working
1. Slicer Extension created and progress made on developing it
1. Deploy AReg tool to the *SlicerAutomatedDentalTools*
1. Validating the tool via method paper

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)

![Some more images](Example2.jpg)
-->
## Comparison between the current and the proposed workflow
![Workflow](https://github.com/lucanchling/ProjectWeek/assets/72148963/a6617e85-df6e-426f-ab4a-eef322453e7e)

## Different regions of reference (comparison between the full segmentation and the mask)
![MaskComparison](https://github.com/lucanchling/ProjectWeek/assets/72148963/7312a43f-8b00-4513-bf75-0cf1a363b310)

## Example of Cranial Base Registration
![AREGCBCTExample](https://github.com/lucanchling/ProjectWeek/assets/72148963/66574b8d-a9b0-465a-a5ef-4206bb2d84dd)

## Screenshot of the User Interface of the developed extension
![AREG](https://github.com/lucanchling/ProjectWeek/assets/72148963/23200b88-21f2-4538-afdf-3dc757454efb)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
