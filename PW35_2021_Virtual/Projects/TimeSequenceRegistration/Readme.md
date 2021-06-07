Back to [Projects List](../../README.md#ProjectsList)

# Time Sequence Registration for Deep Learning

## Key Investigators

- Curtis Lisle (KnowledgeVis,LLC)

## Project Description

I plan to prepare a Lung RadioTherapy patient cohort for deep learning segmentation and annotation.  I will use Slicer and other NA-MIC 
tools to register patients' follow-up scans to their original planning CT scans as a preparatory step for deep learning.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Select example patients with original CTs along with folllow-up CT and/or PETs scans. 
1. Objective B. Align follow-up scans to planning CTs using 3D Slicer, Plastimatch, or other algorithm.
1. Objective C. Develop scripts to run on multiple patients and inspect the results using 3D Slicer. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Start by selecting candidate patient scans and testing registration tools in Slicer and/or PlastiMatch to align them
1. Investigate de-noising or other preprocessing steps for PET scans before registration. Will it help the final result?
1. Compare registration results of different algorithms in Slicer
1. Once an algorithm is selected, automate processing of larger cohort and review the results.
1. If time permits, try MONAI-based DNN training on registered scans. 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

## Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

## Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
