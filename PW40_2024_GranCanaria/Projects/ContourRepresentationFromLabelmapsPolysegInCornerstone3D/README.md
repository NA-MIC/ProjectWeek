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

We've been working hard on implementing polySEG in cornerstone3D, and currently we have implemented the following converters in a PR under review in Cornerstone3D:

- Labelmap to surface


https://github.com/NA-MIC/ProjectWeek/assets/7490180/fbf606ba-bdca-4071-8239-3af054e35d7e



- Surface to labelmap



https://github.com/NA-MIC/ProjectWeek/assets/7490180/f60b0d02-ce67-421b-ba29-ac0051f1b633



- Contour to surface


https://github.com/NA-MIC/ProjectWeek/assets/7490180/d3a79c5e-2a0d-4b8b-9030-46fe0af80e24



- Contour to labelmap

https://github.com/NA-MIC/ProjectWeek/assets/7490180/d92e5e17-3c20-4237-b94a-dbafbb6fda2c



However, we still have two converters remaining that seem to be more complex: surface to contour and labelmap to contour. We're excited to tackle these challenges and continue moving forward. This project aims to work on this.

## Objective

1.  Finish the surface cutting in each slice in the viewport and provide proper API around it for precaching inside a webworker
2.  Try to implement two implement a Edit version using our SVG rendering framework, and try to handle contour holes and islands

## Approach and Plan

1. Convert the representations to Surface and cut through them to render in viewports
2. For editing, get the intersections and travers to find a closed loop polygon
3. Try to identify holes in order to render them as holes 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
