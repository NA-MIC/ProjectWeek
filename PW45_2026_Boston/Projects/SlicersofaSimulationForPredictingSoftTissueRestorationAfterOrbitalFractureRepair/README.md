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

This project aims to develop a reproducible patient-specific SOFA/SlicerSOFA FEM simulation workflow to predict orbital soft tissue restoration after fracture repair using a preformed titanium plate. 

The simulation processes span across multiple scenes from retracting orbital tissue to place a plate and then let the tissue fall onto the plate. The only deformable object is a unified multi-material orbital tissue mesh. The retracting tool, plate, and bony orbit are all simulated as collision-only boundary conditions. 

Currently, collision constraints computation has been identified as a major simulation bottleneck because orbital tissue is confined in the bony orbit. Tissue in fracture orbit also has localized protrusions representing fat herniation that have to be retracted.

Another difficulty is about scene setups and parameter tuning, such as boundary conditions and constraints, including bone-tissue attachment and retracting tool moving trajectory and contour, and experimenting with different parameters and methods. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The main objective is to streamline workflow reproducibility and improve efficiency for patient-specific simulation:
1. Streamlining setting & simplifying constraints and boundary conditions for patient-specific simulation
2. Tracking, quantifying, and visualize tissue position and shape change.
3. Facilitate smooth transition across different SOFA scenes in Slicer and improve interactive simulation.
4. Facilitate parameter tuning, method selection, and performance tracking within Slicer



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Implement Slicer methods to:
1. Streamline scene setup and interaction, such as tissue bone attachment, syncing the interactive transform with the SOFA controller, retraction trajectories, and collision regions
2. Track and visualize tissue deformation, such as using TPS, grid transform, and mark up-based methods.
3. Facilitate performance tracking and parameter tuning & method selection in SlicerSOFA (e.g., exploring using AI agents)
4. Initiate creating a Slicer module based on SlicerSOFA for multi-scene simulation



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="300" alt="Image" src="https://github.com/user-attachments/assets/f3288dea-a17f-4d2f-95ae-3ea9bfc94292" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

