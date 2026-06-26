---
layout: pw45-project

permalink: /:path/

project_title: 'Vox2SegLAM: Protocol-Guided Subcortical Segmentation in 3D Slicer'
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Ahmed Rekik
  affiliation: École de technologie supérieure
  country: Montréal, Canada

- name: Jarrett Rushmore
  affiliation: Center for Morphometric Analysis
  country: Massachusetts General Hospital, Boston, USA

- name: Sylvain Bouix
  affiliation: École de technologie supérieure
  country: Montréal, Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


3D SlicerVox2SegLAM is an extension that brings an AI-assisted, protocol-guided workflow to subcortical brain segmentation and landmarking. A joint CNN+GNN model predicts 26 subcortical structures and 20 anatomical landmarks directly from a T1 MRI, following the Harvard-Oxford Atlas (HOA 2.0) neuroanatomical protocol. 




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Develop an open-source 3D Slicer extension that automatically predicts subcortical segmentation (26 structures) and 20 neuroanatomical landmarks from a single T1 MRI, following the Harvard-Oxford Atlas (HOA 2.0) protocol.
2. Give the expert fast, intuitive tools to correct AI predictions directly in Slicer — drag landmarks, add/remove landmarks, edit segments — without leaving the scene.
3. Enforce anatomical consistency automatically through an explicit, human-readable rule engine that re-applies HOA2.0 protocol constraints after every manual edit, minimizing the time needed to produce gold-standard reference annotations.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. **Architecture**: a CNN extracts multi-scale features, shared with a cascaded GNN that refines a template landmark graph onto the patient's anatomy in 4 steps.
2. **Segmentation**: landmarks drive a rule-based post-processing step that splits coarse CNN groupings into the 26 target structures under anatomical constraints.
3. **Slicer module**: package model + rule engine into `Vox2SegLAM ` — inference, interactive editing of landmarks/segmentation, rule re-application, export.
4. Validate on held-out and out-of-domain scans.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


**Done:**
1. Trained the joint CNN+GNN model: mean Dice = 0.908 ± 0.010 across 26 subcortical structures .
2. Achieved a mean landmark localization error of 1.4 mm under strict point-to-point evaluation, improving to 1.1 mm under an anatomically-tolerant evaluation that accounts for legitimate placement ambiguity (e.g., any voxel along the correct structure boundary or within the correct coronal region counts as correct), across the 20 predefined HOA2.0 landmarks.

**Next steps (at/after PW45):**
1. Built the core of the Slicer extension: inference adapter, protocol rule parser for the HOA protocol and the geometry engine (plane and landmarks fitting.
2. Validated qualitatively on in-domain test data and on out-of-domain scans, confirming anatomically plausible predictions outside the training distribution.
3. Work with Dr. Rushmore to refine the protocol rule set and run a usability/annotation-time study comparing manual vs. AI-assisted annotation.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


- **Figure 1.** Overall architecture: shared CNN encoder–decoder with multi-scale feature exchange feeding a 4-step cascaded GNN that refines landmark positions from a template graph.
<img width="4000" height="2250" alt="Image" src="https://github.com/user-attachments/assets/d4ad19a7-6048-4d48-aa48-f893331e8d80" />

- **Figure 2.** Per-region Dice coefficients (26 structures), mean Dice = 0.908.
<img width="1211" height="329" alt="Image" src="https://github.com/user-attachments/assets/29ddd03b-05c2-42de-9830-0f0201ebf5d1" />

- **Figure 3.** Per-landmark mean localization error (mm): strict ("Classic", 1.1 mm) vs. anatomically-tolerant evaluation (1.4 mm).
<img width="1212" height="330" alt="Image" src="https://github.com/user-attachments/assets/94fb3db5-c38d-47d7-be8b-79b114278796" />

- **Figure 4.** Visual example on in-domain test data:
<img width="3442" height="1884" alt="Image" src="https://github.com/user-attachments/assets/51fcdf47-e1a7-4318-ac84-38637db7b6bc" />
- 
- **Figure 5.** Visual example on out-of-domain data:
<img width="2068" height="1185" alt="Image" src="https://github.com/user-attachments/assets/bafc0a10-95e7-4976-a324-aac7b8e5afc8" />


# Results

- **Video.** Full workflow demo — hub-based remote inference deployment (VolView/CastInterface) followed by the Vox2SegLAM 3D Slicer extension end-to-end:

   <video
   controls muted
   src="https://github.com/user-attachments/assets/c0781e8a-0b7f-4b91-957e-7d9ea8aae0fc"
   style="max-width:800px">
 </video>



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. Rekik et al., "Automatic Landmark-Based Segmentation of Human Subcortical Structures in MRI," *arXiv:2605.14221*, 2026. [Link](https://arxiv.org/abs/2605.14221)
2. Bongratz et al., "Vox2Cortex: Explicit Cortical Surface Reconstruction with Geometric Deep Learning," *arXiv:2203.09446*, 2022. [Link](https://arxiv.org/abs/2203.09446)
3. Rushmore et al., "Anatomically curated segmentation of human subcortical structures in high-resolution MRI," *Frontiers in Neuroanatomy*, 16:894606, 2022. [Link](https://doi.org/10.3389/fnana.2022.894606)
4. Rushmore & Harvard-Oxford Atlas Group, *HOA Subcortical Brain Structure Segmentation Manual*, Harvard University, 2021. [Link](https://cma.mgh.harvard.edu/wp-content/uploads/2023/04/HOA-Subcortical-Brain-Structure-Segmentation-Manual.pdf)

