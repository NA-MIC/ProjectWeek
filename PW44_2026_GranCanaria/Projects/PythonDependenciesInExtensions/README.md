---
layout: pw44-project

permalink: /:path/

project_title: Python dependencies in extensions
category: Infrastructure
presenter_location: 

key_investigators:

- name: Ebrahim Ebrahim
  affiliation: Kitware
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Many Slicer extension developers have to deal with the problem of external python dependencies: how to specify them, how and when to install them, and how to validate that the required things are installed. Everyone addresses the problem in a different way, often re-inventing the wheel and also often generating new great ideas. I'd like to collect all the best practices and turn them into a framework that is built into core slicer for extension developers to more easily grab and use. Something like "stick your dependencies in here and the use `slicer.util.check_python_dependences` and `slicer.util.install_python_dependencies`. If that turns out to be a bad idea for whatever reason, at least I can collect all the best practices and put them into the extension development documentation.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


* Encode into Slicer some way to make it more convenient for extension developers to handle external python dependencies.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


* Gather best practices on external python dependency handling in Slicer extensions, and then distill them into an optimized approach.
* Encode that approach in Slicer somehow, either as utility functions, updates to extension templates, or simply documentation.



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

