---
layout: pw45-project

permalink: /:path/

project_title: Slicer Chest Imaging Platform Reboot
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Kalysta Makimota
  affiliation: Brigham and Women's Hospital
  country: United States

- name: Axel Masquelin
  affiliation: Brigham and Women's Hospital
  country: United States

- name: Raúl San José Estépar
  affiliation: Brigham and Women's Hospital
  country: United States

---

# Project Description

<!-- Add a short paragraph describing the project. -->


`The Chest Imaging Platform (CIP)` is an open-source software suite developed by the `Applied Chest Imaging Laboratory (ACIL)` at Brigham and Women's Hospital (Harvard Medical School). CIP is designed for quantitative chest CT analysis, helping researchers identify and measure phenotypes for Chronic Obstructive Pulmonary Disease (COPD), Interstitial Lung Disease (ILD), Acute Lung Injury (ALI), and pulmonary vascular pruning, and hopefully by the end of this Lung Cancer.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


This relaunch a modern, deep-learning-centric Chest Imaging Platform within 3D Slicer that simplifies model deployment and optimizes inference, while maintaining core functionalities that are being used for tasks such as lung volume estimation. 



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We address two major historical pain points:
`Model Dispersion`: Previously, integrating new deep learning models required custom scripting or manual installation. We will introduce a unified, user-friendly Model Hub. **Further Details pending**
`Pre-processing Discrepancies`: Variations in voxel spacing, orientation, and Intensity (Hounsfield Unit) ranges often degrade model performance. We will provide a standardized, automated preprocessing pipeline that ensures input scans are automatically optimized before running inference.

🛠️ System Architecture & Workflow
The new Slicer-CIP architecture separates the interactive visualization layer (3D Slicer) from the processing layer, allowing users to pull models from our central repository and execute standardized preprocessing on-the-fly.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Reviewing current CIP-Slicer integration and getting feedback and development notes from Rubén San José Estépar.
2. 



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. [Chest Imaging Platform](https://chestimagingplatform.org/)
2. [LobTE](https://pubmed.ncbi.nlm.nih.gov/39644582/)

