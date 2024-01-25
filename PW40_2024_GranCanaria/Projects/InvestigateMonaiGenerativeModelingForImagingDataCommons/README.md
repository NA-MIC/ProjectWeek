---
layout: pw40-project

permalink: /:path/

project_title: Investigate MONAI generative modeling for Imaging Data Commons
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: Inc. USA

- name: Mikael Brudfors
  affiliation: NVIDIA
  country: UK

- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK

- name: Andrey Fedorov
  affiliation: BWH
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Generative learning refers to a class of techniques that process large amounts of training data into models that can be used for a variety of tasks such as synthetic data generation, image compression, enhancing resolution, classifying images, and content based retrieval.  Recently a generative package has been added to the open source MONAI software.

This project will explore the application of MONAI generative tools to data on the NCI Imaging Data Commons.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Study the existing material and collect information from other interested parties
2.  Make plans about what experiments would be interesting
3.  If possible do some small experiments to better understand what's possible and what effort and resources would be required to scale up

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Explore creating an  compatible with [MONAI Datasets](https://docs.monai.io/en/latest/data.html) using [idc-index](https://github.com/ImagingDataCommons/idc-index) to fetch data
2.  Investigate adapting [tutorial code](https://github.com/Project-MONAI/tutorials/tree/main/generative) to work with IDC data
3.  Try running some small tests, such as running the [superresolution tutorials](https://github.com/Project-MONAI/GenerativeModels/blob/main/tutorials/generative/2d_super_resolution/2d_stable_diffusion_v2_super_resolution.ipynb) on IDC data
4.  Document how IDC can be used with MONAI for research

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   Paper describing the generative features in MONAI: <https://arxiv.org/abs/2307.15208>
