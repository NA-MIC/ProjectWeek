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

- name: Ciro Benito Raggio
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


### Progress:
- Improved the user interface to enhance usability and workflow clarity.
- Added export functionality for volumetric meshes in `.vtk` and `.msh` formats.
- Performed extensive code refactoring and systematic bug fixing to improve module stability and robustness.
- Implemented quality and fidelity metrics to quantitatively assess the voxelized volumetric model against the original segmentation.  
  These validation metrics provide objective feedback on how accurately the voxel-based representation preserves anatomical features for a given voxel pitch, supporting informed trade-offs between geometric accuracy and computational cost.
- Discussed and evaluated the integration of the proposed approach within the **Segment Mesher** extension developed by Lasso *et al.* [1].

You can try this extension here: https://github.com/DomenicoRiggio/SlicerModelsVoxelization

### Next Steps:
- Integration within the **Segment Mesher** extension developed by Lasso *et al.* [1].
- Test compatibility and performance with the **SofaSlicer** extension and other FEM-based simulation frameworks.
- Intersection voxel removal: implement a dedicated function to detect and remove voxels generated in overlapping regions (e.g., intersections between multiple segments or between separate models). This preprocessing step aims to ensure non-overlapping volumetric representations and to reduce numerical artifacts prior to simulation.

---

### Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img width="3932" height="2360" alt="before" src="https://github.com/user-attachments/assets/da3689c9-e0ba-4905-bd9b-243d6d832f53" />

<img width="3923" height="2360" alt="After" src="https://github.com/user-attachments/assets/3cdf45fe-2d92-493c-9022-fa52971e41e2" />


---

### Background and References

<!-- If you developed any software, include links to the source code repository.
     If possible, also add links to sample data and relevant publications. -->

[1] Lasso, A., *et al.* **Segment Mesher** – A 3D Slicer extension for generating volumetric meshes from segmentation data.  
GitHub repository: https://github.com/lassoan/SlicerSegmentMesher

