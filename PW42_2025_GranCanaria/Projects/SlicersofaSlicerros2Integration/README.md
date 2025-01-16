---
layout: pw42-project

permalink: /:path/

project_title: SlicerSOFA - SlicerROS2 Integration
category: Infrastructure

key_investigators:

- name: Eléonore Germond
  affiliation: IMT Atlantique
  country: France

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

- name: Paul Baksic
  affiliation: Inria
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: US

- name: Junichi Tokuda
  affiliation: Brigham and Women's Hospital
  country: US

- name: Laura Connolly
  affiliation: Queen's University
  country: Canada

- name: Anton Deguet
  affiliation: Johns Hopkins University
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


SlicerSOFA and SlicerROS2 are two 3D Slicer extensions that bridge mechanical simulations and robotic applications with 3D Slicer. Their recent addition to the 3D Slicer ecosystem opens up new possibilities for developing robotic applications that simulate interactions with medical environments.

In this project, we aim to create a proof-of-concept integration where a Phantom Omni, controlled by SlicerROS2, interacts with a soft organ through SlicerSOFA. We will examine and discuss aspects such as the interface between ROS and SOFA, as well as performance considerations, to guide the future development of robotic applications that integrate simulated environments in 3D Slicer.

![https://camo.githubusercontent.com/03c3af0d069321004f86294efe09f49df1236aaa1a5bc49857367b28994e3f59/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f6b335647733059614533672f6d617872657364656661756c742e6a7067](https://camo.githubusercontent.com/03c3af0d069321004f86294efe09f49df1236aaa1a5bc49857367b28994e3f59/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f6b335647733059614533672f6d617872657364656661756c742e6a7067)
(source: [https://github.com/rosmed/slicer_ros2_module](https://github.com/rosmed/slicer_ros2_module))


 <video
   controls muted
   src="https://github.com/user-attachments/assets/2b5eb319-ef50-43da-b2fe-2865613839f3"
   style="max-height:640px; min-height: 200px">
 </video>




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A: Creating a 3D Slicer-based setup including SlicerROS2 and SlicerSOFA, able to provide with interaction between a robot model and a soft organ




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Setting up a base 3D Slicer, SlicerROS2 and SlicerSOFA.
2. Loading a Phantom Omni robot model (https://slicer-ros2.readthedocs.io/en/latest/pages/robot-visualization.html#phantom-omni).
3. Creating a SOFA simulation for interaction between the robot and a soft organ.
4. Bridging the robot manipulation with the simulation using SlicerSOFA.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


-  Connolly L, Kumar AS, Mehta KK, Al-Zogbi L, Kazanzides P, Mousavi P, Fichtinger G, Krieger A, Tokuda J, Taylor RH, Leonard S, Deguet A. SlicerROS2: A Research and Development Module for Image-Guided Robotic Interventions. IEEE Trans Med Robot Bionics. 2024 Nov;6(4):1334-1344. doi: 10.1109/TMRB.2024.3464683
- SawSensablePhantom repository: https://github.com/jhu-saw/sawSensablePhantom
- Phantom Omni in SlicerROS2: https://slicer-ros2.readthedocs.io/en/latest/pages/robot-visualization.html#phantom-omni
- SlicerSOFA repository: https://github.com/Slicer/SlicerSOFA

