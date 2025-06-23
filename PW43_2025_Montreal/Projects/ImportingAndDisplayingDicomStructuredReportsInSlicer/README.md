---
layout: pw43-project

permalink: /:path/

project_title: Importing and displaying DICOM Structured Reports in Slicer
category: DICOM

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA
  
- name: Chris Bridge 
  affiliation: Massachusetts General Hospital 
  country: USA  

- name: Ron Kikinis
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


In TCIA, multiple collections include CSV files with different measurements. For instance, the [ProstateX collection](https://www.cancerimagingarchive.net/collection/prostatex/) has information about the Gleason score and target biopsy points. Other annotations, such as the lesion bounding boxes for NLST from [Sybil](https://github.com/reginabarzilaygroup/Sybil/tree/main) are in json format. 

There is no easy way to use these measurements. If we want to use them in Imaging Data Commons (IDC), the data needs to be in a standardized format like DICOM Structured Reports (SRs). From the last project week [here](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/CreatingDicomCompatibleCancerAnnotationsForNlst/), we have already created SRs for a few of these collections that hold points and bounding boxes. 

However, right now, Slicer can only load a specific type of SR. We are currently working on adding functionality to load SRs to load and display points, boxes, and lines. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


We will create SRs to hold points and bounding boxes, and modify the DICOMTID1500Plugin to load and display these measurements as markups. 



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1.  Create SRs for the ProstateX (csv from TCIA) and NLST (Sybil) collections. 
2. Modify the DICOMTID1500Plugin.py in [QuantitativeReporting](https://github.com/QIICR/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py) to read these SRs and display as markups. 
3. Show a table holding the measurements. 
4. Display the markups appropriately in the subject hierarchy. 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We have created SRs for ProstateX (points) and NLST Sybil (bounding boxes). 
2. We have modified the plugin to load points, boxes, and lines. 
3. We need to load the appropriate reference DICOM files/have a popup to choose the series to display. 
4. We need to load the markups in a folder in the subject hierarchy. 



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1428" alt="Image" src="https://github.com/user-attachments/assets/cd8a5926-90b1-4e18-8d96-651bcbd2bc6a" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- [Slicer discourse discussion](https://discourse.slicer.org/t/loading-and-displaying-dicom-structured-reports/42754/7)
- [My fork of QuantitativeReporting](https://github.com/deepakri201/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py)
- [Creating SRs from last project week](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/CreatingDicomCompatibleCancerAnnotationsForNlst/)

