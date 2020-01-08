# Neuroanatomical Segmentation 2020

## Key Investigators

- Sylvain Bouix (BWH)
- Jarett Rushmore (Boston University, BWH)
- Kyle Sunderland (Queen's University)
- Nikos Makris (BWH, MGH)
- Andras Lasso (Queen's University)

# Project Description

1.  The objective of this project is to establish tools and techniques to produce a high resolution manual segmentation of the human brain.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Intregrate Freesurfer file formats.  
    Freesurfer is a program used to generate brain surfaces from MRI data.  Freesurfer file formats use their own coordinate space and thus do not seamlessly integrate with the MRI files read by Slicer.  The objective is to make freesurfer file formats easily accessible within Slicer.
2. Sulcal Drawing
The use of 3D tools to draw and delimit brain sulci depends on freesurfer input (number 1) and an algorithm to draw on sulci and extract the lines in coordinate space.  The goal is to troubleshoot this process.
3. Case Management
Integration of a BIDS-based cased management system would aid organization and segmentation.

## Approach and Plan
<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Freesurfer integration
- Load freesurfer surfaces into Slicer

2.  Sulcal Drawing
- Using the white matter surfaces, draw two points in Slicer, each at the base of a sulcus
- Connect the two points with a line at the bottom of the sulcus (i.e., a minimum value)
- Assign the line to a specific sulcal identity.
- Implement a constraint option for markups to force them to be on a surface (i.e. model node, segmentation, or another markup)

3. Case Management
-Pilot organziation

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

# Illustrations

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->