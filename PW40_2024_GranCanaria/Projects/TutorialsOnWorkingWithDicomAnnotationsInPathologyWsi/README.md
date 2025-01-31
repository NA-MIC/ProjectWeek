---
layout: pw40-project

permalink: /:path/

project_title: Tutorials on working with DICOM annotations in pathology WSI
category: DICOM
presenter_location: In-person

key_investigators:

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: Chris Bridge
  affiliation: MGH
  country: USA

- name: David Clunie
  affiliation: PixelMed
  country: USA

- name: André Homeyer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to create tutorials on how to work with DICOM annotations in pathology whole-slide images (WSIs). We will focus on region annotations stored as DICOM Structured Reports (SR) for a dataset of Rhabdomyosarcoma, which was recently ingested into the Imaging Data Commons (IDC). We want to create an easy-to-follow workflow that extracts images and annotations from the IDC and uses established (python) libraries for model training and evaluation.
If time permits we will continue working on nuclei annotations stored as DICOM Microscopy Bulk Simple Annotations (MBSA). This work was started in the last project week in Montreal, but hindered by technical issues (see [here](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/TutorialsOnWorkingWithDicomAnnotationsInPathologyWholeSlideImages/)).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A: Have a Colaboratory notebook ready that explains work with DICOM SR and uses the annotations for some exemplary use case.
2.  Objective B (optional): Have a Colaboratory notebook ready that exemplifies work with DICOM MBSA.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Set-up Google Healthcare DICOM store holding the available DICOM SR annotations.
2.  Investigate which libraries are suitable to show-case an easy to follow workflow, e.g. slideflow or HistomicsTK.

## Progress and Next Steps

1. Set-up Google Healthcare DICOM store holding the available DICOM SR annotations.
2. Investigating libraries suitable to show-case and easy to follow workflow took way more time than expected as most publicly available state-of-the-art algorithms don't work with DICOM images, neither do the work with DICOM annotation objects, like SR or SEG. Instead they usually require some specifically formatted csv file, which is very counterproductive to our main goal: providing easy workflows from DICOM annotations in the IDC to analysis algorithms. However, I had several valuable discussions about other people's best practices and summarized available libraries capabilities trying to figure out the main barriers that prevent direct usage of DICOM objects.
3. [Documentation](https://docs.google.com/document/d/1xI9ZbZOk_nTz8YDP3xeozRspN1T-2zxQ79ecPufFfH0/edit?usp=sharing) and [Code](https://colab.research.google.com/drive/1aM3IgvPSk7OEzmg1YIoxGT-A4AaDxhqn?usp=drive_link) is still work-in-progress and will be extended after the Project Week.

# Illustrations

![Overview DICOM structured reports IOD](./overview_dicom_sr.png) \
*Overview DICOM structured reports IOD. Taken from https://doi.org/10.1038/s41467-023-37224-2.*

# Background and References

- [DICOM Structured Reports](https://dicom.nema.org/dicom/2013/output/chtml/part20/sect_A.3.html)
- Documentation [slideflow](https://slideflow.dev/)
- Documentation [HistomicsTK](https://digitalslidearchive.github.io/HistomicsTK/api-docs.html)
