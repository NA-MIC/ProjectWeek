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

Update the documentation for Slicer development to describe what should
be expected. Provide expanded guidance for how to identify and work through
common issues that arise in different environments.

## Improve Slicer build instructions
Building a custom version of Slicer has become increasingly complex.  
    - Identify how to install Qt on an ARM-based Apple M4 computer.
    - Identify how to install Qt on a Ubuntu 24.04 Linux computer.

## Objective

1. Improve documentation for new (not expert) developers to understand the environment necessary to build Slicer on Linux (Ubuntu 24.04), Mac (M4 new mac), Windows
2. To prepare Slicer for future versions of ITK, but configuring a stable build environment has been more challenging than expected (primarily regarding Qt 5 requirements). 
3. Update BRAINSTools support in Slicer
4. Have Slicer build succesfully with CMake 4.0

Strech Goals 
1. Stretch Goal -- Setup building a large number of extensions to facilitate preparation for ITKv6 C++17  (while maintaining backward compatibility).
2. Investigate updating TCLAP to build cleanly, perhaps update to the latest version of TCLAP.
3. Investigate the status of moving to Qt6.  Provide support/testing environments for migration to Qt6.  [https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/TransitionSlicerDefaultBuildFromQt5ToQt6/](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/TransitionSlicerDefaultBuildFromQt5ToQt6/)

## Approach and Plan

1. Have Cavan follow instructions naively, and update instructions as necessary to get a build environment that allows building of Slicer
2. Find outdated build instructions via Google searching and update/remove documentation.

## Progress and Next Steps

1. Downloaded Slicer source code, tried to build on mac M4 computer.
2. Updates to allow for building with CMake 4+ [https://github.com/Slicer/Slicer/pull/8491](https://github.com/Slicer/Slicer/pull/8491)

``` bash
# Install older version of cmake with homebrew on mac
brew uninstall cmake
# Find and download the formula for the cmake version you wish to install 
curl -O https://raw.githubusercontent.com/Homebrew/homebrew-core/1976f46fc84ea7716722a067c0dcffb072a38388/Formu
la/c/cmake.rb
brew install ./cmake.rb
```

<!--
# Illustrations

< ! -- Add pictures and links to videos that demonstrate what has been accomplished. -- >

_No response_
-->

# Background and References

<!-- If you developed any software, include a link to the source code repository.
     Also add links to sample data and to any relevant publications. -->

The current instructions 2025-06-17 do not work on Arm64-based Mac, primarily due to the inability to install Qt5 on an Arm64 based mac.

[Base Instructions](https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html)

