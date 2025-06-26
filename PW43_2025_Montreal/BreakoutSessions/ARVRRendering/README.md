---
layout: pw43-project

permalink: /:path/

project_title: AR-VR and Rendering

key_investigators:
- name: Simon Drouin
  affiliation: ETS
- name: Steve Pieper
  affiliation: Isomic Inc.
- name: Rafael Palomar
  affiliation: OUH / NTNU
- name: Sankhesh Jhaveri
  affiliation: Kitware Inc.

---
# Description
The goals of this breakout session is to discuss the upcoming changes in the rendering infrastructure of Slicer, investigate ways to make the rendering pipeline more customizable and plan future direction for SlicerVirtualReality to ensure is it more usable, customizable and supports a wide range of AR and VR devices.

## Topics for discussion
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

## Meeting notes

This document was created in the context of the [_Rendering and XR Breakout session_][breakout-session] taking place [43nd Slicer Project Week][43-project-week]

[43-project-week]: https://projectweek.na-mic.org/PW43_2025_Montreal/
[breakout-session]: https://projectweek.na-mic.org/PW43_2025_Montreal/#breakout-sessions

### SegmentAwareCarvingOfVolumes

Discussed the [PW43 project](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/SegmentAwareCarvingOfVolumes/) on interactive carving for volume rendering.

| Unity | Slicer |
|--|--|
| ![image](https://github.com/user-attachments/assets/3d62c8ec-41e5-4a35-b796-52bd417f5f80) | ![image](https://github.com/user-attachments/assets/0713fcdc-7ca0-401b-abaa-060d2fb4c883) |

The implementation uses a sphere of influence that selectively clips volumes based on segmented objects (user-selected). Antialiasing is currently missing in the 3D SLicer implementation (FXAA was used for the Unity implementation). For this project, @AndreyTitov implemented a loadable module (c++) to expose the texture unit by volume rendering to Python. He will re-formulate his solution in a PR to the Slicer core so that the functionality is accessible to all Python extensions.

### Discussion about improving the current rendering pipeline in Slicer

* It is a high priority for the Slicer commmunity to have VTK exposing the entry points for internal rendering data (e.g., texture ids) in such way that it could be used directly in Python.
* One approach is to change the Slicer Core to expose these internals to Python. This could be done while waiting for VTK to catch up and providing access to these from Python.

### Updates on VTK

- New version (V9.5.0) available (not yet in 3D Slicer). See [PR-8427](https://github.com/Slicer/Slicer/pull/8427). A comprehensive list of changes; is in https://docs.vtk.org/en/latest/release_details/9.5.html
- WebGPU support for image mapper & volume rendering is not available in VTK. Target is VTK 10.x. In the meantime, WebGPU compute pipelines are available. See https://www.kitware.com/webgpu-compute-api-in-vtk/
- Shaders are going to change quite some in the future of VTK (e.g., tag replacement in strings will become function re-definitions). This is not yet ready in v9.5.0. However compute shaders infrastructure is ready to play with.
- VTK & wasm. See https://kitware.github.io/vtk-wasm/ 

### SlicerVR

- History of transition of technologies (OpenVR - OpenXR) with some uncertainty in the development towards the future.
- It is partially working but different rusers have had different experiences using it.
- @SimonDrouin raised an issue with manipulation of Markups in OpenVR/XR. Some of the markups handles (particularly the ROI) seem to be 2D facing the camera. This could be causing problems in the context of VR/AR (rendering issue). Interaction with Markups is known to not work (@AndrasLasso).
- Details about mapping of controller actions to VTK events. See https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md
- Meta Quest is not supported out of the box yet in OpenXR, but could be done using the following documentation: https://www.kitware.com/using-vtk-with-the-meta-quest/
- Future for SlicerVirtualReality:
  - There is currently not grant to support development and maintenance
  - There is interest by multiple parties (Chi Zhang, Ron Kikinis, Simon Drouin, Sylvain Bouix) to fix problems and optimize the experience for a limitted set of use cases with common requirements that all include exploring patient scans
  - A version of SlicerVR that is well maintained and stable for these use cases would generate more interest for the module
  - Needed fix:
    - Support major HMD brands ensuring a similar interaction under OpenXR
    - Improve interaction for the above-mentionned use cases
    - Fix functionality that doesn't behave the same way in VR and in the 3D View, i.e. Markups  

## References
* [Notes from PW40](https://projectweek.na-mic.org/PW40_2024_GranCanaria/BreakoutSessions/Rendering/)
* [Notes from PW39](https://projectweek.na-mic.org/PW39_2023_Montreal/BreakoutSessions/RenderingBreakout/)
* [Slicer WebGPU project from PW37](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerWGPU/)(Steve Piper)

