---
layout: pw39-project

project_title: AI-Enhanced Virtual Resections for Improved Slicer-Liver Surgical Planning
category: IGT and Training

key_investigators:
- firstname: Gabriella
  lastname: d'Albenzio
  affiliation: The Intevention Centre (OUS)
  country: Norway

- firstname: Andras
  lastname: Lasso
  affiliation: Queen's University
  country: Canada
  
- firstname: Rafael
  lastname: Palomar
  affiliation: The Intevention Centre (OUS)
  country: Norway
---

# Project Description

The primary aim of this project is to utilize artificial intelligence (AI) to enhance the surgical planning of Slicer-Liver through the generation of virtual resections. The initial focus is on employing AI for liver resection planning, specifically using complex anatomical information obtained from CT and/or MRI scans, such as the hepatic and portal veins, as well as the liver parenchyma. The objective is to train a model capable of generating optimal resections in the form of parametric surfaces, while also providing control points that can be adjusted to modify the suggested plan. To achieve this, two distinct deep learning approaches can be explored:

**Proposal 1 - SplineNet:** Instead of parametrizing a set of points as a spline patch, which can introduce errors due to noise, sparsity, and non-uniform sampling, this proposal suggests employing a neural network to directly predict control points. SplineNet, a neural network referenced in this project, takes the boundary 3D points of a liver segment as input and produces a fixed-size grid of control points, yielding more robust results.

**Proposal 2 - Multimodal deep learning for generating liver resection suggestions:** This proposal involves a two-step process. Firstly, the boundary 3D points of a liver segment and the 3D CT volume, along with anatomical segmentations, are processed by modality-specific feature extraction networks (CNN and PointNet) independently, to identify regional and geometric features for each modality. Subsequently, the modality-based features are fed into a siamese architecture consisting of cross-modal attention blocks, which capture local features and establish their global correspondence across modalities. Finally, a recurrent neural network (RNN) block is utilized to extract the control points, which can be adjusted by the surgeon to modify the suggested plan.

## Objective

1. Engage in collaborative discussion with other members to assess the practicality of implementing the two networks within a clinical environment.
2. Develop a dedicated Slicer module to effectively apply trained models for liver resection surfaces.

## Approach and Plan

- Utilizing the [ABC dataset](https://deep-geometry.github.io/abc-dataset/) for training purposes.
- Employing SPLINet and a multimodal deep learning network for parametric surface reconstruction on the ABC dataset.
- Drawing inspiration from @Tamas to develop a Slicer module with PyTorch implementation of trained models.

## Progress and Next Steps

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

![image_00042](https://github.com/NA-MIC/ProjectWeek/assets/75131750/9bbbb6d9-941b-4d50-ac70-922eb5136621)
![image_00043](https://github.com/NA-MIC/ProjectWeek/assets/75131750/7dba10f9-a151-4b2a-bec5-3ff94071fe73)

# Background and References
[Saiti, E., and T. Theoharis. "Multimodal registration across 3D point clouds and CT-volumes." Computers & Graphics 106 (2022): 259-266.](https://www.sciencedirect.com/science/article/pii/S0097849322001121)
[Sharma, Gopal, et al. "Parsenet: A parametric surface fitting network for 3d point clouds." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part VII 16. Springer International Publishing, 2020.](https://graphics.stanford.edu/courses/cs348n-22-winter/PapersReferenced/ParSeNet%20A%20Parametric%20Surface%20Fitting%202003.12181.pdf)

