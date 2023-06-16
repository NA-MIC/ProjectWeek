---
layout: pw39-project

permalink: /:path/

project_title: AR in Slicer
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Alicia Pose Díez de la Lastra
  affiliation: Universidad Carlos III de Madrid
  country: Madrid, Spain

- name: Simon Drouin
  affiliation: 'École de Technologie Supérieure '
  country: Montreal , Canada
  
- name: Jose Carlos Mateo Pérez
  affiliation: 'Universidad de Las Palmas de Gran Canaria'
  country: Gran Canaria , Spain
  
- name: Pablo Sergio Castellano Rodríguez
  affiliation: 'Universidad de Las Palmas de Gran Canaria'
  country: Gran Canaria , Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Microsoft HoloLens 2 has demonstrated to be an excellent device in many clinical applications. They are mainly used to display 3D patient-related virtual information overlaid to the real world. However, its processing capacity is quite limited, so developing complex applications that require medical image processing is quite convoluted.

A good solution could be to perform the difficult computations on a specialized software on a computer (i.e. 3D Slicer) and send them in real time to HoloLens 2 so that it can focus solely on visualization.
Up to date, there has been a lack of software infrastructure to connect 3D Slicer to any augmented reality (AR) device.

During the last year, [Universidad Carlos III de Madrid](https://igt.uc3m.es/augmented-reality/) (Madrid, Spain) and Perk Lab in Queen's University have worked together to develop a novel connection approach between Microsoft HoloLens 2 and 3D Slicer using OpenIGTLink.

The results of that work are publicly available at [this GitHub repository](https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning).

The current solution is implemented in a 3 elements system. It is composed by A Microsoft HoloLens 2 headset, the Unity software, and the 3D Slicer platform.
The HoloLens 2 application is not directly built on the device, but remotely transferred from Unity in real time using Holographic Remoting.

![image](https://github.com/NA-MIC/ProjectWeek/assets/66890913/6be8aff6-c4e8-48f1-a5ce-dfebff0dc0df)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Evaluate the transferability of the aforementioned project to other AR devices. Specifically, we'll focus on the VARJO XR-3 headset.
![Varjo headset](https://github.com/NA-MIC/ProjectWeek/assets/66890913/d731d842-0809-466f-b676-bf9d728f911e)

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Connect Varjo headset to Unity.
2.  Find a way to remotely render information from Unity to the headset.
3.  3D Slicer creates an OpenIGTLink server.
4.  Unity, containing the AR application, creates an OpenIGTLink client that connects to the server.
5.  Currently, when the application is executed in the Unity editor, it starts sending and receiving messages from 3D Slicer. Simultaneously, it wirelessly streams the app to Microsoft HoloLens 2 using Holographic Remoting. Try to replicate the same with Varjo.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

So far, everything works for HoloLens 2. Our current application transfers geometrical transform and image messages between the platforms.
It displays CT reslices of a patient in the AR device. The user wearing the glasses can manipulate the CT plane to see different perspectives.
The application was build for pedicle screw placement planning.

![20221213_161232_HoloLens](https://user-images.githubusercontent.com/66890913/212931527-035baf4c-4799-4d83-9c60-b8a0f839547e.jpg)

Our main goal for this week is to replicate the exact same application in the new device.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Check out our app in [this GitHub repository](https://github.com/BIIG-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning).
This repository contains all the resources and code needed to replicate our work in your computer.

Transfer of geometrical transforms from HoloLens 2 to 3D Slicer:

![MovingSpine_GIF](https://user-images.githubusercontent.com/66890913/214097820-96b9f875-4651-4efd-879b-831eb88b7b07.gif)

Transfer of images from 3D Slicer to HoloLens 2:

![MovingCT_GIF](https://user-images.githubusercontent.com/66890913/214097469-17a1aa1a-2768-4f73-8c12-bb4ab7d393f0.gif)


# Results
It worked!

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


# Conclusions
The system seems to be easily transferable to any AR or VR headset as long as it can be connected to Unity, either via wifi or with a cable










