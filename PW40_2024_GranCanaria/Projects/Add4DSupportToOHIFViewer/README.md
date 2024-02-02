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

- name: Alireza Sedghi
  affiliation: open health imaging foundation - OHIF
  country: Canada

- name: Mo Al S’ad
  affiliation: Imperial College of London
  country: UK

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
1. Created local DCM4CHEE instance with toy data from Amsterdam and IDC
1. 4D viewport created for OHIF/cornerstone3D (in OHIF [PR #3664](https://github.com/OHIF/Viewers/pull/3664), 
   [cornerstone3D commit 42054522](https://github.com/cornerstonejs/cornerstone3D/commit/42054522680083aada25737d5e64fb22c24cb424)).
1. Expand cornerstone functionality for splitting datasets into different frames [Cornerstone3D PR #1055](https://github.com/cornerstonejs/cornerstone3D/pull/1055).
1. Fix bug in OHIF viewer breaking the scrollbar in `SidePanel` [da595489](https://github.com/JoostJM/Viewers/commit/da5954896a3efa0d42beb782087352758460fdad).
1. Created python scripts for comparing DICOM metadata and exhaustive search of potential 4D splitting tags.

Next Steps/ToDo:

1. During testing, a new use case emerged: Singe SeriesInstanceUID, but 2 valid 4D stacks,
   identifiable by ImageType. To correctly handle this use case, data needs to be first split by 
   ImageType, then by frame identifier (in this case TemporalPositionIndex).
1. Additional ToDo's as specified in OHIF [PR #3664](https://github.com/OHIF/Viewers/pull/3664), concerning updates of
   the 4D datapanel GUI, and only displaying it when a valid 4D dataset is active.
1. Check the functionality of retrieving 4D tag values using cornerstone3D metadata
   providers.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

Support for 4D multistack - DWI split by GE private tag:

 <iframe width="420" height="315" src="https://www.youtube.com/embed/KDeHW6Q8DPA">
 </iframe>

Support for 4D multistack - DCE split by Temporal Position Identifier

<iframe width="420" height="315" src="https://www.youtube.com/embed/cbX-8jjtYM4">
 </iframe>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- [OHIF viewer source code](https://github.com/OHIF/Viewers).
- [OHIF viewer online documentation](https://docs.ohif.org/).
- Related work:
  - OHIF [PR #3664](https://github.com/OHIF/Viewers/pull/3664).
  - Cornestone live-examples: [dynamicpetct](https://www.cornerstonejs.org/live-examples/dynamicpetct)
  - OHIF viewer demo for [dynamic PETCT](https://deploy-preview-3664--ohif-dev.netlify.app/dynamic-volume?StudyInstanceUIDs=2.25.232704420736447710317909004159492840763)
