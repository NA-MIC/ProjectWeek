---
layout: pw44-project

permalink: /:path/

project_title: 'KidneyNav: Real-time kidney ultrasound segmentation and 3D reconstruction in 3D Slicer:'
category: IGT and Training
presenter_location: 

key_investigators:

- name: Gabriella d'Albenzio
  affiliation: Queen's University
  country: Canada

- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada

- name: Ron Kikinis
  affiliation: BWH
  country: USA

- name: Gabor Fichtinger
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


KidneyNav is a 3D Slicer scripted module designed for real-time ultrasound navigation and intraoperative visualization. The module connects to a PLUS server via OpenIGTLink to stream live 2D ultrasound images and tracking transforms, and it supports live volume reconstruction using Slicer’s VolumeReconstruction infrastructure. The current implementation includes automatic node setup (input image, prediction volume, transforms, connectors, reconstruction node/ROI), a custom 2D/3D layout for simultaneous slice and 3D rendering, and tools to record synchronized sequences (ultrasound, predictions, transforms, and needle model) for later analysis.

During this Project Week, we want to validate the module in a real live scanning setting and integrate real-time AI-based multiclass segmentation (kidney + calyces + fluid)). We also want to connect multiclass predictions to live volume reconstruction and discuss best practices for reconstructing volumes from two different (or complementary) prediction streams (e.g., kidney mask vs calyces mask, or two model outputs), including visualization, synchronization, and reconstruction strategies.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. **Objective A.** Validate the end-to-end live workflow by recording synchronized ultrasound, prediction, transform, and needle model sequences during real-time acquisition.
2. **Objective B.** Integrate real-time multiclass AI segmentation (kidney, calyx, fluid) streamed into 3D Slicer via OpenIGTLink and used directly for live volume reconstruction.
3. **Objective C.** Establish and compare reconstruction strategies for multiclass predictions, including single-volume and dual-volume approaches, and derive community-informed recommendations on synchronization, labeling, interpolation, and fusion.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Record short test sequences (ultrasound image, prediction, transforms, needle model).
2. Stream multiclass prediction (kidney / calyx / fluid) into Slicer via OpenIGTLink as a label or scalar volume synchronized with the ultrasound stream.
3. Run live volume reconstruction directly from the prediction stream.
4. Review with the Slicer/IGT community best practices for synchronization, label consistency, interpolation, and reconstruction from dual prediction outputs.
5. Compare reconstruction strategies:    
    - **Single multiclass reconstruction from one prediction volume.**
    - **Separate reconstructions for kidney and calyx, followed by fusion/overlay.**




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

