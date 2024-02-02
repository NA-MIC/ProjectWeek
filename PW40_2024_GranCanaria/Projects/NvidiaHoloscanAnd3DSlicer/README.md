---
layout: pw40-project

permalink: /:path/

project_title: NVIDIA Holoscan and 3D Slicer
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Mikael Brudfors
  affiliation: NVIDIA
  country: UK
- name: Steve Pieper
  affiliation: Isomics
  country: US
- name: Rafael Palomar
  affiliation: NTNU
  country: Norway
- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims at integrating [NVIDIA Holoscan](https://developer.nvidia.com/holoscan-sdk) into 3D Slicer. Holoscan is a hybrid computing platform for real-time streaming data that combines hardware systems for low-latency sensor and network connectivity, optimized libraries for data processing and AI, and core microservices to run surgical video, ultrasound, medical imaging, and other applications anywhere, from embedded to edge to cloud.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Integrate NVIDIA Holoscan with 3D Slicer. Holoscan is both a [hardware platform](https://www.nvidia.com/en-gb/edge-computing/products/igx/) and an [SDK](https://github.com/nvidia-holoscan/holoscan-sdk)). Holoscan SDK runs on both x86 and arm64 platforms, which means it can be deployed on, e.g., regular laptops, as well as NVIDIA Jetson devices, or even in the cloud!

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

There are various options, not yet sure which one is the best (or if there are ones I have not considered):

1. Use [OpenIGTLink](http://openigtlink.org/) to stream data from a Holoscan developer kit to 3D Slicer, over network. This would bypass the fact that 3D Slicer does not easily build on ARM (which is the arch of the IGX Orin).
2. Create operators in 3D Slicer that can pass data to and from Holoscan SDK. This would give a 3D Slicer user access to the API of Holoscan SDK for efficient AI inference, etc.
3. Connect an IGX Orin running Holoscan SDK to the [Plus toolkit](https://plustoolkit.github.io/).

## Progress and Next Steps

1. Worked with Kitware on building Slicer natively on Holoscan OS/hardware (progress, but not completed)
2. Protytpe OpenIGTLink connection streaming slice/volume data through Holoscan
3. Made connections for further development

The implementation for (2) will be made available on the [Holohub repository](https://github.com/nvidia-holoscan/holohub) soon, and will allow a 3D Slicer user to send imaging data to Holoscan SDK, running on a GPU powered device, do efficient inference and the send the results back to 3D Slicer. Another possibility is to send data acquired on the Holoscan device to 3D Slicer for visualization.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![holoscan_3dslicer](https://github.com/NA-MIC/ProjectWeek/assets/6413806/c6e5969e-cccc-4228-9c60-e713ef776731)
