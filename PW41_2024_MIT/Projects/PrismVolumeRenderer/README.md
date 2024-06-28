---
layout: pw41-project

permalink: /:path/

project_title: PRISM Volume renderer
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:
- name: Simon Drouin
  affiliation: ÉTS Montreal
  country: Canada

- name: Aurélie Rasolomanana
  affiliation: ÉTS Montreal
  country: Canada
  
- name: Kylian Pasquereau
  affiliation: ÉTS Montreal
  country: Canada
  
---

# Project Description

The PRISM extention aims at providing a list of advanced interactive volume rendering effects not available through the standard Volume Rendering module in Slicer. Users are able to experiment with the available effects either by rendering their own volume or by using the sample volumes provided for each of the effects. 

From a developper's point of view, it is possible to add new volume rendering effects by adding a python script that defines the parameters of the effect and implements modifications to the standard volume rendering shader. The GUI for the effect is automatically generated from the list of parameters.

## Objective

1. Fix pending bugs that appeared in the latest version of Slicer
2. Make it possible to load a sample volume for an effect without having previously enabled another loaded volume
3. Develop a new shader or modify the outline shader to be able to produce glass-like rendering of tissue boundaries in a volume

## Approach and Plan

1. The glass effect could be obtained by modifying the outline shader to modulate the transparency of the volume by the specular term of the phong model in regions where the volume gradient's amplitude is high.
2. It may be necessary to apply a gaussian filter to the volume before computing the gradient if the signal is too noisy to produce an interesting specular highlight.

## Progress and Next Steps
1. Fixed minor bugs and inconsistencies in the interface update mechanism
1. Rearranged the interface to be more user-friendly
1. Updated the module to use the parameterNodeWrapper mechanism and simplify the interface update
1. Commits of the week:
   1. [rearrange interface and fix bugs](https://github.com/ETS-vis-interactive/SlicerPRISMRendering/commit/1167ad4e5105587c3e48b4f901ef43d3835ddbe6)
   1. [prepare code for parameterNodeWrapper](https://github.com/ETS-vis-interactive/SlicerPRISMRendering/commit/33a08784d190a4fe750a12e9bd43918214a2ab53)
1. Discussed an architecture for an experimental volume rendering module that would enable the implementation of more complex effects.  

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

1.[PRISM at PW39 in Montreal](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/PrismVolumeRendererRefactoringAndBugFixing/)
