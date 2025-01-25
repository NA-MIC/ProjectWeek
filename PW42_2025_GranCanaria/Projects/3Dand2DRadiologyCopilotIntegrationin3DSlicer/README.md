---
layout: pw42-project

permalink: /:path/

project_title: 3D and 2D Radiology Copilot Integration in 3D Slicer
category: Segmentation / Classification / Landmarking

key_investigators:
- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK
- name: Andras Lasso
  affiliation: Queen's University
  country: Canada  
- name: Vishwesh Nath
  affiliation: NVIDIA
  country: US
- name: Nigel Nelson
  affiliation: NVIDIA
  country: US
- name: Sean Huver
  affiliation: NVIDIA
  country: US
- name: Mingxin Zheng
  affiliation: NVIDIA
  country: China
- name: Wenqi Li
  affiliation: NVIDIA
  country: UK
---

# Project Description

This project aims to create the first 3D and 2D radiology copilot in 3D Slicer by developing a module that can consume REST APIs of radiology copilots. The main goal is to demonstrate the benefits of using the NVIDIA Holoscan platform for deploying AI models in medical imaging applications.

## Objective

1. Develop a 3D Slicer module that integrates with radiology copilots via REST APIs.
2. Showcase the capabilities of the NVIDIA Holoscan platform for AI model deployment in medical imaging.
3. Implement functionality to send 3D volumes to the copilot, ask questions, and receive insights.

## Approach and Plan

1. Create a new 3D Slicer module that can communicate with REST APIs - Repository: [https://github.com/diazandr3s/VLM/tree/radcopilot/plugins/RadCoPilot_Slicer](https://github.com/Project-MONAI/VLM/tree/main/plugins/RadCoPilot_Slicer)
2. Integrate the private model trained by East River Imaging and NVIDIA using the RadImageNet dataset.
3. Implement support for the MONAI VILA-M3 model.
4. Develop a user interface within the module to allow sending 3D volumes, asking questions, and displaying copilot insights.
5. Optimize the module's performance using the NVIDIA Holoscan platform.

## Progress and Next Steps

1. Initial project setup and team coordination completed.
2. Research on integrating REST APIs within 3D Slicer modules conducted.
3. Preliminary design of the user interface drafted.

# Illustrations

![3](https://github.com/user-attachments/assets/10090a5c-1307-48ad-87a4-8f22e8a3331d)

[video](https://github.com/user-attachments/assets/0d9fd2c6-ef26-4d14-851e-c761bb218ea7)



# Background and References

- NVIDIA Holoscan SDK: https://github.com/nvidia-holoscan/holoscan-sdk
- East River Imaging: https://eastriverimaging.com/
- NVIDIA: www.nvidia.com
- RadImageNet dataset: https://www.radimagenet.com/
- MONAI VILA-M3 paper: https://arxiv.org/pdf/2411.12915
