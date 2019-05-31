Back to [Projects List](../../README.md#ProjectsList)

# Neuroanatomical Segmentation

## Key Investigators

- Sylvain Bouix (BWH)
- Jarett Rushmore (Boston University)
- Kyle Sunderland (Queen's Univeristy)
- Andras Lasso (Queen's Univeristy)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Design and create a dedicated neuroanatomy segmentation module 
1. Adopt an approach for sulcal definition

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
- Sulcal definition
  1. Load freesurfer surfaces into Slicer
  1. Using the white matter surfaces, draw two points in Slicer, each at the base of a sulcus
  1. Connect the two points with a line at the bottom of the sulcus (i.e., a minimum value)
  1. Assign the line to a specific sulcal identity (with it's associated ontology, and related reference files)

- Implement a constraint option for markups to force them to be on a surface (i.e. model node, segmentation, or another markup)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
