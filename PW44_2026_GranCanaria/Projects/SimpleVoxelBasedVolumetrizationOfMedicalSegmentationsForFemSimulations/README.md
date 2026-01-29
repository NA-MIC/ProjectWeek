---
layout: pw44-project

permalink: /:path/

project_title: Simple Voxel-Based Volumetrization of Medical Segmentations for FEM simulations
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Domenico Riggio
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Laura Lichtlein
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Maria Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project provides a simple and robust voxel-based volumetrization tool for medical models obtained from image segmentation.
Its primary goal is to enable fast simulation prototyping by converting segmented anatomical structures into simulation-ready volumetric representations, without requiring mesh cleaning, manual corrections, or complex tetrahedral meshing procedures (e.g., TetGen).

By avoiding strict mesh quality constraints, the approach allows researchers and students to quickly test segmented models in FEM and physics-based simulations, even when surface meshes are imperfect or non-manifold.
The pipeline is designed as a low-barrier, lightweight solution that prioritizes usability, reproducibility, and rapid iteration over highly optimized meshing accuracy.

The tool is particularly suited for early-stage experimentation, educational use, and proof-of-concept simulations, where fast feedback and robustness are more critical than advanced mesh optimization.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


The objective of this project is to develop a simple, robust, and accessible volumetrization tool that enables the rapid conversion of medical segmentations into simulation-ready volumetric models.
The project specifically targets scenarios in which traditional surface-based meshing pipelines are impractical due to strict mesh quality requirements, extensive manual cleaning, or frequent meshing failures.

The project aims to:
	•	Enable fast testing of segmented anatomical models without requiring mesh cleaning or complex preprocessing.
	•	Avoid traditional surface-based meshing pipelines that depend on high-quality clean processed meshes.
	•	Generate voxel-based volumetric representations that are robust to imperfect or noisy segmentations.
	•	Support rapid prototyping and early-stage simulations, where ease of use and speed are more important than mesh optimization.
	•	Allow users to move from segmentation to simulation with minimal effort.

The overall goal is to lower the barrier to simulation, making it easier to explore segmented models in a FEM environment within a short time.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


The project adopts a simple and user-oriented approach to transform segmented anatomical models into volumetric representations that can be quickly tested in simulations. The focus is on minimizing preprocessing effort and avoiding complex meshing steps, allowing users to move directly from segmentation to a usable volumetric model.

The workflow is designed to be intuitive: users select a model, choose a voxel size, and generate a filled volumetric representation that can be visualized and exported. 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Progress:
A complete and functional workflow is already available within 3D Slicer. The extension allows users to scale models, generate voxel-based volumetric representations with a chosen resolution, and export the results in common formats for further processing or simulation.

The current version enables fast testing of segmented models, even when the original surfaces are imperfect, making it suitable for early-stage experimentation and educational use. The foundation is now in place to build additional features that improve compatibility with simulation pipelines and provide users with better control and feedback, while preserving the simplicity of the original approach

Next steps:
	•	Test with SofaSlicer extension and other FEM frameworks.
	•	Hexahedral-to-tetrahedral conversion (post-voxelization)
Add a method to convert the voxel grid (hexahedral elements) into a tetrahedral volumetric mesh. This could be implemented as a dedicated step after voxelization, or integrated through/alongside Slicer’s existing meshing tools (e.g., extending the Segment Mesher workflow) to provide a “tetrahedral export” option.
	•	Quality and fidelity metrics vs. the original model (pitch-dependent)
Introduce validation metrics to quantify how well the voxel-based volumetric model represents the original segmented anatomy for a given pitch. The goal is to provide objective feedback to help users choose an appropriate voxel size, balancing accuracy and computational cost.
	•	Intersection voxel removal
Implement a function to detect and remove voxels generated in overlapping regions (e.g., intersections between multiple segments or between separate models). This cleanup step should help produce non-overlapping volumetric representations and reduce artifacts before simulation.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1509" height="906" alt="Image" src="https://github.com/user-attachments/assets/f5c989e6-b84a-4656-af6a-373736fd3700" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

