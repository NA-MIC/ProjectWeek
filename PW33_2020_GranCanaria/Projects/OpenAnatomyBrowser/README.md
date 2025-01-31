Back to [Projects List](../../README.md#ProjectsList)

# Open Anatomy Browser in vtkjs

## Key Investigators
- Michael Halle (BWH)
- my smart, experienced, and generous colleagues from across the globe (various)

# Project Description
The Open Anatomy Browser (http://openanatomy.org) is a useful tool for visualizing anatomy atlases and Slicer output. However, the current browser was only intended as a prototype and cannot display many current Slicer scenes. This project will create a new browser prototype based on vtkjs, with ITK image readers.

## Objective
Make the Open Anatomy atlas browser more user friendly and more compatible with the Slicer data and software ecosystem.

## Approach and Plan
1. Display an Open Anatomy atlas in vtkjs.
1. Create a bare React-based application around the render window.
1. Work out coordinate systems and Slicer export.
1. Plan for glTF support.
1. Build out the rest of the user interface.
1. Extend atlas format to deal with scenes.
1. Lock down an API for parsing Open Anatomy scenes.

## Progress and Next Steps
1. Better understanding of common problems between React apps and vtkjs.
1. Understanding of coordinate system mismatch between volumes and models (RAS models), will fix this problem going forward.
1. Provided Andras with latest TA2 draft metadata for labeling atlases.
1. Discussed translation of TA2 to Spanish with Juan Andres.
1. Worked on a preliminary export format for metadata from Slicer.
1. Gained user feedback about metadata uses and atlas viewer needs.

# Illustrations
<img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW33_2020_GranCanaria/Projects/OpenAnatomyBrowser/oa-vtkjs-prostate.jpg" />
<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References
https://openanatomy.org
