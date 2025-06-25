---
layout: pw43-project

permalink: /:path/

project_title: Application of SlicerROS2 in Robotic Catheter Placement for Cardiac Ablation
category: IGT and Training

key_investigators:

- name: Junichi Tokuda
  affiliation: BWH
  country: USA

- name: Yue Chen
  affiliation: BWH
  country: USA

- name: Ehud Schmidt
  affiliation: BWH
  country: USA

- name: Laura Connolly
  affiliation: BWH
  country: USA

---

# Project Description

We investigate the use of SlicerROS2 to simulate robotic catheter in the heart anatomy for cardiac ablation. 



## Objective
1. We will develop a tool to configure robotic catheter and generate URDF data, 
2. Test the URDF for visualization in RViz/3D Slicer and dynamic simulation in the Gazebo simulator.

## Approach and Plan
1. Write a script to generate a URDF file to model the kinematic and visual models of the catheter.
2. Load the model onto the Gazebo dynamic simulator
3. Visualize the simulation outcome on 3D Slicer using SlicerROS2
4. (Optional) Create a 3D geometric model of the cardiovascular structures on 3D Slicer, and incorporate into the scene on the Gazebo simulator.

## Progress and Next Steps
### Generating a URDF file

* https://github.com/tokjun/cath_urdf_generator

A Python script to generate a XACRO file (which can be converted to URDF) for a flexible catheter has been prototyped. The script models a flexible catheter as serial links connected via universal joints and rotary springs. The user can provide parameters to define the serieal links, including N, D, L1, L2, L3, K, and M to mimic the mechanical behavior of the flexible catheter with N links and N-1 universal joints. The serial link consists of the first and the last links representing the tip and the base links, and the bending section conssiting of the remaining (N-2) links. Each joint has rotary springs with a spring constant of K that generate torques to bring it back to the straight positions, when the joint is rotated by the external force. D is the outer diameter of the catheter. L1, L2, and L3 are the lengths of the tip link, the bending section, and the base link. The total weight of the catheter is M.





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

