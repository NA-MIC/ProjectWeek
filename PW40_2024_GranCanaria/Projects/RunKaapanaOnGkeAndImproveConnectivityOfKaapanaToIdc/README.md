---
layout: pw40-project

permalink: /:path/

project_title: Improve connectivity of Kaapana to IDC
category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Mikulas Bankovic
  affiliation: DKFZ
  country: Germany

- name: Vamsi Thiriveedhi
  affiliation: BWH
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Hanno Gao
  affiliation: DKFZ
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The aim of this project is to enhance the integration between Kaapana and IDC, specifically enabling Kaapana to interact with an external DICOMweb endpoint, as Google Healthcare API behind IDC for image storage.

Kaapana is an open-source toolkit designed for platform provisioning in the field of medical data analysis. It leverages a variety of open-source tools relevant to the NA-MIC community, including OHIF Viewer, MITK, and nnU-Net segmentation tools. Kaapana uses DICOM for managing images, image-derived data, and metadata. It offers functionalities such as workflows for large-scale image processing, exploration, visualization, and curation of medical images, extensions for simple integration of new, customized algorithms and applications, an integrated PACS system, and extensive resource and system monitoring for administrators.

NCI Imaging Data Commons (IDC) is a cloud-based repository of publicly available cancer imaging data co-located with the analysis and exploration tools and resources. IDC is a node within the broader NCI Cancer Research Data Commons (CRDC) infrastructure that provides secure access to a large, comprehensive, and expanding collection of cancer research data.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

We aim to add an external DICOMweb-based server specifically, Google Healthcare API DICOM stores, in addition to the internal dcm4chee server, enhancing the ability of Kaapana to process external images.
We aim to achieve the same functionality with external dicomweb server as with we currently have with local dicomweb server.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

The approach involves several steps:

1. **Establish the connection** from kaapana code-server platform to the external dicom server (REST?)
2. Retrieve all dicom **metadata** from the **external** server
3. Write a workflow to add **metadata** to kaapana **opensearch meta dashboard view**
4. Retrieve dicom **thumbnail images** from the server
5. Write a workflow to add them to **datasets view**
6. **Flag** external dicoms to differentiate between **used storage DICOMWeb servers**.
7. Enable using the data in dicom store as input for existing workflows in kaapana
8. If possible, integrate **OHIF viewer** on kaapana with GCP dicom store


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Implemented new dag and operator in kaapana workflow able to **import metadata** and **name the dataset**. (1-3)
2.  Able to retrieve thumbnail images, but unable to integrate it to the kaapana yet, due to choosing the wrong path :D (4)
3.  During import, I identify tags: **00080016 source entity title** and **00080026 source presentation address** as places where to store meta information, that these metadata are from external sources and address where it is possible to retrieve them. This will be reused later.
4.  7-8 WIP

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
Kaapana datasets **thumbnail** view:
![Screenshot from 2024-01-23 15-10-36](https://github.com/NA-MIC/ProjectWeek/assets/33953801/4a63ff25-47b0-4b1f-bac6-994e5fb2b05a)

Ohif Viewer:
![Screenshot from 2024-01-29 09-14-51](https://github.com/NA-MIC/ProjectWeek/assets/33953801/eb30e056-3f55-47f6-9a06-cb9407348e56)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Kaapana Docs: https://kaapana.readthedocs.io/en/stable/

Kaapana Repo: https://github.com/kaapana/kaapana

Google Healthcare API Dicomweb: https://cloud.google.com/healthcare-api/docs/how-tos/dicomweb

Google Healthcare API: https://cloud.google.com/blog/topics/healthcare-life-sciences/getting-to-know-the-google-cloud-healthcare-api-part-1

Google Dicomweb CLI https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli
