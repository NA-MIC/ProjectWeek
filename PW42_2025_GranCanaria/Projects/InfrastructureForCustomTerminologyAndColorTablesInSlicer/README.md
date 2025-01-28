---
layout: pw42-project

permalink: /:path/

project_title: Infrastructure for custom terminology and color tables in Slicer
category: Infrastructure

key_investigators:

- name: Csaba Pinter
  affiliation: Ebatinca
  country: Spain

- name: Andras Lasso
  affiliation: Queens University
  country: Canada

- name: Murat Maga
  affiliation: University of Washington
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Andriy Fedorov
  affiliation: BWH
  country: USA

- name: David Clunie
  affiliation: PixelMed
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Terminologies module are meant to give a structure around using pre-determined set of anatomical and developmental terms for segmentation tasks. This is meant to avoid potential typos for people not familiar with anatomical terminology (e.g., humerus vs humorous, sagittal vs saggital) and give a consistent look and feel (e.g., assign consistent colors to a segmentation across multiple datasets). 

But the existing structure is too rigid, and often is missing terms. We need a flexible structure for people to create and use their own terms when the existing terminiologies are insufficient



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. To resolve this we have created an [issue page](https://github.com/Slicer/Slicer/issues/6975)
2. and working towards resolving the [identified issues](https://github.com/Slicer/Slicer/pull/8112)
3. Discuss how to [design and implement an infrastructure to share user-generated color tables (as well as custom terminologies, volume rendering presets, etc).](https://github.com/Slicer/Slicer/issues/6975#issuecomment-2581121209) 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We are looking into using custom color tables and importing them as terminologies as a solution for flexibility and consistentcy.
2. Discuss the current design considering all known use cases in a breakout session



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. there is a [PR](https://github.com/Slicer/Slicer/pull/8112) that address some of the issues.
2. We had a breakout session on Tuesday with all the key participants. Takeaway
    * The proposed design generally looks acceptable
    * Need a validator to be able to ensure compatibility with main ontologies
    * Need a proper documentation of the new features and their interactions with all data types and use cases
    * Fix bugs, finalize PR, allow people to test in 5.9


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![image](https://github.com/user-attachments/assets/7deac812-bc55-4e88-8640-247f89429944)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* [Pull request](https://github.com/Slicer/Slicer/pull/8112)
* Issue [#7593](https://github.com/Slicer/Slicer/issues/7593)
* Issue [#6975](https://github.com/Slicer/Slicer/issues/6975)

