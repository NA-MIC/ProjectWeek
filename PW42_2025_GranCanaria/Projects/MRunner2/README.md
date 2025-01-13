---
layout: pw42-project

permalink: /:path/

project_title: MRunner2 - MHub.ai for 3D Slicer
category: Uncategorized

key_investigators:
- name: Leonard Nürnberg
  affiliation: AIM, MGB, UM
  country: The Netherlands

- name: Andrey Fedorov
  affiliation: MGB
  country: USA
---

# Project Description

MHub.ai provides a collection of dockerized, DICOM compatible AI models. 
We will provide a new extension for 3D Slicer that allows to run models from MHub.ai directly from within 3D Slicer.

## Objective

This project aims to provide a 3D Slicer extension to run arbitrary MHub.ai models (segmentation) directly from Slicer by running the standard Dicom to Dicom workflow on a Dicom image and automatically importing the generated mask into Dicom memory without the need for any model-specific setup.

## Approach and Plan

Our first version of the plugin ran a slicer specific nrrd-to-nrrd workflow. While this allowed to run any model directly on a loaded node, the generated results were not stored automatically and a slicer specific nrrd-to-nrrd workflow was required to support a specific MHub.ai model. In this iteration of the extension, we aim to improve on these constrains and add some useful features like GPU selection and image management.

## Progress and Next Steps

Roadmap:
- [x] Run the default workflow (dicom-dicom) of MHub.ai models
- [x] Add generated DICOMSEG files to the 3D Slicer DICOM store
- [x] Conenct to the MHub.ai API to provide a list of available models
- [x] Detect available GPUs and provide GPU selection
- [x] Display a list of available mhubai images
- [x] ~~Provide alternative backends (e.g., udocker)~~
- [x] ~~Run models on a remote server (via ssh)~~
- [ ] Display image information (version, disk space, ..)
- [ ] Update and delete images
- [ ] Store run information
- [ ] Implement a model search 
- [ ] Provide additional model information
- [ ] Support for non-segmentation models (using the 3D Slicer table view or DICOM SR)

Ideas to be discussed:
- [ ] Modularize extension such that it can be extended with specific configuration

# Illustrations

![Bildschirmfoto 2025-01-10 um 20 02 28](https://github.com/user-attachments/assets/f14ed4e5-bc2a-46dc-a0f9-1a9f59bb16b1)

# Background and References

*tbd*
