---
layout: pw44-project

permalink: /:path/

project_title: SlicerUltrasound Extension development
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tamas Ungi
  affiliation: ClaroNav
  country: Canada

- name: David Dinh
  affiliation: SlicerUltrasound Team
  country: USA

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany 

---

# Project Description

<!-- Add a short paragraph describing the project. -->


**SlicerUltrasound** is a 3D Slicer extension that currently includes two modules: 1) **_Anonymize_**, which removes both metadata-embedded PHI and burned-in text from DICOM images, and 2) **_Annotate_**,  which supports expert labeling of image findings. 

The **_Anonymize_** module has been used at multiple hospitals (BWH, Lahey, Indiana Methodist to remove PHI from patient exams. Users import DICOM ultrasound images from their local folder, and apply probe-specific masking templates to remove burned-in identifiers. Users specify the transducer type—curvilinear or phased array—which determines the expected fan shape. By marking three or four points on the image, the module interpolates the imaging sector and masks any visual PHI outside this region while preserving diagnostically relevant content. 

The **_Annotate_** module allows experts to annotate lung ultrasound video clips, focusing on features such as pleura lines and B-lines. It provides an intuitive interface for frame-by-frame annotation, supports multiple raters, and saves annotation data for future research and machine learning.

Our goals during the project week are to: 
1. Obtain feedback from developers and clinicians 
2. Implement changes to the extension
3. Connect with and talk to others about the MONAI Ultrasound Working Group - Annotation and Anonymization subgroup. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Demonstrate the current extension to Slicer core developers and obtain feedback
2. Demonstrate to clinicians and obtain feedback 
3. Integrate changes to the extension

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Many people provided useful feedback about possible improvements to the modules.
2. We also looked into the current OHIF viewer, which already allows for users to annotate pleural lines and B-lines. Martin added functionality needed to save additional annotations. 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Anonymize module
<img width="1740" height="980" alt="Image" src="https://github.com/user-attachments/assets/ebfdbe29-4540-47d1-9a10-1d05e172fcd9" />

Annotate module
<img width="1476" height="952" alt="Image" src="https://github.com/user-attachments/assets/7f8b89b7-00f9-42b2-aae1-2558b2e64279" />

Original OHIF app for annotation of pleural lines and B-lines - on our anonymized lung US data: 
<video
   controls muted
   src="https://github.com/user-attachments/assets/c51b4dd0-ba04-4efa-82e7-8b1723e1b7cb"
   style="max-height:640px; min-height: 200px">
 </video>

Enhancements to the OHIF app for annotation of pleural lines and B-lines - on sample cardiac US data. This helps with the clinical workflow, where step 1) the clinician scans through the ultrasound clip and quickly pick the frame that has the maximum number of B-lines, and step 2) the clinician or a fellow can come back later and annotate the pleural lines and B-lines. 

<video
   controls muted
   src="https://github.com/user-attachments/assets/a198f836-b99b-40d4-9336-7a9b186df30d"
   style="max-height:640px; min-height: 200px">
 </video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[Link to code](https://github.com/SlicerUltrasound/SlicerUltrasound)

