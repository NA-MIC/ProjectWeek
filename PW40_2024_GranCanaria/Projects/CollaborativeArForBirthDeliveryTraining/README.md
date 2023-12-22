---
layout: pw40-project

permalink: /:path/

project_title: Collaborative AR for birth delivery training
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

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Birth delivery training equips healthcare professionals with the necessary skills and knowledge to handle various scenarios during childbirth, ensuring the safety and well-being of both the mother and the newborn. This specialized training covers a spectrum of techniques, from normal deliveries to emergency interventions, preparing healthcare providers to manage complications effectively. Proper training enhances the capacity to recognize and address potential risks, fostering a timely response in critical situations.

In this project we aim at creating a new solution for birth delivery training based on augmented reality (AR) with Microsoft HoloLens 2 and the work presented in previous Project Week events within the [ARinSlicer](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/ARinSlicer/) project. This work is also available at [this public GitHub repository](https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning.git). With it, it is possible to send real time information between HoloLens 2 and 3D Slicer to leverage the benefits of both platforms.

This time we want to extend the previous work to create a collaborative AR application that connects multiple HoloLens 2 devices to create an interactive system teacher-student to learn basic birth delivery techniques.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A. Describe **what you plan to achieve** in 1-2 sentences.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Create an application in Unity that sends and receives information in real-time with 3D Slicer and directly streams it to 3D Slicer
2.  The application should enable to decide if we want to be the master or the slave (to chose which user will manipulate the virtual information and which one will be limited to visualization). It should be possible to change this option dynamically.
3.  Import all necessary models to the scene in Unity
4.  Register virtual information with a mannequin in real life to provide haptic feedback (use QR code for automatic registration?)
5.  Combine this information with a tracker (EMTS) to record the movement of tools in real life.
6.  Replicate the movement of actual tools in our virtual models using the same OpenIGTLink bridge

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  So far, we have already acomplished objectives 1 to 3.
2.  During the last year we have also worked on objective 4
3.  The next step is to combine all previous works in a single scene and combine all virtual information with actual mannequins

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<video
 controls muted
 src="https://github.com/NA-MIC/ProjectWeek/assets/66890913/1a8500a1-6d84-4599-9cda-557fc288fc83"
 style="max-height:640px; min-height: 200px">
</video>
This video shows our current progress in showing in Unity the information recorded with 3D Slicer.

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
