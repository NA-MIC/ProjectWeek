---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/ImproveTciaBrowserExtension/README.html

project_title: Improve TCIA Browser extension
category: Infrastructure
presenter_location: Online

key_investigators:

- name: Justin Kirby
  affiliation: Frederick National Laboratory for Cancer Research
  country: USA

- name: Adam Li
  affiliation: Georgetown University
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/) is an NCI-funded service which de-identifies and publishes cancer imaging datasets.  The imaging data are organized as “collections” or "analysis result" datasets defined by a common disease (e.g. lung cancer), image modality or type (MRI, CT, digital histopathology, etc) or research focus. An emphasis is made to provide supporting data related to the images such as patient outcomes, treatment details, genomics and expert analyses where available.

[TCIA Browser](https://github.com/QIICR/TCIABrowser) is an extension that lets users easily download and import TCIA data into 3D Slicer.  This project seeks to improve the TCIA Browser extension for 3D Slicer by updating it to leverage [TCIA-Utils](https://github.com/kirbyju/tcia_utils) to access TCIA's APIs.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The major improvements we'd like to address with TCIA Browser include:

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Identify locations in the code that use the older API to download or query data and update them to leverage TCIA-Utils functions such as downloadSeries(), getCollections(), getPatients(), getStudies() and getSeries().
2.  Implement a new feature to support logging in to TCIA Browser using the getToken() function in TCIA-Utils.
3.  Review the existing metadata fields in the Browser GUI.  Perform queries of the TCIA database to determine how often these fields are populated.
4.  Discuss and agree on other available metadata fields that may be useful to Slicer users.  Run queries to find out how often they're populated.  Include external sources from NCI's Cancer Research Data Commons that may include genomic, proteomic and clinical data on the same subjects that TCIA hosts.
5.  Update the GUI with a "Download TCIA Manifest" button and leverage the TCIA-Utils downloadSeries() function with the input_type = "manifest" option to pass the path of a \*.TCIA manifest file as the series_data parameter.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Identified the code that used the old API and updated them to use the new API.
2.  Added and removed some columns/metadata fields within the browser widget.
3.  Set the default cache option to off.
4.  Next Step: Implement the login function; Update the new API further to use the tcia_utils modules directly; Implement the manifest file download function.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
