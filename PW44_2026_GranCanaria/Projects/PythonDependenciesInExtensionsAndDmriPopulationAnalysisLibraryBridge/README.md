---
layout: pw44-project

permalink: /:path/

project_title: Python dependencies in extensions, and dmri population analysis library bridge
category: Infrastructure
presenter_location: 

key_investigators:

- name: Ebrahim Ebrahim
  affiliation: Kitware
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Many Slicer extension developers these days have to deal with the problem of external python dependencies: how to specify them, how and when to install them, and how to validate that the required things are installed. Everyone addresses the problem in a different way, with a lot of re-inventing the wheel and also a lot of great ideas out there. I'd like to collect all the best practices and turn them into a framework that is build into core slicer for extension developers to more easily grab and use. Something like "stick your dependencies in here and the use `slicer.util.check_python_dependences` and `slicer.util.install_python_dependencies`. If that turns out to be a bad idea for whatever reason, at least I can collect all the best practices and put them into the extension development documentation.

A backup project, in case that one doesn't pan out or gets wrapped up too quickly: I've been working on a python library, currently (badly) named [abcdmicro](https://github.com/brain-microstructure-exploration-tools/abcd-microstructure-pipelines/), for diffusion MRI population analysis. Its goal is to make it easy to have the tools you need for processing population brain diffusion MRI in one convenient-to-set-up python package, with normally disparate processing steps getting linked together nicely. Slicer isn't where one would typically do large population analysis, but it is an excellent for visualizing examples while putting together a pipeline, and it's excellent for interacting with results. For this reason, I'd like to look into bridging abcdmicro with Slicer. This is somewhat related to the above, because it would be yet another example of an extension that has external python dependencies.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


* Encode into Slicer some way to make it more convenient for extension developers to handle external python dependencies.

For the secondary project:

* Make it easy for someone who is building a dmri processing pipeline with abcdmicro to try out the steps of their pipeline in Slicer.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


* Gather best practices on external python dependency handling in Slicer extensions, and then distill them into an optimized approach.
* Encode that approach in Slicer somehow, either as utility functions, updates to extension templates, or simply documentation.

For the secondary project:

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


- The [SlicerOpenLIFU](https://github.com/OpenwaterHealth/SlicerOpenLIFU) extension is where I have most recently applied what I know about handling python dependencies. But it could be so much better.
- [abcdmicro](https://github.com/brain-microstructure-exploration-tools/abcd-microstructure-pipelines/) is the library we have currently been working on for which I'd like to experiment with bridging with Slicer.

