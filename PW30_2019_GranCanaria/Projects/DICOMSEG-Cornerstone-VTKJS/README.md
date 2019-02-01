Back to [Projects List](../../README.md#ProjectsList)

# Interoperability of DICOM SEG between cornerstonejs/vtkjs/dcmjs

## Key Investigators

- James A. Petts (ICR)
- Erik Ziegler (Radical Imaging)
- Steve Pieper (Isomics)
- Mete Akdogan (Stanford)
- Emel Alkim (Stanford)
- Tobias Stein (DKFZ)
- Jasmin Metzger (DKFZ)
- Forrest Li (Kitware)
- Markus Herrmann (MGH & BWH CCDS)

# Project Description

This project aims to work on interoperability of DICOM SEG within the cornerstonejs and vtkjs frameworks,
utilizing dcmjs for IO. This project is the logical continuation of [a previous Project Week project](https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/dcmjs-cornerstone/)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Visualization of DICOM SEG segmentation data in both cornerstonejs and vtkjs frameworks. This will also facilitate cornerstone integration with ePAD.
2. Provide easy interoperability between segmentations visualized using both libraries.
3. Provide an example implementation as plugins to the OHIF viewer, utilizing both cornerstonejs and vtkjs.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Build an easy to use, fast interface for loading DICOM SEG into native cornerstone brush annotation format.
2. Build a bridge between the cornerstoneTools canvas, and vtkjs methods of rendering.
3. Implement an example in a fully fledged web viewer (OHIF Viewer), such that annotations in a vtkjs-enabled window automagically display the relevant cornerstoneTools data related to that series in an appropriate fashion.
4. Bonus goal: use vtkjs to show real-time 3D visualization of the SEG

## Progress

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Added adapters to `dcmjs` that wrap the `Segmentation` class for easy IO in `Cornerstone`. These adapters switch between `cornerstoneTools` formated data and DICOM SEG, without adding `Cornerstone` as a dependency for `dcmjs`. Only binary SEGs for now.
2. Built a bridge in a simple example viewer that shares a common buffer for segmentation data between `Cornerstone` and `vtkjs` viewports.
3. Synced interactive painting of segmentation data (labelmap) between `Cornerstone` and `vtkjs`.
4. We have 3D visualisation of the the SEG leveraging `vtkjs`, rendering the shared `vtkjs`/`Cornerstone` seg buffer.

# Next Steps
1. Make sure the SEG adapters can handle edge cases, including common, but interpretable abuse and/or violation of the standard e.g.:
- abuse: "fractional" SEGs which only have min and max value, 0 and 255, effectively being binary SEGs wasting 8x the storage.
- violation: "binary" SEGs which contain fractional data.
1. Finish the `vtkjs` SEG adapters.
3. Further develop the OHIF plugin framework and incorporate the progress we made on syncronisation.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
* [Segmentation Review System](https://drive.google.com/file/d/1NXiu18mCFXrIaEgQ1WdzBbmq9igIyZNN/view?usp=sharing) (Tobias Stein @DKFZ)
This is showing an examplary application using DICOM SEG in two cornerstone viewers and DICOM Parametric Map overlay above standard DICOM image data using dcmjs and cornerstoneTools. At the end also DICOM SR data is used to show calculated metrics of the segmentation evaluation.
At the moment the upcoming React components are not used, but this would be a great use case.
* [Import of DICOM SEG to `Cornerstone`/OHIF](https://gfycat.com/FakeEasyHuemul).
This shows a `Cornerstone` viewport rendering segmentation data imported from a DICOM SEG.
* [`Cornerstone`/`vtkjs` synchronisation and data harmonization](https://gfycat.com/HalfBowedFrenchbulldog).

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
* DICOM SEG display in vtkjs: https://dcmjs-org.github.io/dcmjs/examples/vtkDisplay/index.html
* DICOM SEG display in cornerstone: https://dcmjs-org.github.io/dcmjs/examples/displaySegmentation/index.html
