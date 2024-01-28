---
layout: pw40-project

permalink: /:path/

project_title: Common spline surfaces infrastructure for surgical planning in Slicer-Heart and Slicer-Liver
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Gabriella D'Albenzio
  affiliation: Oslo University Hospital
  country: Norway

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

- name: Csaba Pinter
  affiliation: Ebatinca
  country: Spain

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The primary goal is to unify the spline surface infrastructures of Slicer-Liver and Slicer-Heart, focusing on the integration of Bezier tensor product surfaces and NURBS tensor product surfaces. This integration aims to create a versatile and robust tensor-product surface filter capable of generating a variety of surface families.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  **Development of a Generic Tensor-Product Surface Filter:**\
    Explore the feasibility of creating a filter that can handle both Bezier and NURBS surfaces, along with other potential surface types.

2.  **Establishment of a Class Hierarchy:**\
    Discuss the design of a class hierarchy that effectively supports different spline surface families. This includes determining the commonalities and differences between the current implementations in Slicer-Heart and Slicer-Liver.

3.  **Creation of a Common Extension Framework:**\
    Aim to develop a common extension framework that can be readily adapted for future extensions, ensuring scalability and flexibility.

4.  **Integration with vtkAddon/VTK:**\
    Consider how this new infrastructure could potentially be incorporated into the vtkAddon or VTK libraries, enhancing the broader community's access to these tools.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

*   **Research and Analysis:**\
    Conduct an analysis of the existing spline surface implementations in Slicer-Heart and Slicer-Liver. Identify the key features, limitations, and potential areas of synergy.

*   **Design and Development:**\
    Develop a detailed plan for the implementation, including the architecture of the generic tensor-product surface filter and an eventual class hierarchy.

*   **Plan for further development:**\
    As a common spline infrastructure could be useful in contexts wider than IGT, plan for further integration of this infrastructure in vtkAddon / VTK.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

TBD

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![heart-NURBS](https://github.com/NA-MIC/ProjectWeek/assets/1978682/756b9f13-d359-4f58-a556-3eca7dc813c3)

![liver_bezier](https://github.com/NA-MIC/ProjectWeek/assets/1978682/ade0e3cc-b44c-465e-ad6b-6ac2d2c1f78b)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

1.  [Slicer-Liver](https://github.com/ALive-research/Slicer-Liver)
2.  [Slicer-Heart](https://github.com/SlicerHeart/SlicerHeart)
3.  <https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/>
