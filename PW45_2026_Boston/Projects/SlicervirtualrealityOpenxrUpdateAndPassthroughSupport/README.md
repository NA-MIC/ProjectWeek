---
layout: pw45-project

permalink: /:path/

project_title: SlicerVirtualReality - OpenXR Update, Passthrough Support, Interactions Refactor
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Sylvain Bouix
  affiliation: ETS Montreal
  country: Canada

- name: Simon Drouin
  affiliation: ETS Montreal
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

![SlicerVirtualReality Logo](https://github.com/KitwareMedical/SlicerVirtualReality/raw/master/SlicerVirtualReality.png)

Currently SlicerVirtualReality is compiled using an older version of OpenXR. This project aims to finalize the integration of the latest version of OpenXR, as well as adding requested features such as passthrough using Meta Quest headsets.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Finalize required changes for updating SlicerVirtualReality to OpenXR
2. Add support for passthrough and environmental occlusion to VR using the Meta Quest




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Fix remaining issues in the OpenXR update ([Branch](https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf)).
2. Integrate PR containing VTK changes into the Slicer fork: ([PR](https://github.com/Slicer/VTK/pull/63))
3. Integrated changes into SlicerVirtualReality ([Branch](https://github.com/Sunderlandkyl/SlicerVirtualReality/tree/openxr_passthrough_update))



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Initial implementations can be found here:
   - https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf
   - https://github.com/Sunderlandkyl/SlicerVirtualReality/tree/openxr_passthrough_update

2. Discussion on updating interaction events:
    - VR Event Handling Levels
      1. Json file maps device specific buttons to device independent buttons ex. Button 1, Button 2, Joystick1, Trigger1, Grip1 etc.
      2. SlicerVirtualReality handles mapping from device independent events to interaction events ex. Pick3DEvent, Pick3DLineEvent, etc.
      3. Displayable managers handle events in the same way that they handle mouse and keyboard interaction events.

3. Summary of code changes:
   - **OpenXR runtime update & passthrough**: updated the bundled OpenXR SDK to 1.1.60 and added AR passthrough (`XR_ENVIRONMENT_BLEND_MODE_ALPHA_BLEND`) to `vtkMRMLVirtualRealityViewNode`/`qMRMLVirtualRealityView`. Also implemented environment-depth occlusion (`XR_META_environment_depth`), debug visualization, and VR scene/depth volume capture; these controls are hidden in the module UI for now since depth occlusion isn't functional with the current Meta runtime.
   - **Generic controller actions**: `SetupActions()` now registers the 28 generic Oculus Touch actions directly (5 default to the legacy VTK 3D events they replace, to preserve existing behavior; the rest keep their own generic event IDs for raw observability). All are rebindable from Python via the existing `AddAction()` helper, and are now invoked on the interactor.
   - **Interaction fixes**: grip button mapped to the "move prop" event; fixed complex gesture handling; added trigger click actions; fixed a bug where grabbed objects would slowly drift ("crawl away") during manipulation (root cause: `vtkTransform::SetMatrix()` updates internal state but never calls `Modified()`, so MRML's observer notifications weren't firing -- switched to `vtkMRMLTransformNode::SetMatrixTransformToParent()`, which does).
   - **UI**: the VR toolbar button now toggles the hardware connection (useful for exiting immersive mode or resetting the connection) instead of toggling rendering enable, which wasn't useful.
   - **Controller render models**: OpenXR has no API for rendering controller models, so vtkRenderingOpenXR falls back to a profile-to-asset JSON lookup table that has to be located next to the VTK build/install tree. Added a JSON mapping entry and a bundled glTF model for the Meta Quest Touch Plus controllers (previously only a generic placeholder rendered in headset), and moved the whole controller-models setup (Meta Quest Touch Plus, HTC Vive, Valve Index) into the module's own `Resources/ControllerModels/`, deployed via CMake and wired up through `vtkOpenXRRenderWindow::SetModelsManifestDirectory()`, so it survives a clean rebuild instead of depending on files manually placed in the VTK build tree.
   - Documentation ([DeveloperGuide](https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md#controller-event-ids), and [User guide](https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md)) updated to match the above. List of observable/overridable controller events is available [here](https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md#controller-event-ids).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img width="640" alt="IMG_20260625_104739134_HDR" src="https://github.com/user-attachments/assets/c1e406e5-4887-4c43-b370-694434bd1fcc" />

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- VTK branch: https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf
- Slicer/VTK PR: https://github.com/Slicer/VTK/pull/63
- SlicerVirtualReality branch: https://github.com/Sunderlandkyl/SlicerVirtualReality/tree/openxr_passthrough_update

