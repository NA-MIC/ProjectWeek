---
layout: pw42-project

permalink: /:path/

project_title: Open Model for Anatomy Segmentation in Computer Tomography
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Murong Xu
  affiliation: University of Zurich
  country: Switzerland

- name: Tamaz Amiranashvili
  affiliation: University of Zurich
  country: Switzerland

- name: Bjoern Menze
  affiliation: University of Zurich
  country: Switzerland

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We have developed a state-of-the-art automated segmentation model capable of identifying 167 anatomical structures in volumetric CT scans. This model has been trained on a combined dataset of more than 22,000 diverse, partially-annotated CT scans, setting a new benchmark in medical imaging. Our goal is to integrate this model into a 3D Slicer extension, making it widely available to the community.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Improve general user experience of the Slicer extension and finalize the development.
2. Prepare for performing large-scale inference on the IDC database.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Enhance user experience of our current prototype of the Slicer extension
   a. explore options for faster CPU-only inference
   b. add DICOM support
   c. incorporate SNOMED naming conventions
2. Finalize extension development (test extension on various OSs, writing tests)
3. Benchmark inference performance and prepare for large-scale inference on the NLST/IDC databases



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Current Achievements:

- finalized Slicer extension UI and added DICOM support
- added support for SNOMED-CT naming conventions
- evaluated hardware requirements for inference on laptops
  - limited memory/CPU only: Trained smaller models

- initial process for working with IDC data: image retrieve, DICOM nifti conversion, restore

Next Steps:
- In progress: test on different OSs




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![334442645-dfbe0cbf-0341-4dfc-991d-bdcf2c621c2d](https://github.com/user-attachments/assets/de0d6f1d-8389-4cde-b597-683e84bb60ea)


![](https://github.com/user-attachments/assets/5cfcf858-b2ac-4c95-99e8-b83307426e58)


<video
   controls muted
   src="https://github.com/user-attachments/assets/4fde92c5-52d9-48a1-af93-dcae64b17c8c"
   style="max-height:640px; min-height: 200px">
 </video>




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* Earlier PW41 project on this topic: [OMAS CT: Open Model for Anatomy Segmentation in Computer Tomography](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/OmasCtOpenModelForAnatomySegmentationInComputerTomography/)
* Earlier work on mapping OMAS labels to SNOMED-CT: [spreadsheet](https://docs.google.com/spreadsheets/d/1pBicNskjMDJBnD3w4yAQroj8SGSAhDfA_TUK24dLEyc/edit?gid=1390863317#gid=1390863317)
