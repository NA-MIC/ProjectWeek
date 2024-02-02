---
layout: pw40-project

permalink: /:path/

project_title: 5D image IO support in Slicer
category: Infrastructure
presenter_location: In-person

key_investigators:
- name: Csaba Pinter
  affiliation: EBATINCA, S.L.
  country: Spain

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada
---

# Project Description

<!-- Add a short paragraph describing the project. -->

Slicer currently does not support reading/writing (IO) of 5D images. In the driving use case this means a sequence of vector volumes. This project is about continuing an existing effort to add such support into Sequences storage.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Keep developing the current implementation
1. Objective B. Collecting use cases (what exactly to support in the first round)
1. Objective C. Discussing implementation details

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use ITK metadata dictionary to change last dimension from `domain` to `time` or other "list" type
2. Start working on 5D image reading

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Build branch in Debug mode on laptop
2. Metadata dictionary is ignored when writing, or at least the "kinds" information
3. Investigate `ITK` and `nrrd` code to find a way to set the last "kind"
4. Manually edit NRRD header and see what SimpleITK reads it as

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

* Working branch: https://github.com/cpinter/Slicer/tree/volume-sequence-io-5D
