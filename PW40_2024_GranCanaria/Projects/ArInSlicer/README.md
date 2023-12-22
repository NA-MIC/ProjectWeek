---
layout: pw40-project

permalink: /:path/

project_title: AR in Slicer
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Alicia Pose Díez de la Lastra
  affiliation: Universidad Carlos III de Madrid

- name: Mónica García Sevilla
  affiliation: Universidad Carlos III de Madrid

- name: Javier Pascau
  affiliation: Universidad Carlos III de Madrid

---

# Project Description

<!-- Add a short paragraph describing the project. -->

In previous Project Week events we have already presented our project [AR in Slicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/). On it, we managed to establish a communication bridge between Microsoft HoloLens 2 and 3D Slicer using OpenIGTLink communication protocol.

To achieve this, we created our own custom-made client-side socket in Unity using C# programming language. Nevertheless, our solution presented some computational limitations and only allowed to send image and geometrical transform messages. Recently, we have found a way to execute python scripts from Unity platform.

The purpose of this project is to explore this methodology to transfer the whole OpenIGTLink protocol, available in Python language, to Unity. Ultimately, we want to offer the possibility to work with the complete set of OpenIGTLink to enable the creation of more complete AR applications.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Incorporate OpenIGTLink communication protocol defined in Python language into Unity

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Read existing literature on the utilization of Python in Unity
2.  Transfer Python scripts defining OpenIGTLink protocol to an empty Unity project
3.  Test their functioning in an application similar to the one presented in [AR in Slicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/) - Also available in [this GitHub repository](https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning.git).

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  We have already identified useful literature regarding this topic.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
