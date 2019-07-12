Back to [Projects List](../../README.md#ProjectsList)

## SimpleElastix Slicer Integration

## Key Investigators
- Patrick Carnahan (Robarts Research Institute) 


# Project Description
Modify the SimpleElastix project to seperate it from the SimpleITK build and instead use SimpleITK as a SuperBuild dependency.
SimpleElastix should then be integrated into the SlicerElastix module to allow direct use of the Elastix registration filters from python.

## Objective
1. Complete build configuration work to enable standalone python wrapping of elastix filters 
1. Integrate building of SimpleElastix fork into SlicerElastix to allow for easy use within Slicer


## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
- Removed all SimpleITK duplicate code from SimpleElastix
- Modified Swig configurations to allow dependency on SimpleITK
- Need to finish CMake clean up to fully seperate SimpleElastix and remove leftover SimpleITK configuration info

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/pcarnah/SimpleElastix
- Documentation: TODO


