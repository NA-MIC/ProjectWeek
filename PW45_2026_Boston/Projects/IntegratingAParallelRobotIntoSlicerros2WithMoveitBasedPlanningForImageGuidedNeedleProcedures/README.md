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

This project aims to integrate a Stewart-platform parallel robot into the [SlicerROS2](https://github.com/rosmed/slicer_ros2_module) ecosystem for image-guided biopsy and ablation procedures. The robot, developed by collaborator Dr. Joonho Seo at KIMM, will be controlled using [ROS2](https://www.ros.org/) and and can align a needle or ablation probe based on patient intraoperative imaging. By integrating robot visualization and motion-planning preview into the 3D Slicer interface, we aim to allow the user to visualize the planned robot motion and probe trajectory before execution. This integration will also provide a foundation for future closed-loop robotic control using medical imaging feedback.

During Project Week, we created an initial ROS 2 package for the KIMM Stewart-platform robot, integrated it with SlicerROS2, and developed a Slicer-side custom-control workflow for sending desired platform poses from 3D Slicer to the robot through ROS 2. The project also motivated a generalizable interface for related medical Stewart-platform robots, including the [AIRS RONAVIS-RD platform](https://airsurgical.net/RONAVIS-RD/) for orthopedic fracture reduction.


## Objective

The objective of this project is to explore and prototype how a parallel robot with custom forward and inverse kinematics can be integrated into the SlicerROS2 and MoveIt-based planning workflow. While current SlicerROS2/MoveIt integration is becoming mature for serial-link manipulators, parallel robots such as Stewart platforms require a different strategy because their kinematics may be provided by an external library rather than by standard MoveIt solvers. During Project Week, we aim to define and demo a practical software architecture for robot visualization, kinematic communication, motion-planning preview, and future execution control from the Slicer interface.

A specific objective is to support two complementary levels of planning for Stewart-platform-like medical robots. The first is pose-space planning of the moving platform from 3D Slicer, followed by custom IK-based validation of actuator feasibility and execution constraints. This level is being prototyped for the KIMM robot. The second, still under development, is a more MoveIt-native integration through custom kinematics and control interfaces, currently being explored with the AIRS orthopedic robot platform.

A broader objective is to make the SlicerROS2 custom-control workflow reusable across related medical Stewart-platform systems, while keeping the 3D Slicer planning interface, ROS 2 communication layer, robot-specific kinematics/control, and clinical application logic separated.


## Approach and Plan

We plan to develop a ROS2 package for the KIMM Stewart-platform robot and align it with a standard ROS2 robot architecture. The package will include a robot description, TF frame representation, virtual joint-state representation, and command interfaces for SlicerROS2 integration.

The technical approach is to represent the Stewart platform in ROS2 in a way that supports visualization and command exchange, while keeping the closed-chain kinematics handled by robot-specific code. Because standard URDF/TF representations do not directly solve closed-chain parallel-robot kinematics, the robot package will expose a simplified visualization and state interface to SlicerROS2, while using custom kinematic calculations for platform pose and actuator feasibility.

We plan to investigate two complementary planning strategies for Stewart-platform robots. For the KIMM robot, the near-term strategy is pose-space planning of the moving platform, followed by IK-based validation of actuator feasibility and execution constraints. In parallel, we plan to review the AIRS robot architecture as a related medical Stewart-platform system with different kinematic and command interfaces, including joint-state command capability.

We also plan to develop a SlicerROS2 custom-control workflow that will allow a user-defined planning transform in 3D Slicer to be sent to the robot through ROS2. The broader architectural approach is to separate the Slicer-based planning and visualization workflow, the ROS2/SlicerROS2 communication layer, and the robot-specific kinematics and control implementation.


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


https://github.com/user-attachments/assets/90a77293-7966-4f0b-9a77-13e2bc41b6a7


<img width="1024" height="768" alt="WhatsApp Image 2026-06-26 at 8 52 27 AM" src="https://github.com/user-attachments/assets/8ae6776e-d66d-4ec7-b534-601c1b0343a2" />


https://github.com/user-attachments/assets/7c947dad-5f3c-482d-a8bf-87c40bb047a0


<img width="783" height="848" alt="Screenshot from 2026-06-26 08-56-15" src="https://github.com/user-attachments/assets/30f9fffa-d999-4eb5-85e4-7302d837f586" />

<img width="782" height="788" alt="Screenshot from 2026-06-26 08-57-00" src="https://github.com/user-attachments/assets/21fea214-60c4-4809-9628-6d33579015de" />

<img width="782" height="788" alt="Screenshot from 2026-06-26 08-57-33" src="https://github.com/user-attachments/assets/fcc16071-4b6a-4165-af2f-083ae59711d1" />


# Background and References

- [ros2_kimm_robot](https://github.com/maribernardes/ros2_kimm_robot)  
  ROS 2 package developed for the KIMM Stewart-platform robot.

- [CustomControl-3DSlicer](https://github.com/maribernardes/CustomControl-3DSlicer)  
  3D Slicer custom-control module for sending robot planning poses from Slicer to ROS 2 through SlicerROS2.

# Funding
- NIH R01EB020667
- NIH R01CA235134
- BWH Department of Radiology GR0131914
