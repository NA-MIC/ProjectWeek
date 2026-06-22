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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




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
<img width="300" alt="image" src="https://github.com/user-attachments/assets/a7a3e5d1-45b3-428f-bda0-e88dfb3b267d" />


Further refinement by creating finer elements near tissue surfaces
![Uploading image.png…]()


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

