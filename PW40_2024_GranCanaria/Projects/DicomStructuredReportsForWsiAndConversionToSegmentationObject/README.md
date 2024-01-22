---
layout: pw40-project

permalink: /:path/

project_title: DICOM Structured Reports for WSI and conversion to segmentation object
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Maximilian Fischer
  affiliation: DKFZ
  country: Germany

- name: Philipp Schader
  affiliation: DKFZ
  country: Germany

- name: Marco Nolden
  affiliation: DKFZ
  country: Germany

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: David Clunie
  affiliation: PixelMed
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Chris Bridge
  affiliation: MGH
  country: USA

- name: Klaus Maier-Hein
  affiliation: DKFZ
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

In this project, we want to investigate and compare several approaches to convert DICOM Structured reports into DICOM segmentation objects. We use the integrated SLIM Viewer in Kaapana to create Structured Reports on DICOM WSI files and also want to compare the QuPath viewer as additional DICOM WSI viewer in Kaapana.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A: Examine existing libraries to render the coordinates from the SR file as segmentation.
2.  Objective B: Examine conversion methods to create DICOM annotation objects from the SR files
3.  Objective C: Evaluate file formats of QuPath DICOM WSI annotations.
4.  Objective D: Explore integration capabilities of QuPath as Viewer in Kaapana

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Familiarize with the highdicom librariy
2.  Compare result with custom visulaizations
3.  Evaluate conversion tools for SR files
4.  Test PACS connectivity of QuPath

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

This project is the continuation from last years project weeks.
[PW 38](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/IDC_DICOM_WSI_workflow/)
[PW 39](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/HistologyAiModelsImportedIntoIdc/)
[Kaapana](https://kaapana.readthedocs.io/en/stable/)
