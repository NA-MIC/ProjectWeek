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



## Progress

- SlicerTMS Navigation workflow automated by integrating Local LLM.
- SlicerTMS Registration feature is controlled by cookbook: RAG router bypassing LLM logic for known tasks. Near zero-latency for defined commands.
- LLM does not write raw Python code. System runs on deterministic medical API execution.

```text
=========================================================================
[ PHASE 1: IMPLEMENTED ] Zero-Hallucination Deterministic Flow
=========================================================================
Concept: Direct route bypasses LLM logic for safe, immediate execution.

[ User Input ] ➔ ( e.g., "Load Patient Data", "Open Registration" )
        ↓
[ RAG Router ]    ━━━ ( Semantic Similarity Calculation )
        ↓
        ┣━━━ [ Match > 0.35 ] ➔ [ Cookbook Execution ] ➔ ( 0s Latency )
        ┃                               ↓ 
        ┃                       Bypass LLM Logic
        ┃                               ↓
        ┃                     [ Strict JSON Payload ]
        ┃                               ↓
        ┃                ( Safe Medical API Execution )
```
Cookbook Matching </br>
<img src="./Cookbook matching.png" width="400" alt="Description">

Surface Registration
<img src="./surface registration.png" width="700" alt="Description"> </br>



## Next Steps

- AI Agent must understand scenes and coordinates before reasoning (Spatial understanding).
- AI agent should execute active Read-Reason-Action loops. System should auto-correct spatial errors like "F10 is 2mm off".
- Local LLMs must be evaluated against cloud models like Claude: accuracy vs execution speed for targeting tasks.
```text
[ PHASE 2: FUTURE WORK ] Active Scene Introspection & Reasoning Loop
=========================================================================
Concept: LLM acts as a "Tool User" with bi-directional spatial awareness.

[ Surgeon Input ] ➔ ( e.g., "F10 is off by 2mm, move it down" )
        ↓
[ RAG Router ]    ━━━ ( Semantic Similarity Calculation )
        ↓
        ┗━━━ [ Match < 0.35 ] ➔ [ LLM Deep Reasoning ] 
                                        ↓
                         [ Bi-Directional Query Loop ]
                                        ↓
                  1. READ   ➔ Calls GetNodeCoordinate("F10")
                  2. RETURN ⬅ Slicer: {"F10": [x:45.2, y:12.1, z:55.0]}
                  3. REASON ➔ Calculate Offset (Z: 55.0 - 2.0 = 53.0)
                  4. ACTION ➔ Triggers Cookbook: MoveNode("F10", [0,0,-2])
```

Active AI Agent </br>
<img src="./future_1.png" width="700" alt="Description"> </br>


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


SlicerTMS, Slicer AI Agent, NousNav

