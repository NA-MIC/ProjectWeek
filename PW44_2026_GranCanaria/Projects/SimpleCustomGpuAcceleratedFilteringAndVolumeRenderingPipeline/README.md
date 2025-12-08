---
layout: pw44-project

permalink: /:path/

project_title: Simple custom GPU accelerated filtering and volume rendering pipeline
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Simon Drouin
  affiliation: ETS Montreal
  country: Canada

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

---

# Project Description

<!-- Add a short paragraph describing the project. -->


3D Slicer has the potential to be a powerful dissemination platform for novel 3D rendering methods targeted at medical imaging. However, its complex architecture is challenging for most experienced graphics programmers. It is difficult to create extensions that implement novel graphics pipeline without mastering a large portion of the Slicer architecture.

Thibault Pelletier at Kitware France has recently contributed a powerful Slicer extension called [Layer Displayable Manager](https://github.com/KitwareMedical/SlicerLayerDisplayableManager). This extension simplifies the creation of new interactive VTK-based graphics rendering pipeline, both from Loadable or Scripted modules. 

Kyle Sunderland has created another valuable tool: [vtkGPUImageFilters](https://github.com/Sunderlandkyl/VTK/commits/vtkGPUImageFilter3). Each filter in this collection can be connected to the regular VTK pipeline, but use GPU for processing without having to bring the data back to the CPU memory between filters. The code is not yet integrated in VTK and is still a

The combination of Layer Displayable Manager and vtkGPUImageFilters has the potential to enable a new range of GPU accelerated filtering and volume rendering effects.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


The goal of this projet is to generate a proof of concept of the potential provided by the integration of LayerDisplayableManader and vtkGPUImageFilters. The project aims at:
* Creating an experimental scripted module that can apply a gaussian blur to a volume in the GPU
* Render the resulting volume without bringing the filtered image back to the CPU memory.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Build a simple volume rendering scripted module that implements a custom pipeline using the Layer Displayable Manager extension and the existing vtkGPUVolumeRaycastMapper
2. Build Kyle Suntherland’s vtkGPUImageFilter as an external VTK module. This step may require major modifications in the code as this collection of filter was implemented for a version of VTK from 2019. 
3. Link the vtkGPUImageFilter module to be usable in the scripted module developed in step 1. 
4. In the loadable module, implement a class that derives from vtkGPUVolumeRaycastMapper but is able to take a volume already in the GPU as an input.
5. Modify the pipeline of the module developed in the first step to filter the input volume and pass it on to the volume rendering mapper.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [Layer Displayable Manager on GitHub](https://github.com/KitwareMedical/SlicerLayerDisplayableManager) 
- [vtkGPUImageFilters](https://github.com/Sunderlandkyl/VTK/commits/vtkGPUImageFilter3) (branch on Kyle Sunderland's VTK fork)

