Back to [Projects List](../../README.md#ProjectsList)

# SlicerDMRI internals modernization: display and i/o refactoring

## Key Investigators

- Isaiah Norton (BWH)
- Lauren O'Donnell (BWH)

# Project Description

## Objective

1. Eliminate remaining dependencies in Slicer core for fiberbundle and DTI volume rendering, to simplify both Slicer core
   and SlicerDMRI maintenance and refactorability.
2. Investigate accessibility of __distributable__ Python dependencies for WhiteMatterAnalysis and `Ni-*` (i/o, diffusion, BIDS?) integration.

## Approach and Plan

- Objective 1:
  - Remove remaining DMRI display-related code from Slicer core
  - Remove remaining DMRI i/o code from Slicer core
- Objective 2:
  - Test pip installation of dependency list in Qt5/VS2015 Slicer on Windows and Mac
  - Discuss with Jc and other contributors 

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->
<!--
![Description of picture](Example2.jpg)

![Some more images](Example2.jpg)
-->
# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: <https://github.com/SlicerDMRI/SlicerDMRI>
- Documentation: <https://dmri.slicer.org>

<!--Link for editing page when displayed in GitHub pages-->
<a href="{{site.github.repository_url}}/edit/master/{{page.path}}">Edit this page on GitHub</a>
