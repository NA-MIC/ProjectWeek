---
layout: pw42-project

permalink: /:path/

project_title: Automatic classification of MR scan sequence type
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital/Harvard Medical School
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital/Harvard Medical School
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Knowing the type of MRI scan is an important data curation step. For instance clinicians and developers need to know if a scan is T1 weighted, T2 weighted, diffusion, etc in order to make a diagnosis or develop an AI model. This curation can take a long time to do manually, especially if the fields in DICOM data are missing or incorrect. Some tools have been developed already, mostly for brain image classification, and only a few are available for abdominal/prostate areas. 

The past two project weeks, we've made some progress in developing tools for AI/ML classification of prostate MR scans. See our: 
- [PW 41 page](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/AutomaticClassificationOfMrScanSequenceType/)
- [PW 40 page](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/DicomSeriesClassificationAndVisualizationOfParameters/)
- [paper here](https://openreview.net/forum?id=1GEz81GU3g) and [code here](https://github.com/deepakri201/DICOMScanClassification). 

In this project week, we will focus on creating a 3DSlicer module. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. We will create a 3DSlicer module to perform the scan type classification on all series in a study. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will first allow the user to pick a study from the DICOM database. 
2. We will run inference using our pre-trained model on all the series in the study. 
3. We will modify the layout automatically 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We have created an CNN that uses both image+metadata information to classify a scan into T1w, T2w, diffusion and apparent diffusion coefficient maps. 




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![PW_42_images](https://github.com/user-attachments/assets/12a8c113-15bd-4fdc-8be7-e0037ac25c86)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[PW 41 work](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/AutomaticClassificationOfMrScanSequenceType/) 
[PW 40 work](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/DicomSeriesClassificationAndVisualizationOfParameters/)

