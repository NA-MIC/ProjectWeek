---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/SlicerIDCBrowser/README.html

project_title: Slicer-IDCBrowser
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada
  
- name: Bill Clifford
  affiliation: Institute for Systems Biology
  country: USA
  
---

# Project Description

<!-- Add a short paragraph describing the project. -->

[NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/) is a cloud-based repository of publicly available cancer imaging data co-located with analysis and exploration tools and resources. Currently, to download images from IDC users need to use command-line `s5cmd` tool. Our objective is to develop an extension providing
user interface within the Slicer platform to allow browsing and download of images from IDC.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Start development of the extension using SlicerTCIABrowser as a template.
2. Release extension.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Starting from the existing TCIABrowser extension, re-implement extension API to utilize IDC API instead of TCIA API to browse IDC content and retrieve collection/patient/study/series lists.
2. Update the UI of the extension to coordinate with the output of IDC API.
3. Compare performance of IDC API vs TCIA API.
4. Deploy `s5cmd` within the extension.


## Progress and Next Steps

1.  Developed initial version of the module: [https://github.com/fedorov/SlicerIDCBrowser](https://github.com/fedorov/SlicerIDCBrowser). Tested on mac with pre-installed s5cmd. Confirmed working functionality to browse collection/patient/study/series and download individual series.
2.  Identified limitations of the [IDC API](https://learn.canceridc.dev/api/getting-started): insufficient documentation, missing features to retrieve necessary attributes at various levels of hierarchy (resulting in blank values for the content of the navigation table). Work on the refined API is underway.
3.  Since IDC API is using BigQuery, there is noticeable latency during interaction when compared with TCIA API. Download of the images is perhaps faster.
4.  Next steps: refine API and update UI once done, automate deployment of s5cmd, revisit the need for cache, refine UI, publish extension.

# Illustrations

![idcbrowser_pw39_small](https://github.com/NA-MIC/ProjectWeek/assets/313942/642dc4dc-c51d-40dd-8f44-60e89dde0ad3)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

* [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/)
* [IDC data download instructions](https://learn.canceridc.dev/data/downloading-data)
* [SlicerTCIABrowser](https://github.com/QIICR/TCIABrowser)
* installation of system-specific libraries from Slicer module - need to do something like this for s5cmd: [https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/ScreenCapture/ScreenCapture.py#L873](https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/ScreenCapture/ScreenCapture.py#L873)
* detection of system configuration to select s5cmd binary: [https://doc.qt.io/qt-5/qsysinfo.html#productType](https://doc.qt.io/qt-5/qsysinfo.html#productType)
