---
layout: pw44-project

permalink: /:path/

project_title: DMRI population analysis library bridge
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Ebrahim Ebrahim
  affiliation: Kitware
  country: USA

- name: Arthur Chakwizira
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We've been working on a python library, currently (badly) named [abcdmicro](https://github.com/brain-microstructure-exploration-tools/abcd-microstructure-pipelines/), for diffusion MRI population analysis. Its goal is to make it easy to have the tools you need for processing population brain diffusion MRI in one convenient-to-set-up python package, with normally disparate processing steps getting linked together nicely. Slicer isn't where one would typically do large population analysis, but it is an excellent for visualizing examples while putting together a pipeline, and it's excellent for interacting with results. For this reason, I'd like to look into bridging abcdmicro with Slicer.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


* Make it easy for someone who is building a dmri processing pipeline with abcdmicro to try out the steps of their pipeline in Slicer.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

* Create vtk-mrml-based versions of some of the [`Resources`](https://github.com/brain-microstructure-exploration-tools/abcd-microstructure-pipelines/blob/e1ca05eed77a9fcc3e934c4de7f6f43fbcf8bc1f/src/abcdmicro/resource.py) in abcdmicro and conversion utilities that allow them to be created and used.



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

- [abcdmicro](https://github.com/brain-microstructure-exploration-tools/abcd-microstructure-pipelines/) is the library we have currently been working on for which I'd like to experiment with bridging with Slicer.

