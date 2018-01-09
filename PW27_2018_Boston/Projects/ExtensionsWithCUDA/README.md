Back to [Projects List](../../README.md#ProjectsList)

# Slicer Extensions with CUDA

## Key Investigators

- Greg Sharp (MGH)
- Adam Rankin (Robarts)
- JC Fillion-Robin (Kitware, Inc.)

# Project Description

Provide an easy path for distributing extensions that use CUDA.

## Objective

1. What work needs done to get CUDA installed on build machine?
1. How can we test the resulting packages?

## Approach and Plan

1. Create sample CUDA extension
   1. Create simple CUDA extension "Slicer CUDA Probe"
   1. Perform manual build, upload, and test 
      1. https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions
      1. https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex
1. Set up VM that matches factory, but with CUDA installed
   1. Create VM, install dev tools to match factory
      1. https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory
   1. Set up factory build of slicer
   1. Create extension index
      1. https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Contribute_Extension_Description_File
   1. Set up dashboard-driven compile
      1. https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/DashboardSetup
   1. Do I need a separate extension server?


## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.

![Description of picture](Example2.jpg)

![Some more images](Example2.jpg)
-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.
- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
-->

