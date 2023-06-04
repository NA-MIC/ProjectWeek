---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/LiveTrackedUltrasoundProcessingWithPytorch/README.html

project_title: Live tracked ultrasound processing with PyTorch
category: IGT and Training

key_investigators:

- name: Tamas Ungi
  affiliation: Queen's University

- name: Colton Barr
  affiliation: Queen's University / BWH

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Our past code for training and deploying ultrasound segmentation in real time was based on TensorFlow. Example project:
<https://youtu.be/WyscpAee3vw>

The goal for this project week is to provide a new open-source implementation using PyTorch and modern AI tools like MONAI and wandb. A Slicer module will also be provided to deploy trained AI on recorded or live ultrasound streams.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Export annotated ultrasound+tracking data for training
2.  Example code for training
3.  Slicer module to use trained models on ultrasound data in Slicer

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  All data processing and training code will be here: <https://github.com/SlicerIGT/aigt/tree/master/UltrasoundSegmentation>
2.  Slicer module will be here: <https://github.com/SlicerIGT/aigt/tree/master/SlicerExtension/LiveUltrasoundAi/TorchLiveUs>

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
