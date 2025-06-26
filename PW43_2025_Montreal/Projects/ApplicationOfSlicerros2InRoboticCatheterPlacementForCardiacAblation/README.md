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

* [https://github.com/tokjun/cath_urdf_generator](https://github.com/tokjun/cath_urdf_generator)

A Python script to generate a XACRO file (which can be converted to URDF) for a flexible catheter has been prototyped. The script models a flexible catheter as serial links connected via universal joints and rotary springs. The user can provide parameters to define the serieal links, including N, D, L1, L2, L3, K, and M to mimic the mechanical behavior of the flexible catheter with N links and N-1 universal joints. The serial link consists of the first and the last links representing the tip and the base links, and the bending section conssiting of the remaining (N-2) links. Each joint has rotary springs with a spring constant of K that generate torques to bring it back to the straight positions, when the joint is rotated by the external force. D is the outer diameter of the catheter. L1, L2, and L3 are the lengths of the tip link, the bending section, and the base link. The total weight of the catheter is M.

To generate a catheter XACRO file,
~~~~
$ python3 catheter_urdf_generator.py --N 12 --D 0.003 --L1 0.20 --L2 0.5 --L3 0.05 --K 0.2 --M 0.5 --output my_catheter
~~~~
The URDF can be published in the ROS network using the following command:
~~~~
$ source /opt/ros/jazzy/setup.bash
$ ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$( xacro /home/junichi/igtdev/cath_urdf_generator/my_catheter.xacro )"
~~~~
To visualize using RViz and control the joint angles with the joint_state_publisher_gui, open a new terminal and use the following commands:
~~~~
$ source /opt/ros/jazzy/setup.bash
$ ros2 run joint_state_publisher_gui joint_state_publisher_gui 
~~~~
Open another terminal and launch RViz:
~~~~
$ source /opt/ros/jazzy/setup.bash
$ ros2 run rviz2 rviz2
~~~~
![rviz_catheter](https://github.com/user-attachments/assets/2997eaeb-f2ce-45e8-8073-bee21ce492d7)


## Dynamic Simulation with Gazebo and 3D Slicer

![dynamic simulation](https://youtu.be/upqZboU-ong)



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

