---
layout: pw39-project

permalink: /:path/

project_title: Towards NousNav Major Version Release
category: IGT and Training
presenter_location: In-person

key_investigators:
- name: Sam Horvath
  affiliation: Kitware, Inc.
  country: USA

- name: Colton Barr
  affiliation: Queen's University / Brigham and Women's Hospital
  country: Canada
  
- name: Sarah Frisken
  affiliation: Brigham and Women's Hospital
  country: USA
  
- name: Sonia Pujol
  affiliation: Brigham and Women's Hospital
  country: USA
  
- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA
  
- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Alex Golby
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->
NousNav is an ongoing project led by Dr. Alex Golby at Brigham and Women's Hospital to build and disseminate a low-cost neuronavigation system. Built as a 3D Slicer Custom App, NousNav uses low cost optical tracking (Optitrack Duo) in combination with custom optically-tracked tools and reference arrays to facilitate patient registration, procedure planning, and navigation.

For this project we are going to finalize remaining issues on the tracker to move towards a 1.0 release

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Triage existing issues into a major/minor release tasks
1. Clear issues for the 1.0 Release

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
![Screenshot 2022-12-05 13 15 04](https://github.com/NA-MIC/ProjectWeek/assets/25040869/8f9fa3be-d527-4fc0-aedc-345852b385eb)

Major tasks to work on:

1. DICOM patient management
    1. Storage of MRBs as secondary captures
    1. Store XML only?
1. Landmarks management rework
    1. Granular color management
    1. Single landmarks class
1. LPS orientation in Nav phase

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Reworked the registration landmark support.
    1. Support any sufficient subset of the complete landmark list
    2. Registration picking provides better control of order of landmark collection
    3. Improved color consistency acroos landmark usage
2. Made patient interface styling consistent with rest of application
3. Demo'd recent changes to the rest of the NousNav team


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![Screenshot 2023-06-13 15 29 24](https://github.com/NA-MIC/ProjectWeek/assets/25040869/cea0c2c0-0f83-4af3-afc6-a2b858ba886a)
![Screenshot 2023-06-13 17 11 09](https://github.com/NA-MIC/ProjectWeek/assets/25040869/7da490fe-f790-49b7-b2b9-1b475f3ec0ea)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
[NousNav website](https://www.nousnav.org/)
