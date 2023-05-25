Back to [Projects List](../../README.md#ProjectsList)

# Slicer-Liver

## Key Investigators

- Rafael Palomar (Oslo Unviersity Hospital/NTNU, Norway)
- Gabriella d'Albenzio (Oslo University Hospital, Norway)
- Ruoyan Meng (NTNU, Norway)
- Ole Vegard Solberg (SINTEF, Norway)
- Geir Arne Tangen (SINTEF, Norway)
- Javier Pérez de Frutos (SINTEF, Norway)

# Project Description

This project will continue the development of the *Slicer-Liver* extension
that will be developed through the [ALive project](https://alive-research.no).
The objective of the Slicer-Liver extension is to provide researchers
with tools to perform liver analytics towards planning of liver interventions
(resections, ablations). At this point in the project we need to port early
prototypes of our resection planning algorithms into 3D Slicer.

## Objectives

   - Liver resection planning:
   
      1. Integration of volumetric analysis for resections
      2. Improve the UI for managing resections
     
   - Computation of vascular territories:
   
      1. Calculation of vascular liver-segments based on multiple vascular systems (hepatic arterial/vein, portal vein) 
      2. Structuring of data for the liver module – implementing object hierarchy
      3. Storing and reloading of module data
      4. User-friendly GUI for liver module – optimize for clinical use.

## Approach and Plan

For this Project week we will build on the advances obtained in the las project
week. Some of the objectives are based on new functionality that has been tested
but not integrated yet, while some other objectives are refinement of
functionality previusly integrated in [Slicer-Liver
PW36](https://github.com/NA-MIC/ProjectWeek/tree/master/PW36_2022_Virtual/Projects/Slicer-Liver
 
## Illustrations

<img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_01.png?raw=true" width="50%">

<img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_02.png?raw=true" width="50%">

<img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_04.png?raw=true" width="50%">

<img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_06.png?raw=true" width="50%">

<img src="https://github.com/ALive-research/Slicer-Liver/blob/master/Screenshots/Slicer-Liver_screenshot_08.png?raw=true" width="50%">

## Progress and Next Steps

In this project week, we have changed the user interaction to use segmentations instead of models, which greatly simplifies the user interaction.

There is a PR for adding this extension to the extension manager. This be effective when we prepare a tutorial video on the use of the extension.

There are still standard features (e.g., volumetry computation) and new research features (e.g, risk maps visualization, new planning algorithms) that we would like to implement in future Project Weeks. 

# Background and References
1. [Slicer-Liver PW36](https://github.com/NA-MIC/ProjectWeek/tree/master/PW36_2022_Virtual/Projects/Slicer-Liver) (January 2022)
1. [Slicer-Liver PW35](https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/Slicer-Liver) (June 2021)
1. [NorMIT-Plan at NA-MIC project week](https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/NorMIT-Plan/) (january 2020)
1. [NorMIT-Plan at NA-MIC project week](https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerLiverAnalysis/) (December 2020)
1. Palomar, Rafael, et al. "A novel method for planning liver resections using deformable Bézier surfaces and distance maps." Computer Methods and Programs in Biomedicine 144 (2017): 135-45.
1. Palomar, Rafael, et al. "Surface reconstruction for planning and navigation of liver resections." Computerized Medical Imaging and Graphics 53 (2016): 30-42.
