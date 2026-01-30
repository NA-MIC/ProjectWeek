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

- name: Emese Elkind
  affiliation: Queen's University
  country: Canada
  
- name: Lily Morrell
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

KidneyNav is a 3D Slicer scripted module designed for real-time ultrasound navigation and intraoperative visualization. The module connects to a PLUS server via OpenIGTLink to stream live 2D ultrasound images and tracking transforms, and it supports live volume reconstruction using Slicer’s VolumeReconstruction infrastructure. The current implementation includes automatic node setup (input image, prediction volume, transforms, connectors, reconstruction node/ROI), a custom 2D/3D layout for simultaneous slice and 3D rendering, and tools to record synchronized sequences (ultrasound, predictions, transforms, and needle model) for later analysis.

During this Project Week, we want to validate the module in a real live scanning setting and integrate real-time AI-based multiclass segmentation (kidney + calyces + fluid)). We also want to connect multiclass predictions to live volume reconstruction and discuss best practices for reconstructing volumes from two different (or complementary) prediction streams (e.g., kidney mask vs calyces mask, or two model outputs), including visualization, synchronization, and reconstruction strategies.



## Objective

1. **Objective A.** Validate the end-to-end live workflow by recording synchronized ultrasound, prediction, transform, and needle model sequences during real-time acquisition.
2. **Objective B.** Integrate real-time multiclass AI segmentation (kidney, calyx, fluid) streamed into 3D Slicer via OpenIGTLink and used directly for live volume reconstruction.
3. **Objective C.** Establish and compare reconstruction strategies for multiclass predictions, including single-volume and dual-volume approaches, and derive community-informed recommendations on synchronization, labeling, interpolation, and fusion.



## Approach and Plan

1. Record short test sequences (ultrasound image, prediction, transforms, needle model).
2. Stream multiclass prediction (kidney / calyx / fluid) into Slicer via OpenIGTLink as a label or scalar volume synchronized with the ultrasound stream.
3. Run live volume reconstruction directly from the prediction stream.
4. Review with the Slicer/IGT community best practices for synchronization, label consistency, interpolation, and reconstruction from dual prediction outputs.
5. Compare reconstruction strategies:    
    - **Creates and registers a volume rendering preset that visualizes segmentation labelmaps using a discrete transfer function derived from Segmentation_ColorTable.**
    - **Visualizes multi-class predictions as a multi-component scalar volume, using Slicer’s Independent Multi-Component Volume Rendering mode**


## Progress and Next Steps

1. Recorded five short ultrasound test sequences on a control group of participants.
2. Trained an nnU-Net–based multiclass segmentation model and obtained a lightweight pretrained model.
3. Streamed multiclass segmentation predictions (kidney, calyx, fluid) into 3D Slicer via OpenIGTLink as a label volume, synchronized with the live ultrasound stream.
4. Performed live volume reconstruction directly from the incoming prediction stream.
5. Implemented Rendering Strategy 1 only: discrete labelmap volume rendering, where each label value is mapped to its predefined color from the Segmentation Color Table.


# Illustrations


![KidneyNav](https://github.com/user-attachments/assets/25fa7367-8c2f-4506-8d56-5a2cd1663fe3)
<img width="1433" height="841" alt="Screenshot 2026-01-30 051110" src="https://github.com/user-attachments/assets/302e2f0a-ffdf-4219-a2f0-864fb112368f" />

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

