Back to [Projects List](../../README.md#ProjectsList)

# Extending DICOM-SR support in dcmjs and adding test cases

## Key Investigators

- Emel Alkim (Stanford University)
- Steve Pieper (Isomics)
- Andrey Fedorov (Brigham and Women's Hospital, Boston)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Identify gaps in dcmjs for reading/writing DICOM-SR
1. Add support for freehand and segmentation
1. Convert AIM to DICOM-SR and DICOM-SR to AIM and show interoperability between ePAD, OHIF and Slicer 3D

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Find some test data and generate test cases for Length and Bidirectional
1. Find some segmentation and/or freehand DICOM-SRs, convert to AIM and back
1. Complete freehand and segmentation implementations and add test cases

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. dcmjs already hsa full implementation for Length and Bidirectional
1. aimapi has the draft implementation on for the conversion of AIM to DICOM-SR and back
1. Got test data from Andrey ([https://www.dropbox.com/s/98rylgt25b2sm9r/planar_annotations.zip?dl=0]). 
- The sample has 1 prostate, one lung.
- They have SCOORD and SCOORD3D instead of measurements to identify polyline and point respectively. dcmjs support is dependent on the measurement existance
- for point dcmjs point object expects a CONTAINS:NUM:center => inferred from: SCOOR3D: point structure, whereas the sample point has CONTAINS:SCOORD3D:Image Region
- for polyline (bounding box), dcmjs has no measurement support implemented for freehand. biridectional implemetation is like CONTAINS:NUM:LongAxis => INFERRED FROM: SCOORD: POLYLINE whereas the sample has CONTAINS:COORD:Image Region=POLYLINE => SELECTED FROM: IMAGE

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
1. dcmjs library https://github.com/dcmjs-org/dcmjs
1. aimapi library https://github.com/RubinLab/aimapi-js
