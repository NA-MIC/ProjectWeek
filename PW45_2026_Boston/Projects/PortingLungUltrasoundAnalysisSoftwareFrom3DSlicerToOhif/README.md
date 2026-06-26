---
layout: pw45-project

permalink: /:path/

project_title: Porting lung ultrasound analysis software from 3D Slicer to OHIF
category: Lung Ultrasound
presenter_location: 

key_investigators:

- name: Dave Dinh
  affiliation: BWH
  country: Brigham and Women's Hospital, USA

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Our team has been developing various 3D Slicer modules for lung ultrasound analysis (https://github.com/SlicerUltrasound/SlicerUltrasound), from de-identification to annotation and adjudication. However, we have slowly started porting the extensions developed in Slicer to OHIF, as this is easier for the clinicians and other researchers to use. It doesn't require them to install any additional software, and they can access OHIF from the web. 

Initial work has been performed by the Radical Imaging team to update OHIF with the B-line quantification tools that our team requires. However, there are some improvements that still need to be made: 
1. We need to make sure annotation of the pleural lines and B-lines are supported, and that the resulting files are saved appropriately. 
2. We would like to have single-rater vs multi-rater modes, where the multi-raters can work together to discuss a case, or adjudicate the annotations. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Fix the current issues with allowing annotations and saving of the files. 
2. Open a PR to the official OHIF repository for our proposed changes. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. First, we will assess the current issues with the B-line detection viewer. 
2. Then we will make the necessary changes to reproduce the functionality from the SlicerUltrasound extension. 
3. Lastly, we will make a PR to the official OHIF repo. 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


3D Slicer extension for annotating pleural lines and B-lines: 
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/00192df6-e400-4f88-8c45-7a2d66feb4e8" />

Current functionality in OHIF: 
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/572f4131-d48c-4fb8-804c-ea2ce1b53f14" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[SlicerUltrasound code](https://github.com/SlicerUltrasound/SlicerUltrasound)

