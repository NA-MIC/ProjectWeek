---
layout: pw40-project

permalink: /:path/

project_title: Contour Representation from Labelmaps - PolySEG in Cornerstone3D
category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Alireza Sedghi
  affiliation: OHIF
  country: Accolade Imaging, Canada
- name: Mo Alasad
  affiliation: XNAT, ICR
  country: UK

---

# Project Description

We've been working hard on implementing polySEG in cornerstone3D, and currently we have implemented the following converters in [a PR under review in Cornerstone3D](https://github.com/cornerstonejs/cornerstone3D/pull/844):

However, we still have two converters remaining that seem to be more complex: surface to contour and labelmap to contour. We're excited to tackle these challenges and continue moving forward. This project aims to work on this.

## Objective

1.  Finish the surface cutting in each slice in the viewport and provide proper API around it for precaching inside a webworker
2.  Try to implement two versions using our SVG rendering framework, and try to handle contour holes and islands

## Approach and Plan

1. Convert the representations to Surface and cut through them to render in viewports
2. For editing, get the intersections and travers to find a closed loop polygon
3. Try to identify holes in order to render them as holes 

## Progress and Next Steps

<video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/7490180/317ba288-c92c-4d43-98e2-5af61da71b42"
   style="max-height:640px; min-height: 200px">
 </video>
 
1. I successfully completed the first task by using vtkClipClosedSurface to cut through the surface and render it as polyData within the viewport.
2. Additionally, I implemented pre-caching of all slices within a web worker. This ensures that all cuts are calculated in advance, eliminating the need to wait for the user to scroll through each slice.


**Next steps**
- include to re-cache upong the orientation change, since we need to cancel the previous job on the worker and start a new one
- Also We need to also add another representation to edit the contours via our contour SVG editing tools, I have got the code from Forrest Li (Kitware) for the vtkContourLoopExtraction and [created a PR to vtk.js here](https://github.com/Kitware/vtk-js/pull/3003)

# Illustrations








*No response*

# Background and References

https://github.com/PerkLab/PolySeg
https://bitbucket.org/icrimaginginformatics/polyseg-wasm/src/master/
