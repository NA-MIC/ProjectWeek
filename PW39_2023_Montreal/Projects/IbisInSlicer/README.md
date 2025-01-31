---
layout: pw39-project

permalink: /:path/

project_title: Ibis in Slicer
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Houssem Gueziri
  affiliation: Montreal Neurological Institute and Hopital
  country: Canada

- name: Étienne Léger
  affiliation: Montreal Neurological Institute and Hopital
  country: Canada

- name: Simon Drouin
  affiliation: École de technologie supérieur
  country: Canada
---

# Project Description
<!-- Add a short paragraph describing the project. -->
Continuing the trend set in the [GPU Rigid Registration project](https://github.com/NA-MIC/ProjectWeek/blob/master/PW35_2021_Virtual/Projects/GPURigidRegistration/README.md), the purpose of this project is to port functionalities from the [Ibis Neuronav](http://ibisneuronav.org/) platform to 3D Slicer to increase compatibility between the two systems. During this week, we will focus on the HardwareModule of Ibis, which handles reading hardware set configuration files and creating scene objects and OpenIGTLink connectors accordingly.

## Objective
<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Final Objective. Be able to read Ibis configuration files from Slicer to produce an equivalent scene.

## Approach and Plan
<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Assess which classes need to be ported.
2. Port/wrap/reimplement necessary components.
3. Test

## Progress
1. Use generic MRMLNode to encapsulate tool/device properties (e.g., Calibration transform, Tool transform, Mask, etc.)
2. Start with a Python implementation (module?)
3. Possibility of using slicer scenes to share configurations

# Background and References
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
- http://ibisneuronav.org
- https://github.com/IbisNeuronav/Ibis
