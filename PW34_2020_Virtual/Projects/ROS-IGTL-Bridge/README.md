Back to [Projects List](../../README.md#ProjectsList)

# ROS-IGTL-Bridge for Prostate Bipsy Robot

## Key Investigators

- Junichi Tokuda (BWH)
- Pedro Moreira (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->
BWH team has been working with Physical Science Inc. on a new generation of robotic device for MRI-guided prostate biopsy.
The new device has active 4-DOF needle guide that directs a biopsy needle to the target in the prostate based on the plan
created on an intraprocedural MRI.

## Objective

In this project, we will implement a new robot controll node on Robot Operating System (ROS) and integrate with 3D Slicer
and MRI scanner using [ROS-IGTL-Bridge](https://github.com/openigtlink/ROS-IGTL-Bridge) and OpenIGTLink.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Define OpenIGTLink messages for the communication between ROS and 3D Slicer
1. Implement a ROS node that compute kinematics and commands individual motors
1. Extend [SliceTracker](https://github.com/SlicerProstate/SliceTracker) to control 3D Slicer and Siemens MRI Scanner.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Created the project page.


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References
The study was funded in part by the National Institutes of Health (4R44CA224853, R01EB020667, R01CA235134, P41EB015898)and Siemens Healthneers.

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
