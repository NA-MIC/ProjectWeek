---
layout: pw41-project

permalink: /:path/

project_title: 'OMAS CT: Open Model for Anatomy Segmentation in Computer Tomography'
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Tamaz Amiranashvili
  affiliation: University of Zurich
  country: Switzerland

- name: Murong Xu
  affiliation: University of Zurich
  country: Switzerland

- name: Bjoern Menze
  affiliation: University of Zurich
  country: Switzerland

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We have developed a state-of-the-art automated segmentation model capable of identifying ~170 anatomical structures in volumetric CT scans. This model has been trained on a combined dataset of more than 22,000 diverse, partially-annotated CT scans, setting a new benchmark in medical imaging. Our goal is to integrate this model into a 3D Slicer extension, making it widely available to the community.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Model development: Train models on partially-annotated datasets for whole-body CT segmentation covering approximately 170 structures.
2. Open source the trained models: Open-source the trained models and the associated codebase on 3D Slicer and other platforms, making them easily accessible and utilizable for clinical and research purposes, among others.
3. Release the data: Release the expansive dataset and corresponding annotations on the Imaging Data Commons (IDC), facilitating further research on medical image analysis.





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Data Management: Collection and curation of CT scans.
2. Model Training and Evaluation: Systematic training and assessment of models.
3. Data Release: Consolidation and release of the dataset and corresponding annotations in appropriate formats (e.g., DICOM) on IDC.
4. Model Release: Publication of final model weights.
5. Software Integration: Development and integration of a module for 3D Slicer, optimized for both CPU and GPU usage to accommodate varying user hardware.
6. Documentation: Creation of detailed user guidelines to facilitate the easy application of the models.





## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Current Achievements:

1. Prototypes of the trained models and an operational inference pipeline have already been developed.

In progress / next steps:

1. Benchmarking on public medical image segmentation challenges, followed by evaluation and analysis of results.
2. Preparing the dataset and labels for public release.
3. Developing the 3D Slicer plugin for integration.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![10000005_snapshot](https://github.com/NA-MIC/ProjectWeek/assets/254898/dfbe0cbf-0341-4dfc-991d-bdcf2c621c2d)




<video
    controls muted
    src="https://github.com/NA-MIC/ProjectWeek/assets/254898/6e27cbda-4607-4179-90d4-446bae2483a5"
    style="max-height:1024px; min-height: 200px">
</video>










# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


TBD

