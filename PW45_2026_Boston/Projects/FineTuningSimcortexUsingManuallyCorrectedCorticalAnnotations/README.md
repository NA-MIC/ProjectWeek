---
layout: pw45-project

permalink: /:path/

project_title: Fine-tuning SimCortex Using Manually Corrected Cortical Annotations
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Kaveh Moradkhani
  affiliation: École de technologie supérieure
  country: Canada

- name: Jarrett Rushmore
  affiliation: Center for Morphometric Analysis
  country: Massachusetts General Hospital, USA

- name: Sylvain Bouix
  affiliation: École de technologie supérieure
  country: Canada

---

### Draft Status

Ready for page creation

### Category

Segmentation / Classification / Landmarking

### Key Investigators

* Kaveh Moradkhani (École de technologie supérieure, Canada)
* Jarrett Rushmore (Center for Morphometric Analysis, Massachusetts General Hospital, USA)
* Sylvain Bouix (École de technologie supérieure, Canada)

### Project Description

SimCortex v2 is a deep learning pipeline for cortical surface reconstruction from brain MRI. In this project, we will fine-tune the existing SimCortex v2 model using manually corrected segmentations and cortical surfaces.

The goal is to evaluate whether manual supervision can improve the reconstructed white and pial surfaces compared with the current SimCortex v2 baseline.

As a practical outcome, we will also prepare a 3D Slicer extension for SimCortex. The extension runs SimCortex through Docker from a native T1-weighted MRI and loads the reconstructed cortical surfaces back into Slicer for visualization.

### Objective

1. Fine-tune SimCortex v2 using manually corrected segmentations and cortical surfaces, and evaluate the fine-tuned model on held-out test data.

2. Prepare the SimCortex 3D Slicer extension for public release, so users can run the pipeline and visualize the reconstructed surfaces directly in 3D Slicer.

### Approach and Plan

1. Review the manually corrected segmentations and cortical surfaces.
2. Prepare the manual annotations in a format compatible with the SimCortex v2 training pipeline.
3. Fine-tune the relevant SimCortex v2 stages using the manual annotations.
4. Run inference with both the baseline and fine-tuned models on the same test data.
5. Compare the results using surface metrics, topology-related checks, and visual inspection.
6. Test the local SimCortex 3D Slicer extension and prepare the repository for public use.

### Progress and Next Steps

1. SimCortex v2 is already available as an open-source cortical surface reconstruction pipeline.
2. Manually corrected segmentations and cortical surfaces are available for fine-tuning.
3. A local prototype of the SimCortex 3D Slicer extension has been developed.
4. The extension can run SimCortex through Docker from a T1-weighted MRI and load the reconstructed white and pial surfaces back into Slicer.
5. Next steps are to finalize the fine-tuning workflow, run initial experiments, evaluate the results, and prepare the Slicer extension for public release.

### Illustrations

The main illustration shows the SimCortex pipeline from brain MRI to segmentation, initial surfaces, deformation, and final predicted cortical surfaces.

<img width="9224" height="2888" alt="Image" src="https://github.com/user-attachments/assets/d3d4cd33-8c13-46a2-a59a-b5af894be9e8" />

A second illustration shows the local SimCortex 3D Slicer extension with reconstructed white and pial surfaces loaded in Slicer.

<img width="2048" height="1351" alt="Image" src="https://github.com/user-attachments/assets/81cdc66f-5362-41cf-af7f-2385b1023b8d" />

### Background and References

* SimCortex GitHub repository:
  https://github.com/Neuro-iX/SimCortex

* SimCortex: Collision-free Simultaneous Cortical Surfaces Reconstruction:
  https://arxiv.org/abs/2507.06955

