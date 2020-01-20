Back to [Projects List](../../README.md#ProjectsList)

# Slicer Sense-Act Framework

(This name is temporary, please suggest better ones!)

## Key Investigators

- Mark Asselin (ACMIT Gmbh & Perk Lab, Queen's University)
- Gernot Kronreif (ACMIT Gmbh, Remote)
- Andras Lasso (Perk Lab, Queen's University)

# Project Description

This project is to create a framework for linking sensors to actuators, providing automated responses to stimuli. This project is in its infancy, and so our main goal this week is to guage which features would be most useful to the community. In this spirit, we welcome input from everyone regarding which features people would find most useful.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Further define and prioritize features
2. Have interesting conversations pertaining to how we can make this contribution maximally useful to the Slicer community.

## Preliminary Feature List

1. Sensor Support
  - Raman
  - 5-ALA
  - OCT
  - Screen reader (for capturing data from closed source tools with no API)
  - Suggestions please!
2. Robotics Support
  - PLUS support for Franka Panda, iSYS One and enhanced Intuitive DaVinci support
  - Robot registration (via a tracked marker on the arm)
  - Continuous robotic re-registration (by comparison of actual and commanded position of the arm)
  - Monitoring for de-registration of robotic system (easily implemented for iSYS One, more difficult for others) to detect if the integrity of the robot registration has been compromised
  - Ability to iteratively approach a target using tracked marker on tool
  - Visualization of reachability constraints
  - Calculation of reachability constraints (i.e. given a position can we reach it?)
  - Safety mechanisms (defining a region which constrains the position of the robot)
  - Collision prevention
  - Convenient and consistent tele-operation of robot (i.e. via OpenIGTLink, game controller or haptic control)
3. Planning Support
  - Visualization of needle paths & automatic detection of intersections with rigid or sensitive structures
  - Leveraging robot reachability to improve ability to plan
  - Auto-planner for liver radio-frequency ablation (Mark's thesis, must be complete by 04-20)
4. Workflow Support
  - Add ability to (easily) model a procedure as a finite state machine in Slicer
  - Implement methods for automatic detection of state transition
  - Detection of missed steps in a procedure
  - Automatic reaction to sensor input data

## Approach and Plan

1. Have as many discussions as possible to ensure that this work is useful to everyone.
2. The goal for this week is to have a good prioritization of
ideas, and to hopefully add some more things to this project which will be useful to the community.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
