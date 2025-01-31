---
layout: pw42-project

permalink: /:path/

project_title: 'OHIF Tools: StackScroll for fusion viewport, 4D interaction'
category: Infrastructure

key_investigators:

- name: Joost van Griethuysen
  affiliation: The Netherlands Cancer Institute
  country: The Netherlands

---

# Project Description

<!-- Add a short paragraph describing the project. -->

OHIF viewer is a much used and much developed open source project exposing a fully functional DICOM viewer in React.js.
However some features, such as support for 4D images and fusion may be further improved.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Create or update the StackScroll tool for fusion windows.
Horizontal scrolling should update the opacity of the fusion.

Review window-levelling tools for PET, to allow window-level with
fixed minimum.

Create overlay tools for working with 4D images.
- Selection of split-tag
- Selection of time point to display

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Create local test environment with OHIF viewer, Cornerstone3D tools and data (DONE).

Overlay controls for 4D images were already created in the XNAT-viewer project.
Investigate whether these can be easily implemented in the main project.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

- Identified & reported bugs in Viewport colorbar
  - [#4743](https://github.com/OHIF/Viewers/issues/4743): Mouse action is exactly opposite for PET data, compared to window-level tool in the viewport.
  - [#4744](https://github.com/OHIF/Viewers/issues/4744): Changing colormap of fusion volume applies change to background volume.
- Create PR proposing fix for the 2nd bug ([#4746](https://github.com/OHIF/Viewers/pull/4746)).
- Create Cornerstone3D tool: [ReferenceProbe](https://github.com/JoostJM/cornerstone3D/tree/feat/reference-probe)
  - Using click & dragging in a viewport, show corresponding location in other viewports (jumping slices as necessary).
- Create FusionStackScroll tool: [FusionStackScroll](https://github.com/JoostJM/cornerstone3D/tree/feat/fusion-stack-scroll)
  - Extends StackScroll tool: delta X adjusts opacity of overlay volume in fusion viewport.

### Next Steps:
- Adjust StackScroll to allow switching timepoints in dynamic volume in delta X direction.
  - In case of Dynamic volume, determine directin (X or Y) of largest change --> Only adjust in this direction (i.e. either stack position or timepoint)
- Investigate option of combining multiple tools on the mouse buttons by adding modifiers (Ctrl, Alt).
  - Change cursor on hover + modifier to provide tooltip indicating function.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

## Reference Probe
![Screenshot from 2025-01-31 11-52-14](https://github.com/user-attachments/assets/a79ddaa6-e201-43cf-831d-8b0b4490f388)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- [Ohif main repo](https://github.com/OHIF/Viewers)
- [Cornerstone3D repo](https://github.com/cornerstonejs/cornerstone3D)

