---
layout: pw42-project

permalink: /:path/

project_title: Extending Radiotherapy Treatment Planning Capabilities within SlicerRT
category: Quantification and Computation

key_investigators:

- name: Niklas Wahl
  affiliation: DKFZ
  country: Germany

- name: Lina Bucher
  affiliation: KIT/DKFZ
  country: Germany

- name: Francesca Spadea
  affiliation: KIT
  country: Germany

- name: Csaba Pinter
  affiliation: EBATINCA
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We will continue the extension of the treatment planning capabilities of SlicerRT by upgrading the corresponding user interface to better separate plan optimization and dose calculation. Algorithms will be interfaced from the open source treatment planning toolkit matRad via its new Python extension pyRadPlan.
Last year, we managed rudimentary treatment planning capabilities - this year, the goal is to allow full treatment planning on data loaded directly in Slicer, returning planned dose cubes for further analysis in Slicer.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Photon & Ion Dose calculation engines available and configurable within SlicerRT ExternalBeamPlanning
2. SlicerRT ExternalBeamPlanning UI to handle plan optimization objectives defined in c++ and Python
3. Infrastructure for interfacing optimizers from Python and C++
4. Interface to pyRadPlan objectives and optimizers



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Update the existing rudimentary interface prototype for dose engines and optimization to the recent pyRadPlan version
2. Build an Optimization Objective Infrastructure derived from SlicerRT's way of handling python and C++ dose engines
3. Create a dedicated Objective view in the SlicerRT graphical user interface
4. Track potential compatibility conflicts and integrate them into the main pyRadPlan release




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->







# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


## Status from 2024 Project Week in Gran Canaria
### Prototype for beam-wise conformal planning:
<img width="1280" alt="Prostate plan with SlicerRT" src="https://github.com/NA-MIC/ProjectWeek/assets/11944339/a02d4c7c-d771-4723-b07f-e84f2daea30a">

### New widget elements / infrastructure for inverse planning:
<img width="583" alt="Widget Extension" src="https://github.com/NA-MIC/ProjectWeek/assets/11944339/3fcc69a8-a5a0-4be8-8c61-3350bab83bbc">

### Dose Influence storage accessible from Python for Beam Nodes:
<img width="409" alt="Dose Influence Matrix accessibility" src="https://github.com/NA-MIC/ProjectWeek/assets/11944339/246a4b84-4e83-4241-9936-38197f708782">



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://pypi.org/project/pyRadPlan](https://pypi.org/project/pyRadPlan)
- [https://github.com/e0404/matRad](https://github.com/e0404/matRad)

