---
layout: pw45-project

permalink: /:path/

project_title: Interactive Workflow Replay and Step-Back Navigation for Slicer Agent
category: AI
presenter_location: 

key_investigators:

- name: Puxun Tu
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Mauro Dominguez
  affiliation: Independent
  country: Argentina

- name: Ron Kikinis
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Sanghyuk Kim
  affiliation: Mass General Brigham & University of Massachusetts
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The Slicer AI Agent is a scripted extension that lets users use natural-language instructions and have the system autonomously generate, validate, and execute Python code within the 3D Slicer scene. For complex multi-step operations, such as extension-specific surgical planning workflows, the agent enters a deterministic workflow runtime that executes a sequence of predefined steps (automated code execution, interactive 3D mark-up placement, user choices, and branching logic) with a progress bar tracking completion.

Currently this progress bar is forward-only: once a step completes, there is no way to go back, inspect what happened at an earlier step, or modify a previous choice and re-run the downstream pipeline. This limits both transparency (users cannot easily understand what was done and why) and usability (a wrong choice means restarting the entire workflow from scratch).

We propose adding a workflow replay timeline that records per-step state and allows users to go back to any completed step, inspect the code and choices that were made, optionally modify parameters, and re-execute the workflow from that point onward.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


We aim to add a workflow replay and step-back navigation capability to the Slicer AI Agent's workflow runtime. By recording per-step state and exposing it through an interactive timeline, users will be able to scrub back to any completed step, inspect what happened, optionally modify a prior choice, and re-run the remaining pipeline — improving both process transparency and the ability to correct mistakes without restarting the workflow from scratch.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Step-level recording: Capture a full replay log for every workflow step, including the generated code, user choices, scene snapshots (before/after), and execution results, so that the complete history of a workflow run is persisted and inspectable.

- Timeline UI with scrubbing: Replace the current linear progress bar with an interactive timeline widget that shows step markers (completed / current / pending), allows dragging to any completed step, and displays a detail panel with the code, choices, and scene diff for that step.

- Step-back re-execution: Enable the user to jump back to a completed step, optionally modify a prior choice or parameter, and re-run the remaining workflow from that point, reusing the existing template-dispatch and auto-advance infrastructure.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


TBD



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


https://github.com/user-attachments/assets/5eb1dab5-9b35-4d5e-9d96-c0cc058e951f

https://github.com/user-attachments/assets/ea27d290-b2c5-4be0-9954-8051650bda90



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Slicer AI Agent source repository: https://github.com/puxuntu/Slicer_agent

