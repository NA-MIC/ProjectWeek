---
layout: pw44-project

permalink: /:path/

project_title: A Modular Pipeline for Quality-Controlled Multi-Model Bone Segmentation in CT Imaging
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Hamid Alavi
  affiliation: University of Twente
  country: The Netherlands

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project focuses on developing a pipeline for large-scale bone segmentation from CT images, with a focus on quality control and human correction.

State-of-the-art segmentation models such as TotalSegmentator, MOOSE, nnU-Net, and MONAI Auto3DSeg provide powerful tools for anatomical segmentation. However, their outputs vary in label definitions, formats, and performance across anatomical structures. Moreover, pretrained models do not cover all structures (e.g., individual tarsal bones), and segmentation errors can occur due to anatomical variability, pathology, or imaging artifacts.

Manual verification of all segmentations is impractical for large datasets. Therefore, this project proposes a system that integrates multiple segmentation models, standardizes their outputs, automatically evaluates segmentation quality using consistency-based metrics, and enables human-in-the-loop correction only for unreliable cases.

The system is structured into three independent stages:
(1) Multi-model segmentation,
(2) Automatic quality control (QC), and
(3) Human-in-the-loop correction.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


The main objective is to build a pipeline that:

- Integrates multiple pretrained and custom bone segmentation models
- Converts all model outputs into a common label schema
- Automatically detects unreliable segmentations by calculating the inconsistency between segmentation
- Assigns a quality score per bone per scan
- Minimizes expert workload by sending only low-quality segmentations for manual correction
- Supports interactive correction using 3D Slicer and SlicerNNInteractive

Ultimately, the goal is to produce a open-access, high-quality, standardized bone segmentation dataset through [https://www.bonehub.eu/](https://www.bonehub.eu/)



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


The system is divided into three separate stages.

**Stage 1 — Multi-Model Segmentation**
Goal: Generate and store segmentation outputs in a unified format.

- Wrap pretrained tools (e.g., TotalSegmentator, MOOSE) and custom models (nnU-Net, Auto3DSeg) using a standardized interface.
- Convert all outputs into a common label schema
- Use a segmentation pipeline capable of:
   - Running multiple models
   - Applying optional input augmentations (rotation, noise, intensity variations)
   - Produce multiple segmentation outputs per case (different models × augmentations).
   - Store all segmentation results for later analysis.
- This stage performs no quality evaluation.

**Stage 2 — Automatic Quality Control (QC)**
Goal: Detect unreliable segmentations

- This stage analyzes only the segmentations produced in Stage 1.
- QC is based on: Compare different segmentations on the same image (e.g., Dice score).
- For each bone and scan, QC metrics are combined into a final QC score, which is stored for later use. No segmentation models are executed in this stage.

**Stage 3 — Human-in-the-Loop Correction**
Goal: Efficiently correct only unreliable segmentations.

- Select segmentations with QC scores beyond a defined threshold.
- Extract a region of interest (ROI) around the target bone to reduce volume size.
- Load ROI image and mask into 3D Slicer with SlicerNNInteractive.
- Allow users to correct segmentations via prompt-based interactions.
- Map corrected masks back to full-volume space and replace the original segmentation artifacts.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

We will make the codes available at [https://github.com/BoneHub/BoneHub-Segmentation](https://github.com/BoneHub/BoneHub-Segmentation)




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

