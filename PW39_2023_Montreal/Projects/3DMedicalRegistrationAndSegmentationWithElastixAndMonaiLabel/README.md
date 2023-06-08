---
layout: pw39-project

permalink: /:path/

project_title: 3D Medical Registration and Segmentation with Elastix and MONAI Label
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Konstantinos Ntatsis
  affiliation: Leiden University Medical Center
  country: the Netherlands

- name: Andres Diaz-Pinto
  affiliation: NVIDIA & King's College London
  country: United Kingdom

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to investigate the application of **itk-elastix** (a python wrapping of Elastix) for image registration in combination with **MONAI Label** for segmentation/classification. Depending on the time/people availability, we will work in one or more sub-projects.

*Initial sub-project:*
We will starty by training a single modality MONAI Label model on Elastix-aligned brain images (T1, T2, FLAIR, etc) using [SynthSeg](https://github.com/BBillot/SynthSeg) as the source of annotations. SynthSeg is a tensorflow-based deep learning segmentation tool for brain MRIs. It consists of a generative network that produces the synthetic images and a 3D U-Net trained to do the segmentation. The only input (training data) is the training labels so no real images are used.

We will use SynthSeg to produce annotations as “ground truth” on a publicly available dataset like BRATS (multimodal + non-healthy brains) or OASIS (temporal/monomodal + healthy brains). Elastix will be used for the co-registration of the different modalities or temporal images and achieve segmentation via registration.

*Other possible sub-projects:*

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Working code, jupyter notebooks, any other artifacts etc that demonstrate the combination of itk-elastix and MONAI Label. They will be helpful for users that would like to solve similar problems.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Configure and run Elastix
2.  Setup and run MONAI Label
3.  Make sure they work together nicely (e.g. output of Elastix should be suitable for MONAI, or the reverse)
4.  Improve the results (a bit)
5.  Polish and store the code/documentation/results so that they are helpful for future generations

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Preliminary registration of the BRATS dataset. Several details need to be sorted out still.
2.  ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   Elastix repo: <https://github.com/SuperElastix/elastix>
*   itk-elastix (python wrapping): <https://github.com/InsightSoftwareConsortium/ITKElastix>
*   MONAI Label: <https://monai.io/label.html>
