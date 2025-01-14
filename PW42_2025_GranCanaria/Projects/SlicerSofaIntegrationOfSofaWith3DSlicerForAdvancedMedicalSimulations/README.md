---
layout: pw42-project

permalink: /:path/

project_title: 'Slicer-SOFA: Integration of SOFA with 3D Slicer for Advanced Medical Simulations'
category: Infrastructure

key_investigators:

- name: Rafael Palomar
  affiliation: Oslo University Hospital and NTNU
  country: Norway

- name: Paul Baksic
  affiliation: Inria
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: US

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware Inc.
  country: US

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Sam Horvath
  affiliation: Kitware Inc
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The SlicerSOFA project aims to integrate the SOFA (Simulation Open Framework Architecture) with 3D Slicer, enhancing the capabilities of medical simulations by providing advanced physics and interaction models. For this PW we aim to consolidate the first release through the 3D Slicer Extension Manager and establish a dialogue with the community to bring this project forward.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Engage with the 3D Slicer  and SOFA communities on the future development of Slicer-SOFA.

2. Objective B. Resolve existing bugs and improve the stability of the integration.
   - [Bug in SparseGridSimulation.py](https://github.com/Slicer/SlicerSOFA/issues/38)
   - [Slicer hangs after starting and stopping the simulation a few times](https://github.com/Slicer/SlicerSOFA/issues/29)
   - [SofaIGTLink Plugin Fails to Load on Windows Build](https://github.com/Slicer/SlicerSOFA/issues/33)

3. Objective C. Expand the functionality by adding new SOFA plugins to the base Slicer-SOFA setup.
   - [Add SOFA default demo as Slicer module](https://github.com/Slicer/SlicerSOFA/issues/37)
   - [Bump SOFA to v24.12](https://github.com/Slicer/SlicerSOFA/issues/36)
   - [Adding new plugins to base Slicer-SOFA](https://github.com/Slicer/SlicerSOFA/issues/30)
   - [Testing and sample data still relying on RafaelPalomar/SlicerSOFATestingData repository](https://github.com/Slicer/SlicerSOFA/issues/25)
   
 4. Objective D. Implement a mechanism to specify a custom SOFA root directory via environment variables.
   - [Add feature to specify custom SOFA_ROOT](https://github.com/Slicer/SlicerSOFA/issues/39)
   - [Enable use of external SOFA and SOFA plugins](https://github.com/Slicer/SlicerSOFA/issues/32)



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop a mechanism in the SofaEnvironment to check for an environment variable `SLICER_SOFA_ROOT` and use it if available.
2. Investigate and fix the reported bugs, ensuring the functionality of components like SparseGridSimulation and SofaIGTLink plugin.
3. Integrate additional SOFA plugins (e.g., BeamAdapter, Shell)
4. Update the SOFA framework to the latest version to maintain compatibility and access new features.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


TBD




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [SlicerSOFA GitHub Repository](https://github.com/Slicer/SlicerSOFA)
- [SOFA Framework](https://www.sofa-framework.org/)
- [3D Slicer](https://www.slicer.org/)
- [Slicer-SOFA PW 41 Project](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SlicerSofa/)
- [Slicer-SOFA PW 40 Project](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerSofaIntegration/)

