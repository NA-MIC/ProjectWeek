back to [Projects List](../../README.md#ProjectsList)

# MONAI Label App for AI-assisted Interactive Lymph Node Segmentation in CT

## Key Investigators
- Roya Khajavi (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)
- Erik Ziegler (Novometrics LLC, Lexington, MA)
- Steve Pieper (Isomics Inc, Cambridge, MA)
- Ron Kikinis (Department of Radiology, Brigham and Women’s Hospital, Boston, MA)

## Project Description
We have designed, developed, and validated deep learning methods for mediastinal lymph node segmentation using 3D U-Net and Tensorflow.
In this project we aim to investigate and build a MONAI Label APP to interactively segment, train, infer, and employ active learning strategies for mediastinal lymph node segmentation in CT scans.

## Objective

To create an end-to-end pipeline for interactive AI-assisted lymph node annotation using MONAI Label and 3D Slicer. 

## Approach and Plan

We will use the mediastinal subset of TCIA CT Lymph Node as data for development and performing experiments. Below is our plan during the course of project week:
1. Download TCIA data, convert to nifti, and organize per requirements of MONAI Label.
1. Set up MONAILabelAPP including network definition
2. Set up MONAI Label training pipeline: including validation split, transformations, and data augmentations.
3. Set up MONAI Label inference pipeline: set type of inferers and inference transforms.
4. Set up MONAI Label active learning strategy
5. Set up MONAI Label server on Google Cloud Platform to efficiently train models on GPUs.

## Progress and Next Steps
