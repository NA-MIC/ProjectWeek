Back to [Projects List](../../README.md#ProjectsList)

# Programmable MultiVolume Rendering Project

## Key Investigators

- Simon Drouin (MNI)
- Csaba Pinter (Queen's)
- Steve Pieper (Isomics)
- Jean-Christophe Fillion-Robin (Kitware)


# Project Description

## Objective

* Review the newly exposed GLSL hooks in VTK as a mechanism to add features to Slicer's Volume Rendering 
* Possible features to explore
  * Optimized performance/quality for multiple overlapping volumes
  * Custom clipping or other rendering features
  * Adding nonlinear deformations

## Approach and Plan

* Review what's new since we [discussed this last year](https://na-mic.org/wiki/Project_Week_25/Next_Generation_GPU_Volume_Rendering)
  * New VTK version and classes
  * New Slicer GUI
  * Other GLSL examples that we can draw from
    * IBIS / PRISM
    * STEP
* Document existing functionality in the VTK wiki on [this page](https://www.vtk.org/Wiki/VTK/ProgrammableMultiVolumeRendering) and identify potential builtin variables and functions that could be added to facilitate the creation of new volumetric effects.
* Replicate the examples presented in the PRISM paper using the improved VTK mapper.
* Replicate the US heart rendering of Philips machine with data from Matt Joley.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations
<!--Add pictures and links to videos that demonstrate what has been accomplished.-->
Philips 3D US             |  Chroma-depth in PRISM
:-------------------------:|:-------------------------:
![jolley-us](matt-jolley-us.png) | ![chroma-depth](chroma-depth-crop.png)
Depth peeling in PRISM | Edge enhancement in PRISM
![](depth-peeling-crop.png) | ![](edge-and-shading.png)
Decluttering in PRISM | Volume carving in PRISM
![](decluttered-crop.png) | ![](volume-carving-crop.png)
Blood flow animation in PRISM | 
![](flow-illustration-crop.png) | 

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [PRISM Paper](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0193636)
- [STEP multivolume deformable rendering (in WebGL)](https://www.youtube.com/watch?v=8dputUoKBTA)
- [Mulitple volume rendering in Slicer 3.6](https://www.slicer.org/wiki/Modules:VolumeRendering-Documentation-3.6)
