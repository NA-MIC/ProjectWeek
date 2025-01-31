Back to [Projects List](../../README.md#ProjectsList)

## SlicerMitralValve

## Key Investigators
- Patrick Carnahan (Robarts)

# Project Description
This extension contains a collection of tools for aiding in patient-specific mitral valve modelling. Currently consists of components for registering bi-plane colour ultrasound into 3D, and interactive-automatically segmenting the mitral valve from 3D TEE data.

## Objective
1. Add Segmentation node support for mold generation.
1. Integrate custom mold base plate to generated leaflet mold from segmentation.

## Approach and Plan

1. Replace exporting of molds to Model nodes with exporting to Segmentation nodes
1. Fix subtracting projected annulus from leaflet mold
1. Align loaded STL base plate model with extracted mold
1. Fill empty spaces between extracted mold and loaded base plate

## Progress

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
1. Working prototype of segmentation and registration modules already developed.
1. Completed segmentation node support.
1. Added alignment of loaded base plate model.
1. Added base plate filling to close bottom of mold.

## Next Steps
1. Need to make filling around base plate more robust.
1. Missing vertical fill when base is placed too low.
1. Need to rotate base plate model to match valve annulus normal after alignment with annulus.

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->
![Mitral Valve Segmenter Module screenshot](https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW29_2018_London_Canada/Projects/SlicerMitralValve/MitralValveSegmenter-Screenshot.png)

![Mitral Valve Segmenter Mold](https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW29_2018_London_Canada/Projects/SlicerMitralValve/MitralValveSegmenter-MoldBottom.png)

![BiPlaneRegistration Module screenshot](https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW29_2018_London_Canada/Projects/SlicerMitralValve/BiPlaneRegistration.png)

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/pcarnah/SlicerMitralValve
