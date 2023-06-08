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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

* [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/)
* [IDC data download instructions](https://learn.canceridc.dev/data/downloading-data)
* [SlicerTCIABrowser](https://github.com/QIICR/TCIABrowser)