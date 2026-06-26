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

During Project Week, we created an initial ROS 2 package for the KIMM Stewart-platform robot, integrated it with SlicerROS2, and developed a Slicer-side custom-control workflow for sending desired platform poses from 3D Slicer to the robot through ROS 2. The project also motivated a generalizable interface for related medical Stewart-platform robots, including the [AIRS RONAVIS-RD platform](https://airsurgical.net/RONAVIS-RD/) for orthopedic fracture reduction.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The objective of this project is to explore and prototype how a parallel robot with custom forward and inverse kinematics can be integrated into the SlicerROS2 and MoveIt-based planning workflow. While current SlicerROS2/MoveIt integration is becoming mature for serial-link manipulators, parallel robots such as Stewart platforms require a different strategy because their kinematics may be provided by an external library rather than by standard MoveIt solvers. During Project Week, we aim to define and demo a practical software architecture for robot visualization, kinematic communication, motion-planning preview, and future execution control from the Slicer interface.

A specific objective is to support two complementary levels of planning for Stewart-platform-like medical robots. The first is pose-space planning of the moving platform from 3D Slicer, followed by custom IK-based validation of actuator feasibility and execution constraints. This level is being prototyped for the KIMM robot. The second, still under development, is a more MoveIt-native integration through custom kinematics and control interfaces, currently being explored with the AIRS orthopedic robot platform.

A broader objective is to make the SlicerROS2 custom-control workflow reusable across related medical Stewart-platform systems, while keeping the 3D Slicer planning interface, ROS 2 communication layer, robot-specific kinematics/control, and clinical application logic separated.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


We reviewed and adjust the existing Stewart-platform code to create a ROS2 package aligned with a standard ROS2 robot architecture, including robot description, transforms, controllers, and interfaces compatible with the MoveIt and ros2_control workflow. This included defining the relevant robot frames, moving platform, actuator representation, needle/probe guide, and joint or actuator interfaces required for visualization, planning, and control.

We are investigating how to connect the robot’s custom forward and inverse kinematics libraries to the MoveIt-based planning workflow. Possible strategies include wrapping the custom FK/IK library as a MoveIt-compatible kinematics plugin, exposing FK/IK through ROS2 services or actions, or using MoveIt for planning-scene management, trajectory preview, and collision checking while handling Stewart-platform-specific kinematics externally.

In parallel, we developed an initial workflow for how to integrate the robot workflow into SlicerROS2. The planned image-guided workflow starts from intraoperative imaging in 3D Slicer, where the user defines a target, entry point, or desired needle/probe trajectory. This trajectory is converted into a desired robot alignment request and sent through the ROS 2/MoveIt interface. The planned robot pose, motion preview, and needle/probe trajectory are then visualized in Slicer before execution.

The current architecture separates three layers: the Slicer-based planning and visualization workflow, the ROS 2/SlicerROS2 robot-communication layer, and the robot-specific implementation. In this structure, Slicer provides image-based planning, target or trajectory definition, transform selection, and visualization; SlicerROS2 provides communication with ROS 2 topics, services, and robot state feedback; and each robot package provides its own kinematics, command modes, controllers, workspace limits, and safety constraints.

For the KIMM robot, the current practical pathway is pose-space planning of the moving platform, followed by IK-based validation of actuator feasibility and execution constraints. For the AIRS robot, joint-state commands are available, supporting a complementary joint-control workflow and ongoing development of a more MoveIt-native integration.

The short-term Project Week goal is to define a practical architecture and initial prototype for connecting SlicerROS2, MoveIt, ros2_control, and the Stewart-platform. Expected outcomes include an updated software architecture, identification of required ROS2 topics/services/actions, a preliminary strategy for custom FK/IK integration, and an initial workflow for visualizing a planned robot alignment from Slicer.


## Progress and Next Steps

1. Created an initial ROS2 package for the KIMM Stewart-platform robot.  
   The package includes a robot description, TF frame representation, virtual joint-state representation for visualization of the closed-chain platform, and command interfaces needed to represent and control the robot from ROS2. Because standard URDF/TF representations do not directly solve closed-chain parallel-robot kinematics, the package uses robot-specific kinematic calculations to update the platform state.

2. Integrated the KIMM robot package with SlicerROS2.  
   The robot can be visualized through the SlicerROS2 workflow, and desired platform poses can be sent from 3D Slicer to ROS2 using a Slicer-side custom-control workflow.

3. Developed a reusable custom-control pattern for Stewart-platform-like medical robots.  
   The 3D Slicer-side interface was structured to separate user-defined planning transforms in 3D Slicer, pose command publication, robot state visualization, and robot-specific command execution. This same pattern is being aligned with the AIRS orthopedic robot platform.

4. Identified two complementary planning levels for parallel robots in SlicerROS2.  
   The first level is pose-space planning of the moving platform, followed by custom IK-based validation of actuator feasibility and execution constraints. This is the current practical approach for the KIMM robot because IK is available, while FK is not currently exposed to the integration. The second level is a more MoveIt-native integration through custom kinematics and control interfaces, which is still ongoing work being explored with the AIRS robot.

5. Identified platform-specific differences that affect planning and control.  
   For the KIMM robot, IK is available and pose-space commands are the current practical pathway, but full joint-space planning is limited by the available kinematic interface. For the AIRS robot, joint-state commands are available, enabling a complementary joint-control workflow and supporting ongoing development toward a MoveIt plugin.

Next steps include refining the KIMM pose-space planning and IK-validation workflow, improving visualization of current and desired platform poses in Slicer, adding clearer robot-state and command-status feedback, and continuing development/testing of custom MoveIt integration strategies for Stewart-platform robots.


# Illustrations

<img width="1024" height="768" alt="WhatsApp Image 2026-06-26 at 8 52 27 AM" src="https://github.com/user-attachments/assets/8ae6776e-d66d-4ec7-b534-601c1b0343a2" />

<img width="782" height="788" alt="Screenshot from 2026-06-26 08-57-00" src="https://github.com/user-attachments/assets/21fea214-60c4-4809-9628-6d33579015de" />

<img width="782" height="788" alt="Screenshot from 2026-06-26 08-57-33" src="https://github.com/user-attachments/assets/fcc16071-4b6a-4165-af2f-083ae59711d1" />

<img width="783" height="848" alt="Screenshot from 2026-06-26 08-56-15" src="https://github.com/user-attachments/assets/30f9fffa-d999-4eb5-85e4-7302d837f586" />


# Background and References



# Funding
NIH R01EB020667
NIH R01CA235134
BWH Department of Radiology GR0131914
