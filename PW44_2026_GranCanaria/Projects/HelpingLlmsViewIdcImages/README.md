---
layout: pw44-project

permalink: /:path/

project_title: Helping LLMs view IDC images
category: Cloud / Web
presenter_location: 

key_investigators:

- name: Michael Halle
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The Imaging Data Commons is filled with imaging data, but idc-index and database searches only return textual data/metadata to LLMs. Modern LLMs have vision capabilities and can view selected images. I will complete a standalone non-interactive imaging utility that will give LLMs an image viewing capability for IDC data.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. A standalone python CLI for displaying an image or mosaic from an IDC series. 
2. A Claude Skill (or an extension of an existing skill) that teaches an LLM to look at IDC images.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Finish the CLI
2. Get feedback
3. Finish the Skill



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1 Prototype "idc-series-preview" is written but needs knowledgable eyes on the project. It also needs some features like annotations added. This project could well be done using fancy DICOM viewer code, but for right now Python works fine for the prototype.
1 During Project Week, I added annotations to the python module and made it into a Claude Skill.

Python module/skill: <https://github.com/mhalle/idc-series-preview>

Skill download: <https://github.com/mhalle/idc-series-preview/releases/latest/download/idc-series-preview.skill>

# Illustrations

"Find the bottom of the lungs in an IDC NLST series".

[Base of lungs](nlst_lung_bases_v070.jpg)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

