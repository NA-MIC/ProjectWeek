---
layout: pw42-project

permalink: /:path/

project_title: MHubRunner - MHub.ai for 3D Slicer (v2)
category: Infrastructure

key_investigators:
- name: Leonard Nürnberg
  affiliation: Brigham and Women’s Hospital, Harvard Medical Schools, Maastricht University
  country: The Netherlands

- name: Andrey Fedorov
  affiliation: Brigham and Women’s Hospital, Harvard Medical Schools
  country: USA

- name: Hugo Aerts
  affiliation: AIM Lab, Brigham and Women’s Hospital, Harvard Medical Schools
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
- [x] Display image information (~~version~~, disk space, ..)
- [x] Update and delete images
- [x] Update the selected node in 3D Slicer (red, green, yellow) upon selection
- [ ] Automatically display generated results after computation -> bug?
- [ ] ~~Store run information~~
- [x] Implement a simple text-based model search
- [x] Include output descriptors and model description in model search
- [x] Provide additional model information
- [x] Disable models incompatible with extension (only segmentation models and single-input models aas of now)
- [x] Show async raw output stream of MHub run command
- [x] Display JSON and CSV files in Slicer Table view
- [x] Maintain a run history of generated output files
- [x] Organize all extension files into a single temp / user folder: input, output, logs, runs

Ideas to be discussed:
- [ ] Docker SDK (Python) vs. Docker CLI (Subprocess)
- [ ] Modularize extension such that it can be extended with specific configuration
- [x] Support for non-segmentation models (using the 3D Slicer table view or DICOM SR)
- [ ] Open Slicer and a specific model in MHubRunner from a link via the mhub.ai website (possible?)
- [x] Explore: Multi-Select (now possible with new History view) and modality check (for dynamic model compatibility)

# Illustrations

Updated UI and Model Search.

![Bildschirmfoto 2025-01-14 um 09 09 50](https://github.com/user-attachments/assets/5d277996-d491-4452-bf38-faed63b027ad)

Updated Model Information and Details.

<img width="602" alt="Bildschirmfoto 2025-01-27 um 11 11 28" src="https://github.com/user-attachments/assets/2d8ba82e-a6f2-41c9-8c57-12cc3418bc77" />
<img width="698" alt="Bildschirmfoto 2025-01-30 um 15 02 04" src="https://github.com/user-attachments/assets/2fda7ed3-bbaa-4bce-8402-ddcca93ce4d1" />

Search for models by segmentation ROI

<img width="693" alt="Bildschirmfoto 2025-01-30 um 15 02 18" src="https://github.com/user-attachments/assets/22c422a9-e440-4f9c-93fa-9b713de5cc8c" />

View and search for model modalities

<img width="696" alt="Bildschirmfoto 2025-01-30 um 15 02 27" src="https://github.com/user-attachments/assets/285a1635-b52c-4983-a131-6076bf7f9273" />

Run prediction models and display as table view

<img width="1283" alt="Bildschirmfoto 2025-01-30 um 15 03 22" src="https://github.com/user-attachments/assets/2013a922-fa9b-40e9-9553-5ce3822d4a95" />

Manage local images

<img width="628" alt="Bildschirmfoto 2025-01-30 um 15 03 39" src="https://github.com/user-attachments/assets/fa73f7cc-8946-4a61-93e5-71726e9c1734" />

# Background and References

- The [MHub.ai model repository](https://mhub.ai/models)
- The MHub.ai [Documentation](https://github.com/MHubAI/documentation)
- Guides for [model contributions](https://mhub.ai/contribute).
- The [first version of the MRunner extension](https://github.com/MHubAI/SlicerMRunner).
