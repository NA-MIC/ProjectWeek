---
layout: pw44-project

permalink: /:path/

project_title: Automated Segmentation of Pelvic Bones from Diverse CT Datasets
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Hamid Alavi
  affiliation: University of Twente
  country: The Netherlands

- name: Gabrielle Tuijthof
  affiliation: University of Twente
  country: The Netherlands

- name: Nico Venrdonschot
  affiliation: University of Twente
  country: The Netherlands

- name: Malte Asseln
  affiliation: University of Twente
  country: The Netherlands

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to segment the hip bones, sacrum, and femur from a collection of public CT datasets that vary in the anatomical regions they cover. To handle this heterogeneity, we aim to develop a four-stage workflow implemented in MONAILabel and 3DSlicer.

Stage 1: Preliminary Bone Segmentation – All CT volumes are processed with TotalSegmentator to generate initial segmentations of the target bones. This provides voxel-level information needed to identify relevant scans.

Stage 2: Selection of Relevant CT Volumes – Using the preliminary segmentations, bone volumes are calculated. Scans with near-zero volumes are excluded, scans within reference ranges are retained, and borderline cases are forwarded to human annotators for review.

Stage 3: Detailed Segmentation and Model Selection – Selected scans undergo precise segmentation using multiple state-of-the-art pretrained models. Aleatoric uncertainty is computed on a subset to select the most consistent model, which is then applied to the remaining scans.

Stage 4: Quality Control and Manual Refinement – Segments with high uncertainty are flagged for review. Annotators refine them interactively using MONAILabel tools like DeepEdit and DeepGrow.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. A MonaiLabel application equipped with multiple segmentation models.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Describe specific steps of **what you plan to do** to achieve the above described objectives.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

