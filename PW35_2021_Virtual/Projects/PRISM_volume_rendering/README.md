Back to [Projects List](../../README.md#ProjectsList)

# PRISM Volume Rendering

## Key Investigators

- Simon Drouin, ETS Montreal
- Steve Pieper, Isomics, Cambridge MA, USA
- Kyle Sunderland, PerkLab, Queen’s University, Canada 
- Andrey Titov, ETS Montreal
- Rafael Palomar, Oslo University Hospital / NTNU, Norway


# Project Description

The goal of this project is to enable the development of advanced 3D rendering techniques in Slicer. The goal is to facilitate access to GPU shaders and enable GPU-based filtering in Slicer by improving shader access multipass rendering in VTK and Slicer. The [PRISM Module](https://github.com/ETS-vis-interactive/SlicerPRISMRendering) in Slicer will serve as a test environment for the new capabilities.

## Objective

1. Facilitate the development and debugging of GPU shaders for Slicer
2. Extend the principles introduced in the PRISM module to surface rendering and other types of rendering
3. Integrate work by Kyle Sunderland on VTK GPU image filters (see branch [here](https://github.com/Sunderlandkyl/VTK/commits/vtkGPUImageFilter3)) so that the filters are usable in Slicer
4. Integrate GPU filters with volume rendering in such a way that filtered volumes do not have to be transfered back to CPU memory before rendering 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. TODO
1. ...
1. ...

# Illustrations

![Opacity Peeling](opacity-peeling.gif)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
- PRISM Module [GitHub repository](https://github.com/ETS-vis-interactive/SlicerPRISMRendering).
- [Original article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0193636) about the PRISM framework that served as a basis to develop the PRISM module in Slicer
- Previous project weeks
  - https://projectweek.na-mic.org/PW30_2019_GranCanaria/Projects/GLSLShaders/
  - https://projectweek.na-mic.org/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/
  - 
