---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/Readme.html
- /PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/README.html

project_title: The future of rendering in VTK and Slicer

key_investigators:
- name: Simon Drouin
  affiliation: École de Technologie Supérieure
  Country: Canada

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA
  
- name: Murat Maga
  affiliation: University of Washington
  country: USA
  
- name: Andras Lasso
  affiliation: Queen's University
  country: Canada
  
- name: Sara Rolfe
  affiliation: Seattle Children's Research Institute
  country: USA
  
- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware, Inc.
  country: USA
  
- name: Stephen Aylward
  affiliation: Kitware, Inc.
  country: USA
  
- name: Rafael Palomar
  affiliation: NTNU
  country: Norway

- name: Sankhesh Jhaveri
  affiliation: Kitware, Inc.
  country: USA

- name: Matt McCormick
  affiliation: Kitware, Inc.
  country: USA

- name: Forrest Li
  affiliation: Kitware, Inc.
  country: USA

- name: Lucas Gandel
  affiliation: Kitware SAS
  country: USA

- name: Jaswant Panchumarti
  affiliation: Kitware, Inc.
  country: USA

- name: Shreeraj Jadhav
  affiliation: Kitware, Inc.
  country: USA

- name: Tom Birdsong
  affiliation: Kitware, Inc.
  country: USA

---

# Description

The goal of this breakout session is to gather all parties interested in the future of rendering in VTK and Slicer, present ongoing development by Kitware and others and discuss potential future directions and clinical and biomedical needs.

## During the Breakout Session

Links and notes are organized at [https://hackmd.io/Mq81LxbYTfqrwOBRjxrb6Q](https://hackmd.io/Mq81LxbYTfqrwOBRjxrb6Q). It is a markdown based document we can collaboratively & interactively edit. 

Once the breakout session is over, we will contribute the information back to this page.

## Topics

* VTK Evolution
  * Status of the replacement for OpenGL (WebGPU)
  * Integration of VTK and VTK.js (common shaders?)
* Rendering
  * Global illumination
  * Support for high resolution volumes
  * Support for shared graphics contexts
  * Support for GPU pre-processing of volumes and meshes
  * Creation of an experimental rendering module:
    * Support for multiple volumes/surfaces handled by the same pipeline
    * Modifiable shaders
    * Multipass rendering
    * Arbitrary number of transfer functions
    * Better support for animation and high-resolution rendering
* AR-VR
  * New Slicer Mixed-Reality module (for Hololens remoting)
  * Support for OpenXR in Slicer Virtual Reality module
  * Status of WebXR in vtk.js

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
* [WebGPU in VTK](https://www.kitware.com/vtk-webgpu-on-the-desktop/)
* [WebGPU in Slicer](https://github.com/pieper/SlicerWGPU) from [Project Week 37](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerWGPU/).
