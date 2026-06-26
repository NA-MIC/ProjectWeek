---
layout: pw45-project

permalink: /:path/

project_title: Fan mask and OCR bound box editing for OHIF-based DICOM De-Identification verification
  mode
category: Lung Ultrasound
presenter_location: 

key_investigators:

- name: Dave Dinh
  affiliation: BWH
  country: Brigham and Women's Hospital, USA

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

- name: Andras Lasso
  affiliation: Queen's
  country: Canada

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Optimal DICOM de-identification for downstream research requires balancing removal and retention. We must scrub embedded PHI in both tags and pixels while preserving valuable non-PHI metadata (e.g., scan settings like depth). Even with both addressed, human review is still needed to catch misses.

We’re building a closed-loop system with two components:
1. an automated pipeline that scrubs DICOM tags (PS3.15 with configurable overrides), masks pixel PHI by manufacturer, extracts non-PHI pixel data, and produces deterministic, reproducible outputs
2. an OHIF-based reviewer for human verification. Each review records passes, failures, and false positives/misses, which feed back as rule updates so errors don’t recur.

The pipeline handles most de-identification automatically, but reviewers still face significant cognitive load when inspecting every metadata diff, OCR-flagged region, and fan crop. The OHIF mode currently surfaces areas in the DICOM metadata that require verification based on predefined rules but reviewers also need tools to edit PHI masks, OCR bounding boxes for non-PHI extraction, and fan geometry for fan-only pixel extraction.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. The OHIF-based mode should allow users to edit PHI / fan masks and OCR bounding boxes.
2. The pipeline uses edits to self-update and re-run flagged DICOMs for the reviewer to re-verify.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


_No response_



## Progress and Next Steps

Deploy to testing environment and iterate on user feedback.







# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


**DICOM De-ID Loop**

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/b95e956f-f422-494c-8c52-91b3d1fbd174" />

**High Level Overview**

<img width="1728" height="861" alt="Screenshot 2026-06-26 at 2 48 10 PM" src="https://github.com/user-attachments/assets/ba0d5bd5-dab4-48ea-9e85-b1646a594e94" />

<img width="1728" height="915" alt="Screenshot 2026-06-26 at 2 48 21 PM" src="https://github.com/user-attachments/assets/9cb1b243-40ef-4955-85e0-cfe71f077d62" />

<img width="1728" height="972" alt="Screenshot 2026-06-26 at 2 48 48 PM" src="https://github.com/user-attachments/assets/3f5ec870-84ca-4076-9b7b-e1b2cf11057f" />

<img width="1728" height="972" alt="Screenshot 2026-06-26 at 2 49 01 PM" src="https://github.com/user-attachments/assets/c2c87d92-6af4-4f76-8fbf-f5d2e3b6f2fd" />


**DICOM De-ID Verification Mode**

Individual DICOM Review:

<img width="1728" height="998" alt="single_view_ocr_overlay" src="https://github.com/user-attachments/assets/3cbe26d1-69ed-425d-9822-f63665288d5b" />

<img width="1728" height="998" alt="ocr_and_phi_bounding_box_editor" src="https://github.com/user-attachments/assets/649cc05e-9aaa-44a0-b9c1-9ce7a8fceb8e" />

<img width="1728" height="998" alt="singe_view_fan_overlay" src="https://github.com/user-attachments/assets/8d852b63-7e77-4d27-a31c-3a6283d16a17" />

<img width="1728" height="998" alt="fan_geometry_editor" src="https://github.com/user-attachments/assets/4d3edb8d-36b0-431a-8e7f-a3f39e0887e7" />

<img width="1728" height="998" alt="single_view_metadata_review" src="https://github.com/user-attachments/assets/e45c9dbb-d36c-44ab-b6d2-cbd05537b1b8" />


Batch DICOM Review:

<img width="1728" height="998" alt="batch_view_ocr" src="https://github.com/user-attachments/assets/2728db03-2dad-43e2-919b-33aea96023ab" />

<img width="1728" height="998" alt="batch_view_fan" src="https://github.com/user-attachments/assets/a734e329-b123-40f8-adc1-82966644258b" />

<img width="1728" height="998" alt="batch_view_deid" src="https://github.com/user-attachments/assets/d4f5d620-f47a-4f59-bc28-2694e1e20de7" />

<img width="1728" height="998" alt="batch_view_fan_crop" src="https://github.com/user-attachments/assets/cc5e2e8b-92a1-4e4a-84c0-021183a27bf9" />

<img width="1728" height="998" alt="batch_view_metadata_review" src="https://github.com/user-attachments/assets/924a5e64-9bf7-447e-8a6f-31642899abd1" />

<img width="1728" height="998" alt="batch_view_summary" src="https://github.com/user-attachments/assets/bc90715a-48b2-4f1f-a8f3-a6a20545e0cc" />




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

