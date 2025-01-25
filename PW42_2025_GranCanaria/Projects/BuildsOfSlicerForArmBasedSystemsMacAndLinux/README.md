---
layout: pw42-project
permalink: /:path/
project_title: Builds of Slicer for ARM-based systems Mac and Linux
category: Infrastructure

key_investigators:
- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK
- name: Steve Pieper
  affiliation: Isomics
  country: US
- name: Rafael Palomar
  affiliation: OUH
  country: Norway
- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: US
- name: Andras Lasso
  affiliation: Queen's University
  country: CA
---

# Project Description

Investigate, document, and fix any issues related to building Slicer from source on ARM-based systems (e.g. Apple silicon or Nvidia linux systems).

During the Slicer Week, we plan to have a working 3D Slicer version on ARM architecture. This version will facilitate the use of Slicer for volume rendering and access to other modules with segmentation AI models for interaction with radiology copilots. We'll have virtual (ssh) access to an IGX box for testing this and finding the gaps for a complete solution to ARM version of 3DSlicer.

## Objective

1. Achieve a functional 3D Slicer build on ARM architecture, specifically targeting Apple silicon and Nvidia linux systems.
2. Identify and resolve issues related to volume rendering, segmentation AI models, and radiology copilot interactions on ARM-based systems.

## Approach and Plan

1. Set up virtual (ssh) access to an NVIDIA IGX box for testing and development.
2. Compile and build 3D Slicer from source on the ARM-based system.
3. Test volume rendering capabilities and identify any performance issues or incompatibilities.
4. Integrate and test segmentation AI models on the ARM version of 3D Slicer.
5. Evaluate the interaction between 3D Slicer and radiology copilots on the ARM architecture.
6. Document all encountered issues, workarounds, and solutions.
7. Collaborate with the Slicer community to implement necessary fixes and optimizations.

## Progress and Next Steps

1. Initiated project planning and team coordination.
2. Secured access to NVIDIA IGX box for development and testing purposes.
3. Began preliminary research on existing ARM-related issues in the Slicer GitHub repository.

Next steps:
- Set up development environment on the NVIDIA IGX box.
- Start the compilation process of 3D Slicer on ARM architecture.
- Begin testing basic functionality and identify initial challenges.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

# Main Challenges

Building and running 3D Slicer on the NVIDIA IGX box (ARM architecture) involves several significant challenges:

1. **Qt Dependency**: There are no official Qt binary packages for arm64, requiring developers to build Qt from source. This process can trigger dependency errors and may force disabling of components such as QtWebEngine and QtPDF.

2. **VTK Compilation**: VTK needs to be built with Qt and Python support on ARM, adding extra complexity to the build process.

3. **CUDA Library Compatibility**: Some Holoscan applications that rely on CUDA have shown instability due to library differences, leading to crashes when deallocating memory.

4. **Long-term Maintenance**: Maintaining these custom builds for ARM devices can pose a significant long-term effort unless a broader community helps to support and test the codebase.

5. **Dependency Management**: Building Qt with necessary plugins like xcb for X11 support requires installing additional dependencies that are not always well-documented.

6. **Component Disabling**: Some Qt components may need to be disabled due to build errors, potentially limiting functionality.

These challenges highlight the complexity of porting 3D Slicer to ARM architecture and the need for careful consideration of the maintenance costs involved.

# Background and References

The effort to build 3D Slicer on ARM architecture is part of a broader initiative to expand the platform's compatibility and leverage the capabilities of modern ARM-based systems. This project aligns with the growing trend of ARM adoption in various computing environments, from mobile devices to high-performance computing.

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- [Slicer ARM-related Issues](https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+arm)
- [NVIDIA IGX Platform](https://www.nvidia.com/en-gb/edge-computing/products/igx/)
