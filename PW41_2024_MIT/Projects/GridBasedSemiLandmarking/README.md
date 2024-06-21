---
layout: pw41-project

permalink: /:path/

project_title: Grid-based Semi-Landmarking via Surface Markups
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:
- name: Sara Rolfe
  affiliation: Seattle Children's Research Institute
  country: US

- name: Murat Maga
  affiliation: Seattle Children's Research Institute
  country: US
---

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

A grid-based semi-landmarking functionality comes up often as a request in context of Slicer/SlicerMorph users. Currently this only exists in proprietary software packages. We aim to provide the following functionality:
1. Objective A. Create a grid of equidistant landmark points can be projected onto a model surface
2. Objective B. As individual landmark points are adjusted manually, the grid is updated and resampled. 
3. Objective C. A module will be created to support the user interactions

## Approach and Plan

The [Surface Landmark Extension](https://github.com/SlicerHeart/SlicerSurfaceMarkup/tree/master) developed by the Slicer Heart group provides the grid point structure that will be needed for this project. The remaining steps will be to:
1. Implement and test projection method to snap grid points to a model
2. Implement methods to update grid points when a single point is moved manually
3. Create a module to handle user interactions

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Projection method to snap Surface Markups to a model

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
[Initial grid projection](GridInitial.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
