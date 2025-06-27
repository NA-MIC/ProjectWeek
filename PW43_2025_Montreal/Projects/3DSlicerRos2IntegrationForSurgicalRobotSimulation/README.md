---
layout: pw43-project

permalink: /:path/

project_title: 3D Slicer–ROS2 Integration for Surgical Robot Simulation
category: IGT and Training

key_investigators:

- name: Joonho Seo
  affiliation: KIMM
  country: South Korea

- name: Juntae Park
  affiliation: AIRS
  country: South Korea

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to simulate fracture reduction surgery using a Stewart platform–based robotic system. Currently, we rely on an Optical Tracking System (OTS) to calibrate the spatial relationship between patient and robot, enabling visualization and execution of the planned reduction path.

However, the use of OTS comes with considerable cost and practical limitations. To overcome these, we plan to integrate ROS2 directly with 3D Slicer and eliminate the need for external tracking hardware. By using only software communication between 3D Slicer and ROS2, we will visualize and simulate fracture reduction trajectories entirely in a virtual environment.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Set up an SDF/URDF based ROS2 simulation environment for the Stewart-platform surgical robot
2. Simulate robot movement in 3D Slicer using ROS2 input



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Analyze and implement SDF/URDF models for the AIRED Stewart-platform robot
  - Create both `.sdf` and `.urdf` files representing the AIRED robot structure
  - Visualize the robot model in ROS2 RViz for verification
  - Attempt visualization using the SlicerROS2 extension

- Develop ROS2–3D Slicer communication nodes
  - Create ROS2 publisher and subscriber nodes to transmit pose data
  - Use ROS2 topics to establish bidirectional communication between ROS2 and 3D Slicer

- Simulate and verify robot motion

  - Send simulated pose commands via keyboard inputs
  - Monitor robot motion in RViz and 3D Slicer during simulation

    



### Progress and Next Steps

- Created a basic URDF model of the AIRED Stewart-platform robot
- Verified URDF-based visualization in ROS2 RViz

![Image](https://github.com/user-attachments/assets/0c8b3cbb-fc25-4b54-8ae5-d1742d387233)

  - Implemented ROS2–3D Slicer communication for pose exchange
  - Test real-time motion simulation in both RViz and 3D Slicer 
    - https://drive.google.com/file/d/1_45UmCQrpRSdvIDcFHZ1BOmo3fDaGMv_/view?usp=drive_link

- Next Steps
  - Implement and test bidirectional data communication between ROS2 and the robot
  - Evaluate the precision of 6-DoF motion of the robot



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


- Fracture reduction surgical robot

![Image](https://github.com/user-attachments/assets/2ceaf39f-505e-4741-886d-fe6174183b67)


- Visualized the URDF model in 3D Slicer using the SlicerROS2 extension

![Image](https://github.com/user-attachments/assets/39515bcd-d53d-4567-8968-6a5df34b2f39)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [SlicerROS2](https://slicer-ros2.readthedocs.io/en/v1.0/index.html)
- [ROS2 Jazzy](https://docs.ros.org/en/jazzy/index.html)
- [https://drive.google.com/file/d/1RaTsGjUCuYQjolq8KW-ABr_gGIWw4BRO/view?usp=drive_link](https://drive.google.com/file/d/1RaTsGjUCuYQjolq8KW-ABr_gGIWw4BRO/view?usp=drive_link)
- [https://rosmed.github.io/tutorials/smarttemplate/](https://rosmed.github.io/tutorials/smarttemplate/)

