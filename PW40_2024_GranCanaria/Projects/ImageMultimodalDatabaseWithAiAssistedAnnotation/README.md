---
layout: pw40-project

permalink: /:path/

project_title: Linkage of Multimodal Medical Databases using FHIR
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
3. Apply a quantitative image analysis method (radiomics) to the dataset
4. Mapping of clinical & imaging data into the FHIR standard
    * Retrieving of DICOM data via DICOM web from the PACS and map it into FHIR ImagingStudy resources
    * Creation of a tool to be able to map clinical data from a CSV file into fitting FHIR resources
    * Mapping radiomics results into FHIR objects
    * Connecting all of the three sources into a FHIR server
5. Visualize the information joined together to get an overview over the cohort in the dataset now enriched with quantitative image analysis results
6. Integrate FHIR server and workflows into Kaapana

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Creation of a [Github repository](https://github.com/pschader/NAMIC-PW24-Multimodel-Medical-Database) for joint development
2.  Choosing the ([TCIA NSCLC](https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics)) dataset for prototyping
3.  Setup and configuration of the local development environment via Docker compose
4.  Investiagtion how to map tabular data into FHIR resources
   * [Fair4Health Data curation tool](https://github.com/fair4health/data-curation-tool): Works good for producing large scale mappings of tabular data into FHIR resources, but strongly dependant on terminology server. For our simple use case of providing researches with a fast tool to map multimodal data into FHIR resources it appears to be too complex.
   * Creation of a simple webapp for loading CSV files and mapping the data into Patient & Observation FHIR resources.
5.   Mapping of the DICOM resources into FHIR objects
       * Creating a python script to fetch DICOM object from DICOM web API of the local ORTHANC server
       * Map the DICOM metadata of the studies to FHIR ImagingStudy resources using [FHIR resources python library](https://pypi.org/project/fhir.resources/)
6. Create radiomics results from the segmentations of the dataset using Kaapana and the radiomics workflow and map those individual values into FHIR Observation resources

Next steps:
1. Upload the FHIR data onto a FHIR server
2. Visualization of the dataset
3. Integration into Kaapana

# Illustrations

## Approach
<!-- <img width="499" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/50300669/c6a540c4-77b5-4042-bf93-8b85fc4856ad"> -->
![ProjectWeekOverview](https://github.com/NA-MIC/ProjectWeek/assets/19309110/5bbcf1ee-c791-4f54-afc5-99c8e382c993)


## Mapping Tool
<!--<img width="953" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/49638920/27fda4fd-e3d2-4eb9-af65-cb3726a8429c">

<img width="923" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/49638920/7a5443a3-f396-4b95-b1ab-a5b00135c96d">-->

![FinalMMDGif](https://github.com/NA-MIC/ProjectWeek/assets/49638920/5daf092e-f3bd-4972-9320-373deee70c67)


## Overview
![DiagramMMDFHIR](https://github.com/NA-MIC/ProjectWeek/assets/49638920/d8becc40-fd2a-4e15-a9d2-5035c3480ddb)



<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   We can use the MIMIC-IV Dataset with genertaed in this publication:
    <https://physionet.org/content/haim-multimodal/1.0.1/>
*   Orthanc database mongoDB plugin: <https://github.com/Doc-Cirrus/orthanc-mongodb>
*   [FHIR Server integration in Kaapana from PW38](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/KaapanaClinicalData/)
*   [Kaapana](https://www.kaapana.ai/)
*   [FHIR](https://www.hl7.org/fhir/)
*   [FHIR resources python library](https://pypi.org/project/fhir.resources/)
*   [Fair4Health Data curation tool](https://github.com/fair4health/data-curation-tool)
*   Datasets: [TCIA NSCLC](https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics)
*   Project repository: [Github repository](https://github.com/pschader/NAMIC-PW24-Multimodel-Medical-Database)
