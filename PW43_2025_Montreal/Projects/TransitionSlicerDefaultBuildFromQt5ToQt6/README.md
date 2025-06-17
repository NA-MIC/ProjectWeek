---
layout: pw43-project

permalink: /:path/

project_title: Transition Slicer Default Build from Qt5 to Qt6
category: Infrastructure

key_investigators:

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: James Butler
  affiliation: Revvity
  country: USA

- name: Hans Johnson
  affiliation: University of Iowa
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project focuses on updating Slicer's build system, dependencies, and related infrastructure to support building, packaging, and distributing Slicer with Qt6.

This effort lays the groundwork for supporting native builds on macOS ARM systems.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Ensure all Slicer dependencies can be built with Qt6.
2. Enable building Slicer itself against Qt6.
3. _Tentative_: Update infrastructure and build environments to support packaging and continuous integration with Qt6 builds.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. **Identify Suitable Qt6 Version**: Evaluate supported Qt6 versions to determine the most compatible and stable version for Slicer (tentatively targeting Qt 6.9).

2. **Test Qt6 Compatibility of Dependencies**: Build Slicer’s external dependencies with Qt6, document any issues encountered, and work toward resolving them.

3. **Enable Qt6 Build of Slicer**: Support configuring Slicer with `Slicer_REQUIRED_QT_VERSION=6.9` (or selected version) to enable Qt6-based builds.

4. **Update Infrastructure and CI for Qt6** (_Tentative_)
   - Update packaging scripts and build environments (e.g., Docker images, GitHub Actions runners) to support Qt6-based builds.
   - Add CI jobs to test, build, and package Slicer against Qt6 on supported platforms (Linux, Windows, macOS ARM/x86_64).
   - Validate the creation of functioning Slicer packages built with Qt6.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


_No response_



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* https://github.com/Slicer/Slicer/issues/6388

