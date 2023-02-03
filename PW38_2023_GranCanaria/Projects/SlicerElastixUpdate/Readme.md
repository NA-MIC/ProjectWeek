Back to [Projects List](../../README.md#ProjectsList)

# SlicerElastix: update elastix version

## Key Investigators

- Simón Oxenford (Charité Berlin)
- Andras Lasso (Queen's University)

# Project Description

<!-- Add a short paragraph describing the project. -->
Elastix recently released a new version [(5.1.0)](https://github.com/SuperElastix/elastix/releases/tag/5.1.0) which allows specifying an ITK file format for transformation output files file.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
The idea is to update SlicerElastix to use this new version and use itk transforms throughout the module.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Locally tested the new elastix version with itk transforms (MacOS).
1. Made a PR to the SlicerElastix repo with proposed changes. [GH PR](https://github.com/lassoan/SlicerElastix/pull/37)

Next steps:

1. Test build for other OSs.
1. Leverage upon the itk transform use to include other features (using initial transform).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

![BSpline registration output](Picture1.png)


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- This fixes some issues when loading Elastix BSpline transforms. [GH issue](https://github.com/lassoan/SlicerElastix/issues/33)
