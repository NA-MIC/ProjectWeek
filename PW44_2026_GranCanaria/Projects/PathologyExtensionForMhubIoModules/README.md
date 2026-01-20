---
layout: pw44-project

permalink: /:path/

project_title: Pathology Extension for MHub IO Modules
category: Infrastructure
presenter_location: 

key_investigators:

- name: Curtis Lisle
  affiliation: KnowledgeVis
  country: LLC, USA

- name: Leonard Nürnberg
  affiliation: MGB
  country: Harvard, The Netherlands

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Pathology (DICOM) images differ greatly from radiology images, e.g., contain multiple resolutions. The MHub core provides 18 IO Modules to import, convert, organize, imaging data. We want to extend this with additional IO Modules to extract a target resolution and to provide an alternative toolchain to generate DICOMSEG output files. The IO Modules will be made publicly available as an MHub.ai module extension.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. A public pathology extension for MHub.ai
2. Adding the RMS model to MHub.ai utilizing the provided IO Modules as a PoC



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a new pathology extension repository
2. Implement an extractor module
3. Implement a specific dicomseg conversion module (e.g., based on highdicom) 
4. Implement the RMS model as PoC



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


## Layer Extraction
<img width="707" height="379" alt="Image" src="https://github.com/user-attachments/assets/e5705efa-0279-4f4a-b485-75e85fa2a167" />

## Proposed Pipeline
<img width="1211" height="391" alt="Image" src="https://github.com/user-attachments/assets/f3ccb9db-3eb4-4b62-8697-3cca89f09f11" />

## RMS Model
<img width="1197" height="642" alt="Image" src="https://github.com/user-attachments/assets/3a356f20-2bef-4400-853c-32dd66ea8989" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [MHub Documentation - Using Model Extensions](https://github.com/MHubAI/documentation/blob/main/documentation/mhub_models/the_mhub_dockerfile.md#install-additional-mhub-io-collections)
- [MHub Documentation - Example Collection Repository](https://github.com/LennyN95/mhubio-test-collection)
- [Reproducible Radiology and Pathology Imaging Analysis Applications in MHub ](https://docs.google.com/presentation/d/1bcP9WhqRf1eZtMZ1lsubE6wCgKdAYA4CIPedhw2Rcuo/edit?slide=id.g34b433d272b_1_0#slide=id.g34b433d272b_1_0) Slide 17-22
- [MHub.ai](https://mhub.ai)

