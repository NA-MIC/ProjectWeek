---
layout: pw43-project

permalink: /:path/

project_title: Dedicated CPR View for Dental Panoramic Visualization in 3D Slicer
category: VR/AR and Rendering

key_investigators:

- name: Taeyoung Ted Park
  affiliation: TruAbutment
  country: South Korea

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to design a dedicated Slice View system for Curved Planar Reformation (CPR) visualization in dental imaging, implemented in 3D Slicer.
Although grid transforms can currently be used to simulate panoramic views, this method is structurally limited due to the following:

Transforms are applied at the node level, making it necessary to duplicate volume nodes in order to display CPR and standard views simultaneously.

Integration with other displayable nodes (segmentations, models, markups) is limited, and standard interaction tools such as cursors and slice handles are not functional within the transformed context.

To overcome these limitations, this project focuses on designing a transform-isolated rendering structure — a dedicated CPR World — where transforms are applied per-view and rendering is independent of the global scene configuration.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Design a CPR-specific slice view where transforms can be applied at the view level
- Enable concurrent display of CPR and standard views without duplicating data
- Architect a CPR Scene structure that supports volume sharing and transform isolation
- Ensure compatibility with the GeneralReformat module
- Define a system where CPR state is serializable via the MRML infrastructure
- Plan for future extensibility to support models, markups, segmentations, and measurement tools in the CPR view



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Analyze Current Slicer Architecture
- Study how transforms are currently applied globally to nodes
- Understand internal mechanisms of vtkMRMLSliceNode, vtkMRMLSliceCompositeNode, vtkImageResliceMapper, etc.

2. Design CPR View Structure
- Define a new layout and view context for CPR without interfering with existing Slicer views
- Extend qMRMLLayoutManager to support CPR-specific view identifiers

3. Architect Transform Isolation
- Design a separate MRML scene (CPR Scene) for view-specific transform logic
- Allow data to be shared between scenes while applying transforms only in CPR context

4. Define CPR Slice Rendering Logic
- Generate reslices along user-defined centerlines (splines or markups)
- Design rendering pipelines capable of displaying volumes, overlays, and models along the panoramic curve

5. Plan for GeneralReformat Integration
- Analyze the structure introduced in PR [#8148](https://github.com/Slicer/Slicer/pull/8148) (GeneralReformat module)
- Design interface compatibility for future functional convergence



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

- Analyzed merged PR [#8148](https://github.com/Slicer/Slicer/pull/8148) and structure of GeneralReformat
- Initiate CPR-specific view and layout architecture
- Define class-level design documents and rendering flow



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Example of CPR view (made by 3D Slicer)

![Image](https://github.com/user-attachments/assets/063bd8ef-e9ce-493b-a963-55e178aa429b)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

