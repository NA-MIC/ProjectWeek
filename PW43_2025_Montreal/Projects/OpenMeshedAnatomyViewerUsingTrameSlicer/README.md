---
layout: pw43-project

permalink: /:path/

project_title: Open Meshed Anatomy Viewer using Trame Slicer
category: Cloud / Web

key_investigators:

- name: Andy Huynh
  affiliation: University of Western Australia

- name: Benjamin Zwick
  affiliation: University of Western Australia

- name: Karol Miller
  affiliation: University of Western Australia

- name: Adam Wittek
  affiliation: University of Western Australia

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The Open Meshed Anatomy Viewer is a web-app for researchers to download and visualize atlas-based meshes/grids for scientific computing based on Trame Slicer. [trame-slicer](https://github.com/KitwareMedical/trame-slicer) is a Python library bringing[ 3DSlicer](https://github.com/Slicer/Slicer/) components in trame as a composable library. It uses 3D Slicer's python wrapping and adds a thin wrapping to make it available with the[ trame framework](https://github.com/Kitware/trame/).

- The meshes/grids are created from [Open Anatomy Project's SPL/NAC Brain Atlas](https://www.openanatomy.org/atlas-pages/atlas-spl-nac-brain.html). 
- The [Trame Slicer](https://github.com/KitwareMedical/trame-slicer) library provides a way for 3D Slicer components to be used in a web-app.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Develop a Trame Slicer based web application to view meshes/grid with images. 
2. Objective B. Download meshes/grids.
3. Objective C. Host web-app on cloud server.
4. Objective D. Upload simulation results.
5. Objective E. Extract statistics based on anatomical labels.
6. Objective F. Morph meshes/grids to target MRI.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a blank Trame Slicer repo project.
2. Host project on cloud server (e.g. using docker, cap rover etc.).
3. Load images and atlas.
4. Test server-side rendering performance. (related [Github Issue](https://github.com/KitwareMedical/trame-slicer/issues/11)).
5. Add features.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We have developed detailed computational meshes using the SPL Brain Atlas.
2. At the [39th Project Week in Montreal (2023)](https://projectweek.na-mic.org/PW39_2023_Montreal/) we developed a Trame-based web application that can be used to visualize the Open Meshed Anatomy in 3D Slicer



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://github.com/user-attachments/assets/4fe0811b-3d21-4a8c-b05f-7a8ab1b4eb47)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. [Open Meshed Anatomy Project Description - NA-MIC Project Week 39 in Montreal (2023)](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/OpenMeshedAnatomy/)
2. [KitwareMedical/trame-slicer: Bring the capabilities of 3D Slicer to the web with modern UI using the trame framework!](https://github.com/KitwareMedical/trame-slicer)

