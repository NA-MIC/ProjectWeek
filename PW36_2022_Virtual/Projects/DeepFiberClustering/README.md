Back to [Projects List](../../README.md#ProjectsList)

# Deep Fiber Clustering: Anatomically Informed Unsupervised Deep Learning for Fast and Effective White Matter Parcellation

## Key Investigators

- Yuqian Chen (BWH & USYD)
- Chaoyi Zhang (USYD)
- Yang Song (UNSW)
- Nikos Makris (BWH)
- Yogesh Rathi(BWH)
- Weidong Cai (USYD)
- Fan Zhang (BWH)
- Lauren J O'Donnell (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Code cleaning.
1. Release code at: https://github.com/SlicerDMRI/DeepFiberClustering.
1. Documentation and Example testing data.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Coding

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
[Deep Fiber Clustering: Anatomically Informed Unsupervised Deep Learning for Fast and Effective White Matter Parcellation](https://link.springer.com/chapter/10.1007/978-3-030-87234-2_47)
White matter fiber clustering (WMFC) enables parcellation of white matter tractography for applications such as disease classification and anatomical tract segmentation. 
However, the lack of ground truth and the ambiguity of fiber data (the points along a fiber can equivalently berepresented in forward or reverse order) pose challenges to this task. 
We propose a novel WMFC framework based on unsupervised deep learning. We solve the unsupervised clustering problem as a self-supervised learning task. 
Specifically, we use a convolutional neural network to learn embeddings of input fibers, using pairwise fiber distances as pseudo annotations.
This enables WMFC that is insensitive to fiber point ordering. 
In addition, anatomical coherence of fiber clusters is improved by incorporating brain anatomical segmentation data. 
The proposed framework enables outlier removal in a natural way by rejecting fibers with low cluster assignment probability. 
We train and evaluate our method using 200 datasets from the Human Connectome Project. Results demonstrate superior performance and efficiency of the proposed approach.
