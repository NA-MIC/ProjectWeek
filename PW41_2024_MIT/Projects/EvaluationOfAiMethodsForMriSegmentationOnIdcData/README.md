---
layout: pw41-project

permalink: /:path/

project_title: Evaluation of AI methods for MRI segmentation on IDC data
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Cosmin Ciausu
  affiliation: Brigham and Women's Hospital
  country: US

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: US

- name: Megha Kalia
  affiliation: Brigham and Women's Hospital
  country: US
  
- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We previously studied the application of a contrast-agnostic approach for MRI/CT abdomen organs segmentation, based on the generation of synthetic data. This synthetic data was then further used as a training set for a fully-supervised U-Net network.
Since this study was performed, other methods aiming to segment MR abdominal organs have been published. Our goal is to evaluate these new methods on IDC MR abdominal-focused data and see how it compares to our method.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Evaluate performance of MR abdominal organs methods on IDC data.
2. Get feedback on our own method.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Select a subset of IDC MR abdominal-focused IDC data.
2. Create evaluation notebooks for newly published methods on this subset.
3. Compare to our method.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. [GitHub repo](https://github.com/deepakri201/mr_seg) for in progress colab notebooks 




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- Our method 
  - [Towards Automatic Abdominal MRI Organ Segmentation: Leveraging Synthesized Data Generated From CT Labels](https://arxiv.org/abs/2403.15609)
- New published methods
  - [MRSegmentator: Robust Multi-Modality Segmentation of 40 Classes in MRI and CT Sequences](https://arxiv.org/pdf/2405.06463)
  - [TotalSegmentator MRI: Sequence-Independent Segmentation of 59 Anatomical Structures in MR images ](https://arxiv.org/abs/2405.19492)
  - [MRISegmentator-Abdomen: A Fully Automated Multi-Organ and Structure Segmentation Tool for T1-weighted Abdominal MRI](https://arxiv.org/abs/2405.05944)
  - [TotalVibeSegmentator: Full Torso Segmentation for the NAKO and UK Biobank in Volumetric Interpolated Breath-hold Examination Body Images](https://arxiv.org/abs/2406.00125)

