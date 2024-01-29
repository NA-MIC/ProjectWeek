---
layout: pw40-project

permalink: /:path/

project_title: Training deep classifiers for B-line detection in lung ultrasound videos using crowdsourced
  labels
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Mike Jin
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tamas Ungi
  affiliation: Queen's University
  country: Canada

- name: Ameneh Asgari-Targhi
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

AI models for medical imaging need labeled data, which can be hard to obtain with the required volume and/or accuracy.

Crowdsourced labels on medical imaging data can help bridge that gap, as suggested by our data showing that crowdsourced classifications and segmentations for B-lines on lung ultrasound videos have comparable or better accuracy than annotations from medical experts with advanced training in lung ultrasound [(Duggan 2023)](https://arxiv.org/pdf/2306.06773.pdf) [(Jin 2023)](https://arxiv.org/pdf/2312.10198.pdf).

To demonstrate this, we will train deep learning B-line classification and segmentation models using crowdsourced annotations on lung ultrasound videos collected from 483 patients and compare their performance to models trained on manual annotations from experts.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Produce models for classification and segmentation of lung ultrasound videos with comparable or improved performance to models trained on manual annotations from experts. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Using crowdsourced labels, train CNN-RNN deep learning models to **classify** lung ultrasound videos as having no B-lines, discrete B-lines, or confluent B-lines.
2.  Using crowdsourced labels, train deep learning models to **segment** individual frames within lung ultrasound videos for the presence and location of individual B-lines using open-source code from [(Lucassen 2023)](https://ieeexplore.ieee.org/document/10143623).
3.  Compare the performance of crowdlabel-trained models to models trained on manual annotations from experts.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Collected manual classifications and segmentations from lung ultrasound experts
2.  Collected crowdsourced classification opinions to form high-quality classifications of 4,030 ultrasound videos from 483 patients
3.  Collected 177,000 crowdsourced segmentation opinions since last Friday (2024-01-26) to form high-quality segmentations of 8,500 frames (so far!) within the videos from 483 patients.

In progress: collecting ~2,000-3,000 additional high-quality frame segmentations per day.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
