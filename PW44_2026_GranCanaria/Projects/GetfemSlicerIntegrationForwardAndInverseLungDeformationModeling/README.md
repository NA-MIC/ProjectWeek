---
layout: pw44-project

permalink: /:path/

project_title: GetFEM Slicer integration - Forward and Inverse Lung Deformation Modeling
category: Other
presenter_location: 

key_investigators:

- name: Domenico Riggio
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Johannes Pfeil
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Florian Schulte
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Maria Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project focuses on the integration of 3D Slicer with the GetFEM library to enable forward and inverse finite element (FEM) simulations directly on anatomical models derived from medical imaging. By combining Slicer’s strengths in segmentation, visualization, and user interaction with GetFEM’s FEM capabilities, the project provides a unified environment for biomechanical modeling.

The integrated framework is applied to the study of lung deformation, enabling both direct FEM simulations under prescribed mechanical conditions and inverse FEM analyses aimed at estimating unknown parameters by fitting simulated deformations to a target anatomy. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


The objectives of the project are to:
	•	Integrate GetFEM-based FEM simulations into the 3D Slicer environment.
	•	Enable both forward and inverse FEM analyses on segmented anatomical models.
	•	Provide tools to estimate mechanical parameters through inverse modeling.
	•	Support interactive definition of boundary conditions and loads.
	•	Apply the framework to lung deformation modeling as a representative use case.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


The project starts by establishing a connection between 3D Slicer and GetFEM, allowing segmented anatomical models to be used directly as inputs for FEM simulations, after a proper volumetrization. Users define the deformable model, boundary conditions, and simulation parameters through a graphical interface in Slicer.

For forward FEM, simulations are performed using predefined material properties and pressure values to generate sequences of deformed models. For inverse FEM, a target model is provided, and mechanical parameters are iteratively optimized by comparing the simulated deformation to the target anatomy. Both workflows share common inputs and are accessible through a unified interface.

The plan is to maintain a modular and extensible architecture, enabling future improvements without altering the core integration.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


The integration between 3D Slicer and GetFEM has been successfully established. A functional Slicer extension has been developed, providing a graphical interface for defining models, constraints, and simulation parameters. Both forward and inverse FEM workflows have been implemented and validated on lung models, demonstrating the feasibility of parameter estimation and deformation analysis within the integrated environment.

Next Steps
Future developments will focus on:
	•	Debugging and optimization.
	•	Improving result management and output model handling.
	•	Adding quantitative metrics for evaluating simulation accuracy.
	•	Enhancing visualization of deformation and pressure regions.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1920" height="1048" alt="Image" src="https://github.com/user-attachments/assets/a1dc8d4e-cb4a-4e91-a47a-bb5522055a2f" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- Steve Pieper, SlicerGetFEM, (https://github.com/pieper/SlicerGetFEM)[[https://github.com/pieper/SlicerGetFEM]

