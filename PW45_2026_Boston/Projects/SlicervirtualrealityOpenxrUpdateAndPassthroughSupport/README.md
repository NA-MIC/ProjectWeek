---
layout: pw45-project

permalink: /:path/

project_title: SlicerVirtualReality - OpenXR Update and Passthrough Support
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

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Currently SlicerVirtualReality is compiled using an older version of OpenXR. This project aims to finalize the integration of the latest version of OpenXR, as well as adding requested features such as passthrough using Meta Quest headsets.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Finalize required changes for updating SlicerVirtualReality to OpenXR
2. Add support for passthrough and environmental occlusion to VR using the Meta Quest




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Fix remaining issues in the OpenXR update ([Branch](https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf)).
2. Integrate PR containing VTK changes into the Slicer fork: ([PR](https://github.com/Slicer/VTK/pull/63))
3. Integrated changes into SlicerVirtualReality (Branch)



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Initial implementations can be found here: https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- VTK branch https://github.com/Sunderlandkyl/VTK/tree/openxr_passthrough_slicer-v9.6.2-2026-05-15-f49a1dbaf
- Slicer/VTK PR https://github.com/Slicer/VTK/pull/63

