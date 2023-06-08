---
layout: pw39-project

permalink: /:path/

project_title: Create Agatston Cardiac Scoring Module
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Curtis Lisle
  affiliation: KnowledgeVis
  country: USA

- name: Andras Lasso
  affiliation: Queens University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The algorithm for calculating Agatston Cardiac scoring (a clinical way to measure arterial occlusion around the heart) was previously written by Jans Johnson et al.  The script was recently tested by members of the community, but it would be more useful if a Slicer Module to run the Agatston scoring was available.  This project is a start to creating the module and eventually a Slicer Extension.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A. Describe **what you plan to achieve** in 1-2 sentences.
    Start building a Slicer Extension to run the existing Agatston scoring algorithm.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Describe specific steps of **what you plan to do** to achieve the above described objectives.
    Create an Extension stub with the Extension Wizard
    Refactor the Python code to fit in the extension
    Add GUI elements and description to guide the user in preparing data
    Test the Extension
    Work with the Slicer core community to publish the Agatston Cardiac Scoring Extension

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.
    Reviewed existing algorithm
    Acquired reference cardiac scan with corresponding Agatston score for testing

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Sample Masked Image as input: <https://github.com/lassoan/PublicTestingData/releases/download/data/CardiacAgatstonScore.mrb>

Existing Algorithm to refactor:
<https://github.com/BRAINSia/CardiacAgatstonMeasures>

A recent update to interpreting Agatston scoring:
<https://pubs.rsna.org/doi/10.1148/ryct.2021200484>
