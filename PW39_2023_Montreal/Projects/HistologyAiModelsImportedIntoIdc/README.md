---
layout: pw39-project

project_title: Histology AI models imported into IDC
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Curtis Lisle, KnowledgeVis
  affiliation: USA

- name: Daniela Schacherer, MEVIS
  affiliation: Germany

- name: David Clunie, PixelMed
  affiliation: USA

- name: Maximillian Fischer, DKFZ
  affiliation: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project focuses on importing whole slide image (WSI) histology images and trained deep learning models into the Imaging Data Commons for access by others. We have developed tissue-level segmentation models for detecting subtypes of rhabdomyosarcoma (RMS) in whole slides. Our project is releasing WSIs and the corresponding models trained on the slide images.

This project will test reading DICOM-WSI imagery (including compression) and focus on how to write out model segmentation results as DICOM-WSI annotations for upload to IDC.   We also have classification and regression models, so we need to decide how to write non-imagery classification results as DICOM, as well.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

*   Write out model segmentation image results as DICOM-WSI Segmentation or Parametric Map objects
*   Test models on sample DICOM-WSI images
*   Determine where to how to store regression and classification model results as DICOM annotations

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

*   Verify the algorithms run on DICOM-WSI source images (including compression)
*   Understand the semantics associated with DICOM Segmentation and Parametric Map objects
*   Write output formatter to generate proper DICOM for single class and multi-class segmentation images

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

*   Gather source images in DICOM-WSI format
*   Gather model source and pre-trained weights for inferencing

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

models wrapped in a girder3 web application: <https://github.com/knowledgevis/rms_infer_web>
