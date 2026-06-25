---
layout: pw45-project

permalink: /:path/

project_title: Exploring Ultrasound Multi-frame Image Storage Structured Report support for Slicer/OHIF
category: DICOM
presenter_location: 

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Chris P. Bridge
  affiliation: Massachusetts General Hospital
  country: USA

- name: Matt McCormick
  affiliation: Fideus Labs
  country: USA

- name: Dave Dinh
  affiliation: BWH
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Our team has built a 3D Slicer extension for ultrasound anonymization, annotation, and adjudication (https://github.com/SlicerUltrasound/SlicerUltrasound). We are currently trying to port the functionality of these tools to OHIF in order to make the processing more streamlined for clinicians and avoid the downloading of additional tools. 

However, we currently store all of our annotations as JSON. This can be problematic as JSON can be prone to misinterpretation; we had to write specialized software to load these annotations into Slicer, and we are missing much of the metadata to associate the file with the referenced image. 

In this project, I want to see if using DICOM Structured Reports (SR) will help our use case. Having our files as SRs would help us to utilize the cloud and retain all important metadata. But it might also make processing more complicated. Therefore, the goal of this week is to see how much effort is needed to add functionality to Slicer/OHIF for Ultrasound Multi-frame Image Storage. 

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Create support for Ultrasound Multi-frame Image Storage in 3D Slicer and OHIF 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Create a DICOM Structured Report for our annotations using Ultrasound Multi-frame Image Storage (both pleura line and B-line points/lines, and manual annotations like pleural percentage)
2. Create these SRs using both highdicom and [itk-wasm](https://docs.itk.org/projects/wasm/en/latest/introduction/file_formats/dicom.html) (as suggested by Matt, better for OHIF)
3. Add functionality to 3D Slicer core for loading, parsing, and viewing these SRs. 
4. Make sure that the SR can be loaded into the official OHIF viewer. 
5. Add functionality to the OHIF `usAnnotation` extension to save the annotations as an SR 
6. Deploy OHIF with `usAnnotation` to connect to the cloud (Google Healthcare DICOM datastore) 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Converted our JSON annotation file to a DICOM SR 
2. Confirmed the DICOM SR can load in OHIF 
3. Added functionality to 3D Slicer to load, parse, and view these DICOM SRs
4. Next week - will make a PR to Slicer
5. WIP - deploying OHIF connected to a Google Cloud Platform DICOM datastore, with the usAnnotation plugin support (Thank you, Martin and Andrey, for your help!)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Current workflow: 

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/6574e377-dc30-4454-9938-78fb3db31f39" />

Successfully loaded the converted annotations in OHIF!

<video
   controls muted
   src="https://github.com/user-attachments/assets/dd84c277-2fd6-47e2-a331-e47ff4af16ad"
   style="max-width:800px">
 </video>

Successfully loaded the converted annotations in Slicer! 

<video
   controls muted
   src="https://github.com/user-attachments/assets/27951621-5f61-4c54-b0e7-d3572df79452"
   style="max-width:800px">
</video>
   
Interactive dashboard to keep track of one type of annotations: 

<img width="1508" height="850" alt="lus_dashboard" src="https://github.com/user-attachments/assets/d3193526-2101-4856-a7f3-896519721d6e" />

<video
   controls muted
   src="https://github.com/user-attachments/assets/6b7796dd-2c60-4c36-9a2c-632d6ec1b6b7"
   style="max-width:800px">
</video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[Google Colab notebook for creating the Structured Report]()

[GitHub code for the dashboard](https://github.com/deepakri201/lus-dashboard/)

_No response_

