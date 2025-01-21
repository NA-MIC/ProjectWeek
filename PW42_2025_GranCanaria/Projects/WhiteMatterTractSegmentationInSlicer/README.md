---
layout: pw42-project

permalink: /:path/

project_title: White matter tract segmentation in Slicer
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Robin Peretzke
  affiliation: German Cancer Research Center
  country: Germany

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Diffusion MRI and white matter tract segmentation play a crucial role in many scenarios such as neurosurgery and psychiatry. Although fully automated methods for tract segmentation have been developed, they may fail in specific scenarios, such as cases with significant anatomical deviations caused by tumors, or they lack generalization across diverse species. In these situations, segmentation is typically carried out by human experts. This process is highly time-consuming, challenging to reproduce, and heavily reliant on graphical user interfaces (GUIs) designed for intuitive interaction.

The aim of this project is to enhance the usability of 3D Slicer for white matter tract segmentation and interaction. Improvements will focus on creating more intuitive tools for user interaction and integrating novel algorithms into the software to streamline the segmentation process.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Objective A
Familiarizing with the existing SlicerDMRI infrastructure is essential, including understanding its current capabilities and workflows. This process involves building a new module while ensuring packages and libraries are updated to maintain compatibility and performance.

Objective B
Exploring and implementing simple white matter tract dissection interactions, such as boolean operations with fibers and regions of interest (ROIs), to improve interactivity and usability within the platform.

Objective C
Investigating and incorporating additional (semi-)automatic tract segmentation algorithms into SlicerDMRI to extend its functionality and better support complex use cases (such as atTRACTive¹)





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. The first step involves exploring the SlicerDMRI architecture, existing documentation, and module-building workflows. Efforts will focus on understanding the integration of relevant libraries and updating packages as needed. This step is fundamental for further developing.

2. Work will focus on enabling basic operations, such as boolean interactions between fibers and ROIs. 

3. The aim is to explore and implement additional tract segmentation algorithms that align with the SlicerDMRI framework.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[1] Peretzke, Robin, et al. "atTRACTive: semi-automatic white matter tract segmentation using active learning." International Conference on Medical Image Computing and Computer-Assisted Intervention. Cham: Springer Nature Switzerland, 2023. [arxiv version](https://arxiv.org/abs/2305.18905)

