---
layout: pw40-project

permalink: /:path/

project_title: Linking segmentation and imaging data with different geometries using dcmqi
category: DICOM
presenter_location: In-person

key_investigators:

- name: Reuben Dorent
  affiliation: BWH
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: Inc., USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

- name: Colton Barr
  affiliation: Queen's University
  country: Canada

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Michael Onken
  affiliation: OpenConnections
  country: Germany

- name: David Clunie
  affiliation: PixelMed
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to clarify best practices and discuss possible fixes for linking segmentation and imaging data with different geometries using dcmqi. This question arose during curation of The Brain Resection Multimodal Imaging Database (ReMIND) for TCIA and subsequent challenges with viewing unlinked segmentations using the OHIF viewer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A: Discuss possible fixes for this dcmqi linking issue when using imaging data and segmentations with differing geometries.
2.  Objective B: Ensure the ReMIND data available in TCIA has the appropriate linking between segmentations and imaging, and can be viewed using OHIF.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Get input from all stakeholders on best practices and potential fixes for this linking problem.
2.  Establish a plan for next-steps.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
1. Andrey summarized the implementation challenges in this issue - need to hear from @dclunie: [https://github.com/QIICR/dcmqi/issues/489](https://github.com/QIICR/dcmqi/issues/489)

2. Perhaps consider something like recent RT Structure Set addition to standard that added [SourceSeriesInformationSequence](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.8.5.html#para_a625a323-0d2f-4922-b292-6d81fb912774) and [SourceSeriesSequence](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.8.6.html#para_ccc7aad7-b3f7-4fdc-b498-5590a1983bdd) ([CP 2296 Provide additional ROI parameters to avoid parsing strings](https://dicom.nema.org/medical/dicom/Final/cp2296_ft_ProvideAdditionalROIParametersToAvoidParsingStrings.pdf))

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
