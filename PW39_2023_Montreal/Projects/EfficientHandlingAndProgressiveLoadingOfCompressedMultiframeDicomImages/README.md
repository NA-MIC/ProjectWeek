---
layout: pw39-project

permalink: /:path/

project_title: Efficient Handling and Progressive Loading of Compressed Multiframe DICOM Images
category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Ozge Yurtsever
  affiliation: Stanford
  country: USA

- name: Emel Alkim
  affiliation: Stanford
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA
  
- name: Alireza Sedghi
- affiliation: Accolade Imaging, Inc.
- country: Canada
---

# Project Description

<!-- Add a short paragraph describing the project. -->

Loading compressed multiframe DICOM images as a whole causes frequent browser crashes, particularly on Microsoft machines. This issue arises due to the large file size of the DICOM images, exceeding the browser's memory capacity.

The browser's rendering engine attempts to load the entire file into memory, due to the significant size of these images, the browser can quickly exhaust its allocated memory, leading to crashes or unresponsive behavior.

This issue affects both ePAD and OHIF with the latest WADO-loader version.  Note that the crash can be reproduced in the current OHIF v3 version, so it has impact on projects including IDC.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Initiate a discourse about the methodologies for saving, storing, and reading DICOM data, and explore strategies for optimizing the handling of compressed multiframe images to achieve enhanced efficiency and avoid browser crashing.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
* Confirm that the DICOM data is valid.  Issues from dciodvfy seem unrelated:
```
Warning - Missing attribute or value that would be needed to build DICOMDIR - Study ID
USMultiFrameImage
Warning - Unrecognized defined term <SECTRA> for value 1 of attribute <Coding Scheme Designator>
Error - Missing attribute Type 2C Conditional Element=<Laterality> Module=<GeneralSeries>
Warning - Unrecognized defined term <L> for value 1 of attribute <Coding Scheme Designator>
```
* Create a deidentified dataset to reproduce the data.  Original US data has burned in patient info, so blank pixel data will be substituted.
*  Done: https://github.com/emelalkim/sampledata/releases/tag/large_multiframe
* Explore changing the code so that instead of loading the entire DICOM file at once, the image loading process can be modified to load the image in smaller chunks or frames progressively. This approach may allow the browser to handle smaller portions of the image, reducing the memory burden and enhancing overall stability.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

We attempted to adapt a solution approach inspired by the PR link below. The link's solution specifically addresses uncompressed images. In our case, we tried a similar method to handle compressed images within the dicom-parser library, unfortunately, the attempted solution did not yield the desired outcome.

PR link: <https://github.com/cornerstonejs/cornerstoneWADOImageLoader/pull/454#issue-1287614710>
Ticket link: <https://github.com/cornerstonejs/dicomParser/issues/248>

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![crash-image](https://github.com/NA-MIC/ProjectWeek/assets/9955081/9f80cbd7-cfa7-4c54-934c-9d165fe38e1a)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Unfortunately the ultrasound images are not deindentified, we can not provide sample data yet. We are working on getting a data set.

Related libraries:
<https://github.com/cornerstonejs/cornerstoneWADOImageLoader>
<https://github.com/cornerstonejs/dicomParser>
