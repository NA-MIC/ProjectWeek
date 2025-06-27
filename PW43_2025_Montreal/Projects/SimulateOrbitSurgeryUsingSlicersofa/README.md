---
layout: pw43-project

permalink: /:path/

project_title: Simulate orbit surgery using SlicerSOFA
category: VR/AR and Rendering

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M College of Dentistry
  country: US

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

- name: Steve Pieper
  affiliation: Isomics
  country: US

- name: Paul Baksic
  affiliation: INRIA
  country: France

- name: Andrew Read-Fuller
  affiliation: Texas A&M College of Dentistry

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Simulating orbital fracture repair process using SlicerSOFA.

<p>
<img src="https://github.com/user-attachments/assets/5c46f298-f059-4c4c-8114-4f21906f9dd2" width="200"/></p>

Surgical Guidance using MatrixOrbital preformed plates from Johnson&Johnson DePuy Synthesis: [https://www.jnjmedtech.com/en-US/product/matrixorbital-preformed-orbital-plates](https://www.jnjmedtech.com/en-US/product/matrixorbital-preformed-orbital-plates)



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Learn programing using SlicerSofa. Deform a simple orbital tissue model.
2. Load and deform multiple models and create a simple simulation of lifting orbital tissue using a scoope-like tool.
3. Stretching goal: create a volumetric model of the meshed plate and bend it using SlicerSOFA



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Currently, I was able to do a simple simulation in SOFA. Models are prepared in Gmsh. My goal is to transfer all of these processes, including model preparation, in Slicer and SlicerSOFA.
1. Segmentation using TotalSegmentator and DentalSegmentator. Orbital fat tissue and maxillary sinus also need to be added to the model.

<p>
<img src="https://github.com/user-attachments/assets/8cf719a4-304b-4ac8-a010-23bd5f6b91b8" width="200"/><br>
<img src="https://github.com/user-attachments/assets/90be9429-97d6-451e-b9c7-5f9a85c7d32c" width="200"/>
</p>

2. Volumetric model preparation using Gmsh. Plate geometry is too complicated and can only be created in Gmsh but not in SegmentMesher. 

<p>
<img src="https://github.com/user-attachments/assets/334e7775-2bdf-437e-862e-06465ebb1f42" width="180"/><br>
<img src="https://github.com/user-attachments/assets/c950c1df-d0be-4a2d-a1e6-c9d80ed9c50f" width="120"/>
</p>

3. Did a simple orbital tissue retraction in SOFA. The retractor model is created using Fiducial to Model module in Slicer.

<p>
<img src="https://github.com/user-attachments/assets/15d09c71-796f-4a31-9087-afc68fade26d" width="230"/><br>
<img src="https://github.com/user-attachments/assets/f8ca83fe-7308-4d63-8e35-405ba2aa5f25" width="230"/>
<img src="https://github.com/user-attachments/assets/096e04fa-53be-4f08-b786-4e4b5ffcc7bf" width="230"/>
</p>



## Progress and Next Steps

1. General plan is to first learn and design simulation and SOFA, followed by doing simulation using basic SlicerSOFA function in a Slicer scene by simple scripting, and then learn simulation at the SlicerSofa module level.
2. Move & rotate objects using keybaord. Simplify simulation.<br>
[![Watch the video](https://youtu.be/QgoJxyJ06to)](https://youtu.be/QgoJxyJ06to)


3. Using SlicerHeart Baffle Planner to create a 2D model roughly capture the shape of the plate and use Shell plugin for simulate plate bending: 
[![Watch the video](https://youtu.be/QgoJxyJ06to)](https://youtu.be/iLCJW_BHsg8)

4. Testing simple simulation via import Sofa in Slicer Scene
https://youtu.be/3xOu1HUu0Uc
[![Watch the video]([https://youtu.be/3xOu1HUu0Uc])(https://youtu.be/3xOu1HUu0Uc)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img src="https://github.com/user-attachments/assets/5c46f298-f059-4c4c-8114-4f21906f9dd2" width="200"/>

Surgical Guidance using MatrixOrbital preformed plates from DePuy (see below for reference).


<img src="https://github.com/user-attachments/assets/66a054ca-7751-4fe7-8c82-94ab1da61509" width="200"/>

Transconjunctival approach for retracting orbital tissue. From: [https://surgeryreference.aofoundation.org/cmf/pediatric-trauma/midface/orbital-floor/reconstruction](https://surgeryreference.aofoundation.org/cmf/pediatric-trauma/midface/orbital-floor/reconstruction)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Surgical Guidance using MatrixOrbital preformed plates from DePuy Synthesis: [https://www.jnjmedtech.com/en-US/product/matrixorbital-preformed-orbital-plates](https://www.jnjmedtech.com/en-US/product/matrixorbital-preformed-orbital-plates)

