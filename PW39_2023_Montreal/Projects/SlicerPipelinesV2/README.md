---
layout: pw39-project

permalink: /:path/

project_title: Slicer Pipelines v2
category: Infrastructure
presenter_location: Online

key_investigators:

- name: Harald Scheirich
  affiliation: Kitware, Inc.
  country: United States

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Slicer Pipelines is a framework to support the creation of workflows (Pipelines) inside of slicer. It allows users to attach a variety of slicer operations with pipeline support to each other and create a module that can then be executed on its own. Pipelines v2 is based on the work that Connor and others did with the ParameterWrapper.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Adapt the PipelineCaseIterator to the new pipeline architecture

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Basic refactoring so that PipelineCaseIterator runs with a simple test case
2.  Move from allowing single input directory to driving input through csv file
3.  Adapt the output side of the case iterator to support multiple values
4.  Write output data into csv file
5.  Test with different pipelines

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Refactoring has been done, basic CaseIterator runs with test pipeline
2.  CSV files can be read to drive input parameters
3.  Name and store nodes for pipelines that produce multiple nodes
4.  Write `results.csv` with scalar ouput values and result node paths

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- Slicer Pipelines Module Repository: <https://github.com/KitwareMedical/SlicerPipelines>
- Project Week 36: <https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/SlicerPipelines/>
- Project Week 38: <https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerPipelines/>
