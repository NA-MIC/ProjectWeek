---
layout: pw43-project

permalink: /:path/

project_title: AR-VR and Rendering

key_investigators:
- name: Simon Drouin
  affiliation: ETS
- name: Steve Piper
  affiliation: Isomic inc.
- name: Rafael Palomar
  affiliation: OUH / NTNU

---
# Description
The goals of this breakout session is to discuss the upcoming changes in the rendering infrastructure of Slicer, investigate ways to make the rendering pipeline more customizable and plan future direction for SlicerVirtualReality to ensure is it more usable, customizable and supports a wide range of AR and VR devices.

## Topics
* Status of the transition between OpenGL and WebGPU as the rendering backend of VTK
  * Andrey's Demo of Anatomy Carve extension (port of Unity project, project page [here](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/SegmentAwareCarvingOfVolumes/))
  * MVP for volume rendering: run a compute shader on a volume texture with output to an RGBA buffer that can be volume rendered.
  * Support for an arbitrary number of input channels
  * Gradient precomputation
* Status of SlicerVirtualReality
  * Stability issues: interaction and markups 
  * Funding ideas to maintain the extension in the long term
  * Possible improvement
    * Support for GUI in VR (Show entire Slicer interface?)
    * Support for video Passthrough
    * Custom interaction for various use cases (a more outside-in experience as opposed to the current inside-out immersive experience)

## References
* [Notes from PW40](https://projectweek.na-mic.org/PW40_2024_GranCanaria/BreakoutSessions/Rendering/)
* [Notes from PW39](https://projectweek.na-mic.org/PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/)
* [Slicer WebGPU project from PW37](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerWGPU/)(Steve Piper)

# Notes
