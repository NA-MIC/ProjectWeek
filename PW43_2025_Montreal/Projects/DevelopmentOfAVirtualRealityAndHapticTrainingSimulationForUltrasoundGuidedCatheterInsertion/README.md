---
layout: pw43-project

permalink: /:path/

project_title: Development of a virtual reality and haptic training simulation for ultrasound-guided
  catheter insertion
category: VR/AR and Rendering

key_investigators:

- name: Naomi Catwell
  affiliation: ÉTS
  country: Canada

- name: Simon Drouin
  affiliation: ÉTS
  country: Canada

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

- name: Steve Pieper
  affiliation: Isomics
  country: Inc., United States

---

# Project Description

<!-- Add a short paragraph describing the project. -->


**Context**
Ultrasound-guided IV catheter insertion is the most commonly performed medical procedure in hospitals. However, it has been associated with high complication rates. Virtual reality and haptic enabled simulations may improve training for such a procedure. The aim of this project is to evaluate the effectiveness of haptic feedback for ultrasound-guided peripheral IV insertion training in a virtual reality simulation. 

**Current state**
A virtual reality training and evaluation simulator equipped with real-time ultrasound image rendering and a haptic force feedback model has been developed with Unity and two Haply Robotics Inverse3 devices. 

**Project Week**
In the context of Project Week, the aim is to improve the simulation with skin deformation physics using [SOFA-Slicer](https://github.com/Slicer/SlicerSOFA). This would improve perception of depth and identification of the needle insertion point in the virtual environment.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Integration of SOFA-Slicer Project into the Unity simulation
2. Simulation of believable skin deformation with SOFA physics



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Get a working version of a recent SOFA-Slicer version on Windows. See this [forked version of Slicer-SOFA ](https://github.com/pieper/SlicerSOFA) and lungsimple.py sample project
2. Re-integrate SOFA with the existing simulation - use SOFA version 24.12
3. Define an interactive SOFA configuration file to simulate forearm skin deformation in Unity
4. Integrate a version of Slicer-SOFA into the Slicer configuration file of the simulation
5. Work with SOFA-Slicer project team 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. [Project Week 41](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SOFAUnityHapticModel/) - familiarisation with SOFA and a first integration of SOFA into Unity



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://github.com/user-attachments/assets/6d74833a-af17-41ed-9cbe-fd084dabb651)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

