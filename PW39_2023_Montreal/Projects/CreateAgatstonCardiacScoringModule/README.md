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

The algorithm for calculating Agatston Cardiac scoring (a clinical way to measure arterial occlusion around the heart) was previously written for an older version of Slicer by Jans Johnson and Jessica Forbes. Andras updated the algorithm and his script was recently tested by members of the community.  This clinical module would be more useful if a Slicer Extension is build so the Agatston scoring is available for clinicians.  This project is a start to creating a Slicer Extension.

## Objective

- Objective A. Describe **what you plan to achieve** in 1-2 sentences.
    Start construction a Slicer Extension to run the existing Agatston scoring algorithm.

## Approach and Plan
    - Create an Extension stub using the Extension Wizard
    - Refactor the Python code to fit in the extension
    - Update the GUI elements and description to guide the user in preparing data
    - Test the Extension
    - Work with the Slicer core community to publish the Agatston Cardiac Scoring Extension

## Progress and Next Steps

    - Reviewed existing algorithm and Andras re-written version
    - Acquired reference cardiac scan with corresponding Agatston score for testing
    - Extension Wizard was easy to get started, though comment text and acknowledgement text entered in the GUI was lost
    - **there is still a runtime error, but we are close**

# Illustrations

Below is the module interface with the debugging buttons from the Extension Wizard still showing. A sample image is loaded
![GUI-Image](https://data.kitware.com/api/v1/file/648a9d9a488633cbb1275cda/download)

# Background and References

Sample Masked Image as input: <https://github.com/lassoan/PublicTestingData/releases/download/data/CardiacAgatstonScore.mrb>

Existing Algorithm to refactor:
<https://github.com/BRAINSia/CardiacAgatstonMeasures>

Andras' updated algorithm on GIST:
<https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02>

A recent update to interpreting Agatston scoring:
<https://pubs.rsna.org/doi/10.1148/ryct.2021200484>
