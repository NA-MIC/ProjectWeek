---
layout: pw45-project

permalink: /:path/

project_title: Standardizing DICOM De-ID with Actionable Rules and Tests
category: DICOM
presenter_location: 

key_investigators:

- name: Dave Dinh
  affiliation: BWH
  country: Brigham and Women's Hospital, USA

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Matt McCormick
  affiliation: Fideus Labs
  country: USA

- name: Andras Lasso
  affiliation: Queen's
  country: Canada

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


DICOM de-identification (De-ID) efforts often overlap in the rules used to process DICOM metadata. This project aims to translate [an existing DICOM De-ID standard](https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_E.1.1) into a set of actionable rules that can serve both as an implementation guide and as a verifiable audit trail for tools and AI systems.
For example, a standard may permit multiple actions for a given metadata field. A baseline reference can recommend a default action, while still allowing users to specify alternative behaviors as needed. The proposed generator will take user input and produce:

1. A reference list of itemized, actionable rules
2. A unit and end-to-end test specification that users can apply to their specific use cases

The initial user interface for the generator will be a command-line (CLI) tool. It will operate based on a predefined decision tree and output rules and test specifications in formats suitable for humans, AI systems, and supported programming languages.

In practice, DICOM De-ID outputs can vary depending on modality, imaging protocols, contractual requirements, and application domains. However, there remains a consistent need to validate that outputs conform to a predefined set of rules. This library represents a step forward in programmatically generating verifiable rules for reliable and consistent implementation.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


_No response_



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We want to create a well tested CLI based tool that takes in user input and generates the following:

- A reference list of itemized, actionable rules
- A unit and end-to-end test specification that users can apply to their specific use cases



## Progress and Next Steps

Open source project and integrate with two existing de-id projects: pipeline for batch dicom de-id and an OHIF mode for verifying de-id DICOMs.







# Illustrations

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 57 49 PM" src="https://github.com/user-attachments/assets/323d698e-72f9-49c7-8b62-e578f381987b" />

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 58 07 PM" src="https://github.com/user-attachments/assets/34d77706-ab9f-49db-8582-423798646533" />

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 58 11 PM" src="https://github.com/user-attachments/assets/3b063291-b9c9-4482-ba1b-92ad280785d6" />

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 58 16 PM" src="https://github.com/user-attachments/assets/ecfa0c06-98c4-48a5-82e3-7a29847ec40e" />

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 58 21 PM" src="https://github.com/user-attachments/assets/2af5eaf4-6074-406f-9d58-559757243aae" />

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 58 24 PM" src="https://github.com/user-attachments/assets/2c60403e-1300-499c-aeb5-e06ed031b9d8" />

<img width="1728" height="1082" alt="Screenshot 2026-06-26 at 2 58 29 PM" src="https://github.com/user-attachments/assets/49d8cca1-dda5-4335-9d10-c7830927facc" />





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- <https://dicom.nema.org/medical/dicom/current/output/html/part15.html#sect_E.1.1>

- <https://github.com/clintools/dicom-curate>

- <https://github.com/pydicom/deid>

