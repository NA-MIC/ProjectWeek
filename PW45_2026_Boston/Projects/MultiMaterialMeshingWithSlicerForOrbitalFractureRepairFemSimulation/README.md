---
layout: pw45-project

permalink: /:path/

project_title: Multi-material meshing with Slicer for orbital fracture repair FEM simulation
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M College of Dentistry
  country: US

- name: Rafael Palomar
  affiliation: Norwegian University of Science and Technology
  country: Norway

- name: Paul Baksic
  affiliation: INRIA
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


A reproducible meshing workflow is essential for reproducible and efficient FEM simulation. Meshing is a laborious and subjective process due to complex tissue geometry. First, orbital tissue are difficult to segment. 

To simplify set up for tracking orbital tissue position changes after fracture repair, we are using a multi-material unified orbital tissue mesh, in which elements in different regions are assigned different tissue material properties. This helps bypassing many complex setups, including define boundary conditions of tightly contact multiple soft tissue. 

Multi-material mesh requires generating fine elements at the tissue boundaries to better capture the geometry and assign different material properties accordingly. Currently, this can be done in gmsh by constructing a distance field from the surface within a unified mesh. However, this usually leads to higher number of elements, thus limiting simulation 

However, the process can requires significant manual preprocessing. A challenge is local fat herniation and complicated fractured boundary.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Continue the automated segmentation training using Monai-nnUNet.
2. Streamline manual processing, including handling patient-specifc fat herniation and fracture patterns.
3. Quantify the effect of different levels of mesh refinement on quantifying tissue position and shape changes.
4. Explore different methods for multi-material meshing for balancing simulation speed and geometric accuracy.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Describe specific steps of **what you plan to do** to achieve the above described objectives.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

