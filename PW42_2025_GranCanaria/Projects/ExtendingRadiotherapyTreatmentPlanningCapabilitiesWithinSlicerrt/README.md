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

1. Updated to the latest version of pyRadPlan for Python native dose calculation and inverse planning
2. Extension of SlicerRT infrastructure to manage Plan Optimizers & Objectives
3. Add pyRadPlan Optimization Interface & Objective Interface
4. Extension of pyRadPlan/SlicerRT interface to handle multiple beams
5. First fully intensity-modulated photon and proton plans

## Next steps 
1. Performance improvement in data transfers
2. Improve GUI flexibility
3. PR & Code Review SlicerRT

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
## Extended ExternalBeamPlanning Interface with Optimization Settings 
![Photons_5Beams_Plan](https://github.com/user-attachments/assets/25df44e6-0e2b-4972-9958-7305172993d3)

## 5 beam photon plan with SlicerRT pyRadPlan interface:
![Photons_5Beams](https://github.com/user-attachments/assets/4bc2bd58-83ca-433c-8669-51a6937af3e2)

## Dose Influence storage accessible from Python for Beam Nodes:
![Photons_5Beams_DVH](https://github.com/user-attachments/assets/8195eb7d-c6cc-4498-90a1-1f7a4439181e)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://pypi.org/project/pyRadPlan](https://pypi.org/project/pyRadPlan)
- [https://github.com/e0404/matRad](https://github.com/e0404/matRad)

