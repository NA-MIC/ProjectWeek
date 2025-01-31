Back to [Projects List](../../README.md#ProjectsList)

# Slicer 5++ : Roadmap forward for 3D Slicer

## Key Investigators

- Sam Horvath (Kitware Inc.)
- Andras Lasso (Queen's University, Kingston, Canada)
- Steve Pieper (Isomics Inc., Cambridge, MA, USA)
- Jean-Christophe Fillion-Robin (Kitware Inc.)

# Project Description

During this project week, we would like to discuss a *broad* roadmap for major features and changes to Slicer between now and Slicer 6

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Develop that starting point of the Slicer 6 roadmap

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Discussion!
    - Had breakout session Wed @ 2pm
1. Should Qt6 = Slicer 6?

## Working Roadmap

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
1. Long term (Slicer 6 to be released in ~3 years)
    1. Modularization ("pip install slicer")
        - Heavily dependent on improved VTK remote module support
        - Exampe of current progress with VTK remote modules can be found in [SlicerLookingGlass](https://github.com/Kitware/LookingGlassVTKModule)
        - This modularization will support 3D Slicer cloud projects as well as simplifying the build system
    1. Distributing a Slicer SDK
        - Allowing development on C++ modules without building all of Slicer
        - We have been working on making VTK SDKs [available](https://vtk.org/files/wheel-sdks/)
    1. Ability to update an installed Slicer version
    1. Laying the groundwork for hybrid desktop / web Slicer applications
1. Short term (Slicer minor releases in the next year)
    1. Using oriented image data support already available in VTK
    1. Extension auto updates (already available for preview)
    1. Expanding language support
    1. Improved volume display mechanism
        - Volume behavior is inconsistent for show/hide compared to other data
    1. Qt 6 transition
        - Qt 6 support already in VTK upstream
        - ALso look at Pyside6 transition
    1. Investigate using libraries (openslide, etc) to support smooth viewing of larger images

## Next steps

1. Transition this roadmap to Slicer GitHub wiki
2. Begin hacking!


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- [Slicer 5 Roadmap](https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap)
- [3D Slicer Roadmap](https://github.com/Slicer/Slicer/wiki/Roadmap)
- [Slicer 6 Roadmap notes](https://docs.google.com/document/d/1X3Lv5yNBxViB-dMEYjEaw1g9825mlEVH-8R40jGSnJQ/edit?usp=sharing)
