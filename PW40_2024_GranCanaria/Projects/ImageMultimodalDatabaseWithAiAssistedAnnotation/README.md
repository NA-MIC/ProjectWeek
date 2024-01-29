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

- name: Umang Pandey
  affiliation: Universidad Carlos III de Madrid
  country: Spain
      
- name: Philipp Schader
  affiliation: DKFZ
  country: Germany

- name: Odile Elias
  affiliation: DKFZ
  country: Germany

- name: Marco Nolden
  affiliation: DKFZ
  country: Germany
---

# Project Description

<!-- Add a short paragraph describing the project. -->

Despite various existing solutions for DICOM Medical Database, (e.g. Kaapana, XNAT server, ...) these systems lack capablities to accompany the imaging data with medical records.
However, (to the best of our limited knowledge) there exist very few open sources solutions that can store multimodal data (DICOM, Electronic Health Records, REDCAP questionnaires & FHIR) for clinical research.

FHIR represents a globally recognized standard for the interoperable exchange and integration of medical information. Adopting FHIR in medical image analysis enables more in-depth analysis by combining clinical information with imaging data. Moreover, it facilitates the representation of analysis results in a standardized format. 

Initial steps towards adopting FHIR within medical image analysis platforms have been taken during the [38th Project week](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/KaapanaClinicalData/). 

However, aspects like the general mapping of tabular data into FHIR resources remains challenging which should be addressed in this project as well as the joint visualization of results from computational image analysis together with clinical data from the patients.

The project would comprise set up a PACS as well as a FHIR Server for storing of multimodal patient data for further AI analysis. This data storage will be designed to assist AI enabled interactive annotation. Additionally it would include visualizing capabilities (e.g., descriptive statistics). Ideally the database will also support data retieval API for data visualization dashboard. In the end the prototype should be integrated in Kaapana.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

This project aims to develop an open-source and ideally community-maintained solution for:

1. Data Standardization: All collected data will be converted and standarized into research format (e.g. FHIR format)
2. Having a multimodal research database or integration of medical records.
3. Visualization tools using the system enable exploration of the multimodal dataset
4. Ideally: The infrastructure would enable connection to annotation tools such as available Kaapana / MONAI Label.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Select and download a suitable multimodal Dataset ([TCIA NSCLC](https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics))
2.  Creating a local development setup
    * Setup a local ORTHANC PACS server
    * Setup a local HAPI FHIR server
<!-- 3.  U
2.  Define an standardize (or extended in teh community) format to optimally store multimodal data  ( e.g. the Brain Imaging Data Structure BIDS format extension)
3.  Create a mongoDB database for optimal storage
4.  Configure ORTHANC server for visualization and integration prposes
5.  (optional) Add possibility to export to an structured format, integrating Magnetic Resonance Imaging (MRI) (maybe in DICOM but would support NIFTI conversion), Electronic Health Records (EHR)...
6.  Enable data anotation capabilites ( e.g.  OHIF viewer with MONAI label) -->

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.
2.  Data curation
3.  Basic ORTHANC server proptotyping

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<!-- <img width="499" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/50300669/c6a540c4-77b5-4042-bf93-8b85fc4856ad"> -->
![ProjectWeekOverview](https://github.com/NA-MIC/ProjectWeek/assets/19309110/5bbcf1ee-c791-4f54-afc5-99c8e382c993)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   We can use the MIMIC-IV Dataset with genertaed in this publication:
    <https://physionet.org/content/haim-multimodal/1.0.1/>
*   Orthanc database mongoDB plugin: <https://github.com/Doc-Cirrus/orthanc-mongodb>
*   [FHIR Server integration in Kaapana from PW38](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/KaapanaClinicalData/)
*   [Kaapana](https://www.kaapana.ai/)
*   [FHIR](https://www.hl7.org/fhir/)
*   Datasets: [TCIA NSCLC](https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics) 
