---
layout: pw43-project

permalink: /:path/

project_title: Automated Bone Segmentation and 3D Modelling using Tracked 2D Ultrasound Imaging
category: DICOM

key_investigators:

- name: Nicholas Kawwas
  affiliation: Concordia University
  country: Canada

- name: Hassan Rivaz
  affiliation: Concordia University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to create sub-millilitre accurate bone modeling using Ultrasound imaging, Optical tracking (OptiTrack) and Deep learning. Modelling can be split into two key steps: segmentation and reconstruction. Segmentation considers each Ultrasound B-mode image and uses deep learning to automatically segment the bone. These segmented bone surfaces along with their respective OptiTrack coordinates associated with the US image are used to create a 3D model of the imaged bone. A free-hand sweep with the US probe will be used to generate a 3D volume of the bone, enabling fast, precise bone modelling at low cost and without radiation. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Perform free-hand sweep capturing 2D US images along with the associated coordinates
2. Reconstruct the bone using the bone surface, image coordinates and probe positioning
3. Provide a fast, sub-millilitre precise 3D bone model with no radiation and low cost




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Perform free-hand sweep capturing 2D US images with Verasonics along with the associated coordinates from OptiTrack
2. Segment automatically each US image, obtaining the bone location with deep learning
3. Reconstruct the bone using the segmented bone surface shape, image coordinates and probe angles using Neural Fields
4. Provide a fast, sub-millilitre precise 3D bone model with no radiation and low cost
5. Visualize each slice and entire model in 3DSlicer




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Trained new segmentation model with high DICE and low surface distance error
2. Collect US and OptiTrack data from thigh for femur reconstruction
3. Train Neural Fields model like MaskField for 3D model generation from multiple 2D images and coordinates




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

