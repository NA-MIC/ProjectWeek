Back to [Projects List](../../README.md#ProjectsList)

# Interoperability of DICOM SEG between cornerstonejs/vtkjs/dcmjs

## Key Investigators

- James A. Petts (ICR)
- Erik Ziegler (Radical Imaging)
- Steve Pieper (Isomics)

# Project Description

This project aims to work on interoperability of DICOM SEG within the cornerstonejs and vtkjs frameworks,
utilizing dcmjs for IO. This project is the logical continuation of [a previous Project Week project](https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/dcmjs-cornerstone/)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Visualization of DICOM SEG segmentation data in both cornerstonejs and vtkjs frameworks.
2. Provide easy interoperability between segmentations visualized using both libraries.
3. Provide an example implementation as plugins to the OHIF viewer, utilizing both cornerstonejs and vtkjs.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Build an easy to use, fast interface for loading DICOM SEG into native cornerstone brush annotation format.
2. Build a bridge between the cornerstoneTools canvas, and vtkjs methods of rendering.
3. Implement an example in a fully fledged web viewer (OHIF Viewer), such that annotations in a vtkjs-enabled window automagically display the relevant cornerstoneTools data related to that series in an appropriate fashion.
4. Bonus goal: use vtkjs to show real-time 3D visualization of the SEG

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
* DICOM SEG display in vtkjs: https://dcmjs-org.github.io/dcmjs/examples/vtkDisplay/index.html
* DICOM SEG display in cornerstone: https://dcmjs-org.github.io/dcmjs/examples/displaySegmentation/index.html
