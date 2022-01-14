Back to [Projects List](../../README.md#ProjectsList)

# Deep Diffusion MRI Registration (DDMReg): code release via SlicerDMRI 

## Key Investigators

- Fan Zhang (BWH)
- William M. Wells III (BWH)
- Lauren J O'Donnell (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Code cleaning.
1. Release code at: https://github.com/SlicerDMRI/DDMReg
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

<img width="2134" alt="f1_overview_R1" src="https://user-images.githubusercontent.com/7855446/149539700-13fe5fba-9465-4498-a765-a5d4d67af899.png">

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

[Zhang, Fan, William M. Wells, and Lauren J. O'Donnell. "Deep Diffusion MRI Registration (DDMReg): A Deep Learning Method for Diffusion MRI Registration." IEEE TMI (2022).](https://ieeexplore.ieee.org/document/9665765)

In this paper, we present a deep learning method, DDMReg, for accurate registration between diffusion MRI (dMRI) datasets. In dMRI registration, the goal is to spatially align brain anatomical structures while ensuring that local fiber orientations remain consistent with the underlying white matter fiber tract anatomy. DDMReg is a novel method that uses joint whole-brain and tract-specific information for dMRI registration. Based on the successful VoxelMorph framework for image registration, we propose a novel registration architecture that leverages not only whole brain information but also tract-specific fiber orientation information. DDMReg is an unsupervised method for deformable registration between pairs of dMRI datasets: it does not require nonlinearly pre-registered training data or the corresponding deformation fields as ground truth. We perform comparisons with four state-of-the-art registration methods on multiple independently acquired datasets from different populations (including teenagers, young and elderly adults) and different imaging protocols and scanners. We evaluate the registration performance by assessing the ability to align anatomically corresponding brain structures and ensure fiber spatial agreement between different subjects after registration. Experimental results show that DDMReg obtains significantly improved registration performance compared to the state-of-the-art methods. Importantly, we demonstrate successful generalization of DDMReg to dMRI data from different populations with varying ages and acquired using different acquisition protocols and different scanners.
