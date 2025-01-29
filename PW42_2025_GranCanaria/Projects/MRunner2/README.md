---
layout: pw42-project

permalink: /:path/

project_title: MRunner2 - MHub.ai for 3D Slicer
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
- [ ] Maintain a run history of generated output files
- [ ] Organize all extension files into a single temp / user folder: input, output, logs, runs

Ideas to be discussed:
- [ ] Docker SDK (Python) vs. Docker CLI (Subprocess)
- [ ] Modularize extension such that it can be extended with specific configuration
- [x] Support for non-segmentation models (using the 3D Slicer table view or DICOM SR)
- [ ] Open Slicer and a specific model in MRunner2 from a link via the mhub.ai website (possible?)
- [ ] Multi-Select (now possible with new History view) and modality check (for dynamic model compatibility)

# Illustrations

Updated UI and Model Search.

![Bildschirmfoto 2025-01-14 um 09 09 50](https://github.com/user-attachments/assets/5d277996-d491-4452-bf38-faed63b027ad)

Updated Model Information and Details.

<img width="602" alt="Bildschirmfoto 2025-01-27 um 11 11 28" src="https://github.com/user-attachments/assets/2d8ba82e-a6f2-41c9-8c57-12cc3418bc77" />


# Background and References

- The [MHub.ai model repository](https://mhub.ai/models)
- The MHub.ai [Documentation](https://github.com/MHubAI/documentation)
- Guides for [model contributions](https://mhub.ai/contribute).
- The [first version of the MRunner extension](https://github.com/MHubAI/SlicerMRunner).
