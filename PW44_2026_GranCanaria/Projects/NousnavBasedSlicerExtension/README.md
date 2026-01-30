---
layout: pw44-project

permalink: /:path/

project_title: NousNav based Slicer Extension
category: IGT and Training
presenter_location: 

key_investigators:

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Tina Kapur
  affiliation: BWH/HMS
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Andras Lasso
  affiliation: Queen's
  country: Canada

- name: Kyle Sunderland
  affiliation: Queen's
  country: Canada

- name: Csaba Pinter
  affiliation: Ebatinca
  country: Spain

- name: Martin Bellehumer
  affiliation: Germany

- name: Rafael Palomar
  affiliation: Norwegian University of Science and Technology
  country: Norway

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The goal of this project is to create a Slicer Extension (tentative name SlicerNav) that starts with the functionality of NousNav, which is a CustomApp, and then grows from there.



## Tasks

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. PRIORITY: Clear out pending NousNav todos and prepare a new release
    1. Autosave / segmentation lag
    1. Other issues from Sonia
1. Refactor modules to a new extension: SlicerOpenNav
1. Test build with refactored modules
1. Test extension with latest Slicer version
1. Code modernization
    1. Update NousNav to latest Slicer
    1. Parameter node usage


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. NousNav 1.1
    1. Finished pending todos from Sonia Pujol (usability of Patients module)
    1. NousNav 1.1.0 tagged
    1. NousNav 1.1.0 installer generated - needs testing before release is created
1. SlicerOpenNav
    1. Generated from NousNav modules, with history preserved
    1. Works from:
        1. Build tree
        1. Installation
        1. Source Tree
1. SlicerOpenNav -> NousNav
    1. NousNav refactored to use SlicerOpenNav (on branch)
    1. Home module will remain as customization point





# Illustrations

<img src="https://raw.githubusercontent.com/NousNav/SlicerOpenNav/refs/heads/main/SlicerOpenNav.svg" width="256" height="256" alt="SlicerOpenNav">

![](https://github.com/user-attachments/assets/42c47e5a-aabb-4bf5-b106-06f8437ad85c)

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- [SlicerOpenNav](https://github.com/NousNav/SlicerOpenNav)
