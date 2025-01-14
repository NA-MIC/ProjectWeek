---
layout: pw42-project

permalink: /:path/

project_title: Remote VISTA3D server (NIM) for CT segmentation
category: Segmentation / Classification / Landmarking

key_investigators:
- name: Stephen Aylward
  affiliation: NVIDIA

- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK

---

# Project Description

## Objective

Provide access to MONAI-based foundation models to users running 3D Slicer on low-end
(e.g., no GPU) machines by launching those AI methods on freely available (albeit
limited total usage) high-end servers.

## Overview
We will develop the first (VISTA3D) of a set of Slicer Extensions that will allow Slicer
users to call AI methods built using MONAI and running on NVIDIA servers.

Access to the servers requires registration which is free, to get an API key with which
1,000 or more images can be processed for free. Research users can also register as
developers (also for free) to get unlimited local access.

The first Extension will allow Slicer users (with a free API key) to process images using
the MONAI VISTA-3D segmentation (remote) running on NVIDIA servers. Via this Extension,
Slicer users will be able to perform large / fast CT image AI segmentations on low-end
(e.g., no GPU) machines.

TLDR:
Try the VISTA-3D module running on 
[NVIDIA VISTA3D NIM](https://build.nvidia.com/nvidia/vista-3d)

We are proposing to make that service callable using a simple Slicer extension, to enable
remote VISTA-3D processing of data from within 3D Slicer.

## Details
NVIDIA is defined NIMs (NVIDIA Inference Microservices) as optimized containers for
portable, scalable AI. These are nominally offered on NV AI Enterprise / GPU Cloud servers
as callable methods. Anyone can register for free and get 1,000 to 5,000 free credits
(depending on email domain used for registration, with 1 credit used for each image
processed). Additionally, anyone can register for free to become an NVIDIA Developer, and
then they can download NIMs for free for research purposes - enabling unlimited data
processing, albeit using local GPU resources. NIMs can also run on AWS and Azure servers.

NVIDIA AI Enterprise / GPU-Cloud servers use high-end GPUs (e.g., H100s) so via NIMS
running on these servers it is possible to evaluate very large AI models and very large
images very rapidly.

1. Developed a "MONAI VISTA-3D segmentation (remote) Extension.
2. Possibly provide a Slicer GUI that simplifies registering for an NVIDIA AI Enterprise account
3. Possibly provide access to advance VISTA3D features
  * Only segmenting specific structures
  * Using seeds to indicate the inside and outside of an arbitrary object of interest

## Approach and Plan

The extension will
1. Allow the user to select a currently loaded image.
2. Ask the user to enter their NVIDIA Enterprise API key.
3. Provide a warning if the intensity range or voxel spacing is outside the norm
4. Convert that data to isotropic voxel spacing and CT intensity range
5. Upload the image to file.io to generate a URL that can be passed to the VISTA3D NIM.
6. Pass the file's URL to the VISTA3D NIM along with the API key.
7. Receive the segmentation results (mask) in the response from the NIM
8. Register the segmentation results (mask) as a segmentation volume associated with the original input image.

Optionally:
1. Provide a GUI for registering for an NVIDIA Enterprise key
2. Allow the user to select specific anatomic structures to be segmented
3. Allow the user to specify landmarks that indicate the inside and outside of a region of interest

## Progress and Next Steps

1. A jupyter notebook that does the above steps outside of Slicer has been implemented and proven to work correctly.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

* [VISTA3D NIM URL](https://build.nvidia.com/nvidia/vista-3d)
