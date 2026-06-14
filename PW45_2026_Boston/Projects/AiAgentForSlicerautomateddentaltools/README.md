---
layout: pw45-project

permalink: /:path/

project_title: AI-Agent for SlicerAutomatedDentalTools
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


**Problem**: The Slicer Automated Dental Tools extension provides robust craniofacial analysis, but complex module selection and parameter tuning create a steep learning curve for users.

**Solution**: This project introduces an AI Agent and chatbot UI integrated into 3D Slicer to streamline the workflow. By allowing drag-and-drop inputs and natural language prompts, users can easily request complex tasks (e.g., segmentation, landmarking, or orientation on CBCT/IOS). The agent autonomously translates these requests into actions, selecting the right tools and automatically configuring the parameters to execute the workflow.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Local LLM Integration: Uses Ollama to run a lightweight local model (currently llama3:latest).
- Cross-Encoder Retrieval: the system leverages a Cross-Encoder. It directly scores the semantic relevance between the user's query and tool use cases to retrieve the top 3 most appropriate modules.
- Autonomous Execution: The LLM analyzes the retrieved context, selects the optimal tool, extracts the required parameters from the user's text, and automatically triggers the execution within Slicer.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Build the core backend pipeline integrating the Cross-Encoder retrieval model and the local LLM.
- Deploy the pipeline within 3D Slicer and connect it to the user-facing chatbot UI.
- Implement an autonomous feedback loop. The model will verify if the selected Slicer tools executed successfully or encountered an error, and provide real-time feedback to the user.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


**Current Progress**
The backend retrieval system is completely operational. The Cross-Encoder model reliably identifies and selects the appropriate Slicer tool from natural language input.

**Next Steps**
- LLM Integration: Implement the logic for the local LLM to parse the user's prompt, auto-fill the required parameters, and trigger the tool execution.

- Slicer Deployment: Embed the interactive UI and connect the entire AI pipeline directly within the 3D Slicer environment.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


What would the Slicer user interface look like?

<img width="504" height="934" alt="Image" src="https://github.com/user-attachments/assets/3c7b953c-a923-4a70-9af1-5f5bf711c64b" />


Slicer Automated Dental Tools Overview : 

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/32b13db1-2e45-4067-8fd6-1d18a84fd662" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- SlicerAutomatedDentalTools: <https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools>

