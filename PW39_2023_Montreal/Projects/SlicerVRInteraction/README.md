---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/SlicerVRInteraction/README.html
- /PW39_2023_Montreal/Projects/SlicerVRInteraction/Readme.html

project_title: SlicerVR - Restore Interactions
category: VR/AR and Rendering
presenter_location: Remote

key_investigators:
- name: Csaba Pintér
  affiliation: EBATINCA
  country: Spain

- name: Simon Drouin
  affiliation: ÉTS Montréal
  country: Canada

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware, Inc.
  country: USA

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

1. Fixed 3D pinch interaction in commit [SlicerVirtualReality@49f1896d6](https://github.com/KitwareMedical/SlicerVirtualReality/commit/49f1896d652c6b27051cd41e8244b52cd28c2dab)
2. Rebased the GUI widgets branch into a [new branch](https://github.com/cpinter/SlicerVirtualReality/tree/gui-widget-20230612)
3. Fixed lookup of `vtk_openvr_actions.json` and `vtk_openvr_binding_*.json` files for both build and install tree. See commit [SlicerVirtualReality@a4d465b73](https://github.com/KitwareMedical/SlicerVirtualReality/commit/a4d465b7321a6cdd2e0c3aa85eb04899be471b17) integrated through [PR-117](https://github.com/KitwareMedical/SlicerVirtualReality/pull/117)
4. Make in-VR GUI widget work (with many workarounds and limitations)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->


Laser pointer interactions with widget existing in Slicer:

<video
  controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/1325980/a6fc0061-e40e-43e3-92a0-b31badb14c43"
  style="max-height:640px; min-height: 200px">
</video>

Laser pointer interactions with custom widget:

<video
  controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/1325980/7c457f93-2b80-4806-9cb5-e58acc393aa4"
  style="max-height:640px; min-height: 200px">
</video>

More comprehensive demonstration:

[![More comprehensive demonstration](https://i9.ytimg.com/vi_webp/Ny5gmIFbhK4/mq1.webp?sqp=CJTDrKQG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEsgSyhlMA8=&rs=AOn4CLDerRLwDJQoa2buCxVCCoKyIv-glA)](https://youtu.be/Ny5gmIFbhK4)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

![Class diagram SlicerVR vs VTK](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerVRInteractions/slicer-vr-class-diagram-2.png)

Past project week pages
* [Project week #38 page](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerVRInteractions/)
* [Project week #37 page](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerVRInfrastructure)
* [Project week #35 page](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SlicerVR/)
* [Project week #34 page](https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerVR/)

Pinter, C., Lasso, A., Choueib, S., Asselin, M., Fillion-Robin, J. C., Vimort, J. B., Martin, K., Jolley, M. A. & Fichtinger, G. (2020). SlicerVR for Medical Intervention Training and Planning in Immersive Virtual Reality. IEEE Transactions on Medical Robotics and Bionics, vol. 2, no. 2, pp. 108-117, May 2020, doi: 10.1109/TMRB.2020.2983199.
