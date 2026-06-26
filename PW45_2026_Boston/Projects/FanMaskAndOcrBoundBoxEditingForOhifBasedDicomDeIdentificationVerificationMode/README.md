---
layout: pw45-project

permalink: /:path/

project_title: Fan mask and OCR bound box editing for OHIF-based DICOM De-Identification verification
  mode
category: DICOM
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

Deploy to development environment to get feedback from end users.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


**DICOM De-ID Loop**

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/b95e956f-f422-494c-8c52-91b3d1fbd174" />

**DICOM De-ID Verification Mode**

Single DICOM review mode:

<img width="1728" height="998" alt="single_view_ocr_overlay" src="https://github.com/user-attachments/assets/3d5c1180-e155-4ec7-b896-9d5efcdd3a06" />

<img width="1728" height="998" alt="ocr_and_phi_bounding_box_editor" src="https://github.com/user-attachments/assets/c2dec3cd-6d54-4a5c-aa1b-e246aeb8d0f5" />

<img width="1728" height="998" alt="singe_view_fan_overlay" src="https://github.com/user-attachments/assets/bdb21fa1-4240-4ce0-9560-2f590b8b5bad" />

<img width="1728" height="998" alt="fan_geometry_editor" src="https://github.com/user-attachments/assets/4b1e4b7c-8b51-44ee-8307-f3c944e1aa4d" />

<img width="1728" height="998" alt="single_view_metadata_review" src="https://github.com/user-attachments/assets/8d86bc7a-c5b9-4d4f-9479-dba74cd95c10" />

<img width="1728" height="998" alt="single_view_summary" src="https://github.com/user-attachments/assets/ced5757d-c93c-4fcd-9a86-5c9f171e40e1" />

Batch DICOM review mode:

<img width="1728" height="998" alt="batch_view_ocr" src="https://github.com/user-attachments/assets/5d76a0a3-fb31-4d63-aa01-b481fa1f02f7" />

<img width="1728" height="998" alt="batch_view_fan" src="https://github.com/user-attachments/assets/07d73882-44a1-4b5b-acc7-b9043bba4db6" />

<img width="1728" height="998" alt="batch_view_deid" src="https://github.com/user-attachments/assets/0507a25e-af39-40fc-afed-e62d9ac42422" />

<img width="1728" height="998" alt="batch_view_fan_crop" src="https://github.com/user-attachments/assets/f6f75edf-2c9f-418e-b919-72b520d1b8e9" />

<img width="1728" height="998" alt="batch_view_metadata_review" src="https://github.com/user-attachments/assets/57ae4227-8686-403c-8b1e-4a39c396fa93" />

<img width="1728" height="998" alt="batch_view_summary" src="https://github.com/user-attachments/assets/551f4921-c695-4eeb-ae16-ebc90930227c" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

