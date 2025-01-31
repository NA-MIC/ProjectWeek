---
layout: pw42-project

permalink: /:path/

project_title: Deploying ScribblePrompt and MultiverSeg for interactive segmentation as a 3D Slicer
  extension
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Hallee Wong
  affiliation: MIT
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We will develop a 3D slicer extension to deploy two interactive segmentation models aimed at helping researchers and clinicians perform new segmentation tasks:

[ScribblePrompt](https://scribbleprompt.csail.mit.edu/) is a deep learning model that enables users to interactively segment an image using scribbles, clicks, and bounding boxes. The model is designed to generalize to new labels and types of biomedical images and uses a lightweight UNet-based architecture so it runs quickly even without a GPU.

[MultiverSeg](https://multiverseg.csail.mit.edu/) extends this interactive approach to speed up the segmentation of sets of similar images. Using the same interaction types as ScribblePrompt (scribbles, clicks, bounding boxes), the system learns from each segmentation to improve subsequent predictions. Given enough similar example segmentations, MultiverSeg can also automatically segment new images without any user interaction.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement a 3D slicer extension for interactive segmentation with ScribblePrompt using scribbles, clicks, and bounding boxes
2. Add MultiverSeg to the extension to enable interactive and automatic segmentation of sets of images (or slices from 3D volumes)
3. Compare to other interactive segmentation tools




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will start by following the [tutorial](https://training.slicer.org/) for developing a 3D slicer extension




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<video
   controls muted
   src="https://github.com/user-attachments/assets/3fdab347-2bd9-4640-8be7-9284d9f8925c"
   style="max-height:640px; min-height: 200px">
</video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Relevant Publications:

Wong, H.E., Rakic, M., Guttag, J., & Dalca, A.V., (2024). ScribblePrompt: Fast and Flexible Interactive Segmentation for Any Biomedical Image. In European Conference on Computer Vision.
[paper](https://arxiv.org/abs/2312.07381) [code](https://github.com/halleewong/ScribblePrompt)

Wong, H.E., Ortiz, J.J.G., Guttag, J. & Dalca, A.V., (2024). MultiverSeg: Scalable Interactive Segmentation of Biomedical Imaging Datasets with In-Context Guidance. arXiv preprint arXiv:2412.15058.
[paper](https://arxiv.org/abs/2412.15058) [code](https://github.com/halleewong/MultiverSeg)

Related 3D Slicer extensions:
- [MonaiLabel](https://github.com/Project-MONAI/MONAILabel)
- [MedSAM](https://github.com/bowang-lab/MedSAMSlicer)
- [FastSAM3D](https://github.com/arcadelab/FastSAM3D_slicer)
- [SAMM](https://github.com/bingogome/samm)
- [TomoSAM](https://github.com/fedesemeraro/SlicerTomoSAM)
- [SlicerSegmentWithSAM](https://github.com/mazurowski-lab/SlicerSegmentWithSAM)
