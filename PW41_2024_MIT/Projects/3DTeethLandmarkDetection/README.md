---
layout: pw41-project

permalink: /:path/

project_title: 3D Teeth Landmark Detection
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

- name: Lucie Dole
  affiliation: University of North Carolina
  country: USA

- name: Florian Davaux
  affiliation: University of North Carolina
  country: USA

- name: Jeanne Claret
  affiliation: University of Michigan
  country: USA

- name: Gaëlle Leroux
  affiliation: University of Michigan
  country: USA

- name: Lucia Cevidanes
  affiliation: University of Michigan
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


## Background:

Accurate landmark identification is crucial in various dental procedures. Manual identification is time-consuming and prone to errors. An AI-driven model will automate this process, offering a reliable, scalable solution.

## Goals:

1. Develop an Accurate Model: Use advanced machine learning algorithms for high-precision landmark identification.
2. Training and Validation: Train using the 3DTeethLand-MICCAI2024 dataset and validate with diverse samples.
3. Integration: Seamlessly integrate with other dental software.
4. User Interface: Create an intuitive interface in 3D Slicer for this new extension


## Methodology:

Data Collection: Use the 3DTeethLand-MICCAI2024 dataset, containing annotated 3D dental models.
Model Development: Employ deep learning techniques, such as convolutional neural networks (CNNs), to develop the model.

## Validation and Testing: 

Perform extensive testing with validation datasets to ensure robustness and accuracy.
Software Integration: Collaborate with dental software developers for smooth integration.
User Training: Provide training and support for effective model utilization.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Develop and validate an advanced AI model to accurately identify anatomical landmarks in dental models, enhancing precision in dental treatments, diagnostics, and educational applications.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


## Day 1 

### Data Download & Preprocessing and Exploration

Download the 3DTeethLand-MICCAI2024 dataset and explore the data structure. Visualize landmarks, surface models and setup the data for training. 

## Day 2: Model Development, Training, and Testing

### ShapeAXI models for shape analysis

Use point cloud (PC) and multi-view approaches for shape analysis. 

### Initial Model Training:
Begin training the model using the preprocessed dataset.

## Day 3: Model Validation and Fine-Tuning

### Model Validation and model refinement

- Hyperparameter Tuning
- Architecture changes

## Day 4: Integration, UI Development

### UI Design and Implementation:

Create a basic user interface in 3D Slicer.
Documentation and Presentation Preparation.
        
## Key Deliverables by End of Week:

- Preprocessed and augmented dataset.
- CNN model implemented and trained in PyTorch.
- Validated and tested model with performance metrics.
- APIs/plugins for integration with dental software.
- Functional UI in 3D Slicer.
- Project documentation and presentation materials.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Download the data.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![image](https://github.com/NA-MIC/ProjectWeek/assets/7086191/4732bb2b-b24f-4833-91c0-ca1b8f519b07)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Baquero, Baptiste, Maxime Gillot, Lucia Cevidanes, Najla Al Turkestani, Marcela Gurgel, Mathieu Leclercq, Jonas Bianchi et al. "Automatic Landmark Identification on IntraOralScans." In Workshop on Clinical Image-Based Procedures, pp. 32-42. Cham: Springer Nature Switzerland, 2022.


# Results of the approach

![image](https://github.com/NA-MIC/ProjectWeek/assets/7086191/02a65a32-940c-4284-b3d9-cb68d5789aff)
![image](https://github.com/NA-MIC/ProjectWeek/assets/7086191/9bcde2d2-3209-4ba5-9d24-60bb97f91a27)

<img width="797" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/7086191/cbb3688e-8158-479a-b468-cb42a22ee146">




