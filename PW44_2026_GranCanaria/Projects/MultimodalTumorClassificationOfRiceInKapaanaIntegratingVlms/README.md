---
layout: pw44-project

permalink: /:path/

project_title: Multimodal tumor classification of RICE in Kapaana - integrating VLMs
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Robin Peretzke
  affiliation: DKFZ
  country: Heidelberg

- name: Maximilian Fischer
  affiliation: DKFZ
  country: Heidelberg

---

# Project Description

<!-- Add a short paragraph describing the project. -->


- New contrast-enhancing lesions following treatment of intracranial tumors may reflect either true tumor recurrence or radiation-induced contrast enhancements (RICE). Distinguishing between these entities remains unreliable but is critical for subsequent treatment decisions.
- We have developed and trained a multimodal deep learning model (RICE-Net) that achieves good performance in differentiating RICE from tumor recurrence using longitudinal MRI data (e.g., post-intervention, post-pseudoprogression) in combination with radiation treatment plans.
- RICE-Net is currently integrated into Kapaana, providing a structured environment for processing imaging and radiotherapy data and enabling inference on these inputs within a clinical routine.
- However, relevant clinical information, including pathology and radiology reports as well as medication plans, is not yet integrated, although it could substantially improve model performance and clinical utility. Corresponding multimodal extensions are currently under development and planned for integration into a new Kapaana workflow.im

<img width="960" height="540" alt="Image" src="https://github.com/user-attachments/assets/15a5ca20-6ef7-4e92-b605-220c263ef539" />

- However, such models cannot yet be integrated into Kapaana, as the platform currently does not support text processing or the integration of large language and vision–language models.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Extend Kapaana to support inference with vision-language models.
- Enable ingestion, parsing, and tokenization of PDF-based clinical documents for use as model inputs.
- Create the technical basis for multimodal models that combine imaging, textual, and structured clinical data.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Develop the necessary infrastructure within Kapaana for deployment and inference of LLM/VLM models.
- Implement robust pipelines for extracting and tokenizing text from clinical documents and aligning them with imaging data.
- Integrate textual and tabular clinical information with longitudinal MRI and radiation data in a unified multimodal model.
- Evaluate the extended model on retrospective cohorts with respect to performance, robustness, and interpretability.
- Prepare the system for subsequent prospective evaluation and use in interdisciplinary tumor board settings.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

