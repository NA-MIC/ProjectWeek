---
layout: pw42-project

permalink: /:path/

project_title: Lighting problems with latest SlicerVR
category: VR/AR and Rendering

key_investigators:

- name: Csaba Pinter
  affiliation: EBATINCA
  country: Spain

- name: Andras Lasso
  affiliation: PerkLab
  country: Queen's, Canada

- name: Matt Jolley
  affiliation: CHOP
  country: USA

- name: Kitware?
  affiliation: Jc / Thibault

---

# Project Description

<!-- Add a short paragraph describing the project. -->


There is a regression with how latest SlicerVR lights the scene, both with the old VR and the new XR backend.
- OpenVR: Default lighting looks as expected, but now SSAO and Lights module options are not applied on the VR view (even if the view node IDs are explicitly selected)
- OpenXR: Default lighting looks washed out



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Make both backends of SlicerVR work like before the regression
    * "Normal" lighting by default
    * Lights module changes have effect on VR view as well



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Investigate the problem with the help of people directly involved in the OpenXR integration
2. If we find the root cause of either issues, try to address them



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


The following screenshots demonstrate shadows vs no shadows in OpenVR: 

![OpenVR no shadows](OpenVR_NoShadow.png)
Left: Slicer view using OpenVR without shadows 
Right: VR view (with back lights / without two sided lighting)

![OpenVR_Shadow](OpenVR_Shadow.png)
Left: Slicer view using OpenVR with shadows
Right: VR view  (with back lights / without two sided lighting)


__________________________________________________________________________________________________________

The following screenshots demonstrate different lighting options in OpenXR: 

![OpenXR_NoShadow](OpenXR_NoShadow.png)
Left: Slicer view using OpenXR without shadows 
Right: VR view (with back lights / without two sided lighting) 

![OpenXR_Shadow](OpenXR_Shadow.png)
Left: Slicer view using OpenXR without shadows 
Right: VR view (without back lights / without two sided lighting) 




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


For those who have access to SlicerHeart internals, this is the link to the issue: https://github.com/JolleyLab/Internal/issues/205#event-14879920416

