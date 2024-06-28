---
layout: pw41-project

permalink: /:path/

project_title: Skin Surface Segmentation for NousNav
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Reuben Dorent
  affiliation: Brigham and Women's Hospital
  country: Harvard Medical School, USA

- name: Colin Galvin
  affiliation: Brigham and Women's Hospital
  country: Harvard Medical School, USA

- name: Sarah Frisken
  affiliation: Brigham and Women's Hospital
  country: Harvard Medical School, USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: Harvard Medical School, USA

- name: Sam Horvath
  affiliation: Kitware
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project was initiated during the [PW36](https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/SkinSegmentation/).
It aims to create an automated skin segmentation tool for pre-operative scans for NousNav.

A model has been already trained to automatically segment scans in multi-parametric MRI. In this project, we aim to integrate the developed tool into Slicer for further integration in NousNav.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Create a Slicer Extension for automatic skin segmentation based on a pre-trained nnUnet framework
2. Test the Slicer Extension in different settings, including different OS and different hardware configuration (only CPU, GPU, Mac)
3. Integrate the Slicer module into NousNav




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Leverage the existing TotalSegmentator Slicer extension as template
2. Create a small database that can be shared to test the algorithm in different settings
3. Discuss with the NousNav development team for its integration




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. The Slicer extension has been implemented and is publicly available [here](https://github.com/ReubenDo/SlicerSkinSegmentator).
2. The extension has been tested on CPU (MacOS and Windows) and GPU (Windows)
3. The integration in NousNav is still pending.


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1728" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/17268715/fc907ff6-8872-45ab-a619-2fc444cb0ba1">




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

