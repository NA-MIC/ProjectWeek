---
layout: pw44-project

permalink: /:path/

project_title: Collaborative AR application using OpenIGTLink, 3D Slicer and Magic Leap 2
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Alicia Pose Díez de la Lastra
  affiliation: Universidad Carlos III de Madrid
  country: Madrid, Spain

- name: Javier Pascau
  affiliation: Universidad Carlos III de Madrid
  country: Madrid, Spain

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Ron Kikinis
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


In previous Project Weeks, we showed a way to communicate Microsoft HoloLens 2 with 3D Slicer using OpenIGTLink protocol. The current solution is implemented in a 3 elements system. It is composed by A Microsoft HoloLens 2 headset, the Unity software, and the 3D Slicer platform. The HoloLens 2 application is not directly built on the device, but remotely transferred from Unity in real time using Holographic Remoting. The communication workflow is represented in the following image:

![image](https://github.com/NA-MIC/ProjectWeek/assets/66890913/6be8aff6-c4e8-48f1-a5ce-dfebff0dc0df)

The results of that work are publicly available at [this GitHub repository](https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning).


In more recent Project Weeks we evaluated the transferability of the aforementioned project to other AR devices. Specifically, we focused on the VARJO XR-3 headset, obtaining fast and high-quality results:

<video
  controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/66890913/c0fa7cd4-eadc-4721-bb1d-b78695e5ead6"
  style="max-height:640px; min-height: 200px">
  </video>

<video
  controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/66890913/8f257f29-fa9c-4319-8c49-4138003eba27"
  style="max-height:640px; min-height: 200px">
</video>

This time, we aim to follow a similar approach, this time with Magic Leap 2, with the ultimate goal of creating a colaborative application between multiple headsets communicating through OpenIGTLink.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A: Adapt previous Unity apps to Magic Leap 2.
2. Objective B: Exchange information between Magic Leap 2 and 3D Slicer.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Adapt previous Unity apps to Magic Leap 2.
2. Test Holographic Remoting in Magic Leap 2.
3. Test the exchange of information between Magic Leap 2 and 3D Slicer.
4. Add a new headset to the system and try to exchange information between HoloLens 2 and Magic Leap 2 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Bring both a HoloLens 2 and a Magic Leap 2 headsets to PW.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

