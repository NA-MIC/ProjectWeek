---
layout: pw40-project

permalink: /:path/

project_title: Visualization and review of segmentations
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Vamsi Krishna Thiriveedhi
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Cosmin Ciausu
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Ron Kikinis
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

We have multiple sets of segmentation results that we would like to review with radiologists and clinicians. The first set of results are from running TotalSegmentator on patients from the National Lung Screening Trial (NLST). The second set includes results from work that Deepa and Cosmin are performing with training a model for abdominal MR/CT segmentation using synthesized data.

We would like to review this work, and showcase some results during project week.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Review results from TotalSegmentator on NLST patients. Use the Netter Atlas to learn about anatomy, and correlate this with the data that TotalSegmentator used for training, to further understand our results.
2.  Review results from the abdominal segmentations on both MR and CT patients.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  We will run TotalSegmentator on a sample of 1000 patients from NLST, convert to DICOM representation, and create OHIF links.
2.  We will create DICOM SEG representations of the abdominal segmentations on IDC data, and create OHIF links.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

*No response*

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[TotalSegmentator ](https://github.com/wasserth/TotalSegmentator)
[SynthSeg](https://github.com/BBillot/SynthSeg)
