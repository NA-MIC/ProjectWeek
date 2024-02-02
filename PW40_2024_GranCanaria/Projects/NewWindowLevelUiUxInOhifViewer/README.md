---
layout: pw40-project

permalink: /:path/

project_title: New window level UI/UX in OHIF Viewer
category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Alireza Sedghi
  affiliation: OHIF
  country: Accolade Imaging, Canada

---

# Project Description

This project will aim to update the OHIF Viewer based on the new design of the Window Level interactions. Using per-viewport interactions makes a lot of sense (similar to commercial pacs viewers such as Siemens, and GE) since you can filter the options based on the available context (modality, 3D vs non-3D, fusion etc.)


![CleanShot 2024-02-01 at 22 09 07](https://github.com/NA-MIC/ProjectWeek/assets/7490180/9c6ab6d4-6cf1-4610-b8ca-076b226df357)

## Objective

1.  Move the patient information to the top right instead of per viewport
2.  Improve upon current setup for the All-in-one-menu

## Approach and Plan

1.  Follow zeplin designs and implement the UI components

## Progress and Next Steps

1. I successfully completed the UI element for the window level presets and connected it to enable ww/wc changes.
2. Additionally, I added a toggle for the color bar. The color bar component is already integrated into cornerstone3D.

Next Steps:
-  Implementing the ability to track and maintain states for each viewport that displays the color bar.
-  Incorporating the colorLUT changes into the UI.

# Illustrations

 <video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/7490180/e277fa0f-9bb5-4951-a398-076894b588b2"
   style="max-height:640px; min-height: 200px">
 </video>




# Background and References

Color bar in cornerstone3D
- https://www.cornerstonejs.org/live-examples/colorbar
- https://www.cornerstonejs.org/live-examples/advancedcolorbar

OHIF PR
- https://github.com/OHIF/Viewers/pull/3914
