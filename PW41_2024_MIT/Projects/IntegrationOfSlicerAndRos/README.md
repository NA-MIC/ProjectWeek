---
layout: pw41-project

permalink: /:path/

project_title: Integration of Slicer and ROS
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Junichi Tokuda
  affiliation: BWH

- name: Anton Deguet
  affiliation: JHU

- name: Steve Pieper
  affiliation: Isomics

- name: Mariana Bernardes
  affiliation: BWH

- name: Laura Connolly
  affiliation: Queen's University

- name: Simon Leonard
  affiliation: JHU

---

# Project Description

SlicerROS2 is an extension that enables direct communication between the Robot Operating System 2 (ROS2) and 3D Slicer. The ROS is a set of software libraries and tools for building robot applications. ROS2 has been developed and distrubted using an open-source model and widely used in the robotics community. The goal of SlicerROS2 is to facilitate the integration of 3D Slicer and ROS to build systems for image-guided robot-assisted intervention. 

SlicerROS2 provides UI and API to communicate with other ROS nodes through Data Distribution Service (DDS), the publish-subscribe data transport middleware used in ROS2, allowing 3D Slicer to sychnonize its scen graph (MRML) with ROS's [tf](https://wiki.ros.org/tf2). It also has an interface to load a visual model of the robot onto the Slicer scene from robot description data in the URDF format published on the ROS system. 

## Objective

The objectives of this project are as follows:
1. **Improve existing implementation based on feedback from Slicer experts.** We will discuss use-cases with current and potential users in the community.
2. **Explore options for binary distribution.** Since the module must be built against 3D Slicer with system SSL and specific versions of ROS2, it is not possible to be built as part of the nightly build process.


## Approach and Plan

Questions discuss during the week:
- Questions of future use
  - Limited to robots or anything with a ROS2 interface (e.g. haptic devices, IMU, optical and magnetic trackers…)
  - Other software packages: [Gazebo](https://gazebosim.org/home), [AMBF](https://github.com/WPI-AIM/ambf), US/CT/MRI simulators…

- Detailed questions
  - Is multithreading possible?  Any other way to trigger a periodic computing task (now using QtTimer)
  - vtkObjects all have a name and timestamp.  Is the name used in Slicer?  Can we have a timestamp that is not a counter?
  - Improving unit testing, we have some but implementation seems clunky
  - For binary distributions, is there a way to host build and/or tgz files?  I can host build on JHU computers.
  - Is there an existing way to document code in modules, e.g. doxygen
  - Small issues: QLatinString in 2 places breaks compiling on older Qt and likely useless, some missing const


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


_No response_

