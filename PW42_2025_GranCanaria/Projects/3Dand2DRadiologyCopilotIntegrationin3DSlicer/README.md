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
  country: USA
- name: Nigel Nelson
  affiliation: NVIDIA
  country: USA
- name: Sean Huver
  affiliation: NVIDIA
  country: USA
- name: Mingxin Zheng
  affiliation: NVIDIA
  country: China
- name: Wenqi Li
  affiliation: NVIDIA
  country: UK
- name: Xueyan Mei
  affiliation: Mount Sinai
  country: USA
- name: Zelong Liu
  affiliation: Mount Sinai
  country: USA
- name: Tim Deyer
  affiliation: East River Imaging
  country: USA  
---

# Project Description

This project aims to create the first 3D and 2D radiology copilot in 3D Slicer by developing a module that can consume REST APIs of radiology copilots. The main goal is to demonstrate the benefits of using the NVIDIA Holoscan platform for deploying AI models in medical imaging applications.

## Objective

1. Develop a 3D Slicer module that integrates with radiology copilots via REST APIs.
2. Showcase the capabilities of the NVIDIA Holoscan platform for AI model deployment in medical imaging.
3. Implement functionality to send 3D volumes to the copilot, ask questions, and receive insights.

## Approach and Plan

1. Create a new 3D Slicer module that can communicate with REST APIs
2. Integrate the private model trained by East River Imaging and NVIDIA using the RadImageNet dataset.
3. Implement support for the MONAI VILA-M3 model.
4. Develop a user interface within the module to allow sending 3D volumes, asking questions, and displaying copilot insights.
5. Optimize the module's performance using the NVIDIA Holoscan platform.

## Progress and Next Steps

1. Initial project setup and team coordination completed.
2. Research on integrating REST APIs within 3D Slicer modules conducted.
3. Preliminary design of the user interface drafted.
4. Repository: [https://github.com/Project-MONAI/VLM/tree/main/plugins/RadCoPilot_Slicer](https://github.com/Project-MONAI/VLM/tree/main/plugins/RadCoPilot_Slicer)

## Next Steps:

### For RadViLLA server:

- In the server, create a session so loading volume and resizing doesn't need to happen every time the user send a prompt
- Cache the volume so inference is faster

### VILA-M3:

- [Current server](https://github.com/Project-MONAI/VLM/pull/66) using NVCF doesn't accept volumes in the cloud with HTTPS. Change this flag or make sure it also accepts volumes hosted using HTTP
- Get the current slice and send it to the prompt request rather than keeping it hard coded in the server

# Illustrations

![updatedSlicerModule](https://github.com/user-attachments/assets/4c2bb0cb-0367-4758-bbb6-786283206c73)


[video](https://github.com/user-attachments/assets/0d9fd2c6-ef26-4d14-851e-c761bb218ea7)



# Background and References

- [NVIDIA Holoscan SDK](https://github.com/nvidia-holoscan/holoscan-sdk)
- [East River Imaging](https://eastriverimaging.com/)
- [NVIDIA](www.nvidia.com)
- [RadImageNet dataset](https://www.radimagenet.com/)
- [MONAI VILA-M3 paper](https://arxiv.org/pdf/2411.12915)
