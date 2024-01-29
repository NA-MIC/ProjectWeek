---
layout: pw40-project

permalink: /:path/

project_title: AR in Slicer
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Alicia Pose Díez de la Lastra
  affiliation: Universidad Carlos III de Madrid
  country: Spain

- name: Mónica García Sevilla
  affiliation: Universidad Carlos III de Madrid
  country: Spain

- name: Javier Pascau
  affiliation: Universidad Carlos III de Madrid
  country: Spain

- name: Felix von Haxthausen
  affiliation: Universidad Carlos III de Madrid
  country: Spain

- name: Amaia Iribar Zabala
  affiliation: Fundación Vicomtech

- name: Rafael Benito Herce
  affiliation: Fundación Vicomtech
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->

In previous Project Week events we have already presented our project [AR in Slicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/). On it, we managed to establish a communication bridge between Microsoft HoloLens 2 and 3D Slicer using OpenIGTLink communication protocol.

To achieve this, we created our own custom-made client-side socket in Unity using C# programming language. Nevertheless, our solution presented some computational limitations and only enable the exchange of one message of each kind (one transform and one image).

This project aims to optimize this issue. One option is to optimize how the system currently works with our C# scripts. Alternatively, we can explore the incorporation of the native OpenIGTLink scripts defined in Python or C++ language.

To give some context to the project, we focus this time on Birth Delivery Training. Birth delivery training equips healthcare professionals with the necessary skills and knowledge to handle various scenarios during childbirth, ensuring the safety and well-being of both the mother and the newborn. This specialized training covers a spectrum of techniques, from normal deliveries to emergency interventions, preparing healthcare providers to manage complications effectively. Proper training enhances the capacity to recognize and address potential risks, fostering a timely response in critical situations.

In this project we aim at creating a new solution for birth delivery training based on an optimized version of the previous [AR in Slicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/) project. This new app will enable collaborative teacher-student interaction with the holograms for a better learning experience. 

## Objective

This project has a double purpose:

1.  Optimize the message exchange by the platforms. One option for that is to explore the incorporation of OpenIGTLink protocol in Python language into the Unity project.
   1.1. Ultimately, we could to offer the possibility to work with the complete set of OpenIGTLink to enable the creation of more complete AR applications.
2.  Create a collaborative AR application that connects multiple HoloLens 2
   2.1. We focus on the field of birth delivery training. In this app, a teacher can show the birth delivery maneuvers to a student using this AR system.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Read existing literature on the utilization of Python in Unity
2.  Transfer Python scripts defining OpenIGTLink protocol to an empty Unity project
3.  Test their functioning in an application similar to the one presented in [AR in Slicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/) - Also available in [this GitHub repository](https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning.git).
4.  Create an application in Unity that can share multiple messages with 3D Slicer. The application should enable to decide if we want to be the master or the slave (to chose which user will manipulate the virtual information and which one will be limited to visualization). It should be possible to change this option dynamically.
5.  Import all necessary models to the scene in Unity
6.  Register virtual information with a mannequin in real life to provide haptic feedback
7.  Combine this information with a tracker (EMTS) to record the movement of tools in real life.
8.  Replicate the movement of actual tools in our virtual models using the same OpenIGTLink bridge

## Progress and Next Steps

1.  We have already identified useful literature regarding this topic.
2.  We already have all mannequins and some prerecorded maneuvers.

# Illustrations

<video
 controls muted
 src="https://github.com/NA-MIC/ProjectWeek/assets/66890913/1a8500a1-6d84-4599-9cda-557fc288fc83"
 style="max-height:640px; min-height: 200px">
</video>
Although a little bit step-py, this video shows our current progress in the Birth Delivery Training app. (Transform messages are being sent from 3D Slicer to Unity)

# Background and References

All source code for the [AR in Slicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/) project is contained in [this GitHub repository](https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning.git)
