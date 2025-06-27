---
layout: pw43-project

permalink: /:path/

project_title: Dynamic citation counter badge for papers with code
category: Other

key_investigators:

- name: Mauro Ignacio Dominguez
  affiliation: Independent
  country: Argentina

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Dynamic citation counter badges display up-to-date citation counts, making it easy to track a paper’s real-time impact. They encourage researchers to share code by linking visibility and recognition to reproducible work. Embedding badges in GitHub or documentation connects the code directly with its academic influence. They ensure transparency by pulling citation data from trusted sources automatically. Overall, they promote open science, reproducibility, and fair recognition in the research community.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Achieve a dynamic citation counter badge from a given paper with code if possible 



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Write the steps to get the dynamic citation counter badge from a given paper with code
2. Research most trustable and comprehensive scientific-research metrics web sites or APIs
3. Write a python script that takes a DOI (i.e. Digital Object Identifier) and a scientific-research metrics source as input and gives a dynamic citation counter badge image (and its markdown code) as output
4. Test and implement on a paper with code repository, on the README.md



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Project was successful 
2. Implementation here:
https://gist.github.com/mauigna06/81a593644ec46e520adf4a7561d2075e
3. Use `badgeCreator` function on python



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


- Dynamic badge _with_ link reference: [![auto-commit-msg](https://img.shields.io/badge/dynamic/json?label=Citations&query=%24.citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2FDOI%3A10.1016%2Fj.stlm.2023.100109%3Ffields%3DcitationCount)](https://www.sciencedirect.com/science/article/pii/S2666964123000103#section-cited-by) ([code](https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/8351095086965ad68db3b9257f3e356c13148e49/README.md?plain=1#L15))
- Dynamic badge _without_ link reference: ![auto-commit-msg](https://img.shields.io/badge/dynamic/json?label=Citations&query=%24.citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2FDOI%3A10.1016%2Fj.stlm.2023.100109%3Ffields%3DcitationCount)
- Demo picture below of repository of [BoneReconstructionPlanner](https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/main#bonereconstructionplanner) extension
![Image](https://github.com/user-attachments/assets/8d4ddff1-1784-442a-84e1-996052371e35)
- Dynamic badge for Slicer's paper: [![auto-commit-msg](https://img.shields.io/badge/dynamic/json?label=Citations&query=%24.citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2FDOI%3A10.1016%2Fj.mri.2012.05.001%3Ffields%3DcitationCount)](https://www.sciencedirect.com/science/article/abs/pii/S0730725X12001816?via%3Dihub#preview-section-cited-by)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- https://shields.io/badges/dynamic-json-badge
- https://www.semanticscholar.org/
- https://openalex.org/
- https://www.crossref.org/
- https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/main#bonereconstructionplanner

