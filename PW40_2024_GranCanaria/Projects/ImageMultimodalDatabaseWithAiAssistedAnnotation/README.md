---
layout: pw40-project

permalink: /:path/

project_title: Image Multimodal Database with AI Assisted Annotation
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Maria Monzon
  affiliation: ETHz
  country: Switzerland

- name: Catherine Jutzeler
  affiliation: ETHz
  country: Switzerland

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Despite various existing solutions for DICOM Medical Database, (e.g. XNAT server), the storage of medical records.
However, (to the best of my limited knowledge) there exist very few open sources solutions that can store multimodal data (DICOM, Electronic Health Records, REDCAP questionaires) for clinical research.
The project would comprise set up a ORTHANC PACS Server with a non-relational MongoDB database as a backend for efficient stoarage of patient multimodal data and high thoughtput for further AI analysis. This database will be designed to assist AI enabled interactive annotation. Additionally the database would include visualizing capabilities (e.g., descriptive statistics). Ideally the database will also support data retieval API for data visualization dashboard

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

This project aims to develop an open-source and ideally community-maintained solution for:

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

0.  Define an standardize (or extended in teh community) format to optimally store multimodal data  ( e.g. the Brain Imaging Data Structure BIDS format extension)
1.  Create a mongoDB database for optimal storage
2.  Configure ORTHANC server for visualization and integration prposes
3.  (optional) Add possibility to export to an structured format, integrating Magnetic Resonance Imaging (MRI) (maybe in DICOM but would support NIFTI conversion), Electronic Health Records (EHR)...
4.  Enable data anotation capabilites ( e.g.  OHIF viewer with MONAI label)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Data curation
2.  Basic ORTHANC server proptotyping

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

None

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   We can use the MIMIC-IV Dataset with genertaed in this publication:
    <https://physionet.org/content/haim-multimodal/1.0.1/>
*   Orthanc database mongoDB plugin: <https://github.com/Doc-Cirrus/orthanc-mongodb>
