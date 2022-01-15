Back to [Projects List](../../README.md#ProjectsList)

# Superficial White Matter Analysis (SupWMA): A deep learning framework for superficial white matter parcellation, code release via SlicerDMRI 

## Key Investigators

- Tengfei Xue (BWH & Usyd)
- Fan Zhang (BWH)
- Chaoyi Zhang (Usyd)
- Yuqian Chen (BWH & Usyd)
- Weidong Cai (Usyd)
- Lauren J O'Donnell (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Code cleaning.
1. Release code at: https://github.com/SlicerDMRI/SupWMA
1. Documentation and Example testing data

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Coding

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. ... <!--How to intergate into SlicerDMRI so users can use via Slicer interface.  -->

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

![v4_SupWMA_Overview](https://user-images.githubusercontent.com/56477109/149606217-ed5f329f-fc1d-43d1-9f6a-a903a884baf3.png)

![v7_Contrastive learning](https://user-images.githubusercontent.com/56477109/149606222-a6954063-80cf-4ebd-8843-6bf8142bbeff.png)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

<!-- 
[Tengfei Xue, Fan Zhang, Chaoyi Zhang, Yuqian Chen, Yang Song, Nikos Makris, Yogesh Rathi, Weidong Cai, Lauren J. O’Donnell. "SUPWMA: CONSISTENT AND EFFICIENT TRACTOGRAPHY PARCELLATION OF
SUPERFICIAL WHITE MATTER WITH DEEP LEARNING." ISBI (2022).](Coming soon) -->

Tengfei Xue, Fan Zhang, Chaoyi Zhang, Yuqian Chen, Yang Song, Nikos Makris, Yogesh Rathi, Weidong Cai, Lauren J. O’Donnell. "SUPWMA: CONSISTENT AND EFFICIENT TRACTOGRAPHY PARCELLATION OF SUPERFICIAL WHITE MATTER WITH DEEP LEARNING." ISBI (2022).

In this paper, we propose a deep-learning-based framework, Superficial White Matter Analysis (SupWMA), that performs an efficient and consistent parcellation of 198 SWM clusters from whole-brain tractography. A point-cloud-based network is modified for our SWM parcellation task, and supervised contrastive learning enables more discriminative representations between plausible streamlines and outliers. We perform evaluation on a large tractography dataset with ground truth labels and on three independently acquired testing datasets from individuals across ages and health conditions. Compared to several state-of-the-art methods, SupWMA obtains a highly consistent and accurate SWM parcellation result. In addition, the computational speed of SupWMA is much faster than other methods.
