---
layout: pw43-project

permalink: /:path/

project_title: Improvements of SlicerTMS
category: Infrastructure

key_investigators:

- name: Lipeng Ning
  affiliation: Brigham and Women's Hospital and Harvard Medical School
  country: USA

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

- name: Tae Young Park
  affiliation: TruAbutment Inc.
  country: USA

- name: Daniel Haehn
  affiliation: University of Massachusetts Boston
  country: USA

- name: Benjamin Zwick
  affiliation: The University of Western Australia
  country: Australia

- name: Satya Barak
  affiliation: The University of Western Australia
  country: Australia

- name: Cameron Paterson
  affiliation: The University of Western Australia
  country: Australia

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The SlicerTMS project has been developed to predict the electric field induced by transcranial magnetic stimulation by using deep neural networks and magnetic resonance imaging data. In this project week, we further develop the software to improve the performance and integrate additional functions into this module.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Improve the overall software architecture for integration with other electric field solvers.
2. Objective B. Develop and test an example on the integration of the SimNIBS solver. 
3. Objective C. Validate and update the sampling algorithms in SlicerTMS and improve the file I/O strategy for vector nifti files.
4. Objective D. Discuss and improve the integration with neuronavigation and other fast segmentation and meshing techniques.
5. Objective E. Investigate the use of markerless tracking of the patient head and TMS probe for neuronavigation.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Meet to review existing SlicerTMS software structure and other external solvers (e.g., SimNIBS).
2. Discuss and prototype an improved architecture.
3. Compare the vtk-based resampling with SimNIBS to improve the accuracy of SlicerTMS models.
4. Talk with other teams about related toolboxes, e.g., OpenIGTLink, for improvement.



## Progress and Next Steps

A very productive week!
* We discussed our TMS work with the community in relation to other navigation, TMS, and FEM projects
* We investigated and now better understand SimNIBS mesh file format conventions for gray/white matter and other tissue
* We tested and expanded our RPyC-based integration of SimNIBS with 3D Slicer for simulation of TMS.
* A small test model (~22K tetrahedra) can be simulated in real-time in SlicerTMS with a SimNIBS back end.
* A "clinical grade" simulation (~4M tetrahedra) can be simulated in about 3 seconds a frame.
* A reduced resolution field simulation with a full resolution anatomical display can be displayed in approximately 1 second per frame.
* The simulation was extended to include additional TMS coil configurations and display of the model in 3D Slicer.
  
![image](https://github.com/user-attachments/assets/c09f2676-030f-4843-96db-e36f68d0f73f)

Next steps:
* Now we can extend our previous work by training and testing our real-time deep learning approximations to the FEM results "head to head" in a common software environment to assess accuracy and performance tradeoffs
* We have ordered navigation equipment so we can leverage the NousNav infrastructure to simulate navigated TMS
* We will work to incorporate our previous work into the new integrated framework:
    * We will experiment with volume rendering and other e-field visualization methods
    * We will explore the integration of SlicerDMRI tractography technology to investigate the white matter tracts influenced by TMS therapy
* We will extend our previous work
    * We will work to integrate new segmentation methods, such as the new version of SynthSeg that can generate full-head tissue segmentations for a wider range of input data, possibly making patient-specific head models less expensive and thus expanding the availability of more precise TMS
    * We will test novel tetrahedral mesh generation technology being developed by Will Schroeder at Kitware based on Sarah Frisken's SurfaceNets approach
    * We will work with the NousNav team to optimize the price/performance of tracking cameras and related technologies in the hopes of making patient-specific neuronavigated TMS more widely available, with the possible outcome of improved patient response to therapy
    * We will work with neurology and other specialties to better understand the challenges and potential applications
    * We will streamline the user interface to facilitate experiments in these areas


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [SlicerTMS GitHub Repository](https://github.com/SlicerTMS/SlicerTMS)
- [3D Slicer](https://github.com/Slicer/Slicer)
- [Real-Time Visualization of TMS-evoked Potentials PW 40 Project](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/RealTimeVisualizationOfTmsEvokedPotentials/)

