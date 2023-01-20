Back to [Projects List](../../README.md#ProjectsList)

# Automatic Segmentation of Teeth and Alveolar bone using MONAI Label

## Key Investigators

- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Yucheng Tang (NVIDIA, USA)
- Andres Diaz Pinto (NVIDIA, UK)
- Daniel Palkovics (Semmelweis University, Budapest, Hungary)
- Csaba Pinter (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)

# Project Description

A three-dimensional visualization of dento-alveolar structures can enhance the surgical planning process. However, no fully automated segmentation methods are currently available to generate realistic 3D virtual models of teeth and alveolar bone.

We have a dataset of 43 CBCT scans with manual segmentation of teeth and alveolar bone.

<img src="https://user-images.githubusercontent.com/10816661/213661126-e7e8d640-38e0-40b4-9232-beb9da0791bf.png" alt="drawing" width="650"/>

We have already tested segmentation and deepedit models in MONAI Label. Those models are good for single label teeth segmentation or mandible segmentation. However, results are not optimal when trying to perform a multi-label segmentation where all teeth are correctly identified and segmented.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Implement multi-stage approach for teeth segmentation using MONAI Label pipelines. At least, two stages: (1) teeth localization and (2) teeth segmentation.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
1. ...
1. ...

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
