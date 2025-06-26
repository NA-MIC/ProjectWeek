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

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada
  
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


1. Create SRs for the ProstateX (csv from TCIA) and NLST (Sybil) collections. 
2. Modify the DICOMTID1500Plugin.py in [QuantitativeReporting](https://github.com/QIICR/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py) to read these SRs and display as markups. 
3. Show a table holding the measurements. 
4. Display the markups appropriately in the subject hierarchy. 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. We have created SRs for ProstateX (points) and NLST Sybil (bounding boxes). 
2. We have modified the plugin to load points, boxes, and lines. 
3. We have loaded the markups in a folder in the subject hierarchy and have displayed the table.
4. Currently, we are working on loading the correct referenced series. 

I had some good discussions this week with Ron, Steve, and Andras about how to improve the extension. 

Summary of the discussion: 
- How to effectively display the different annotations
- How to store data describing each of the annotations - node attributes vs table
- Improvements in the subject hierarchy - making sure table/markups are linked to the series/study 
- How this interface can be used to later save SRs
- How this work can fit into the larger scheme of data exploration 
- How to modify and preconfigure the layout for each of the types of annotations, for instance, below for bounding boxes: 
- <img width="963" alt="Screenshot 2025-06-25 at 1 37 56 PM" src="https://github.com/user-attachments/assets/1b8d855b-f4bf-4f17-a06d-c1be873904dc" />

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Example of a DICOM SR with points - ProstateX biopsy target points
<img width="1508" alt="ProstateX_point" src="https://github.com/user-attachments/assets/1ecccd9c-94eb-4dcf-a9a7-c27acc6af019" />

Example of a DICOM SR with bounding boxes - Sybil lesion annotations for NLST
<video
   controls muted
   src="https://github.com/user-attachments/assets/d8976a62-3a53-4de9-a78f-00fb6d6c8920"
   style="max-height:640px; min-height: 200px">
 </video>

Example of a DICOM SR with lines 
<img width="1428" alt="Image" src="https://github.com/user-attachments/assets/cd8a5926-90b1-4e18-8d96-651bcbd2bc6a" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- [Slicer discourse discussion](https://discourse.slicer.org/t/loading-and-displaying-dicom-structured-reports/42754/7)
- [My fork of QuantitativeReporting](https://github.com/deepakri201/QuantitativeReporting/blob/master/DICOMPlugins/DICOMTID1500Plugin.py)
- [Creating SRs from last project week](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/CreatingDicomCompatibleCancerAnnotationsForNlst/)

