---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/TranslationRotationOfSelectPointsInAList/README.html

project_title: Translation/rotation of select points in a list
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Sara Rolfe
  affiliation: Seattle Children's Research Institute
  country: USA

- name: Murat Maga
  affiliation: University of Washington
  country: USA

- name: Gabriella D'Albenzio
  affiliation: Oslo University Hospital
  country: Norway

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The goal of this project is to facilitate selection and independent manipulation of points in a list.

This can currently be done in the Markups module by copying the points to a new list, translating/rotating the points, and copying the point positions back to the original node. However this process is tedious and error-prone.

The initial motivation for this project was to simplify creation of synthetic data from landmark transforms by transforming an original set of landmarks into the target landmark set.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Discuss overlapping goals between related projects (SlicerMorph, Slicer-Liver)
2.  Develop strategy for implementation

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Two possible solutions have been discussed for the implementation:
1. Add functions to Markups Editor module in the SlicerMorph extension
2. Add to Slicer core in the Markups module
   
## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Met to discuss use cases and overlap in needs between SlicerMorph and SlicerLiver Groups
2.  Built working prototype in 3D Slicer that meets the needs of both groups
3.  Testing by remote team members
4.  Identified a bug and testing fix
5.  Plan to submit pull request by the end of the week

# Illustrations

<img width="1920" alt="Translation of points 1" src="https://github.com/NA-MIC/ProjectWeek/blob/8e621994e02f65089ebd3a29b9da3ed307ff4925/PW39_2023_Montreal/Projects/TranslationRotationOfSelectPointsInAList/TranslatePoints1.png">
<img width="1920" alt="Translation of points 2" src="https://github.com/NA-MIC/ProjectWeek/blob/8e621994e02f65089ebd3a29b9da3ed307ff4925/PW39_2023_Montreal/Projects/TranslationRotationOfSelectPointsInAList/TranslatePoints2.png">

![Translation of points 1](https://github.com/NA-MIC/ProjectWeek/blob/8e621994e02f65089ebd3a29b9da3ed307ff4925/PW39_2023_Montreal/Projects/TranslationRotationOfSelectPointsInAList/TranslatePoints1.png)

![Translation of points 2](https://github.com/NA-MIC/ProjectWeek/blob/8e621994e02f65089ebd3a29b9da3ed307ff4925/PW39_2023_Montreal/Projects/TranslationRotationOfSelectPointsInAList/TranslatePoints2.png)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

1.  Forum post [here](https://discourse.slicer.org/t/moving-a-subset-of-points-in-a-list/29198) discussing the issue and possible solutions.
