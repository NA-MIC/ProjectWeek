Back to [Projects List](../../README.md#ProjectsList)

# Markups redesign and new markups for curve, line, and angle measurement

## Key Investigators

- [Davide Punzo](http://www.davidepunzo.com/) (remotely)
- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- Sara Rolfe (University of Washington, USA)
- [Kyle Sunderland](http://perk.cs.queensu.ca/users/sunderland) (Queen's University, Canada)
- Jean-Christophe Fillion-Robin (Kitware)
- Steve Pieper (Isomics)

# Project Description

## Objective

- Fix all issues and improve markup fiducial points widgets
- Add angle, line, and curve widgets

## Approach and Plan

Complete redesign of markups is needed, due to high complexity and low performance of current implementation. The main change is that we give up on relying on widgets provided by VTK, as they use unnecessarily complex, inconsistent design, extremely slow, and lack essential features. See more information on the [Markups improvements Slicer labs page](https://slicer.org/wiki/Documentation/Labs/Improving_Markups).

The new infrastructure relies on:
- storing all data in standard VTK data objects, which are stored in MRML nodes and directly shared between widgets
- widgets are rendered using hardware accelerated glyph filter
- one (or few) VTK actor for each widget (not adding a new actor for each markup point as before)

Plan is to integrate the reworked markups infrastructure and new markups during the project week then continuously fix issues and add the numerous planned features.

## Progress and Next Steps

- Davide Punzo has reworked markup point list widget:

  [Pull request](https://github.com/Slicer/Slicer/pull/1079) 
  
  [Points video](https://www.dropbox.com/s/p8v1m7mgopsnrp4/Widget-rework.mkv?dl=0)
  
  and added angle, line, and curve widgets.
  
  [Open Curve video](https://www.dropbox.com/s/ap67lmxo0xh77h0/OpenCurve.mkv?dl=0)
 
### Result

- To be completed

# Illustrations

  ![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/Line.png)
  ![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/Angle.png)
  ![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/OpenCurve.png)
  ![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/ClosedCurve.png)

<!--

| Philips 3D US | Chroma-depth in PRISM | Depth peeling in PRISM |
| --- | --- | --- |
| ![](../../../PW28_2018_GranCanaria/Projects/MultiVolumeRendering/matt-jolley-us.png) | ![](../../../PW28_2018_GranCanaria/Projects/MultiVolumeRendering/chroma-depth-crop.png) | ![](../../../PW28_2018_GranCanaria/Projects/MultiVolumeRendering/depth-peeling-crop.png) |

-->

# Background and References

- [Labs page](https://slicer.org/wiki/Documentation/Labs/Improving_Markups)
- [Previous discussions](https://discourse.slicer.org/t/markups-for-angle-line-and-closed-open-spline/4729)
- [Draft implementation from vovythevov](https://github.com/Slicer/Slicer/pull/1010)
