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

Once the breakout session is over, we will contribute the information back to this page. See [Notes](#notes) below.

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
 
# Notes

## VTK C++: WebGPU

_Contact: Sankhesh Jhaveri @ Kitware_

WebGPU effort in VTK aims to provide a future-proof rendering backend as an alternative to OpenGL.

* VTK’s data model and visualization pipeline will have no architectural changes.
* For the most part, there will be no frontend user-facing changes to the rendering classes either. Applications would still have to instantiate `vtkRenderWindow`, `vtkRenderer`, `vtkActor`, etc.
* There will be changes with respect to how platform-specific windows are created. These windows no longer need to be tied to the graphics backend i.e. no need for `vtkXOpenGLRenderWindow`, etc.
* For advanced users of VTK who modify rendering logic, use shader replacements, etc. there will be *significant* changes. This should be expected, IMO.

Experimental:
* RenderingWebGPU: https://docs.vtk.org/en/latest/modules/vtk-modules/Rendering/WebGPU/README.html
* Draft: WebGPU: Native graphics backend. See https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10239

Questions:
* multi-volume rendering
  * Will it be the default ? In the OpenGL backend, there were two backends.
  * vtkMultiVolume issues
      * `SetVisibility` issue 
      * `UserMatrix` not taken into account for the first volume (issue) (works in `TestGPURayCastMultiVolumeOverlapping`)
      * Cropping
      * Shading
      * Only shows up in Composite w/ Shading, but nothing in MIP (Error: Shader failed to compile in `raycastervs.glsl`)
* context sharing ?
  * Goal is to reduce the memory footprint by avoiding having duplicate of teture memory (e.g multiple 3D views of the same volume data)
  * Availability of result of compute shader for rendering.
* Compute shaders
    * WebGPU ?

Notes:
* [moltengl](https://moltengl.com/moltengl/): Applications built for OpenGL ES 2.0 can use MoltenGL to run on top of Metal,
* Unity allows to easily compose complex rendering pipeline.
* RenderingWebGPU:
  * The shader is the center piece
  * Possibly use [SPIRV-Reflection](https://github.com/KhronosGroup/SPIRV-Reflect) to decipher shader inputs, their attributes/dimensionality and expose a VTK interface to populate shader bindings with vtkImageData, vtkDataArray, etc.

* Compute Shader
  * https://github.com/Punzo/SlicerAstro/tree/master/vtkOpenGLFilters
  * Simon will share details about experiment for implementing compute shader

* AI and WebGPU for training ?
  * Rendering into texture ?
  * https://virtualgl.org/
  * Idea would be to support Differential Rendering
      * https://towardsdatascience.com/differentiable-rendering-d00a4b0f14be
      * 

* Review meeting ?

### WebAssembly

_Contact: Jaswant Panchumarti @ Kitware_

* Slides: [WASM/WebGPU in VTK](https://docs.google.com/presentation/d/1Nl0TVa55616QKCSHP54BoYBvByMKe6lIUl6IFZqSeJo/edit#slide=id.p)

* Docs: [Getting Started / Using WebAssembly](https://docs.vtk.org/en/latest/getting_started/index.html#using-webassembly)

* Leverage efforts done in the context of https://wasm.itk.org/

## VTK C++: OpenXR

_Contact: Lucas Gandel @ Kitware_

Improvement roadmap for `OpenXR` and `OpenXR Remoting` support in VTK:

* OpenXR controller model support:
  * `vtkOpenXRManager` already supports for querying the controller models in a buffer (see [here](https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenXR/vtkOpenXRManager.cxx#L297))
  * The buffer should be forwarded to vtkGLTFReader using vtkResourceStream/vtkResourceParser
  * Need to add vtkResourceStream/vtkResourceParser support to vtkGLTFReader (see [PLYReader](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10224/diffs) )
* OpenXR Remoting hand interaction improvements
  * The current interactor style does not allow for accessing different poses from a single Move3D event (see discussions in [this MR](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/9595#note_1255954))
  * Possible options are:
    * Add support for storing additional poses (maybe as additional TrackedDevice)
    * Add support for [hands joints tracking](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#_conventions_of_hand_joints) and implement basic gestures recognition
* Add support for [scene understanding](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_MSFT_scene_understanding) in OpenXR Remoting, to occlude the VTK scene with the real world.

## SlicerVirtualReality

* Are we ready to transition to OpenXR ?
  * Before doing so, we would need to generalize the function [vtkOpenVRRenderWindow::GetOpenVRPose()](https://github.com/Slicer/VTK/blob/9bde2b3fa9887a801e3eec686ce591072986977f/Rendering/OpenVR/vtkOpenVRRenderWindow.cxx#L546-L558) currently specific to `Rendering/OpenV` and only available in  `Slicer/VTK`

## SlicerMixedReality

_Contact: Jean-Christophe Fillion-Robin @ Kitware_

See https://github.com/KitwareMedical/SlicerMixedReality/pull/2

Question: What to do once we start working on adding `OpenXR` support to `SlicerVirtualReality`.


## vtk.js: Rendering Non-uniform image series

_Contact: Shreeraj Jadhav @ Kitware_

See https://docs.google.com/presentation/d/1mrMe8w2G5hgRan0KzdwqrxgKGLfyR-h3mM7Kj5KYz4c/edit#slide=id.p


## vtk.js: Interactive, in-browser cinematic volume rendering of medical images

_Contact: Stephen Aylward & Forrest Li @ Kitware_

> The diversity and utility of cinematic volume rendering (CVR) for medical image visualisation have grown rapidly in recent years. At the same time, volume rendering on augmented and virtual reality systems is attracting greater interest with the advance of the WebXR standard. 

See https://doi.org/10.1080/21681163.2022.2145239

See https://volview.kitware.com/

## vtk.js: WebXR

_Contact: Tom Birdsong @ Kitware_

* Blog: [VTK.js Transforms Web-based Visualization with Immersive Virtual and Augmented Reality](https://www.kitware.com/vtk-js-transforms-web-based-visualization-with-immersive-virtual-and-augmented-reality/)
* Blog: [Holograms Over the Web: Kitware Extends vtk.js to Support Looking Glass Factory’s Displays](https://www.kitware.com/holograms-over-the-web-kitware-extends-vtk-js-to-support-looking-glass-factorys-displays/)
* Example and FAQs: https://kitware.github.io/vtk-js/docs/develop_webxr.html
    * [Supported devices](https://kitware.github.io/vtk-js/docs/develop_webxr.html#What-mixed-reality-devices-are-supported-by-VTK-js)
    * [Feature Support Roadmap](https://github.com/Kitware/vtk-js/issues/2571)

## VTK & ITK interoperability

Web:
* ITK IO are compiled to WASM and re-used in vtk.js based web application
* ITK-WASM is a building block for VTK-WASM

OME-Zarr: 
* https://www.biorxiv.org/content/10.1101/2023.02.17.528834v1 
* https://github.com/InsightSoftwareConsortium/itkwidgets/blob/main/examples/integrations/zarr/OME-NGFF-Brainstem-MRI.ipynb

Slicer + Large Image Rendering:

* We currently do not have any readily available implementation in Slicer, from a high level, the idea would be to:
  - support streaming dataset at different resolutions and updating the rendering accordingly.
  - leverage ITK+Zarr integration and ensure information flow all the way through the VTK pipeline
    - Consolidate ITKVTKGlue modules

* Improve ITK module: ITKIOOMEZarrNGFF. See https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF

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
