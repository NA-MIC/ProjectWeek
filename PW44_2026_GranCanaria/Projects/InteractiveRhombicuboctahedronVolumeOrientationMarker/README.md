---
layout: pw44-project

permalink: /:path/

project_title: Interactive rhombicuboctahedron volume orientation marker
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Make an orientation marker for OHIF whose 26 surfaces (6 faces, 8 corners and 12 edges) can be clicked to reorient the volume in 3D/VRT viewport.

<img width="339" height="293" alt="Image" src="https://github.com/user-attachments/assets/d9a50e00-74ba-4549-93a7-6d34229c4c18" />



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Enhanced usability of 3D viewport.  
Provide volume orientation control when the rotate tool is rotating the clipping planes.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Seek advice on implementation (VTK, cornerstone,....)




## Progress and Next Steps



## Orientation Controller Tool with VTK Widget Approach

### Summary

Adds an interactive orientation controller for 3D volume viewports using a VTK.js widget. Provides a clickable 26-faced polyhedron (rhombicuboctahedron) for reorienting the camera and visualizing orientation.

### Description

The OrientationController tool displays an interactive orientation marker in volume3d viewports. Users can click faces to reorient the camera and see the current orientation.

### VTK Widget Approach

Uses a VTK.js-based widget architecture:

#### Architecture Overview

1. **`vtkOrientationControllerWidget`** (`packages/tools/src/utilities/vtkjs/OrientationControllerWidget/`)
   - Core widget managing VTK actors and interaction
   - Creates and manages `vtkActor` instances for the polyhedron
   - Handles mouse picking via `vtkCellPicker`
   - Manages actor lifecycle (add/remove from viewports)
   - Handles positioning and sizing relative to viewport corners

2. **`AnnotatedRhombicuboctahedronActor`** (`packages/tools/src/utilities/vtkjs/AnnotatedRhombicuboctahedronActor/`)
   - Generates the 26-faced polyhedron geometry
   - Creates VTK actors with textured faces and labels
   - Supports main faces (6), edge faces (12), and corner faces (8)
   - Applies anatomical labels (L/R, A/P, S/I) using LPS convention

3. **`OrientationController` Tool** (`packages/tools/src/tools/OrientationController.ts`)
   - Cornerstone3D tool extending `BaseTool`
   - Wraps the VTK widget for integration
   - Manages tool lifecycle (enable/disable)
   - Handles configuration updates and viewport synchronization

[Test in OHIF](https://na-mic-projectweek44-g0g4a5c5dgc5dcf3.westeurope-01.azurewebsites.net/viewer?StudyInstanceUIDs=2.16.840.1.114362.1.11972228.22789312658.616067305.306.2&hangingProtocolId=primary3D)


<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->





# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img width="1438" height="1004" alt="image" src="https://github.com/user-attachments/assets/fcb867a9-42dd-417f-951d-2e0bf3c03a05" />

_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

# Acknowledgements

This project is supported by [Frei Universitat Berlin](https://www.fu-berlin.de/en/index.html)


_No response_

