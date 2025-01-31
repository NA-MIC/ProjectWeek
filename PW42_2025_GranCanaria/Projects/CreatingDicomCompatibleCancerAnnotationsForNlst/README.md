---
layout: pw42-project

permalink: /:path/

project_title: Creating DICOM-compatible cancer annotations for NLST
category: DICOM

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Suraj Pai
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Leonard Nürnberg
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

- name: David Clunie
  affiliation: PixelMed Publishing
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->


The National Lung Screening Trial (NLST) is one of the largest lung cancer collections, with over 25K patients. In Imaging Data Commons (IDC), we have segmentations of anatomical regions using the TotalSegmentator model, but, we are missing any annotations of cancer. 

There were several initiatives to add cancer nodule annotations to NLST data in IDC. One set of nodule segmentations was created from an AI model from [this initiative]([https://zenodo.org/records/10081112](https://zenodo.org/records/10081112)), but only a percentage of them have been  verified by an expert.

However, there is one initiative from MIT ([https://github.com/reginabarzilaygroup/Sybil](https://github.com/reginabarzilaygroup/Sybil)) that had experts annotate center points and bounding boxes for nodules in NLST patients. Our plan is to convert these json annotations to DICOM Structured Reports, which can then be ingested into IDC and displayed. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


We will first convert the json point annotations to DICOM Structured Reports. Then we will ingest them into a DICOM datastore, and deploy our own OHIF application to display the points overlaid on the image data. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will understand the format of the json files by plotting them in Slicer. 
2. We will create a DICOM SR for a patient, starting with one point annotation per patient. 
3. We will store these DICOM SR objets in a DICOM data store. 
4. We will deploy OHIF, and display our point annotations along with the image. 
5. If that works, we will add the ability for the DICOM SR to store multiple annotations. 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We have started to understand the format of the json files by plotting them in Slicer. 

![image](https://github.com/user-attachments/assets/2bd2dc91-378b-42fa-bc0b-47e5b8051064)

2. We successfully created a DICOM Structured Report for holding the cancer annotation.
3. Later we will create bounding box DICOM Structured Reports. 


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<video
   controls muted
   src="https://github.com/user-attachments/assets/e2fa70b3-4422-492c-b82c-9e6193003385"
   style="max-height:640px; min-height: 200px">
 </video>


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[Current Google Colab notebook](https://colab.research.google.com/drive/1E_LkCbCqhJTLJ__TPMjNt7bx7tyL-cyw?usp=sharing)

Resources from David Clunie: 
1. [Understanding ImagePatientPosition and ImageOrientation](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html)
2. [DICOM SR for understanding planar annotations](https://www.researchgate.net/publication/353243563_DICOM_SR_for_communicating_planar_annotations_-_An_Imaging_Data_Commons_IDC_White_Paper)
3. [OHIF github issues](https://github.com/OHIF/Viewers/issues/1215)


