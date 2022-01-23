Back to [Projects List](../../README.md#ProjectsList)

# Slicer-Liver

## Key Investigators

- Rafael Palomar (Oslo Unviersity Hospital/NTNU, Norway)
- Gabriella d'Albenzio (Oslo University Hospital, Norway)
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

![3D Bezier Surface Markup](screenshot.png)

[Early prototype of the resection planning module](https://youtu.be/7M3DULQp81k)

## Objectives

1. Integrate the components developed during the [last
   ProjectWeek](https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/Slicer-Liver
   "Slicer-Liver in the last ProjectWeek") in a resection planning working prototype. 

2. Add a Slicer module for computation of liver vascular territories.

## Approach and Plan

### Liver resection planning module

1. Integration of resection deformation and resection initialization.
1. Add complex interactions (move groups of control points).
1. Adding load/saving functionality.
1. Development of distance measurements visualized in the resections using shaders.
1. Add a GUI to manage resections.

### Liver analysis module

1. Creation of a new Slicer module.
1. Implementation of end-points placement (markups).
1. GUI to manage segments (add, remove, edit).
1. Loading/saving vascular territories.

## Illustrations

![3D Bezier Surface Markup](bezier_surface_markup.png)

![Resection initialization](resection_initialization.png)

![Resection planning](resection_planning.png)

## Progress and Next Steps

During Project Week, we have been able to add *real-time computation of safety
margins* to our resection planning module, as well as create a new module for
*computation of vascular territories*

[![Alt text](https://img.youtube.com/vi/--dIcE97RVQ/0.jpg)](https://www.youtube.com/watch?v=--dIcE97RVQ)

Our next step is to work on the user interface and the loading/saving
functionality needed to make this a complete Slicer extension.

# Background and References
1. [Slicer-Liver PW35](https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/Slicer-Liver
   "Slicer-Liver in the last ProjectWeek") (June 2021)
1. [NorMIT-Plan at NA-MIC project week](https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/NorMIT-Plan/) (january 2020)
1. [NorMIT-Plan at NA-MIC project week](https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerLiverAnalysis/) (December 2020)
1. Palomar, Rafael, et al. "A novel method for planning liver resections using deformable Bézier surfaces and distance maps." Computer Methods and Programs in Biomedicine 144 (2017): 135-45.
1. Palomar, Rafael, et al. "Surface reconstruction for planning and navigation of liver resections." Computerized Medical Imaging and Graphics 53 (2016): 30-42.
