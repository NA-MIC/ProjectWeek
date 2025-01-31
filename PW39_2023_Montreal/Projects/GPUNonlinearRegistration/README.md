---
layout: pw39-project

permalink: /:path/

project_title: GPU Nonlinear Registration
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Houssem Gueziri
  affiliation: Montreal Neurological Institute and Hopital
  country: Canada

- name: Mohammadreza Eskandari
  affiliation: Montreal Neurological Institute and Hopital
  country: Canada
---

# Project Description
<!-- Add a short paragraph describing the project. -->
This project aims to add a multimodal nonlinear registration plugin to Slicer. This work extends the functionality of [GPU Rigid Registration project](https://github.com/NA-MIC/ProjectWeek/blob/master/PW35_2021_Virtual/Projects/GPURigidRegistration/README.md) (which was initially part of [Ibis Neuronav](http://ibisneuronav.org/)). This project is based on [Multi-Modal Image Registration Based on Gradient Orientations of Minimal Uncertainty](https://ieeexplore.ieee.org/abstract/document/6298013).
## Objective
<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Be able to nonlinearly register a source image to a target image from different modalities

## Approach and Plan
<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Figure out what needs to be changed compared to rigid registration
2. Add required components
3. Test

## Progress
1. Theoretical foundation of the method has been investigated
2. Previous implementation has been reviewed
3. Successfully integrated CPU implementation of non-rigid registration in Ibis

## Next setps
1. Replace metric value computation with OpenCL code

# Background and References
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
[1] De Nigris, D., et al., 2014. SymBA: Diffeomorphic Registration Based on Gradient Orientation Alignment and Boundary Proximity of Sparsely Selected Voxels. In Biomedical Image Registration: 6th International Workshop, WBIR 2014, London, UK, July 7-8, 2014. Proceedings 6 (pp. 21-30). [link](https://link.springer.com/chapter/10.1007/978-3-319-08554-8_3)
- http://ibisneuronav.org
- https://github.com/IbisNeuronav/Ibis

# Illustrations

Before registration:
![image](https://github.com/NA-MIC/ProjectWeek/assets/8172629/27d88c0c-8694-4548-9ea9-f1c2f3a88517)

After registration:
![image](https://github.com/NA-MIC/ProjectWeek/assets/8172629/e1a8e139-5244-4293-99b6-57284d0fe513)
