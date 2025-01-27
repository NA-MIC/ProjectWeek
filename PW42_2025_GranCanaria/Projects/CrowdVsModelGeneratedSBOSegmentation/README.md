---
layout: pw42-project

permalink: /:path/

project_title: Comparison of crowd sourced vs. model generated accuracy on abdominal ultrasound
category: Segmentation / Classification / Landmarking

key_investigators:
- name: Jacqueline Foody
  affiliation: Centaur Labs/MGB
  country: USA

- name: Mike Jin
  affiliation: Centaur Labs/MGB
  country: USA

- name: Hallee Wong
  affiliation: MIT
  country: USA

- name: Tina Kapur
  affiliation: MGB
  country: USA
---

# Project Description

Abdominal ultrasound images were given to a crowd of novice labelers using the Centaur platform to segment the bowel to assist in diagnosis of small bowel obstruction.
In some cases the crowd successfully segmented the bowel and in others, they were not able to correctly identify bowel in the ultrasound clips. We want to determine if a model, prompted by one frame annotated by an expert, can segment the bowel as well or better than the crowd.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Implement MultiverSeg for predictions on abdominal ultrasound images.
2. Objective B. Evaluate the accuracy of the model for generating segmentations relative to the crowd consensus.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Using a set of ultrasound images (which were annotated by a crowd of non-expert labelers and validated by an expert physician) with segmentations of small bowel, prompt the model using an increasing number of context frames to evaluate the similarity between the crowd consensus and model generated segmentations.
2. Similarly, add in user input to evaluate the impact on accuracy of predictions
3. Use this information to propagate predictions on a separate set of ultrasound clips which have 1-4 frames with expert segmentation.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- [https://github.com/halleewong/MultiverSeg](https://github.com/halleewong/MultiverSeg)
- [https://github.com/halleewong/ScribblePrompt](https://github.com/halleewong/ScribblePrompt)

Relevant Publications:

Wong, H.E., Ortiz, J.J.G., Guttag, J. & Dalca, A.V., (2024). MultiverSeg: Scalable Interactive Segmentation of Biomedical Imaging Datasets with In-Context Guidance. arXiv preprint arXiv:2412.15058. 
[paper](https://arxiv.org/abs/2412.15058) [code](https://github.com/halleewong/MultiverSeg)
