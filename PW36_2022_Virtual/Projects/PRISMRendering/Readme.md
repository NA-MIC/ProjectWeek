Back to [Projects List](../../README.md#ProjectsList)

# PRISM Volume Rendering

## Key Investigators

- Simon Drouin, ETS Montreal
- Steve Pieper, Isomics, Cambridge MA, USA
- Andrey Titov, ETS Montreal
- Rafael Palomar, Oslo University Hospital / NTNU, Norway

# Project Description

The goal of this project is to enable the development of advanced 3D rendering techniques in Slicer. The goal is to facilitate access to GPU shaders and enable GPU-based filtering in Slicer by improving shader access multipass rendering in VTK and Slicer. The [PRISM Module](https://github.com/ETS-vis-interactive/SlicerPRISMRendering) in Slicer will serve as a test environment for the new capabilities.

## Long-term Objective

1. Facilitate the development and debugging of GPU shaders for Slicer
2. Extend the principles introduced in the PRISM module to surface rendering and other types of rendering
4. Integrate GPU filters with volume rendering in such a way that filtered volumes do not have to be transfered back to CPU memory before rendering 
5. Explore custom rendering to simplify integration with the vtk render process.  Prior work includes:
  * Python scripted Actor/Mappers: https://www.slicer.org/wiki/Slicer3:Python:ScriptedActor
  * SimpleMapper: https://github.com/IbisNeuronav/Ibis/tree/master/IbisVTK/vtkExtensions

## PW36 Objective

1. Enable opening shaders with tags in a text editor while running Slicer (Previous efforts by Simon Drouin were made to facilitate shader debugging. Code is available in [this branch](https://gitlab.kitware.com/drouin-simon/vtk/-/tree/volume-shader-readability).
1. Move vtkShaderProperties to the vtkMRMLDisplayNode level to allow usage with surface shaders too.
1. Integrate work by Kyle Sunderland on VTK GPU image filters (see branch [here](https://github.com/Sunderlandkyl/VTK/commits/vtkGPUImageFilter3)) so that the filters are usable in Slicer

## Progress and Next Steps

# Illustrations

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
- PRISM Module [GitHub repository](https://github.com/ETS-vis-interactive/SlicerPRISMRendering).
- [Original article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0193636) about the PRISM framework that served as a basis to develop the PRISM module in Slicer
- Previous project weeks
  - [PW35](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PRISM_volume_rendering/)
  - [PW30](https://projectweek.na-mic.org/PW30_2019_GranCanaria/Projects/GLSLShaders/)
  - [PW28](https://projectweek.na-mic.org/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/)
