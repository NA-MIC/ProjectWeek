---
layout: pw40-project

permalink: /:path/

project_title: New Interaction Widget for Transforms/Markups
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Kyle Sunderland
  affiliation: PerkLab - Queen’s University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to implement a new interaction handle widget that can be used to modify linear transform nodes. This implementation will be based on the existing interaction handle pipeline in the Markups module, but with improvements to functionality and appearance. Both the transforms and markups interaction widgets will be derived from the same base class.

The center of rotation for the transform node can be changed by holding ALT and clicking+dragging on one of the translation handles. The center of rotation can also be change in python using the "vtkMRMLTransformNode::SetCenterOfTransformation" function.

Transforms can also be scaled uniformly by holding ALT and clicking+dragging on one of the scale handles.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Integration of new interaction widget into 3D Slicer.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Provide an installer for precompiled version of Slicer that includes the new interaction widget.
2.  Update based on feedback gathered from the project week.
3.  Integrate new widget into the Slicer core.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Created installer for a version of 3D Slicer containing the new widget. (See link in "Background and References" section).
2.  Created [PR](https://github.com/Slicer/Slicer/pull/7562) to integrate changes into 3D Slicer.
3.  Add options to enable/disable visualization of specific axes.
4.  Add uniform scaling option.
5.  Improved visualization based on feedback.
6.  Integrated into latest preview release!

### Next steps

1. Use a simplified widget visualization when the user is not interacting with it.
2. Add a shortcut to allow users to cancel the transformation.
3. Add shortcut to enable snapping to angles.

# Illustrations


## Existing widgets

| Transforms| Markups |
|----------|:-------------:|
| ![image](https://github.com/NA-MIC/ProjectWeek/assets/9222709/aa0e1abb-ee47-478e-b712-a9cfd666b311) | ![image](https://github.com/NA-MIC/ProjectWeek/assets/9222709/f65d323f-e84c-481b-94c1-1001eb209ce5) |

## New widget

| Transforms| Markups |
|----------|:-------------:|
| ![image](https://github.com/NA-MIC/ProjectWeek/assets/9222709/dbc01ab4-31c0-4b17-b184-6e5c67c35bf7) | ![image](https://github.com/NA-MIC/ProjectWeek/assets/9222709/d0773aef-86d1-46de-9a21-afc53c54ecb8) |

<video
  autoplay loop controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/9222709/43e2d906-a8c0-4909-b357-757d41457d7a"
  style="max-height:640px; min-height: 200px">
</video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- Installers:
  - V1: ~https://1drv.ms/u/s!Al0lwIPqdM2dgql4-5NkWigrmjeU8A?e=lIHd2H~
  - V2: ~https://1drv.ms/u/s!Al0lwIPqdM2dgql7p_gc9DsbDt4New?e=crjT6A~
  - V3: Latest nightly build!
- Pull request: https://github.com/Slicer/Slicer/pull/7562
- Current branch: <https://github.com/Sunderlandkyl/Slicer/tree/interaction_display_manager>
