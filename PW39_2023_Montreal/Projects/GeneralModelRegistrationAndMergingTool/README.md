---
layout: pw39-project

permalink: /:path/

project_title: General model registration and merging tool
category: VR/AR and Rendering

key_investigators:

- name: Chi Zhang
  affiliation: Seattle Children's Research Institute
  country: USA

- name: Arthur Porto
  affiliation: Louisiana State University
  country: USA

- name: Sara Rolfe
  affiliation: Seattle Children's Research Institute
  country: USA

- name: Murat Maga
  affiliation: University of Washington
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

We are working on developing a general purpose model registration tool in Slicer. At this moment, I developed a simple test module (<https://github.com/chz31/registration_test>) using rigid registration functions (RANSAC + ICP) from Open3D and new ITK-based ALPACA module. This can allow people to test registration for purposes such as ALPACA automated landmarking.

We are thinking about expanding this module into its own system for other purposes related to model registrations. One purpose is to register and align models that represent different parts of an object with overlapping area, and fuse them together. This could be useful for some purposes. For example, it would allow align and fuse models acquired from different angles, such as different parts of an object acquired by photogrammetry techniques. It would also allow virtual fossil reconstruction, which is usually done using commercial software such as Geomagic Studio.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Develop a general purpose model registration tool in Slicer. Adding more utilities, such as a parameter adjustment tab.
2.  Add new functions for other purposes related to model registration. At this moment, we are thinking about how to align models that represent different parts of an object and fuse them together. This could be useful for photogrammetry and virtual fossil reconstruction.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Add parameter adjustment tab for the current test version
2.  Merge registered models that represent different parts of an object into one. One way to aid the alignment is allow users to place a few matching landmarks on two or more models.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Current testing version is here: <https://github.com/chz31/registration_test>. It uses rigid registration functions (RANSAC + ICP) from Open3D and new ITK-based ALPACA module.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

These are the models acquired by photogrammetry from two angles. The yellow one has no top, and the red one has no bottom. Rigid registration from Open3D can align them pretty well, though not perfect.

A sample virtual reconstruction in Geomagic Studio. The skull missed a part at the right side. The yellow part is the mirror image of the counter part at the left side.

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Current testing version is here: <https://github.com/chz31/registration_test>. It uses rigid registration functions (RANSAC + ICP) from Open3D and new ITK-based ALPACA module.

ALPACA module (including the ITK version) repository: <https://github.com/SlicerMorph/SlicerMorph/tree/master/ALPACA>

ALPACA tutorial: <https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA>

Open3D rigid registration utilized in ALPACA: <http://www.open3d.org/docs/release/tutorial/pipelines/global_registration.html>
