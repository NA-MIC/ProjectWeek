Back to [Projects List](../../README.md#ProjectsList)

# Conversion of Matlab Bridge modules to integrated 3DSlicer modules

## Key Investigators

- Sharon Peled (Brigham and Women’s, USA)
- Andras Lasso (Queen’s University, Canada)
- Anyone else that is interested

# Project Description

Matlab Bridge is a very quick and convenient way to combine the display features of 3DSlicer with Matlab analysis code. A straightforward way of exporting Matlab modules to Python and incorporation of the code in 3DSlicer may allow Matlab programmers to make their modules available to the Slicer community.

## Objective

- Create tutorial about the process of translating a Matlab Bridge module to a Slicer Python scripted module.

## Approach and Plan

1. Investigate freeware to convert Matlab code to Python.
1. Document a complete pipeline for Matlab-proficient non-developers on the process of creating a Python module.

## Progress and Next Steps
<!--Describe progress and next steps in a few bullet points as you are making progress.-->
Progress
- A couple of examples of Matlab Bridge modules with all their dependent functions were collected here:
https://www.dropbox.com/sh/36vvhsi90z90arq/AACTInsRPBkQdhaH8jf_qml9a?dl=0

- It was concluded that conversion needs to be done manually - Matlab to Python converters would not work well for this purpose.
- The tutorial “Programming in Slicer4” by Sonia Pujol and Steve Pieper (https://www.dropbox.com/s/wrhrvvmplosiis1/Slicer4_ProgrammingTutorial_SPujol-SPieper_Nightly.pdf?dl=0#)
was worked through and summarized in the following document for quick reference: https://www.dropbox.com/s/0wukoaesndf3ug4/SlicerPython.pdf?dl=0

Next steps:
- Add a summary of the tutorial “Developing and contributing extensions for 3D Slicer” by Andrey Fedorov, Jean-Christophe Fillion-Robin, and Steve Pieper (https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g420896289_0216) to the document.

- Summarize essential Python for Matlab users and add to the document.

https://bastibe.de/2013-01-20-a-python-primer-for-matlab-users.html

https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html

- Convert the example Matlab Bridge modules to Python and add a two column comparison of the Python code versus the Matlab code to the document.

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

<!--
- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
-->
