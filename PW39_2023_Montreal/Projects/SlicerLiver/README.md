---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/SlicerLiver/README.html

project_title: Slicer-Liver
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Gabriella D'Albenzio
  affiliation: Oslo University Hospital
  country: Norway

- name: Ruoyan Meng
  affiliation: NTNU
  country: Norway

- name: Ole V. Solberg
  affiliation: SINTEF
  country: Norway

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[Slicer-Liver](https://github.com/ALive-research/Slicer-Liver) is an advanced 3D Slicer extension developed for liver therapy planning. The extension currently offers essential features for liver resection planning and accurate computation of vascular territories. As part of an ongoing project, our aim is to further enhance the existing functionalities and introduce new tools for volumetry computation. Our objective is to provide a comprehensive and user-friendly solution for liver therapy planning within the Slicer platform.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Advanced manipulation of deformable surfaces for resection planning. Our current solution for resection planning involves the deformation of Bezier surfaces in a 4x4 grid implemented by means of Slicer Markups (<https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html>). We are planning to  include advanced features such as coloring and grouping of markups for a more effective manipulation.
2.  Volumetry computation. Planning of liver therapies largely relies on a volumetry analysis derived from the therapy plan. We are planning to include versatile tools for volume computations.
3.  Release of Slicer-Liver 1.0. As Slicer-Liver is becoming an feature rich extension, we aim to release the latest developments achieved during this and the last Project Week in the extension manager (currently, the version released in the Extension Manager does not contain the latest advances).

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Discussion and find a strategy to improve our Markups-based resections interaction (Custom C++ markups vs. Python logic)
2.  Implementation of the new features (new markups interaction and volumetric computation tools).
3.  Testing of the new features and release of the new extension.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Thanks to changes made by Sara Rolfe in the markup module (Seattle Children's Research Institute USA) we are now able to modify the interaction of Markups-based resections.
2.  Integrated a new set of volumetric computation tools using the region growing method

![liver-volumetry-resection0](https://github.com/NA-MIC/ProjectWeek/assets/75131750/91485aa5-b4ff-431f-933c-681cacaf54d1)

![liver-volumetry-resection](https://github.com/NA-MIC/ProjectWeek/assets/75131750/388743ad-45ca-4c9c-bcd6-f72d2e14d7ca)



# Illustrations

<p float="left">
  <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_01.png?raw=true" width="30%">
  <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_04.png?raw=true" width="30%">
  <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_02.png?raw=true" width="30%">  
</p>

<p float="left">
   <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_08.png?raw=true" width="40%">
   <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_06.png?raw=true" width="40%">
   
</p>

<img width="50%" alt="resection" src="https://user-images.githubusercontent.com/75131750/216592014-82fc6c37-0b58-41dd-8a73-6ab97d1aede0.gif">


<img width="50%" alt="resectogram" src= "https://user-images.githubusercontent.com/75131750/216590392-62093987-8c14-4e43-88ad-4215a9764766.gif">

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [Slicer-Liver on Project Week](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/)
*   <https://discourse.slicer.org/t/changing-size-and-color-of-individual-interaction-handles-of-roi/26360/7>
