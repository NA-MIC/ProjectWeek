Back to [Projects List](../../README.md#ProjectsList)

## SimpleElastix Slicer Integration

## Key Investigators
- Patrick Carnahan (Robarts Research Institute)


# Project Description
Modify the SimpleElastix project to seperate it from the SimpleITK build and instead use SimpleITK as a SuperBuild dependency.
SimpleElastix could then potentially be integrated into the SlicerElastix module to allow direct use of the Elastix registration filters from python.

## Objective
1. Complete build configuration work to enable standalone python wrapping of elastix filters
1. Integrate building of SimpleElastix fork into SlicerElastix to allow for easy use within Slicer


## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
- Removed all SimpleITK duplicate code from SimpleElastix
- Modified Swig configurations to allow dependency on SimpleITK
- SimpleElastix imported into Slicer and useable for registration
- Next steps are to work with core SimpleElastix developer on upstreaming the changes

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/pcarnah/SimpleElastix
- Documentation: TODO
