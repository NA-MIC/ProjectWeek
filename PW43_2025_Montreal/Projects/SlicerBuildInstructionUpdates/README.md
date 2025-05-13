---
layout: pw43-project

permalink: /:path/

project_title: Slicer Build Instruction Updates
category: Infrastructure

key_investigators:

- name: Hans Johnson
  affiliation: University of Iowa

- name: Cavan Riley
  affiliation: University of Iowa -- Working from Iowa

- name: Slicer Core Developers
  affiliation: Jean-Christophe Fillion-Robin / Others ??

---

# Project Description

<!-- Add a short paragraph describing the project. -->


# Improve Slicer build instructions
Building a custom version of Slicer has become increasingly complex.  
    - Identify how to install Qt on an ARM-based Apple M4 computer.
    - Identify how to install Qt on a Ubuntu 24.04 Linux computer.






## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Improve documentation for new (not expert) developers to understand the environment necessary to build Slicer on Linux (Ubuntu 24.04), Mac (M4 new mac), Windows
2. To prepare Slicer for future versions of ITK, but configuring a stable build environment has been more challenging than expected (primarily regarding Qt 5 requirements)

Strech Goals 
1. Stretch Goal -- Setup building a large number of extensions to facilitate preparation for ITKv6 C++17  (while maintianing backward compatibility).
2. Investigate the status of moving to Qt6.  Provide support/testing environments for migration to Qt6.
3. Investigate updating TCLAP to build cleanly, perhaps update to the latest version of TCLAP.





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Have Cavan follow instructions niavely, and update instructions as necessary to get a build environment that allows building of Slicer
2. Find outdated build instructions via google searching and update/remove documentation.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Downloaded Slicer source code, tried to build on mac M4 computer.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[Base Instructions](https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html)

