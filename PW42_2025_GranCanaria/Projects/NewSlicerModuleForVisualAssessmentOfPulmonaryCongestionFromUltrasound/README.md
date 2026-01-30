---
layout: pw42-project

permalink: /:path/

project_title: New Slicer Module for Visual Assessment of Pulmonary Congestion from Ultrasound
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Mike Jin
  affiliation: Centaur Labs, Brigham and Women's Hospital
  country: USA

- name: Tamas Ungi
  affiliation: Queens's University
  country: Canada

- name: Fahimeh Fooladgar
  affiliation: University of British Columbia
  country: Canada

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This work is part of an NIH Trailblazer R21 grant to our team to develop and validate computational methods for quantifying pulmonary congestion using B-lines in heart failure patients from bedside lung ultrasound in emergency settings. Tools for automated quantification could help emergency department physicians more rapidly and frequently examine patients to assess progress and adjust treatment, resulting in improved care and patient outcomes.

![grid_Case001_0](https://github.com/user-attachments/assets/87bd5a3e-9601-45fb-a1c1-c0cdc99a665f)


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Add a new public module for annotation of pulmonary congestion in ultrasound
2. Add new feature to existing public Anonymizer module: AI-assisted detection of image fan boundaries in ultrasound to streamline anonymization, followed by OCR in output which produces warning if any text is detected in image



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We will spend Project Week developing the software to support these features and hopefully release the modules publicly.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. We have added a new AnnotateUltrasound module to the Ultrasound extension that allows for easy annotation of sectors representing B-lines (indicating pulmonary congestion).
2. As part of the public Anonymizer module, we have added a new button that uses an AI model to auto-detect the boundaries of the ultrasound image fan.

   Next steps: we will work on adding OCR text detection to add an additional check that anonymized images don't contain any remaining PHI text prior to export.


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![](https://github.com/user-attachments/assets/80e53527-a968-4319-a9b0-c5b75f6bc8c0)


![image001](https://github.com/user-attachments/assets/90aeaef1-8d07-4efa-b434-830adacfc671)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. Asgari-Targhi et al. (2024).  Can Crowdsourced Annotations Improve AI-based Congestion Scoring For Bedside Lung Ultrasound?  MICCAI 2024.  ([link](https://papers.miccai.org/miccai-2024/paper/3582_paper.pdf) to paper)
