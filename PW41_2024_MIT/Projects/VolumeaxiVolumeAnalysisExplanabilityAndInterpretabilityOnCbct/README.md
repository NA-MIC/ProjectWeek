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

Artificial Intelligences offer a wide range of applications. There is more and more research about its uses in the medical field and especially on patient images. The question of trustworthiness is on every mind, every time a prediction is given. For that reason, we propose to develop **interpretable deep learning models** for the automated classification of impacted maxillary canines and assessment of root resorption in adjacent teeth using Cone-Beam Computed Tomography (CBCT). 
Deep learning models based on Convolutional Neural Network (CNN) architectures were developed and evaluated for classifying impacted maxillary canine position and detecting root resorption. Gradient-weighted Class Activation Mapping (Grad-CAM) was integrated to generate visual explanations of the CNN predictions, enhancing interpretability and trustworthiness for clinical adoption.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


We are using MONAI frameworks in this project.

1. Data Preparation and Pre-processing
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

1. Trained models with DenseNet architecture to classify the bucolingual position of the impacted maxillary canine and to classify the root resorption.
2. Implementation of GRAD-CAM with MONAI for visualization


Next Steps:
1. Find the best hyper-parameters for the given application to improve the results
2. Deploy a module or an extension in 3D Slicer 


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


#### Well predicted case
Class 1 predicted as a class 1. (right impacted canine)
![Screenshot from 2024-06-18 11-59-48](https://github.com/NA-MIC/ProjectWeek/assets/91120559/16cadc2c-0a22-4257-af1a-d07e252888ac)

The number of layers included change the precision of the focus on the tooth:
![MN099_classIdx_1_slice_120](https://github.com/NA-MIC/ProjectWeek/assets/91120559/3664c3ba-4cea-4adf-83fe-724ff37c3682)





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[VolumeAXI repository](https://github.com/Jeanneclre/VolumeAXI)

