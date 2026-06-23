---
layout: pw45-project

permalink: /:path/

project_title: Integrating a Parallel Robot into SlicerROS2 with MoveIt-Based Planning for Image-Guided
  Needle Procedures
category: IGT and Training
presenter_location: 

key_investigators:

- name: Mariana Bernardes
  affiliation: BWH
  country: USA

- name: Joonho Seo
  affiliation: Korea Institute of Machinery Materials
  country: Republic of Korea

- name: Junichi Tokuda
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to integrate a Stewart-platform parallel robot into the [SlicerROS2](https://github.com/rosmed/slicer_ros2_module) ecosystem for image-guided biopsy and ablation procedures. The robot, developed by collaborator Dr. Joonho Seo at KIMM, will be controlled using [ROS2](https://www.ros.org/) and and can align a needle or ablation probe based on patient intraoperative imaging. By integrating robot visualization and motion-planning preview into the 3D Slicer interface, we aim to allow the user to visualize the planned robot motion and probe trajectory before execution. This integration will also provide a foundation for future closed-loop robotic control using medical imaging feedback.

In parallel, we aim to define an architecture that can be extended to other medical Stewart-platform robotic systems with custom kinematics, including the [AIRS RONAVIS-RD platform](https://airsurgical.net/RONAVIS-RD/) for orthopedic fracture reduction.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


The objective of this project is to explore and prototype how a parallel robot with custom forward and inverse kinematics can be integrated into the SlicerROS2 and MoveIt-based planning workflow. While current SlicerROS2/MoveIt integration is getting mature for serial-link manipulators, parallel robots such as Stewart platforms require a different strategy because their kinematics may be provided by an external library rather than by standard MoveIt solvers. During Project Week, we aim to define and demo a practical software architecture for robot visualization, kinematic communication, motion-planning preview, and future execution control from the Slicer interface.

A secondary objective is to make this architecture reusable across related medical Stewart-platform systems, including the KIMM robot for image-guided biopsy and ablation and the [AIRS](https://airsurgical.net) RONAVIS-RD orthopedic robot platform for fracture-reduction guidance.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We will first review and adjust the existing Stewart-platform code to create a ROS2 package aligned with a standard ROS2 robot architecture, including robot description, transforms, controllers, and interfaces compatible with the MoveIt and ros2_control workflow. This will include defining the relevant robot frames, moving platform, actuator representation, needle/probe guide, and joint or actuator interfaces required for visualization, planning, and control.

We will then investigate how to connect the robot’s custom forward and inverse kinematics libraries to the MoveIt-based planning workflow. Possible strategies include wrapping the custom FK/IK library as a MoveIt-compatible kinematics plugin, exposing FK/IK through ROS2 services or actions, or using MoveIt for planning-scene management, trajectory preview, and collision checking while handling Stewart-platform-specific kinematics externally.

In parallel, we will explore how to integrate the robot workflow into SlicerROS2. The planned image-guided workflow starts from intraoperative imaging in 3D Slicer, where the user defines a target, entry point, or desired needle/probe trajectory. This trajectory is converted into a desired robot alignment request and sent through the ROS 2/MoveIt interface. The planned robot pose, motion preview, and needle/probe trajectory are then visualized in Slicer before execution.

The short-term Project Week goal is to define a practical architecture and initial prototype for connecting SlicerROS2, MoveIt, ros2_control, and the Stewart-platform. Expected outcomes include an updated software architecture, identification of required ROS2 topics/services/actions, a preliminary strategy for custom FK/IK integration, and an initial workflow for visualizing a planned robot alignment from Slicer.

The software architecture will be designed to separate the clinical-based workflow, the ROS 2/MoveIt robot-integration layer, and the robot hardware-specific implementation. This separation will make it easier to adapt the workflow from the KIMM needle-guidance robot to related medical Stewart-platform systems, including the AIRS platform, while allowing each robot to provide its own kinematics, controllers, workspace limits, safety constraints.


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

