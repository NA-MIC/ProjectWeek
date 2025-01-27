---
layout: pw42-project

permalink: /:path/

project_title: Compute shaders and customized shaders for surface rendering
category: VR/AR and Rendering

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


The volume rendering module in Slicer contains an infrastructure that makes it possible to specify shader replacements for the volume rendering mapper. These shader replacements are automatically considered in every 3D view, including virtual reality. 

The goal of this project is to implement a similar interface for surface rendering and to propose a generalized architecture (to be implemented later) that makes it simple to implement new rendering techniques that use an arbitrary combinations of volumes, surfaces, transfer functions, custom parameters and custom shaders and may include preprocessing steps based on Compute Shaders



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement shader replacement for surface rendering in Slicer
2. Validate the possibility to use Compute Shaders in the Slicer OpenGL context and determine the interface for doing so
3. Come up with a long term plan for an infrastructure that would facilitate the implementation new rendering techniques that use an arbitrary combinations of volumes, surfaces, transfer functions, custom parameters and custom shaders and may include preprocessing steps based on Compute Shaders




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Replicate the shader replacement mechanism architecture of the volume rendering module in the models module
2. Create a prototype modification of the volume rendering module that can run a simple ComputeShader (e.g. gaussian blur) on the volume before rendering.
3. Determine how mappers can make use of textures already present in the GPU rather than uploading volumes to textures.
4. Volume rendering: Use multiple perfectly overlapping volumes without paying the overhead for multi volume rendering




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations
Custom volume rendering done in Unity VR, to be ported to VTK and 3D Slicer. The current implementation relies on Compute Shaders.
<iframe width="640" height="360" src="https://youtu.be/YFl7LF5hWxI">
 </iframe>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* Related previous project: https://projectweek.na-mic.org/PW41_2024_MIT/Projects/PrismVolumeRenderer/

