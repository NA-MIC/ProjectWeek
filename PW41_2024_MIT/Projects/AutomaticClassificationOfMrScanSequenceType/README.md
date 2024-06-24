---
layout: pw41-project

permalink: /:path/

project_title: 'Automatic classification of MR scan sequence type '
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Cosmin Ciausu
  affiliation: BWH
  country: USA

- name: Megha Kalia
  affiliation: BWH
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Data curation is a necessary step before using many AI or ML models, but it can be difficult and time-consuming to do manually. For instance in prostate cancer, most tools use multiple types of MR sequences as input to develop models and perform tasks such as segmentation. 

In this project, we will develop methods for automatic classification of MR sequences. We had some great discussions and headway [last project week](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/DicomSeriesClassificationAndVisualizationOfParameters/), and are continuing this work. 

We also made some progress since last project week and developed a few methods for classification of T2 axial, diffusion weighted (DWI), apparent diffusion coefficient (ADC) images, and dynamic contrast enhanced (DCE) images. We used combinations of image data and DICOM metadata as input, and developed a random forest classifier, and also two CNN-based classifiers -- see our [paper here](https://openreview.net/forum?id=1GEz81GU3g) and [code here](https://github.com/deepakri201/DICOMScanClassification). 

This project week, we'd like to talk to more people, address limitations of our work, and hopefully work on developing a more robust method for classification of scans. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. We would like to discuss the limitations of our previous work, and brainstorm new ideas for automatic classification of the MR series type. 
2. We would like to create an easy colab notebook for people to try out the methods
4. We would like to think about developing a more robust method



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will talk to people to discuss limitations of our method. For instance, what types of metadata should we use for the classification? Should we have a class for unknown scan type? Should we do a hierarchical classification method? How can we make the model agnostic to the area scanned? 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. WIP [Colab notebook](https://github.com/deepakri201/DICOMScanClassification_pw41/blob/main/DICOMScanClassification_user_demo.ipynb) - we download data from IDC, and run inference using the three pretrained models. 
2. WIP [HuggingFace space demo](https://huggingface.co/spaces/deepakri201/DICOMScanClassificationDemo) - we want the user to choose which data to download from IDC, and then will choose a pre-trained model to run inference 




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[Progress from previous project week](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/DicomSeriesClassificationAndVisualizationOfParameters/)

[Current work](https://openreview.net/forum?id=1GEz81GU3g)

[Current code](https://github.com/deepakri201/DICOMScanClassification)


