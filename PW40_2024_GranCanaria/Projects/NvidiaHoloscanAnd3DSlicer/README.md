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

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims at integrating [NVIDIA Holoscan](https://developer.nvidia.com/holoscan-sdk) into 3D Slicer. Holoscan is a hybrid computing platform for medical devices that combines hardware systems for low-latency sensor and network connectivity, optimized libraries for data processing and AI, and core microservices to run surgical video, ultrasound, medical imaging, and other applications anywhere, from embedded to edge to cloud.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Integrate Holoscan with 3D Slicer. As Holoscan is both a hardware platform ([NVIDIA IGX Orin](https://www.nvidia.com/en-gb/edge-computing/products/igx/)) and an SDK ([Holoscan SDK](https://github.com/nvidia-holoscan/holoscan-sdk)) the integration could be of either of these components, or both.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

There are various options, not yet sure which one is the best (or if there are ones I have not considered):

1. Use OpenIGTLink to stream data from a Holoscan developer kit to 3D Slicer, over network. This would bypass the fact that 3D Slicer does not easily build on ARM (which is the arch of the IGX Orin).
2. Create operators in 3D Slicer that can pass data to and from Holoscan SDK. This would give a 3D Slicer user access to the API of Holoscan SDK for efficient AI inference, etc.
3. Connect an IGX Orin running Holoscan SDK to the [Plus toolkit](https://plustoolkit.github.io/).

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

None

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

None

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

None
