---
layout: pw44-project

permalink: /:path/

project_title: Updating SlicerSOFA
category: Infrastructure
presenter_location: 

key_investigators:

- name: Rafael Palomar
  affiliation: NTNU / OUH
  country: Norway

- name: Paul Baksic
  affiliation: Inria
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


SlicerSOFA is a 3D Slicer extension integrating the simulation framework SOFA in 3D Slicer. The extension packages the SOFA-framework, together with `SofaPython3` and exposes SOFA to 3D Slicer through Python. In addition, SlicerSOFA provides functionality to connect and transfer data between 3D Slicer objects and SOFA objects. In this project, we plan to update SlicerSOFA to have better cross-platform coverage (currently a MacOS version is not available) and work with the latest 3D Slicer and SOFA versions, as well as integrating external execution of simulations through =RPyC=.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Update SlicerSOFA to use SOFA v25.12 (latest available).
2. Update SlicerSOFA to run on the latest 3D Slicer stable and development versions.
3. Fix SlicerSOFA MacOS integration.
4. Integrate RPyC external execution
5. Update project documentation




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


The core SOFA library will be updated first to it's latest version (v25.12) and test on the latest Slicer (stable+dev). After an updated working version for Windows and GNU/Linux, a fix for MacOSX will be provided. Finally, a new executor using RPyC will be provided (tests will be performed in external processes (local + remote machine)). Finally, the updates and the new additions will be documented.



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

