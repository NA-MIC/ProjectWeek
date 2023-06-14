---
layout: pw39-project

permalink: /:path/

project_title: PRISM Volume Renderer – Refactoring and bug fixing
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Andrey Titov
  affiliation: ÉTS
  country: Canada

- name: Camille Hascoët
  affiliation: ÉTS
  country: Canada

- name: Simon Drouin
  affiliation: ÉTS
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The goal of this project is to enable the development of advanced 3D rendering techniques in Slicer. The goal is to facilitate access to GPU shaders and enable GPU-based filtering in Slicer by improving shader access multipass rendering in VTK and Slicer. The [PRISM Module](https://github.com/ETS-vis-interactive/SlicerPRISMRendering) in Slicer will serve as a test environment for the new capabilities.

PRISM has a significant amount of unused and/or legacy code that was made for version 4.11, which isn't used anymore. The goal of the project is to simplify PRISM volume renderer to make it easier to work with and to remove as many bugs as possible.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Fixing the Outline shader
2.  Closing Slicer after opening PRISM shouldn't generate errors

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Debug the code to see what is happening
2.  Try to simplify the shader until something appears on the screen, and then add the code back

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  The scale of the gradients calculated on the volume has been properly adjusted.
2.  This gradient computation was necessary to make Edge Enhancement work.
3.  Minor refactoring of the code.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![image](https://github.com/NA-MIC/ProjectWeek/assets/22062174/eef32864-83d5-4da8-a447-1d5b4f4b29f1)
![image](https://github.com/NA-MIC/ProjectWeek/assets/22062174/613897ec-e2a3-4345-b03e-423d64a0fe39)
![image](https://github.com/NA-MIC/ProjectWeek/assets/22062174/28a4c483-b9cd-467c-a182-33b87b1086d9)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

<https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PRISM_volume_rendering/>
