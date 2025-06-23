---
layout: pw43-project

permalink: /:path/

project_title: Real-Time Point Cloud Streaming to 3D Slicer via OpenIGTLink
category: Infrastructure

key_investigators:

- name: Vitor Azevedo Padovani
  affiliation: Researcher
  country: Brazil

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project explores the real-time streaming of dynamic 3D point clouds or surfaces to 3D Slicer using OpenIGTLink and OpenIGTLinkIO. The goal is to generate synthetic time-varying surface data (e.g., a deforming mesh or animated point cloud), package it as VTK PolyData, and transmit it to Slicer for visualization and possible downstream processing. This will also allow benchmarking the performance of OpenIGTLinkIO versus the traditional OpenIGTLink API for sending non-transform data types like surfaces.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. **Objective A.** Implement a function to generate time-varying surface data (e.g., a sinusoidal wave or morphing geometry).
2. **Objective B.** Package this data into vtkPolyData and stream it to Slicer in real time using OpenIGTLinkIO.
3. **Objective C.** Test the same setup with the original OpenIGTLink library and compare performance.
4. **Objective D.** Evaluate the responsiveness, latency, and frame rates when visualizing dynamic surface data in Slicer.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a C++ module that synthesizes a point cloud or surface that varies over time (e.g., a wave surface or a breathing-like deformation).
2. Use vtkPolyData to store the generated geometry at each time step.
3. Integrate OpenIGTLinkIO to send this PolyData to a 3D Slicer scene using an appropriate device type (e.g., Mesh or PolyData device).
4. Validate the rendering in Slicer, ensuring correct reception and visualization.
5. Repeat the above using the standard OpenIGTLink library and measure latency, throughput, and CPU usage.
6. Record performance differences and summarize findings.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


- Local development environment with OpenIGTLinkIO, VTK, and 3D Slicer already set up



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

