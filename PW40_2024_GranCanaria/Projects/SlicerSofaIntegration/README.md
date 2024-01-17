---
layout: pw40-project

permalink: /:path/

project_title: Slicer-SOFA integration
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Rafael Palomar
  affiliation: Oslo University Hospita
  country: Norway

- name: Paul Baksic
  affiliation: INRIA
  country: France

- name: Steve Pieper
  affiliation: Isomics
  country: US

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

SOFA is an open source framework targeted at interactive biomechanical simulation, with an emphasis on medical simulation and robotics. Relying on a C++ implementation, SOFA offers efficient algorithms and methods to solve continuum mechanics problems. Its interactive capability makes it a great tool for off- and on-line medical applications. The SOFA core has a LGPL license, which is permissive and non-contaminating.

Relying on the Finite Element Methods (FEM), SOFA requires a mesh (space discretization) of the simulated objects as input. Eventhough SOFA offers several numerical strategies to reach the best performances possible (preconditionning, multithreading, etc…), this mesh has a direct impact on the simulation stability and performance. This is usually overcome through a long process of mesh refinement and simulation testing to reach computation time suitable for interactive simulation of deformable bodies.

Integrating SOFA to Slicer may ease this process and offer a fully integrated pipeline bridging medical imaging, processing and patient-specific simulation. This integration may be of great interest for the Slicer community to help design and bootstrap finite element simulations.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Define correctly the integration’s limits. What is desirable and at which point it is meaningless and the user should then switch to SOFA itself + a roadmap for the complete integration.
2.  Define through what means the integration will be done : Python bindings / C++.
3.  Enable the sharing of data structures to be able to use the meshs without the need of multiple copies.
4.  Define the prefabs needed to automatically create a sofa scene without the need of fine tuning directly the scene with the current meshes.
5.  Integrate the SOFA scene graph in read/write to be able to interact with sofa objects.
6.  Add a way to define bounding boxes for sofa or manually specify indices for boundary conditions.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Discuss with Slicer devs and users that also use SOFA to gather the needs. Defines the actual steps to reach the desired integration and distribute them among the projet members (it may take more time than the actual project week).
2.  Define a simple POC with few features that is doable during the remaining days of the week to start working on it directly.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![liver2](https://github.com/NA-MIC/ProjectWeek/assets/1978682/cf22da12-5459-43cb-b7e2-1021d5648f69)

![LiverRendered](https://github.com/NA-MIC/ProjectWeek/assets/1978682/3219f2dc-1cfb-4053-bf1f-f0bd9b34249c)

![ImagingUSScene_IRCAD_00000005](https://github.com/NA-MIC/ProjectWeek/assets/1978682/02aa0256-a641-476e-a03e-541cfc86192d)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

SOFA 2012 paper: <https:/hal.inria.fr/hal-00681539>
GitHub: <https://github.com/sofa-framework/sofa/>
API doc: <https://www.sofa-framework.org/api>
