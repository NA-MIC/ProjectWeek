Back to [Projects List](../../README.md#ProjectsList)

# Build latest VTK with Slicer

## Key Investigators

- Csaba Pinter (EBATIN, S.L., Pixel Medical Inc.)
- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- Jean-Christophe Fillion-Robin (Kitware)

# Project Description

Slicer is currently stuck on an old version of VTK (2018/10), which prevents us from making progress with various developments. It is important to make Slicer compatible with the new build structure in VTK 8.90 to enable further progress. This is also critical for the [Slicer 5](https://github.com/NA-MIC/ProjectWeek/blob/master/PW33_2020_GranCanaria/Breakouts/Slicer5/README.md) release.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Have a successful Slicer build with VTK 8.90

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Start from Andras' [work-in-progress](https://github.com/Slicer/Slicer/pull/1252) [branch](https://github.com/lassoan/Slicer/tree/build-with-vtk89)
1. Continue from there...

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Rebase to latest Slicer
1. [Fix](https://github.com/cpinter/CTK/tree/build-with-vtk89) CTK errors
1. [Fix](https://github.com/cpinter/MultiVolumeExplorer/tree/build-with-vtk89) MultiVolumeExplorer errors
1. [Fix](https://github.com/cpinter/Slicer/tree/build-with-vtk89) some of the errors in Slicer

# Illustrations

```diff
- Lots of red text in output
- More red text in output
- Lots of red text in output
- More red text in output
- Lots of red text in output
- More red text in output
- Lots of red text in output
- More red text in output
- Lots of red text in output
- More red text in output
```

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
