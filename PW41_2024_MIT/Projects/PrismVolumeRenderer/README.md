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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

1.[PRISM at PW39 in Montreal](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/PrismVolumeRendererRefactoringAndBugFixing/)
