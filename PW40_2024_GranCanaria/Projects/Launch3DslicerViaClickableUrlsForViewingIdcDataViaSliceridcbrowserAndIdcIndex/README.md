---
layout: pw40-project

permalink: /:path/

project_title: Launch 3DSlicer via clickable URLs for Viewing IDC Data via SlicerIDCBrowser and IDC
  Index
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Vamsi Thiriveedhi
  affiliation: BWH
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

IDC (Imaging Data Commons) has several TB of radiology data that can be viewed with various tools, such as OHIF v2, v3, and Kitware’s VolView. However, one could argue that none of these tools can match the power and versatility of 3DSlicer, which offers a wide range of features for exploring and analyzing radiology data. Steve has come up with a brilliant idea to make 3DSlicer more accessible and user-friendly: a simple URL that can be clicked to launch 3DSlicer and load the desired IDC data. This project aims to ease the way we view IDC Data on 3DSlicer by making it as easy as clicking a link by extending the capabilities of the SlicerIDCBrowser extension.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Enable the local 3DSlicer to launch from slicer://idc-browser/ URLs
2.  Register the slicer://idc-browser/ protocol on Linux, Windows, and MacOS
3.  Integrate the protocol registration for slicer://viewer/ into the 3DSlicer installation process for Linux and MacOS

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Incorporate  class in SlicerIDCBrowser code base
2.  Handle registration of custom browser protocol automatically based on the underlying OS

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  A prototype independent of SlicerIDCBrowser is working but the method is not so user friendly

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

The discussion here made it easier to test a prototype and this project builds on the suggestions made here.

[How to load nifti file from web browser link? - Development - 3D Slicer Community](https://discourse.slicer.org/t/how-to-load-nifti-file-from-web-browser-link/18664/5)
[SlicerSandbox/LoadRemoteFile/LoadRemoteFile.py at master · PerkLab/SlicerSandbox (github.com)](https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py)
