---
layout: pw42-project

permalink: /:path/

project_title: 'TorchXRayVision Meets 3D Slicer: Bridging Deep Learning and Medical Imaging'
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Constantin Constantinescu
  affiliation: Lucian Blaga University of Sibiu
  country: Romania

- name: Juan Ruiz-Alzola
  affiliation: University of Las Palmas de Gran Canaria
  country: Spain

- name: Csaba Pintér
  affiliation: EBATINCA
  country: Spain
  
- name: Oscar Martin
  affiliation: EBATINCA
  country: Spain

- name: Borja Fernandez
  affiliation: EBATINCA
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project focuses on developing a 3D Slicer module for the automatic processing of chest X-rays, integrating powerful deep learning capabilities provided by TorchXRayVision. The module streamlines radiological analysis by offering the following features:

- Segmentation: Automatically identify and outline anatomical regions in chest X-rays, such as lungs or other structures.
- Anomaly Detection: Detect abnormalities and highlight regions of interest for further investigation.
- Pathology Classification: Classify pathologies such as pneumonia, atelectasis, or other common conditions.

By combining the advanced machine learning models from TorchXRayVision with the versatile 3D Slicer platform, this module aims to provide a robust tool for clinicians and researchers to enhance diagnostic workflows, reduce manual workload, and improve consistency in radiological interpretation.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. A 3D Slicer Module
2. TorchXRayVision models included in the module
3. Torch XRays automatic segmentation, anomaly detection and pathology classification
4. Heatmaps




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a Slicer Module 
2. Create an interface to upload X-Rays and perform automatic analysis
3. Use TorchXRayVision framework to perform automatic analysis
4. Compute heatmaps




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Creating a 3D Slicer Module
2. Building the interface
3. Including the TorchXRayVision models
4. Incorporate mechanisms to facilitate the interpretability of the predictions made by the models





# Illustrations

Loading the X-Ray Image:
<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![1](https://github.com/user-attachments/assets/e70dd149-885b-4674-ae5e-7f6a959d2084)

Running automatic analysis:
![2](https://github.com/user-attachments/assets/a694a23c-aaf3-4e6f-8101-8f955bfe336f)

View segmentation:
![3](https://github.com/user-attachments/assets/87216562-bc43-4578-8295-7bbf95ba5450)

Pathologies scores and heatmap validation:
![4](https://github.com/user-attachments/assets/7965821f-d508-4f1d-bdc8-8063e78adef0)


![5](https://github.com/user-attachments/assets/c114764a-ddbc-4054-9fa4-bfe701ea6287)


# Background and References

https://github.com/mlmed/torchxrayvision

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


