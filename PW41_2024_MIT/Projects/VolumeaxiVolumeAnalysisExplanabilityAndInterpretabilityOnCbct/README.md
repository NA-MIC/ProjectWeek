---
layout: pw41-project

permalink: /:path/

project_title: VolumeAXI - Volume Analysis, Explanability and Interpretability on CBCT
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Jeanne Claret
  affiliation: University of Michigan
  country: USA

- name: Gaëlle Leroux
  affiliation: University of Michigan
  country: USA

- name: Lucia Cevidanes
  affiliation: University of Michigan
  country: USA

- name: Claudia Mattos
  affiliation: University of Michigan
  country: USA

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Volume Analysis, eXplainability and Interpretability, Volume-AXI, is an explainability approach for classification of bone and teeth structural defects in CBCT scans gray-level images. We propose to develop interpretable AI algorithms to visualize diagnostic features in dental and craniofacial conditions. This work is built on neural network models in Python, specifically using the MONAI framework.

The first clinical application of Volume-AXI is related to dentistry, aiming to identify the position of tooth impaction and damage to adjacente structures.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Create AI algorithms capable of visualizing diagnostic features in dental and craniofacial conditions using CBCT (Cone Beam Computed Tomography) scan gray-level images.
2. Integrate the developed AI algorithms with clinical workflows.
3. Enhancing Explainability and Interpretability in Medical Imaging by deploying a module in 3D Slicer



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Data Preparation and Pre-processing

2. Model Development and Training: Explore and select appropriate neural network architectures (e.g., ResNet, SENets) for image classification and feature visualization.

3. Explainability and Visualization Techniques: Implement methods to make AI decisions transparent and understandable such as Grad-CAM.

4. Validation and Testing

5. Documentation and Training: Create comprehensive documentation and user guides explaining the functionality and benefits of the AI tools.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Trained preliminary models with SENets to classify the position of the impacted tooth
2. Implementation of GRAD-CAM with MONAI
3. creation of Volume to visualize in 3D Slicer, slice by slice

Next Steps:
1. Finish implementation of a Cross Validation
2. Find the best hyper-parameters for the given application to improve the results
3. Work on another application
5. Deploy a module or an extension in 3D Slicer 



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


#### Well predicted case
![GRADCAM well predicted class](https://github.com/NA-MIC/ProjectWeek/assets/91120559/fcdbcbeb-e67d-4651-826d-17d03c072466)

#### Same case in 3D Slicer
![Volume seen in 3D Slicer](https://github.com/NA-MIC/ProjectWeek/assets/91120559/3253216d-ca98-469f-a6c1-57d6121603f6)





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[VolumeAXI repository](https://github.com/Jeanneclre/VolumeAXI)

