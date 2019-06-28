Back to [Projects List](../../README.md#ProjectsList)

# Slicer Extensions with CUDA

## Key Investigators

- Greg Sharp (MGH)
- JC Fillion-Robin (Kitware, Inc.)

# Project Description

Provide an easy path for distributing extensions that use CUDA.

## Objective

1. Get CUDA installed on build machine?
1. Test using CUDAprobe extension

## Approach and Plan

1. Start with CUDAprobe extension created last year
   1. https://github.com/gregsharp/Slicer-CUDAProbe

## Progress and Next Steps

1. Review compatibility of CUDA versions with respect to build machines
    - https://discourse.slicer.org/t/cuda-version-for-build-machines/7298
1. Sample extension updated and pull request created
    - https://github.com/Slicer/ExtensionsIndex/pull/1648
1. Add CUDA install recommendations to factory build page
    - https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory
1. Update linux docker instructions to download and install CUDA
    - https://github.com/Slicer/SlicerBuildEnvironment/pull/12/commits/4ec466f0cd78a2775dddc4818372b786e3819e24

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
