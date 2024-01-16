---
layout: pw40-project

permalink: /:path/

project_title: Adding 4D data support in OHIF Viewer v3
category: Cloud / Web
presenter_location: Online

key_investigators:
- name: Joost van Griethuysen
  affiliation: The Netherlands Cancer Institute
  country: The Netherlands

- name: Alireza Sedghi, 
  affiliation: open health imaging foundation - OHIF
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

OHIF Viewer v3 provides a very flexible and extensible DICOM viewer with zero-footprint running in your browser.
It is based on Cornerstone including multiplanar reformatting support, segmentations, etc. However, OHIF viewer
does not support 4D DICOM data natively. This especially affects dynamic or function CT/MR data, such as diffusion-
weighted imaging (DWI) and dynamic contrast enhanced (DCE) CT/MR.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Get a feel for how OHIF creates display sets for displaying data using cornerstone. 
1. Create functionality to split a given display set into multiple subsets based on the value in a provide DICOM tag
   (e.g. TemporalPositionIdentifier (0020, 0100) or DiffusionBValue (0018, 9087)).
1. *Optional* Create functionality to detect if a display set is "4D", and provide a list of valid tags that can be
   used to split the display set.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Create a local instance of OHIF viewer
1. Create a toy dataset containing 3D, valid 4D and "invalid" 4D data (e.g. DICOM volume consisting of differently 
   angled subvolumes) to test/view functionality.
1. Create OHIF viewer extension to test/develop functionality, create mode to allow interaction with the extension.
1. Create functionality for splitting dataset (first on single or few known tags, no checking)
1. Improve functionality from previous point (custom tags, checking validity prior to splitting, etc.)
1. If time remains, check as to the feasibility/difficulty of supporting rendering 4D data directly.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. OHIF viewer installed locally and ready for testing/customization.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

*None yet*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- [OHIF viewer source code](https://github.com/OHIF/Viewers).
- [OHIF viewer online documentation](https://docs.ohif.org/).
- Similar work:
  - Cornestone live-examples: [dynamicpetct](https://www.cornerstonejs.org/live-examples/dynamicpetct)
  - OHIF viewer demo for [dynamic PETCT](https://deploy-preview-3664--ohif-dev.netlify.app/dynamic-volume?StudyInstanceUIDs=2.25.232704420736447710317909004159492840763)
