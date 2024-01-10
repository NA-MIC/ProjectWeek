---
layout: pw40-project

permalink: /:path/

project_title: 'Evaluation of AI methods for prostate cancer segmentation '
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

When it comes to evaluating AI methods, it's important to have reproducible code and methods. We are interested in evaluating state-of-the-art AI methods for prostate cancer segmentation on data in Imaging Data Commons. Additionally, we have a non-public BWH internal dataset that we would like to use for evaluation.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  We first need to identify a set of publicly available AI methods that we can use for prostate cancer segmentation.
2.  We then need to identify datasets in IDC that we can use for evaluation, preferably ones with expert delineated segmentations.
3.  Then, we will run inference using those methods, convert our output to a standard format (hopefully DICOM SEG) and visualize in OHIF and Slicer.
4.  We will make our code and results publicly available in GitHub.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  We will do a literature/code repo search of the methods.
2.  We will search for  appropriate data in IDC using the portal/BigQuery.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

3.  We have started evaluation of the PICAI supervised nnUNet baseline model and the MONAI Deploy MAP on their training data.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![Red (ground truth) and green (predicted) using nnUNet supervised baseline on PICAI dataset](https://github.com/NA-MIC/ProjectWeek/assets/59979551/c7545409-d451-4267-a0bc-989b59290a88)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
