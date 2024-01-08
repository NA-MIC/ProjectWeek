---
layout: pw40-project

permalink: /:path/

project_title: WSI-DICOM Improvement - From Viewer to Analysis
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Fabian Hörst
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Lukas Heine
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Moon Kim
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Fin H. Bahnsen
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Jens Kleesiek
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Despite various existing solutions for the conversion of WSI data into DICOM, there is a distinct lack of conversion tools (vendor agnostic) that result in DICOM files. Current solutions fall short in generating DICOM files compatible with OpenSlide (4.0.0) and OHIF/SLIM-Viewer, including a PACS, impeding seamless integration and compromising overall performance.

Our objective is to 1. assess available conversion tools, 2. examine their seamless integration capabilities, and 3. enhance or develop our own solutions for WSI-DICOM conversion that integrates into PACS systems connected to web-based viewers (OHIF/SLIM), but also works locally with open-source Viewers such like QuPath (newest version 0.5.0). As automatic slide analysis with AI algorithms (mostly Python) is a cornerstone of computational pathology, OpenSlide integration is another necessary requirement.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

This project aims to test existing software solutions for vendor-agnostic WSI to DICOM conversion in digital pathology and deliver/develop an open-source, community-maintained software solution. The tool must adhere to established software design patterns, ensuring ease of contribution from the community.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Provide a testing suite for testing resulting DICOM files, consisting of PACS/Viewer/Analysis-Components
2.  Test existing WSI DICOM solutions and find shortcomings
3.  Develop/Improve WSI DICOM conversions
4.  Deliver key insights into shortcomings to push conversion forward

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

Next steps are to build the test suite in advance, prepare test data and begin to collect more tools

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![idea](https://github.com/NA-MIC/ProjectWeek/assets/67600643/ff39403e-8dc6-411e-9f78-31189f242ea0)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

None
