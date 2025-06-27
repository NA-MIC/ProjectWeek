---
layout: pw43-project

permalink: /:path/

project_title: Visualizing Brain Deformation
category: Quantification and Computation

key_investigators:

- name: Isabel Frolick
  affiliation: McGill University
  country: Canada

- name: Elise Donzselmann-Lund
  affiliation: McGill University
  country: Canada

- name: Étienne Léger
  affiliation: McGill University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


A 3D Slicer plug-in to visualize the dense quantification of brain shift as seen during MRI-ultrasound registration.

There are a few 3D Slicer plug-ins that allow the user to visualize the deformation field as either a vector field or a grid (such as Transform Visualizer), but there are a few shortcomings. Namely, 1) they don’t inherently function on ultrasound data (you must specify the deformation as either rigid, affine, or B-spline, none of which will work on ultrasound out of the box) and 2) they don’t quantify brain shift in millimetres, only in abstract vector fields.

We hope to do MRI-ultrasound registration and then densely quantify how much brain shift is present in millimetres at each voxel.

For the registration, we will implement a published and validated MRI-ultrasound registration pipeline from our lab [Rivaz, 2014] as a basis for non-rigid registration. Then we will use the resulting transformation to quantify how much brain shift (deformation) is occurring at each voxel and, as there should be a 1:1 mapping of the voxel space to the physical space, convert this deformation to millimetres. We would like to visualize this millimetre deformation in an intuitive way on both the slices and volumes to better understand where and how much deformation is occurring. 





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Implement a MRI-ultrasound registration pipeline as a 3D Slicer module for use on brain tumour resection data (validated on publicly available datasets such as RESECT, REMIND, and BITE)
2. Objective B.  Densely quantify how much deformation is present at each voxel in millimetres and visualize as a 3D Slicer module.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Implement a previously published and validated registration pipeline from our lab for T1/ T2 MRI - B-mode ultrasound as a 3D Slicer module. Validate on publicly available datasets.
2. Develop Slicer module that accepts a moving image (US), source image (MRI), and transformation (output from Step 1) to visualize the deformation field intuitively. 
3. Quantify how much deformation is present at each voxel using either mean curvature or gradient orientation information, or akin. Define conversion between voxel space and physical space to produce measure of deformation in  millimetres.
4. Output of the Slicer module will be the MRI and US volumes overlaid with an intuitive colour map representing deformation with 1) millimetre magnitude and 2) orientation.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Displacement visualization (in mm) with configurable colour maps
2. Cursor glyph shows displacement
4. Allow UI to change opacity, threshold colour maps
5. Visualize where the ultrasound data exists on the MRI
6. Insert landmarks to visualize



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

[https://mcgill-my.sharepoint.com/:v:/g/personal/etienne_leger_mcgill_ca/EYxMVat9qgxHnoQ-7JhEq_0BCcxIrsJj4NhBqJVAEP02cQ?e=57a12U&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D](https://mcgill-my.sharepoint.com/:v:/g/personal/etienne_leger_mcgill_ca/EYxMVat9qgxHnoQ-7JhEq_0BCcxIrsJj4NhBqJVAEP02cQ?e=57a12U&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


The registration method being implemented: Rivaz H, Karimaghaloo Z, Fonov VS, Collins DL. Nonrigid registration of ultrasound and MRI using contextual conditioned mutual information. IEEE Trans Med Imaging. 2014 Mar;33(3):708-25. doi: 10.1109/TMI.2013.2294630. PMID: 24595344.

