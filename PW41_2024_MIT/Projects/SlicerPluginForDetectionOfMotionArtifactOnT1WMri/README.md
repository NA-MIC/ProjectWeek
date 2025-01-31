---
layout: pw41-project

permalink: /:path/

project_title: Slicer Plugin for Detection of Motion Artifact on T1w MRI
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Charles Bricout
  affiliation: ÉTS
  country: Canada

- name: Sylvain Bouix
  affiliation: ÉTS
  country: Canada

- name: Owen Borders
  affiliation: Massachusetts General Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We want to create a Slicer module to detect and / or quantify motion artifacts in T1 weighted MRI.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Create a Slicer module to plug our models.
2. Connect our models with Slicer (retraining might be necessary).
3. Include an estimation of uncertainty.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Describe specific steps of **what you plan to do** to achieve the above described objectives.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Review and improved the synthetic data generation pipeline
   - Change magnitude of motion
   - Change interpolation method
2. Create a Slicer Module to expose pretrained models
   - Inference in 0.5 seconds on CPU
   - Light preprocessing
   - Display full histogram output
   - Keep history of motion metrics for comparison between files
3. **Next Steps** :
   - Ability to export history to CSV
   - Connector with [Comet.ml](https://www.comet.com) to retrieve models associated with specific experiment from Slicer

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![Capture d'écran 2024-06-28 091535](https://github.com/NA-MIC/ProjectWeek/assets/28633686/3ad44c02-c05e-40a3-9735-4083cc5fcfbb)


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_
