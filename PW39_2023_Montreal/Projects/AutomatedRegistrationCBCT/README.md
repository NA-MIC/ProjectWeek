---
layout: pw39-project

permalink: /:path/

project_title: Automated Registration of Cone-Beam Computed Tomography
category: Uncategorized

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

The registration method is based on an automatic tool [AMASSS](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools) to perfom a segmentation of the different region of reference (described [here](#illustrations)) used for the regional voxel-based registration

Our code is available [here](https://github.com/lucanchling/areg)



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Continue to develop the Slicer tool
1. Deploy AREG CBCT in the Slicer extension *SlicerAutomatedDentalTools*

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use the previous work done on developing other Slicer Extensions

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Slicer Extension created and progress made on developing it

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->