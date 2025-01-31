---
layout: pw41-project

permalink: /:path/

project_title: Brain Tumor segmentation with Missing Data
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Reuben Dorent
  affiliation: BWH
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

- name: Sarah Frisken
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to create a Slicer extension that can automatically segment brain tumors in brain multi-parametric MRI, even in the presence of missing data.

This project will focus on two use cases where:
- all MR sequences (T1, contrast-enhanced T1, T2, FLAIR) are available
- only pre-contrast T1 and contrast-enhanced T1

The algorithm will not only segment the scans but also perform the required pre-processing steps (co-registration and skull-stripping).




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Develop a Slicer module that can automatically perform brain tumor segmentation
3. Create a module that has the flexibility to handle two potential sets of input data
4. Integrate pre-processing steps for end-to-end inference
5. Validate the module with a subset of BraTS and clinical data




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Train two combinations of nnUnet using the BraTS dataset.
2. Integrate the pre-trained nnUnet frameworks into Slicer using the TotalSegmentator Slicer plugin as a template
3. Leverage Slicer tools to perform the BraTS preprocessing steps
4. Collect clinical data for validation




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


- nnUnet have been trained for two combinations of input (ceT1 + T1 and ceT1 + T1 + T2 + FLAIR).
- Preprocessing has been implemented using base Slicer extensions.
- The extension has been tested on Windows (GPU and CPU) and MacOS (CPU).
- Next steps: clean the GitHub [repository](https://github.com/ReubenDo/SlicerTumorSegmentator).






# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![image](https://github.com/NA-MIC/ProjectWeek/assets/17268715/24b9168d-832d-49e9-a6d9-fbe3d08a8870)

<img width="576" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/17268715/fb31bd51-d301-4598-b05b-11af83acf5d1">




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_
