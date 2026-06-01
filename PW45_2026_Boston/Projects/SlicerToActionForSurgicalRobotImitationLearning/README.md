---
layout: pw45-project

permalink: /:path/

project_title: Slicer-to-Action for surgical robot imitation learning
category: IGT and Training
presenter_location: 

key_investigators:

- name: Taewoo Yoon
  affiliation: AIRS Inc
  country: Republic of Korea

- name: Joonho Seo
  affiliation: Korea Institute of Machinery Materials
  country: Republic of Korea

---

# Project Description

<!-- Add a short paragraph describing the project. -->


3D Slicer can function as a tool to display real-time object movements in a 3D view. 
We intend to utilize this **3D view as training data for robotic motion**.
The 3D Slicer view will function just like a real camera mounted on the robot.
Furthermore, it will allow us to build **custom simulation environments to generate and train on virtual data**.

<img width="1139" height="311" alt="Image" src="https://github.com/user-attachments/assets/09d40dbd-0033-45a7-8e0d-324c90201013" />



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Establishing a pipeline to integrate 3D Slicer's visual data with robot joint data for advanced policy learning and real-time inference.
- Establishing an environment dedicated to generating and training on synthetic simulation data.

<img width="1334" height="530" alt="Image" src="https://github.com/user-attachments/assets/9b099b3d-69ae-4c0a-b26b-c2931b94ead2" />



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Establishing an environment to track an object rigidly coupled with the robot in the 3D view, ensuring its pose updates dynamically in accordance with the robot's motion.
2. Capture the 3D view for a specified number of frames while simultaneously acquiring the corresponding robot joint data.
3. Train the policy based on the training dataset created in step 2.
4. After training the policy, inferred joint positions are fed as control commands into either a simulation tool or physical robot.
5. Input the 3D Slicer view into the trained model for inference.
6. Feed the inferred joint position into either the simulation tool or physical robot, and sequentially input the updated 3D Slicer view as the next state input as the robot moves.



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

