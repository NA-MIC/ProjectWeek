---
layout: pw45-project

permalink: /:path/

project_title: Clinical Information Extraction via Locally Fine-Tuned LLMs
category: AI
presenter_location: 

key_investigators:

- name: Paul Dumont
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Alexandre Buisson
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Juan Carlos Prieto
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Eduardo Caleme
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Lucia Cevidanes
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project develops a privacy-preserving extraction framework using locally deployable open-weight LLMs to structure dense clinical narratives. We aim to bypass expensive and non-private cloud APIs by fine-tuning models to extract Common Data Elements (CDEs) from Orthodontic and TMJ progress notes entirely offline.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Fine-tune local LLMs (Llama-3.1-8B, Qwen-2.5-7B) to parse variable clinical shorthand into deterministic JSON dictionaries.

2. Benchmark these local models against cloud baselines and human inter-rater ceilings for accuracy and computational efficiency.

3. Deploy these trained models directly into 3D Slicer by developing a custom extension.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Fine-tune Meta-Llama-3.1-8B for orthodontic notes and Qwen-2.5-7B for TMJ records.

2. Evaluate the extractions using exact match F1-scores.

3. Build a fully offline 3D Slicer extension for secure, on-device data processing.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Fine-tuned Llama-3.1-8B (LoRA) achieved a 0.740 F1 score on orthodontic notes , and fully fine-tuned Qwen-2.5-7B reached a 0.78 F1 score on TMJ records.
Next Steps: Deploy these trained models directly within 3D Slicer by developing a custom extension with a dedicated user interface (UI) for clinical application.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


An illustrative example of the pipeline for local clinical data extraction.
<img width="1156" height="297" alt="Image" src="https://github.com/user-attachments/assets/61831e68-d674-4c4c-a4eb-88614df9cdab" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

