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
     
### Temporary documentation of existing event mapping
| OpenXR Quest 3 bindings           | VTK action paths     | Type      | VTK function or event id (default) |
| --------------------------------- | -------------------- | --------- | ---------------------------------- |
|                                   | elevation            | vector2   |                                    |
| /user/hand/left/input/aim         | handpose             | pose      |                                    |
| /user/hand/right/input/aim        | handpose             | pose      |                                    |
|                                   | handposegrip         | pose      |                                    |
|                                   | haptic               | vibration |                                    |
|                                   | complexgestureaction | boolean   |                                    |
| /user/hand/right/input/thumbstick | movement             | vector2   |                                    |
|                                   | nextcamerapose       | boolean   |                                    |
|                                   | positionprop         | boolean   |                                    |
| /user/hand/right/input/b          | showmenu             | boolean   |                                    |
|                                   | startelevation       | boolean   |                                    |
| /user/hand/right/input/thumbstick | startmovement        | boolean   |                                    |
| /user/hand/right/input/a          | triggeraction        | boolean   |                                    |
| /user/hand/left/input/y           | forwardthickcrop     |           |                                    |
| /user/hand/left/input/menu        | nextcamerapose       |           |                                    |
| /user/hand/left/input/x           | backthickcrop        |           |                                    |

### New event mapping proposal
| OpenXR Quest 3 bindings           | VTK action paths     | Type      | VTK function or event id (default) |
| --------------------------------- | -------------------- | --------- | ---------------------------------- |
|                                   | elevation            | vector2   |                                    |
| /user/hand/left/input/aim         | handpose             | pose      |                                    |
| /user/hand/right/input/aim        | handpose             | pose      |                                    |
|                                   | handposegrip         | pose      |                                    |
|                                   | haptic               | vibration |                                    |
|                                   | complexgestureaction | boolean   |                                    |
| /user/hand/right/input/thumbstick | movement             | vector2   |                                    |
|                                   | nextcamerapose       | boolean   |                                    |
|                                   | positionprop         | boolean   |                                    |
| /user/hand/right/input/b          | showmenu             | boolean   |                                    |
|                                   | startelevation       | boolean   |                                    |
| /user/hand/right/input/thumbstick | startmovement        | boolean   |                                    |
| /user/hand/right/input/a          | triggeraction        | boolean   |                                    |
| /user/hand/left/input/y           | forwardthickcrop     |           |                                    |
| /user/hand/left/input/menu        | nextcamerapose       |           |                                    |
| /user/hand/left/input/x           | backthickcrop        |           |                                    |

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img width="640" alt="IMG_20260625_104739134_HDR" src="https://github.com/user-attachments/assets/c1e406e5-4887-4c43-b370-694434bd1fcc" />

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- VTK branch: https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf
- Slicer/VTK PR: https://github.com/Slicer/VTK/pull/63
- SlicerVirtualReality branch: https://github.com/Sunderlandkyl/SlicerVirtualReality/tree/openxr_passthrough_update

