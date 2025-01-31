---
layout: pw41-project

permalink: /:path/

project_title: Visual Model for Respiratory Motion of Airways with SOFA-Slicer
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Quinn Williams
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Rafael Palomar
  affiliation: Oslo University Hospital / NTNU
  country: Norway

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Integration of a softbody physics simulation of lung movement during breathing in SOFA into slicer. It will be used as a virtual reference for bronchoscopy alongside streamed camera data.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Integrate current simulation into the slicer with the slicer-SOFA extension
2. Refine the respiratory motion
3. Create UI elements to control breathing parameters
4. Sync camera position data with a virtual camera in the airways
5. Define a standard pipeline from segmentation to simulation for further bronchoscopy procedures




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Talk with slicer-sofa devs to understand the communication with sofa and slicer
2. Talk with SOFA devs for advice on lung physics in SOFA
3. Script the UI elements for the simulation
4. Figure out whether creating a virtual camera is benificial
5. Create a write-up on the process used to create the simulation and how to recreate it




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Created a module for slicerSOFA extension
2. Created scene for lung simulation with lung vtk mesh
3. Created UI elements to control simulation parameters(breathing force, period, youngs modulus)
4. Updated collision parameters for ribs

Next steps:
1. fix rib collisions
2. allow rib movement during breathing
3. fix simulation caching
4. create a transformation for the airway segmentation based on the lung deformation




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Current Lung Simulation in Slicer

<video
  controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/63506358/14216829-f656-432d-a001-b0d52a27e386"
  style="max-height:640px; min-height: 200px">
</video>






Old Version in SOFA:

![Current airway movement simulated with SOFA](https://github.com/NA-MIC/ProjectWeek/assets/63506358/2e408192-19b0-477f-8939-5a102cd10cff)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
- Lung Simulation Module for slicerSOFA
  - https://github.com/Quilliams85/Lung-Simulation-Module-SlicerSOFA.git

- Old airway sofa simulation
  - [https://github.com/Quilliams85/Lung-Simulation-SNR-Lab.git](https://github.com/Quilliams85/Lung-Simulation-SNR-Lab.git)
