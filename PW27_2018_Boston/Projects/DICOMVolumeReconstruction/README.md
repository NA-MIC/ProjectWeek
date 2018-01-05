Back to [Projects List](../../README.md#ProjectsList)

# DICOM volume reconstruction tools

## Key Investigators

- Andrey Fedorov (BWH)
- Andrew Beers (MGH)
- Joost van Griethuysen (NKI)
- Steve Pieper (Isomics)

# Project Description

## Objective

A common task in medical image analysis is to convert the DICOM image series into a 3d volume that is suitable for the analysis using ITK, deep learning studies, etc. The goal of this project is to summarize, discuss, and evaluate various publicly available tools that exist for this task.

Initially, we want to focus on the very narrow task of converting a scalar volume image series.

## Approach and Plan

1. Identify the list of requirements: what kind of data should be acceptable
1. Compile the list of tools suitable for this task. Include main features of the tool: language, license, support/history of development, pros and cons, ...
1. Collect feedback from the community - what tool do you use? what issues have you encountered? do you feel like you have a solution that is working reliably?
2. Compile a list of representative datasets, discuss approaches that could be used to evaluate a tool.

## Progress and Next Steps

### Tools

#### 3D Slicer DICOM ScalarVolumePlugin

[https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py
](https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py)

#### dcm2niix

[https://github.com/rordenlab/dcm2niix](https://github.com/rordenlab/dcm2niix)

#### dicom2nifti

[https://github.com/icometrix/dicom2nifti](https://github.com/icometrix/dicom2nifti)

#### dcmstack

[https://github.com/moloney/dcmstack](https://github.com/moloney/dcmstack)

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

#### vtk-dicom/dicomtools/dicomtonifti

[https://github.com/dgobbi/vtk-dicom](https://github.com/dgobbi/vtk-dicom)

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

# Background and References

* Clunie D. How Thick am I? The Sad Story of a Lonely Slice. 2013. http://dclunie.blogspot.com/2013/10/how-thick-am-i-sad-story-of-lonely-slice.html. Accessed January 5, 2018.
