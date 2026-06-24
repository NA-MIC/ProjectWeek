---
layout: pw45-project

permalink: /:path/

project_title: Extracting deep learning features from CT images of the thoracic region for lung cancer
  applications
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Renzo Phellan Aro
  affiliation: Lunenfeld-Tanenbaum Research Institute
  country: Sinai Health, Canada

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project focuses on creating or using existing foundational deep learning models in 3D Slicer to process CT images of the thoracic region. The objective is to extract features that can be used for lung cancer applications, such as classification, screening, and risk prediction.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. The main objective is to create a 3D Slicer application that receives either one or multiple CT images, processes them with a deep learning model, and generates features that can be used for various lung cancer applications.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Identify members of the 3D Slicer community interested in participating in the project.
2. Meet and discuss the scope of the project during the 3D Slicer week preparation meetings.
3. List the functional and GUI requirements for the application.
4. Identify useful deep learning foundational models for lung cancer applications.
5. Develop the 3D Slicer application to extract features from CT images of the thoracic region.



## Progress

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Worked on identifying members of the 3D Slicer community interested in participating in the project.
2. Usid Claude AI to generate the graphical interface in 3D Slicer to process medical images using the [Tangerine](https://github.com/niccolo246/3D-MAE-MedImaging) model.
3. Created a stand-alone command-line interface to access the model via OHIF.

## Next Steps

1. Look for more model models that can encode CT images to add to the interface.
2. Connect VS studio code via ssh to a server, for easier development with Claude AI.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->






# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. <https://projectweek.na-mic.org/PW44_2026_GranCanaria/Projects/ExplorationOfFoundationModelsAndTheirEmbeddingsForOtherTasksUsingTheCloud/>
2. <https://github.com/AIM-Harvard/TumorImagingBench>
3. <https://imagingdatacommons.github.io/nlst-sybil-connectome/?model=CTClipVit&match=c&color=cancerType>
4. <https://github.com/niccolo246/3D-MAE-MedImaging>
5. <https://arxiv.org/pdf/2501.09001>
6. <https://pmc.ncbi.nlm.nih.gov/articles/PMC12876872/>

