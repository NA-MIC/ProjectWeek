Back to [Projects List](../../README.md#ProjectsList)

# Slicer-Liver

## Key Investigators

- Rafael Palomar (Oslo Unviersity Hospital/NTNU, Norway)
- Gabriella d'Albenzio (Oslo University Hospital, Norway)
- Ruoyan Meng (NTNU, Norway)
- Ole Vegard Solberg (SINTEF, Norway)
- Geir Arne Tangen (SINTEF, Norway)

# Project Description

This project will continue the development of the *Slicer-Liver* extension
that will be developed through the [ALive project](https://alive-research.no).
The objective of the Slicer-Liver extension is to provide researchers
with tools to perform liver analytics towards planning of liver interventions
(resections, ablations).

## Objectives

   - Liver resection planning:

      1. *Integration of resection contours* : introduce a new resection surface generated from a curved contour; this implies less interactions with the 3D Models.
      2. *Real-time 2D resection risk maps* : extract functional information in real time from the 3D resection surface and then map it onto a 2D map with intuitive and detailed information for surgical risk assessment and planning decisions.

   - Testing:

      1. Improve testing infrastructure of the project

## Approach and Plan

For this Project week we will build on the advances obtained in the las project
week. Some of the objectives are based on new functionality that has been tested
but not integrated yet, while some other objectives are refinement of
functionality previusly integrated in [Slicer-Liver
PW36](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/Slicer-Liver

## Illustrations

<p float="left">
  <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_01.png?raw=true" width="30%">
  <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_04.png?raw=true" width="30%">
  <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_02.png?raw=true" width="30%">
</p>

<p float="left">
   <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_08.png?raw=true" width="40%">
   <img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_06.png?raw=true" width="40%">

</p>

# Resection from curved contour
We create a new resection surface generated directly from a curved contour; this implies fewer interactions with the 3D Models and quicker planning.

<img width="50%" alt="resection" src="https://user-images.githubusercontent.com/75131750/216592014-82fc6c37-0b58-41dd-8a73-6ab97d1aede0.gif">

# Resectogram
We create Real-time 2D resection risk map: which extracts functional information in real-time from the intersection between the 3D resection surface and liver model and then maps it onto a 2D map, resulting in quicker risk analysis with less cognitive cost while planning the surgery.

<img width="50%" alt="resectogram" src= "https://user-images.githubusercontent.com/75131750/216590392-62093987-8c14-4e43-88ad-4215a9764766.gif">

## Lung Surgery Planning with Rudolf Bumm
We also tried to extend our user scenario from liver resection to lung resection.   With the help of Dr. Rudolf, we plan a lung surgery case using Slicer liver extension.

<p float="left">
   <img width="40%" alt="lung-2D" src="https://user-images.githubusercontent.com/75131750/216588131-43cb4077-7e01-4cc4-a908-8aaf5eb5a4bc.png">
   <img width="40%" alt="lung-3D" src="https://user-images.githubusercontent.com/75131750/216588148-5bff64e0-67c6-42cd-a65d-98f4cad9b955.gif">
</p>


## Progress and Next Steps

In this project week, we have changed the user interaction to use segmentations instead of models, which greatly simplifies the user interaction.

There is a PR for adding this extension to the extension manager. This be effective when we prepare a tutorial video on the use of the extension.

There are still standard features (e.g., volumetry computation) and new research features (e.g, risk maps visualization, new planning algorithms) that we would like to implement in future Project Weeks.


# Background and References
1. [Slicer-Liver PW37](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/Slicer-Liver) (July 2022)
1. [Slicer-Liver PW36](https://github.com/NA-MIC/ProjectWeek/tree/master/PW36_2022_Virtual/Projects/Slicer-Liver) (January 2022)
1. [Slicer-Liver PW35](https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/Slicer-Liver) (June 2021)
1. [NorMIT-Plan at NA-MIC project week](https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/NorMIT-Plan/) (january 2020)
1. [NorMIT-Plan at NA-MIC project week](https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerLiverAnalysis/) (December 2020)
1. Palomar, Rafael, et al. "A novel method for planning liver resections using deformable Bézier surfaces and distance maps." Computer Methods and Programs in Biomedicine 144 (2017): 135-45.
1. Palomar, Rafael, et al. "Surface reconstruction for planning and navigation of liver resections." Computerized Medical Imaging and Graphics 53 (2016): 30-42.
