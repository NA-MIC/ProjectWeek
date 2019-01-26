Back to [Projects List](../../README.md#ProjectsList)

# Slicer Case Iterator

## Key Investigators

- Joost van Griethuysen (The Netherlands Cancer Institute)
- Steve Pieper (Isomics)

# Project Description

This project aims to expand the usage of Slicer Case Iterator to work with DICOM(WEB) backend to support workflows where the data is available in DICOM format.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Generalize internal batch definition to allow different input modes (CSV, DICOM)
1. Link to Slicers DICOM browser to retrieve images
1. Implement prefetching of next n cases to speed up processing
1. Store segmentation results as DICOM SEG objects

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Create class implementing generator to hold batch, with different input methods a inherited subclasses
1. Talk to Slicer developers on how to best approach this (what kind of identifiers, methods to use, etc.)
1. Closely related to point above. Investigate on how to analyze input to determine best conversion step, how to store results of this evaluation.
1. Talk to Slicer developers on how to store a Slicer Segmentation object as DICOM SEG object (when input image is DICOM format)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Nothing yet

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- [Slicer Case Iterator source code](https://github.com/JoostJM/SlicerCaseIterator)
