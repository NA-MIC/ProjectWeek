---
layout: pw45-project

permalink: /:path/

project_title: AI driven interface for SlicerTMS
category: IGT and Training
presenter_location: 

key_investigators:

- name: SangHyuk Kim
  affiliation: BWH & UMass Boston
  country: USA

- name: Puxun Tu
  affiliation: BWH & SJTU
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Lipeng Ning
  affiliation: BWH & HMS
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


SlicerTMS is a 3DSlicer module for patient-specific transcranial stimulation. It integrates several functions, including neuronavigation, electric field modeling, real-time EEG streaming and recording, and TMS control. These functions involve a complex user interface, and some tasks, such as neuronavigation registration, may need more than one user. To simplify the interface and improve the user experience, we will develop a new version leveraging LLM models and Slicer AI Agent tools. Specifically, we will eliminate LLM hallucinations at the infrastructure level by executing medical software APIs through human-verified Markdown Cookbooks and local Vector RAG technologies. Furthermore, the system establishes a next-generation intelligent environment featuring a self-evolving Auto-Correction engine that tracks and learns directly from clinician adjustment patterns, all while seamlessly supporting the trusted clinical interfaces medical professionals already use.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Implement a voice-based interface for neuronavigation registration.
- Improve the data visualization interface using the AI agent, e.g., by switching between visualization methods.
- Simplify the interface with the EEG and TMS devices AI agent.
- Minimize LLM hallucination in SlicerTMS by compiling user intent into strict template-based execution payloads.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Zero-Hallucination RAG System: Modularize verified VTK recipes into Markdown Cookbooks, embed them into a local Vector DB, and inject real-time scene variables for deterministic execution.
- UI and UX Modernization: Integrate high-density clinical data and 2D/3D visualizations into a dynamic spatial layout to overcome Slicer's legacy UI constraints.
- Architecture Evaluation Benchmark inference accuracy, latency, and medical data privacy between closed-network offline models and cloud-based counterparts.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


_No response_



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


SlicerTMS, Slicer AI Agent, NousNav

