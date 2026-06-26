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

1. Convert a SOFA scene into a Slicer scene and created a prototype module using SlicerSOFA infrastructure
2. Use sequence module to generate a playback sequence recording.<br>
[Screencast from 06-25-2026 09_59_22 PM.webm](https://github.com/user-attachments/assets/1cbec52b-194e-46c7-8a3b-b2b621fb20eb)

<img width="768" height="432" alt="Screencast from 06-25-2026 09_59_22 PM webm" src="https://github.com/user-attachments/assets/75b7209e-9d93-4363-8b6e-1acfe5b18f15" />

<img width="768" height="432" alt="Screencast from 06-25-2026 09_59_22 PM webm (1)" src="https://github.com/user-attachments/assets/a226a13b-18e3-4f02-8156-07ec1e41e2b2" />

<img width="640" height="360" alt="Recording 2026-06-26 002342" src="https://github.com/user-attachments/assets/af7ab06f-c669-462a-8fd3-a889a9ccfab0" />



2. Newton Physics demo

[Screencast from 06-25-2026 04_26_48 PM.webm](https://github.com/user-attachments/assets/c44a0bf2-3d30-4b52-afb7-4c17c164d9e2)

<img width="768" height="432" alt="Screencast from 06-25-2026 04_26_48 PM webm" src="https://github.com/user-attachments/assets/95625807-6fbf-4bea-b9b6-ea22ea058314" />


Next steps
- Continue improve workflow reproducibility and gui for fracture cases
- Compare outcome with post-op images for more optimization and improvment.

# Illustrations
<img width="1411" height="532" alt="Screenshot 2026-06-26 003232" src="https://github.com/user-attachments/assets/241d7938-4b61-42e1-b402-16a42be4b926" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

