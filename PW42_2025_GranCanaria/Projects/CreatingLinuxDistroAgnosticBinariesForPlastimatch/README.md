---
layout: pw42-project

permalink: /:path/

project_title: Creating Linux distro-agnostic binaries for Plastimatch
category: Infrastructure

key_investigators:

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital, Harvard Medical Schools
  country: USA

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Plastimatch is an open-source software for medical image processing and registration.
It is written in C++ and can be built from source in Linux and Windows.
Binary packages are available for Windows, Debian (plus its derivatives), and Arch Linux users.
No Linux distro-agnostic binaries are currently available.
During this week we will explore the possibility of creating a binary version of plastimatch easily portable/deployed in different Linux distros.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Create a Plastimatch distro-agnostic binary package



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Prepare a fresh build environment
2. Compile Plastimatch from source
3. Figure out how to bundle/embed the required libraries



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. A bash script to compile Plastimatch and its dependencies has been written
2. We decided to use ManyLinux 2.28 docker container as a building environment
3. We found out the Plastimatch file probe fails to identify the dicomRT (this happens only when we move the binary)
4. We found out it was needed to set -DDCMTK_DEFAULT_DICT=builtin -DDCMTK_ENABLE_PRIVATE_TAGS=ON during DCMTK configuration step




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://gitlab.com/plastimatch/plastimatch](https://gitlab.com/plastimatch/plastimatch)
