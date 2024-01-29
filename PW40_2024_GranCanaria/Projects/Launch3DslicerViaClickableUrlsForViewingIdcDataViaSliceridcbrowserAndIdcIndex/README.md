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

Notes for discussion: 
* we could also have a mode where user clicking on IDC manifest would trigger Slicer opening and downloading the content of the manifest - this would be similar to TCIA manifest downloader. Need to think how to report progress, since for large cohorts it will take time, and s5cmd batch run does not provide the progress reporting means. TODO: link the s5cmd progress reporting issue
* warn/communicate to the user download size on disk

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Enable the local 3DSlicer to launch from slicer://idc-browser/ URLs
2.  Register the slicer://idc-browser/ protocol on Linux, Windows, and MacOS
3.  Integrate the protocol registration for slicer://viewer/ into the 3DSlicer installation process for Linux and MacOS
4.  Sequence of steps (under discussion) of how this should work when everything is done:
   * user interacts with IDC Portal, which includes URLs at the study/series level for the types of data that can be handled by Slicer (exclude SM)
   * when user clicks on a Slicer URL
       * if user has Slicer installed, but no SlicerIDCBrowser extension - the only handler available is the default one - should it detect that extension is missing and inform user that it is needed?
       * if user has Slicer and extension installed - open Slicer, select SlicerIDCBrowser, populate information in the GUI about what is being downloaded and automatically trigger the download and load into scene - need to discuss how to do error checking and alert user if certain series cannot be loaded. @vkt1414 thinks it may add delay and should just load the downloaded data into scene.
       * if user does not have Slicer - probably nothing can be done, it won't work - 404

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Incorporate  class in SlicerIDCBrowser code base
   * need to add support for progress reporting - Vamsi suggests to look at the number of files - or we can use total size of the downloaded files, since s5cmd creates multiple files during download
2.  Handle registration of custom browser protocol automatically based on the underlying OS

## Progress and Next Steps
1. SlicerIDCBrowser can now register the slicer://idc-browser/ protocol on Linux and Windows
2. The downloading experience currently is dictated by the network speed
3. Need to explore/handle the behavior when multiple versions of slicer are present on the user's system

# Illustrations

## Demo on Windows 
![NewMerge-ezgif com-video-to-gif-converter](https://github.com/NA-MIC/ProjectWeek/assets/115020590/61e49e50-65a3-4f26-88c9-e0e7a3c7893d)

## Demo on Linux (Ubuntu)
![Video_240129105420_Slice1-ezgif com-video-to-gif-converter](https://github.com/NA-MIC/ProjectWeek/assets/115020590/02c3957a-93d8-4f01-930f-c529e8de0758)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

The discussion here made it easier to test a prototype and this project builds on the suggestions made here.

[How to load nifti file from web browser link? - Development - 3D Slicer Community](https://discourse.slicer.org/t/how-to-load-nifti-file-from-web-browser-link/18664/5)
[SlicerSandbox/LoadRemoteFile/LoadRemoteFile.py at master · PerkLab/SlicerSandbox (github.com)](https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py)
