Back to [Projects List](../../README.md#ProjectsList)

# Deep Fiber Clustering: Anatomically Informed Unsupervised Deep Learning for Fast and Effective White Matter Parcellation

## Key Investigators

- Yuqian Chen (BWH & USYD)
- Chaoyi Zhang (USYD)
- Yang Song (UNSW)
- Tengfei Xue (BWH & USYD)
- Nikos Makris (BWH)
- Yogesh Rathi(BWH)
- Weidong Cai (USYD)
- Fan Zhang (BWH)
- Lauren J O'Donnell (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->
We propose an unsupervised deep learning framework for fast and effective white matter fiber clustering (WMFC) (Chen et al 2021, MICCAI). It enables parcellation of white matter tractography. Current WMFC methods are facing several challenges such as fiber computation efficiency, sensitivity to fiber direction, combination of spatial and anatomical information, existence of outlier fibers as well as correspondence across subjects. To overcome these challenges, we propose a self-supervised learning strategy to achieve fast and effective WMFC. In this project, we will work on releasing the code of this method. We will provide the trained model and testing samples for demonstration.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Build deep learning training model for white matter fiber clustering and evaludation it on testing data.
2. Code cleaning and release code at: https://github.com/SlicerDMRI/DeepFiberClustering.
4. Documentation and Example testing data.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. In our method, we use a convolutional neural network to learn embeddings of input fibers, using pairwise fiber distances as pseudo annotations. 
2. In our method, we improved anatomical coherence of fiber clusters by incorporating brain anatomical information. 
3. In our method, outlier removal is performed in a natural way by rejecting fibers with low cluster assignment probability.
4. Coding with python.
5. Performed experiments on three independently acquired datasets including traning model and testing.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Currently we have the code to get the fiber clustering results in (Chen et al 2021, MICCAI).
2. We will make some improvements of the current method and add more experiments.
3. We will clean our previous code and complete new code during the project week.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![image](https://user-images.githubusercontent.com/59594831/149714486-3e57731f-e146-42b9-8bba-687f9fb13c2d.png)
![image](https://user-images.githubusercontent.com/59594831/149785097-cb71b90c-6713-4a93-b748-c1521aeecf1d.png)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
[Deep Fiber Clustering: Anatomically Informed Unsupervised Deep Learning for Fast and Effective White Matter Parcellation](https://link.springer.com/chapter/10.1007/978-3-030-87234-2_47)

