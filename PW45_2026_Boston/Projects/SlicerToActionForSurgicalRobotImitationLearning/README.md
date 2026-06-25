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

We are developing a robotic system for fracture reduction using SlicerROS2. The goal of this project is to investigate whether recent imitation learning approaches, such as visuomotor policies or Vision-Language-Action (VLA) models, can be applied to this robot system.
In this project, 3D Slicer functions as a tool to display real-time object movements in a 3D view. 
We intend to utilize this **3D view as training data for robotic motion**.
The 3D Slicer view will function just like a real camera mounted on the robot.
Furthermore, it will allow us to build **custom simulation environments to generate and train on virtual data**.

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/09d40dbd-0033-45a7-8e0d-324c90201013" />



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Establishing a pipeline to integrate 3D Slicer's visual data with robot joint data for advanced policy learning and real-time inference.
- Establishing an environment dedicated to generating and training on synthetic simulation data.

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/9b099b3d-69ae-4c0a-b26b-c2931b94ead2" />



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

**1. Synthetic Training Data Generation**   
Randomly generate diverse bone fragment configurations.  
Generate and apply a reduction trajectory that reduces each configuration.  
During the reduction process, capture images from four views (Axial, Lateral, Medial, ISO) in 3D Slicer, and store the corresponding strut lengths as an episode.  
Save the data as a dataset of 100+ episodes.  
**2. Training Policy**  
Feed the stored dataset into the LeRobot visuomotor policy framework.  
Train an ACT (Action Chunking with Transformers) policy to obtain the policy network (100K steps, loss < 0.03).  
**3. Run Reduction**  
Randomly generate an arbitrary bone fragment configuration.  
(1) Capture the four views in Slicer and feed them, together with the corresponding strut lengths, into the policy as the observation.  
(2) Infer strut lengths.  
(3) Perform forward kinematics analysis and update the robot's pose.  
(4) Return to (1) and iterate.  


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
<img width="1054" height="567" alt="image" src="https://github.com/user-attachments/assets/99518a87-4d88-4dd1-acc5-0b851af118d4" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
References
[1] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware," in Proc. Robotics: Science and Systems (RSS), 2023. arXiv:2304.13705.  
[2] R. Cadene, S. Alibert, A. Soare, Q. Gallouédec, A. Zouitine, T. Wolf, et al., "LeRobot: State-of-the-art Machine Learning for Real-World Robotics in PyTorch," 2024. [Online]. Available: https://github.com/huggingface/lerobot  


