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

1. Implement shader replacement for surface rendering in Slicer
2. Validate the possibility to use Compute Shaders in the Slicer OpenGL context and determine the interface for doing so
3. Come up with a long term plan for an infrastructure that would facilitate the implementation new rendering techniques that use an arbitrary combinations of volumes, surfaces, transfer functions, custom parameters and custom shaders and may include preprocessing steps based on Compute Shader.

## Approach and Plan

1. Replicate the shader replacement mechanism architecture of the volume rendering module in the models module
2. Create a prototype modification of the volume rendering module that can run a simple ComputeShader (e.g. gaussian blur) on the volume before rendering.
3. Determine how mappers can make use of textures already present in the GPU rather than uploading volumes to textures.
4. Volume rendering: Use multiple perfectly overlapping volumes without paying the overhead for multi volume rendering

## Progress and Next Steps

1. Discussions with all parties interested in advanced graphics in Slicer allowed us to identify the list of requirements for future graphics programming capabilities in Slicer:
    * **Target experienced graphics programmers with no VTK and Slicer experience**. The rational for that requirement is that many graphics programmers develop valuable rendering methods directly on basic APIs (OpenGL, DirectX, Vulkan), on prototyping systems (ex. [InViwo](https://inviwo.org/)), or game engines, all of which make it difficult to the more clinically oriented research community and clinical users to use them on a daily basis. We would like to create an incentive for porting to Slicer.
    * **Provide basic implementation of surface and volume rendering that can take an arbitrary number of inputs of various type**. Although current volume rendering infrastructure enable multiple input volume and shader replacement, the infrastructure is relatively rigid, using multiple volumes is slow because it assumes they are not perfectly overlapping, and coordination between input volumes and shader variables is complicated.
    * **Provide Compute Shaders that can be assembled in pipelines with an arbitrary number of inputs and outputs**. The input of the pipeline could include Slicer nodes that represent volumes, surfaces, color tables, transfer functions and transforms. The output of the pipeline would be connectable to Surface and Volume rendering implementations mentionned above without having to bring the data back to the CPU memory.
    * **Make all the above-mentionned functionality customizable from the Python interface**. One simple way to fulfill this requirement is to enable pipeline construction from Python as well as shader specification. The Shaders code should declare its inputs and outputs so that Slicer can determine automatically how the pipeline can be connected and automatically assign inputs and outputs to the proper shader variables.
1. The AR/VR and Rendering breakout session involved a discussion with Sankesh and Jaswant for Kitware, who are both involved in the development of the WebGPU backend to replace OpenGL in VTK. The new backend promises to provide the appropriate infrastructure to implement the list of requirements identified above.
    * The documentation for the WebGPU backend is available [here](https://docs.vtk.org/en/latest/modules/vtk-modules/Rendering/WebGPU/README.html)
    * The current implementation already supports **Surface Rendering** and an infrastructure for **Compute Shader** pipelines.
    * Volume rendering is not implemented at this point
1. The next step for the community should be to create an experimental rendering module that can wrap the existing WebGPU backend feature and enable the construction of simple rendering pipeline for Surface rendering and make sure the construction of pipeline is possible through the Python interface.

# Illustrations
Custom volume rendering done in Unity VR, to be ported to VTK and 3D Slicer. The current implementation relies on Compute Shaders.
<iframe width="560" height="315" src="https://www.youtube.com/embed/YFl7LF5hWxI?si=5rTmbpG4WKaT_LnX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* Related previous project: [https://projectweek.na-mic.org/PW41_2024_MIT/Projects/PrismVolumeRenderer/](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/PrismVolumeRenderer/)
