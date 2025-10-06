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


This project introduces a 3D Slicer plug-in for visualizing and quantifying non-linear brain deformation fields as seen during MRI-ultrasound registration.


While existing tools such as Transform Visualizer can display vector fields or deformation grids, they have several limitations for the purposes of non-linear MRI-ultrasound registration — notably, limited compatibility with ultrasound-derived data (you must specify the deformation as either rigid, affine, or B-spline, none of which will work on ultrasound out of the box) and the inability to express deformation magnitudes in real-world physical units.

Our module addresses these gaps by enabling quantitative visualization of deformation in two ways: 1) dense displacement magnitude in millimetres and 2) determinant of the Jacobian magnitude to quantify the local stretching or squishing of space, to provide intuitive visual feedback on tissue expansion and compression.

This module can be used with any non-linear registration method. Testing data was developing using published and validated MRI-ultrasound registration pipeline from our lab [Rivaz, 2014] as a basis for non-rigid registration. We then use the resulting transformation to quantify how much brain shift (deformation) is occurring at each voxel and convert this deformation to millimetres. 

This module allows researchers to better understand the extent and spatial distribution of brain shift occurring during neurosurgical interventions.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Quantitative Deformation Visualization: Compute voxel-wise deformation in millimetres and visualize both displacement magnitude and Jacobian-based expansion/compression as an out-of-the-box solution. Introduce intuitive colour maps and functionality to enable users to examine quantitative deformation using the cursor.
2. Objective B. Simplified Landmark-Based Analysis: Introduce functionality for .tag to .fcsv (Slicer compatible) landmark registration. Explictly show the Euclidean distance between corresponding landmarks within the module, for improved visualization.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop Slicer module that accepts a moving image (US), source image (MRI), and transformation (output from Step 1) to visualize the deformation field intuitively.
2. Compute physical displacements from voxel-wise transformation fields, converting deformation to millimetres in real-world space. Additionally, calculate the Jacobian determinant to characterize local tissue expansion or compression.
3. Develop an intuitive visualization interface that overlays deformation maps on the MRI or ultrasound volumes, supporting both default and custom colour maps, opacity adjustment, and threshold control.
4. Incorporate landmark handling and interactive displacement queries:
   - Convert .tag files to Slicer-compatible .fcsv format.
   - Display Euclidean distances between corresponding landmarks.
   - Track cursor position and dynamically display displacement in millimetres.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Completed:
- Implemented displacement visualization in millimetres
- Added Jacobian magnitude visualization for local expansion/compression.
- Integrated custom and default colour map options.
- Added cursor tracking, showing displacement magnitude in real time.
- Implemented landmark conversion from .tag → .fcsv and visualization of Euclidean distances between corresponding landmarks.
- Added opacity and threshold controls for flexible visualization.

Next Steps:
- Refine user interface for smoother workflow integration in Slicer.
- Validate deformation quantification on additional datasets.
- Developing test cases and debugging

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

[https://mcgill-my.sharepoint.com/:v:/g/personal/etienne_leger_mcgill_ca/EYxMVat9qgxHnoQ-7JhEq_0BCcxIrsJj4NhBqJVAEP02cQ?e=57a12U&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D](https://mcgill-my.sharepoint.com/:v:/g/personal/etienne_leger_mcgill_ca/EYxMVat9qgxHnoQ-7JhEq_0BCcxIrsJj4NhBqJVAEP02cQ?e=57a12U&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


The registration method being implemented on testing data: Rivaz H, Karimaghaloo Z, Fonov VS, Collins DL. Nonrigid registration of ultrasound and MRI using contextual conditioned mutual information. IEEE Trans Med Imaging. 2014 Mar;33(3):708-25. doi: 10.1109/TMI.2013.2294630. PMID: 24595344.

For use of testing data, please contact isabel.frolick@mail.mcgill.ca

