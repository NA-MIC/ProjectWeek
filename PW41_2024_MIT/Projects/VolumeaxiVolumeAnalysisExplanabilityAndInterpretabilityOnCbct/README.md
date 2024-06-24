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

This project aims to develop interpretable deep learning models for the automated classification of impacted maxillary canines and assessment of dental root resorption in adjacent teeth using Cone-Beam Computed Tomography (CBCT). Impacted maxillary canines (IC) are a common clinical problem that can lead to complications if not diagnosed and treated early. We propose to develop a 3D slicer module, called Volume Analysis, eXplainability and Interpretability (Volume-AXI), with the goal of providing users  an explainable approach for classification of bone and teeth structural defects in CBCT scans gray-level images. We test various deep learning models based on Monai Convolutional Neural Network (CNN) architectures to classify  impacted maxillary canine position and detect root resorption. Gradient-weighted Class Activation Mapping (Grad-CAM) has already been  integrated to generate visual explanations of the CNN predictions, enhancing interpretability and trustworthiness for clinical adoption. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Classify tooth position within the bone using the Monai Densenet 121 and 201.
2. Enhance Explainability and Interpretability of the Classification by generating salience maps  using  Monai GradCAM 
3. Create the VolumeAXI 3D Slicer module and deploy the model as part toe the Slicer automated Dental tools extension




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Data Preparation and Pre-processing
2. Model Development and Training: Explore and select appropriate neural network architectures (e.g., ResNet, SENets, DenseNet) for image classification and feature visualization.
3. Explainability and Visualization Techniques: Implement methods to make AI decisions transparent and understandable such as Grad-CAM.
4. Validation and Testing
5. Documentation and Training: Create comprehensive documentation and user guides explaining the functionality and benefits of the AI tools.





## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Trained models with DenseNet architecture to classify the buccolingual position of the impacted maxillary canine.
2. Implementation of GRAD-CAM with MONAI for visualization
   
Next Steps:
1. Test different architectures and methods to classify root resorption.
2. Find the best hyper-parameters for the given applications to improve the results
3. Clean and organise the code
4. Deploy the models as a module extension in 3D Slicer
5. Write the documentation and provide examples to use the code.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


#### Well predicted case


![Position_grouped](https://github.com/NA-MIC/ProjectWeek/assets/91120559/46528c60-eb97-4011-953a-7d03f9671fbb)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[VolumeAXI repository](https://github.com/Jeanneclre/VolumeAXI)

