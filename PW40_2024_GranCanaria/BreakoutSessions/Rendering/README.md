---
layout: pw40-project

permalink: /:path/

project_title: Future of Rendering in VTK, ITK and Slicer

key_investigators:
- name: Rafael Palomar
  affiliation: NTNU
  country: Norway

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware, Inc.
  country: USA

- name: Sankhesh Jhaveri
  affiliation: Kitware, Inc.
  country: USA

- name: Matt McCormick
  affiliation: Kitware, Inc.
  country: USA

- name: Lucas Gandel
  affiliation: Kitware SAS
  country: USA

- name: Forrest Li
  affiliation: Kitware, Inc.
  country: USA

---

# Description

The goal of this breakout session is to gather all parties interested in the future of rendering in VTK and Slicer, present ongoing development by Kitware and others and discuss potential future directions and clinical and biomedical needs.

## During the Breakout Session

Links and notes are organized at [https://hackmd.io/j0xxip3jR_O9220uJUjJKg](https://hackmd.io/j0xxip3jR_O9220uJUjJKg). It is a markdown based document we can collaboratively & interactively edit. 

Once the breakout session is over, we will contribute the information back to this page. See [Notes](#notes) below.

## Topics

* VTK C++:
  * WebGPU
  * OpenXR
* itk-viewer and itkwidgets
* vtk.js
* SlicerVirtualReality


# Notes

### VTK C++: WebGPU

_Contact: Sankhesh Jhaveri @ Kitware_

* Direct replacement of OpenGL for native desktop and webassembly for browsers
* Better separation between windowing UI and rendering API
* Implementation agnostic support via the [webgpu C API](https://github.com/webgpu-native/webgpu-headers) that would allow switching between dawn, wgpu, and future webgpu implementations.
* What is the timeline to transition to WebGPU ?
  - this is pending funding, we are currently waiting for review of NSF grant

Notes:
* Custom shader code written in GLSL would have to be coverted to WGSL shader language
* Moving forward we will have one volume rendering implementation
* ANARI will allow to have multiple backend for ray tracing
* Sanhesh et al are active and involved with the WebGPU forum

See [notes](https://projectweek.na-mic.org/PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/#vtk-c-webgpu) from 39th project week.

### VTK C++: WebAssembly

_Contact: Jaswant Panchumarti @ Kitware_

See [notes](https://projectweek.na-mic.org/PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/#webassembly) from 39th project week.

### VTK C++: OpenXR

_Contact: Lucas Gandel @ Kitware_

* Hand interaction improvements for the Hololens 2:
    * Combine 'aim/select' and 'grip/squeeze' poses, mimic the Unity behavior
    * Hand joints/finger tracking
* Support occlusion from the real world in the Hololens 2:
    * Implement scene understanding extension
* Custom controller model:
    * The controller model extension is not implemented by most of the runtimes. We should provide an API for users to load their own controller model files (GLTF, OBJ, with textures).
* Registration of multiple devices:
    * Investigate spatial anchors persistency and sharing such anchors across sessions.
    * Enable QR code detection extension
    * https://publik.tuwien.ac.at/files/publik_299074.pdf

See [notes](https://projectweek.na-mic.org/PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/#vtk-c-openxr) from 39th project week.


### SlicerVirtualReality

_Contact: Jean-Christophe Fillion-Robin @ Kitware_


### vtk.js: Interactive, in-browser cinematic volume rendering of medical images

_Contact: Stephen Aylward & Forrest Li @ Kitware_

* vtk.js goals
    * support vtk-wasm as a rendering backend
    * unified WebGPU implementation (see VTK C++ WebGPU above)
* VolView goals
    * improved streaming support
    * demos with python-based processing server


### itk-viewer and itkwidgets

_Contact: Matt McCormick @ Kitware_

* [3D Slicer on the Web via ITK-Wasm and friends](https://docs.google.com/presentation/d/1IHgkgNZuN9c_uYkWAnY984kLQySznB5S66S2aHt0blQ/edit#slide=id.g2a5c217f66c_0_1091)
* `itk-viewer`: Multi-dimensional web-based image, mesh, and point set viewer
* [`itkwidgets`](https://itkwidgets.readthedocs.io/en/latest/): Python interface for visualization on the web platform to interactively generate insights into multidimensional images, point sets, and geometry.

Notes & Links:
* https://itkwidgets.readthedocs.io/en/latest/deployments.html
* ITKIOOMEZarrNGFF
    * https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF
    * https://pypi.org/project/itk-ioomezarrngff/

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
* [39th Project Week - Rendering breakout session](https://projectweek.na-mic.org/PW40_2024_GranCanaria/)
* [WebGPU in VTK](https://www.kitware.com/vtk-webgpu-on-the-desktop/)
* [WebGPU in Slicer](https://github.com/pieper/SlicerWGPU) from [Project Week 37](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerWGPU/).
