---
layout: pw45-project

permalink: /:path/

project_title: Local AI-Copilot for Slicer medical imaging workflows
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


This project will attempt to build a free, confidential, and fully local alternative to cloud-based LLMs for medical imaging workflows. To bypass expensive and non-private cloud models, we will attempt to create an AI Agent for 3D Slicer designed to run entirely offline. We aim to enable private models powered by Ollama to accurately query the Slicer API without relying on external cloud infrastructure.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Build a private MCP pipeline linking Ollama to 3D Slicer for secure, context-aware API scripting.
2. Benchmark local model performance (Llama-3, DeepSeek) against cloud baselines for accuracy and cost.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Connect a local LLM client to existing Slicer MCP execution servers to enable code execution.
Evaluate zero-shot coding accuracy on multi-step Slicer workflows using purely local inference



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Progress: Reviewed current cloud-reliant MCP integrations (slicer-skill, mcp-slicer) and local LLM baselines (SlicerChat).



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


slicerClaw: https://github.com/jumbojing/slicerClaw
mcp-slicer: https://github.com/zhaoyouj/mcp-slicer
slicer-skill: https://github.com/pieper/slicer-skill
SlicerChat: https://arxiv.org/abs/2407.11987

