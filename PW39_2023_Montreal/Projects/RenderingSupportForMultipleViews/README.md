---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/README.html

project_title: Rendering support for multiple views
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Sara Rolfe
  affiliation: Seattle Children's Research Institute
  country: USA

- name: Murat Maga
  affiliation: University of Washington
  country: USA

- name: Chi Zhang
  affiliation: Seattle Children's Research Institute
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The goal of this project is to extend the Volume Rendering interface to improve the convenience of multiple volume comparisons. We aim to create and test prototypes of features that will be added to the SlicerMorph extension in the short term and discuss appropriateness of integration into Slicer core.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Features to support multiple volume comparisons:

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Objective A: Create module to manage two relative views, manage nodes displayed/transformed in each
2.  Objective B: Create prototype that links individual rendering properties of each volume in a folder.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Created a Python function to link/unlink relative views.
2.  Developed prototype for module to manage temporarily linked views: QuickAlign
3.  Module name contributed by Andras Lasso
4.  Testing use of QuickAlign
5.  Added beta version as a test module to the SlicerMorph extension: https://github.com/SlicerMorph/SlicerMorph/tree/master/QuickAlign

# Illustrations
Initial rendering of two fetal mouse scans:

<img width="50%" alt="ViewSyncBefore" src= "https://github.com/NA-MIC/ProjectWeek/raw/master/PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/viewSyncBefore.gif">

After alignment and temporary view linking using ViewSync:

<img width="50%" alt="ViewSyncAfter" src= "https://github.com/NA-MIC/ProjectWeek/raw/master/PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/ViewSyncAfter.gif">


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
