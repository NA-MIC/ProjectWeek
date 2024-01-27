---
layout: pw40-project

permalink: /:path/

project_title: Extending Radiotherapy Treatment Planning Capabilities within SlicerRT
category: Other
presenter_location: In-person

key_investigators:

- name: Niklas Wahl
  affiliation: DKFZ
  country: Germany

- name: Csaba Pinter
  affiliation: EBATINCA
  country: Spain

- name: Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Italy

---

# Project Description

<!-- Add a short paragraph describing the project. -->

We will extend the treatment planning capabilities of SlicerRT by upgrading the corresponding user interface to better separate plan optimization and dose calculation. Algorithms will be interfaced from the open source treatment planning toolkit matRad via its new Python extension pyRadPlan.
The goal is to allow full treatment planning on data loaded directly in Slicer, returning planned dose cubes for further analysis in Slicer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Python connection between SlicerRT ExternalBeamPlanning & pyRadPlan (matRad's Python interface)
2.  Photon & Ion Dose calculation engines available within SlicerRT ExternalBeamPlanning
3.  Updated SlicerRT ExternalBeamPlanning UI to better display planning workflow
4.  Rudimentary treatment plan optimization capabilities within SlicerRT

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Evaluate existing internal prototype for SlicerRT / matRad Python Interface
2.  Interface Forward dose calculation engines from matRad for photons and ions
3.  Update ExternalBeamPlanning Infrastructure to represent four-step planning process in slicerRT: Geometry Definition, Inverse Dose precomputation, Optimization, Forward dose calculation (already existing within ExternalBeamPlanning module in SlicerRT).

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

*No response*

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
