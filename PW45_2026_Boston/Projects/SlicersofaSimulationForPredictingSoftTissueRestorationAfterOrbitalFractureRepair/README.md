---
layout: pw45-project

permalink: /:path/

project_title: SlicerSOFA simulation for predicting soft tissue restoration after orbital fracture
  repair
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M College of Dentistry
  country: USA

- name: Andrew Read-Fuller
  affiliation: Texas A&M College of Dentistry
  country: USA

- name: Rafael Palomar
  affiliation: NTNU / OUH
  country: Norway

- name: Paul Baksic
  affiliation: INRIA
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Orbital fractures are typically caused by blunt-force trauma. Fracture repair frequently requires placing a titanium plate to reconstruct bony orbit and restore tissue position and function from disturbed conditions, such as enophthalmos ("sunken eye") and muscle entrapment & conformational changes. 

This project aims to develop a reproducible and scalable patient-specific SOFA/SlicerSOFA FEM simulation workflow to predict orbital soft tissue restoration after fracture repair using a preformed titanium plate.The simulation processes span across multiple scenes from retracting orbital tissue to place a plate and then let the tissue fall onto the plate. The only deformable object is a unified multi-material orbital tissue mesh. Tetrahedrons inside different tissue regions to assign with different material properties. The retracting tool, plate, and bony orbit are all simulated as rigid bodies.

Currently, it still relies on many steps of manual set up in Slicer, including retraction plane position and moving trajectory and distances, attachment points, input/output across staged scenes, and tissue-bone attachment points.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The main objective is to streamline workflow reproducibility and improve efficiency for patient-specific simulation:
1. Streamlining setting & simplifying constraints and boundary conditions for patient-specific simulation, including bone-tissue attachment, collision simplification, retracting moving trajectories and retraction stages, and transitions across scenes.
2. Tracking, quantifying, and visualize tissue position and shape change.
3. Use Slicer methods to facilitate simulation setup, smooth transitions across multiple scenes, outcome visualization, and parameter tuning.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Implement Slicer methods to:
1. Initiate a SlicerSOFA-based module prototype to streamline scene setup and interaction, such as tissue bone attachment, syncing the interactive transform with the SOFA controller, retraction trajectories, and collision regions
2. Track and visualize tissue deformation, such as using TPS, grid transform, and mark up-based methods.
3. Facilitate performance tracking and parameter tuning & method selection in SlicerSOFA (e.g., exploring using AI agents)


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Fat herniation and inferior rectus muscle conformational changes in floor fx<br>
<img width="400" halt="image" src="https://github.com/user-attachments/assets/761de370-d5b6-4e52-9b29-3e7e42be01fe" />

Create a multi-material mesh from a combined orbital tissue surface model from segmentations using Gmsh.<br>
<img width="300" alt="Screenshot from 2026-05-11 15-56-43" src="https://github.com/user-attachments/assets/4baf2e0b-2aa6-42d8-8fbb-21bcbe9e02a5" />
<img width="300" alt="Screenshot from 2026-05-11 16-01-20" src="https://github.com/user-attachments/assets/6b4d494e-234b-4bb1-8136-01d5510beec5" />

Orbital tissue attachment points at the superior surface set up in Slicer and visualized in SOFA<br>
<img width="300" alt="image" src="https://github.com/user-attachments/assets/9d7a8100-d3a3-4e5c-8a2e-91ad1f67f537" />
<img width="300" alt="Screenshot from 2026-06-03 08-29-36" src="https://github.com/user-attachments/assets/0410b324-f338-4eeb-acf1-5ac5e6aabcd6" />

Simulation of tissue retraction using plane models in SOFA (skull hidden) and the same process in Slicer SOFA. The left picture shows one plane holds one area of the tissue to enable another plane for further retraction.<br>
<img width="300" alt="Screenshot from 2026-06-08 16-53-29" src="https://github.com/user-attachments/assets/825565a5-a6cf-425c-a31e-663681b4b70a" />
<img width="300" alt="image" src="https://github.com/user-attachments/assets/af9db4b1-d37a-4e8f-a16d-64acbd4bf85d" />

Tissue restoration onto the plate<br>
<img width="300" alt="Screenshot from 2026-06-10 11-37-40" src="https://github.com/user-attachments/assets/9654a234-6d05-4d87-8984-82a3add9c35a" />
<img width="300" alt="Screenshot from 2026-06-10 11-39-07" src="https://github.com/user-attachments/assets/06a22496-2f09-43f4-874c-b9b60991f2dd" />

Tracking and visualizing globe & inferior rectus changes after restoration (not very accurate though):<br>
<img width="600" alt="Screenshot from 2026-06-11 17-39-30" src="https://github.com/user-attachments/assets/096f4d10-3875-4754-9553-9726e2a7bec2" />


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

