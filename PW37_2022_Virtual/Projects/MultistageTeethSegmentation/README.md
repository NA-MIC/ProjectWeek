Back to [Projects List](../../README.md#ProjectsList)

# Multi-stage deep learning segmentation of teeth

## Key Investigators

- Daniel Palkovics (Semmelweis Medical University)
- Csaba Pinter (Ebatinca)
- David Garcia Mato (Ebatinca)
- Andres Diaz-Pinto (NVidia)

# Project Description

<!-- Add a short paragraph describing the project. -->

Segmenting and identifying the teeth in a mandible or maxilla is a difficult task, especially due to the high number of structures and their similarity. Recent results suggest that multi-stage segmentation may yield more accurate segmentation in these scenarios.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The idea is to create a simple two-stage approach in MONAILabel where the first stage detects the teeth centre and the second stage accurately segments the teeth themselves.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Discuss with Andrés the details about multi-stage segmentation in MONAILabel
1. Design the changes to be made

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

There are some promising preliminary results

![Good result](PreliminaryTeethSegmentation_1.PNG)
![Good result](PreliminaryTeethSegmentation_2.PNG)
![Good result](PreliminaryTeethSegmentation_4.PNG)

but there is room for improvement!

![Bad result](PreliminaryTeethSegmentation_3_Bad.PNG)
![Bad result](PreliminaryTeethSegmentation_5_Bad.PNG)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- https://github.com/NA-MIC/ProjectWeek/tree/master/PW36_2022_Virtual/Projects/AutomaticSegmentationofTeethandAlveolarBone
