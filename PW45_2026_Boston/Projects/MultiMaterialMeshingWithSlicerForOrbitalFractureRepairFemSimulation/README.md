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


Creating a volumetric mesh is essential for FEM simulation. However, meshing for orbital tissue with fracture is challenging due to multiple thin structures confined in a bony orbit, low CT contrast, and presence of trauma. To ease the process, we prepared a unified multi-material mesh for orbital tissue to avoid dealing with tissue boundaries. We are currently training a preliminary model using MONAI-nnUNet for orbital tissue segmentation using 13 specimens, each of which augmented to 5 additional volumns using TorchIO. We then created a unified orbital tissue segmentation, converted to a surface model, and created a tetrahedral mesh using gmsh. Sub-tissue regions were then selected in SOFA using specific tisssue surface models. Overall, though much easier than creating multiple tissue meshes, this step still requires many manual steps, including segmentation refinement and surface model downsampling and uniform remeshing, in Slicer and gmsh. Furthermore, due to the coarseness of interior tetrahedra, the selected tetrahedra could not accurately reflect internal tissue geometry, creating errors in tissue geometry tracking in simulation. Mesh refinement was used to create finer elements at interior tissue surface but it led to a over-detailed mesh with too many elements.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Imporve nnUNet modeling training for orbital segmentation
2. Streamline mesh preprocessing in Slicer and create a reproducible, standardize segmentation-to-meshing recipe.
3. Improve mesh refinement to balance geometric accuracy and mesh size.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Explore how to construct better TorchIO image augmentation effects for improving model training.
2. Improve thin orbital bone segmentation
3. Explore gmsh and alternative toolkits for mesh size control and refinement
4. Explore using AI agent to streamline and standardize segmentation-to-meshing workflow.




## Progress and Next Steps

Using claude slicer-skill [https://github.com/pieper/slicer-skill](https://github.com/pieper/slicer-skill) to create a prompt to streamline a segmentation to meshing workflow. Overall it took me five hours. 

Initially, I tried to teach it step-by-step. Giving sample outcomes from my own manual preprocessing as ground truth helped.

Steps:
1. Create a combined orbital tissue segment from individual segments
2. Create a 0.5 mm gap between tissue segment & bony orbit: expand the skull by 0.5mm and subtract tissue segment from it
3. Smoothing the segment and removing isolated voxels.
4. Convert combined orbital tissue segment to a surface model and downsample + uniform remesh it to about 1.5k pts
5. Using a customized gmsh script to do the meshing. Redo surface remesh and/or gmsh spacing set up until getting around 10 to 15K tetrahedra.
6. Convert individual tissue segments to models with <1k pts for MeshROI tet selection in SOFA


<img width="637" height="445" alt="image" src="https://github.com/user-attachments/assets/3c33e217-cf09-4ef5-8b91-698a1e5c27f3" />

https://github.com/user-attachments/assets/233a780e-c723-4821-a830-ee283b6d458a

<img width="478" height="744" alt="Screenshot from 2026-06-25 16-44-44" src="https://github.com/user-attachments/assets/a213a2bb-c21f-4f35-8b03-872cb7bf2c5f" />
<img width="457" height="726" alt="Screenshot from 2026-06-25 16-48-19" src="https://github.com/user-attachments/assets/c5d5a531-6e3f-4f17-8145-2ba302f69d4f" />

In the end, it produced a prompt and a script for segmentation and Surface Toolbox effects for reusing.

<img width="693" height="484" alt="Screenshot from 2026-06-24 23-44-17" src="https://github.com/user-attachments/assets/9775d4b2-1420-430f-ac52-db070644ede7" />

I also had to constantly monitor the "thinking" process in case Claude did extra unncessary steps:

<img width="485" height="214" alt="Screenshot from 2026-06-25 00-25-56" src="https://github.com/user-attachments/assets/7649c150-fe3a-47bf-ba52-ca27298faf6f" />

<img width="1360" height="740" alt="Screenshot from 2026-06-25 16-46-15" src="https://github.com/user-attachments/assets/f593e62a-02bb-463d-97ab-4c5181fdbfd6" />


# Illustrations

Segmentation using a preliminary nnUNet model trained via MONAI <br>
<img width="300" alt="image" src="https://github.com/user-attachments/assets/8212cf59-0f20-4861-936c-087d09a63619" />
<img width="300" alt="image" src="https://github.com/user-attachments/assets/8f1d5afe-d086-4b02-abf8-4e7f79f3b553" />

Create a combined uniform tissue segmentation and convert into a surface model <br>
<img width="300" alt="image" src="https://github.com/user-attachments/assets/7ccbc660-30b1-403d-b825-3c1e249e3dd9" />

Convert into a tetrahedral mesh (15k nodes in this case)<br>
<img width="300" alt="image" src="https://github.com/user-attachments/assets/11d006de-55f1-4781-b3e8-b08f738a1fda" />

Assign different material properties in SOFA using surface models: globe, muscles, optic nerve, and orbital fat <br>
<img width="300" alt="image" src="https://github.com/user-attachments/assets/ff4fc457-eeda-4b72-8d23-e9f29bc6e91e" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/a7a3e5d1-45b3-428f-bda0-e88dfb3b267d" />


Further refinement by creating finer elements near tissue surfaces <br>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/2f1898dc-92df-477f-8124-294e97ed6f7b" />



_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

