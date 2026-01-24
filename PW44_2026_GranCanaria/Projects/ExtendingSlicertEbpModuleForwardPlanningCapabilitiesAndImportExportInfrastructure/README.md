---
layout: pw44-project

permalink: /:path/

project_title: Extending SliceRT EBP Module - forward planning capabilities and import-export infrastructure
category: Infrastructure
presenter_location: 

key_investigators:

- name: Lina Bucher
  affiliation: KIT & DKFZ
  country: Germany

- name: Maria Francesca Spadea
  affiliation: KIT
  country: Germany

- name: Niklas Wahl
  affiliation: DKFZ
  country: Germany

- name: Csaba Pintér
  affiliation: EBATINCA
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Recent work on SlicerRT's EBP module has focused on its inverse planning infrastructure for dose calculation and plan optimization, integrating the multi-modality treatment planning toolkit pyRadPlan (see [https://github.com/e0404/pyRadPlan](https://github.com/e0404/pyRadPlan)).

Now we want to further extend the module's forward planning capabilities as well as its export and import features.

Our overall goal is to establish a well-integrated treatment planning tool in Slicer, that remains customizable and user-friendly.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. **RTPlan recalculation:** Advance the pyRadPlan dose engine for forward calculations on loaded plans.
2.  **Import/Export Features:** Build infrastructure for saving and loading dose influence matrices and objectives.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. **RTPlan recalculation:** Implement handling of loaded MLC shapes (photon plan), spot positions (ion plan) and machine specifications in the pyRadPlan dose engine.
2.  **Import/Export Features:** Revise storing of the dose influence matrices (currently beam-wise) and develop method for exporting and reloading into plan. Include saving/exporting of the user-specified objectives table in the optimization workflow.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

