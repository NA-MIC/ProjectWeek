---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/SlicerVRInteraction/README.html
- /PW39_2023_Montreal/Projects/SlicerVRInteraction/Readme.html

project_title: SlicerVR - Restore Interactions
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:
- name: Simon Drouin
  affiliation: ÉTS Montréal
  country: Canada
  
- name: Csaba Pintér
  affiliation: EBATINCA
  country: Spain

- name: Andrey Titov
  affiliation: ÉTS Montréal
  country: Canada
  
- name: Tina Nantenaina
  affiliation: ÉTS Montreal
  country: Canada
  
- name: Lea Vong
  affiliation: ÉTS Montréal
  country: Canada

- name: Lucas Gandel
  affiliation: Kitware, Inc.
  country: France
  
- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware, Inc.
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->

The main controller interactions in SlicerVR have been broken for about a year, some interaction types even longer. It would be crucial for keeping SlicerVR usable to make the interactions work again.

Kitware and Robarts (Jean-Christophe Fillion Robin, Lucas Gandel, Sankhesh Jhaveri, Adam Rankin) have been investing resources and effort in rehauling the AR/VR backend in VTK for a while, thus now we have a new OpenXR backend and restructured libraries SlicerVR is built on. The goal is to give a small push to their efforts in terms of SlicerVR interactions during the project week, towards restoring at least the previous feature set.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

In PW 37, basic interaction has been fixed. 

1. Fix the two-controller world move/zoom (i.e. 3D pinch) 
2. Customization of controller buttons. Either via the
    * Method in-place (functions integrated [here](https://github.com/KitwareMedical/SlicerVirtualReality/pull/87), see also [here](https://github.com/KitwareMedical/SlicerVirtualReality/pull/83))
    * Json manifest files (see [here](https://github.com/Kitware/VTK/tree/master/Rendering/OpenVR))

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Set up a VR workstations at ETS to be able to test and develop
2. Fix two hands interactions
3. Implement custom interaction to test both customization methods

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Fixed 3D pinch interaction in [commit](https://github.com/KitwareMedical/SlicerVirtualReality/commit/49f1896d652c6b27051cd41e8244b52cd28c2dab)
2. Rebased the GUI widgets branch into a [new branch](https://github.com/cpinter/SlicerVirtualReality/tree/gui-widget-20230612)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

![Class diagram SlicerVR vs VTK](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerVRInteractions/slicer-vr-class-diagram-2.png)

Past project week pages
* [Project week #38 page](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerVRInteractions/)
* [Project week #37 page](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerVRInfrastructure)
* [Project week #35 page](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SlicerVR/)
* [Project week #34 page](https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerVR/)

Pinter, C., Lasso, A., Choueib, S., Asselin, M., Fillion-Robin, J. C., Vimort, J. B., Martin, K., Jolley, M. A. & Fichtinger, G. (2020). SlicerVR for Medical Intervention Training and Planning in Immersive Virtual Reality. IEEE Transactions on Medical Robotics and Bionics, vol. 2, no. 2, pp. 108-117, May 2020, doi: 10.1109/TMRB.2020.2983199.
