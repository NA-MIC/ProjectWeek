---
layout: pw45-project

permalink: /:path/

project_title: Fan mask and OCR bound box editing for OHIF-based DICOM De-Identification verification
  mode
category: DICOM
presenter_location: 

key_investigators:

- name: Dave Dinh
  affiliation: Consultant
  country: Brigham and Women's Hospital, USA

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->







# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


DICOM De-ID Loop:
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/b95e956f-f422-494c-8c52-91b3d1fbd174" />

OHIF Mode:

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/f4a099f4-5f71-40a3-a22f-f84ace253d0e" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

