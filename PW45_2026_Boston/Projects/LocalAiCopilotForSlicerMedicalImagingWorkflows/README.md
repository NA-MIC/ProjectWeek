---
layout: pw45-project

permalink: /:path/

project_title: Testing Local LLMs for Agentic Tasks via Slicer Skills
category: Infrastructure
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

- name: Lucia Cevidanes
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project develops a free, confidential, and fully local alternative to cloud-based LLMs for medical imaging workflows. To bypass expensive and non-private cloud infrastructure, we are building an offline AI Agent for 3D Slicer powered by Ollama. Specifically, we aim to evaluate the capability of these local models to leverage existing "Slicer skills" to execute agentic user tasks via the Slicer API. Finally, we will benchmark the performance, context-awareness, and reliability of these local models against established cloud baselines like Claude.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Evaluate the capability of local LLMs (deployed via Ollama) to leverage the existing "Slicer skill" to execute agentic user tasks.
2. Benchmark the performance, context-awareness, and reliability of these local models against established cloud baselines (Claude).


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Connect a local LLM client to existing Slicer MCP execution servers to enable code execution.
Evaluate zero-shot coding accuracy on multi-step Slicer workflows using purely local inference



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Progress: Reviewed current cloud-reliant MCP integrations (slicer-skill, mcp-slicer) and local LLM baselines (SlicerChat).



# Illustrations
<img width="1076" height="1250" alt="image" src="https://github.com/user-attachments/assets/fdd3dde3-90e3-4bab-8520-9538315ec5f9" />


Results:
Result in the 3D Slicer scene after a simple prompt with a local 7B Qwen model:

- Using the Slicer MCP tool execute_python, write and run Python code that creates a red cube model and adds it to the 3D scene.

- Using the Slicer MCP tool load_sample_data, load the MRHead sample dataset.

<img width="1428" height="1006" alt="image" src="https://github.com/user-attachments/assets/9ab35d03-7c82-4825-ae67-9ca98d443329" />

Chatbot Interface (Cline)
<img width="1052" height="2082" alt="image" src="https://github.com/user-attachments/assets/523b064d-85b1-44d2-b354-28eaf68837c7" />

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- slicerClaw: <https://github.com/jumbojing/slicerClaw>
- mcp-slicer: <https://github.com/zhaoyouj/mcp-slicer>
- slicer-skill: <https://github.com/pieper/slicer-skill>
- SlicerChat: <https://arxiv.org/abs/2407.11987>

NIH funding NIDCR [R01DE024450](https://reporter.nih.gov/project-details/11458698)
