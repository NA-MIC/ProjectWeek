Back to [Projects List](../../README.md#ProjectsList)

# ROS-MED: Integration of 3D Slicer and ROS2 for Image-Guided Robot-Assisted Interventions

## Key Investigators

- Junichi Tokuda (Brigham and Women's Hospital)
- Tamas Ungi (Queen’s University)
- Axel Krieger (Johns Hopkins University) 
- Simon Leonard (Johns Hopkins University)
- Mark Fuge (University of Maryland)
- Lydia Al-Zogbi (Johns Hopkins University)
- Milad Habibi (University of Maryland)
- Pedro Moreira (Brigham and Women's Hospital)

# Project Description

The ultimate goal of this project is to provide a software platform to integrate medical image computing
software (3D Slicer) into a system for image-guided robot-assisted interventions, in which 2D/3D medical
images are used for planning, navigation, monitoring, and validation. 
Examples of such robot-assisted systems include image-guided robotic needle-guide systems and surgical
CAD/CAM systems. Those systems often require a wide range of image computing capabilities such as
segmentation of anatomical structures, registration of multiple images, 2D/3D image visualization,
image-based planning, and data sharing with the robot controller and the hospital’s picture archiving
and communication systems (PACS). Integration of a solid medical image computing platform into a robotic
system is becoming more important than ever with the growing interest in AI-based treatment planning and guidance. 

However, the engineering effort to implement those features is often underestimated in academic research
due to limited engineering resources or the scope of the project. Fortunately, many of those features have
already been implemented and validated in the research community and often distributed as open-source software. 
Therefore it has become essential for academic researchers to take advantage of those existing tools and
incorporate them into their own research instead of reinventing the wheel. 

Our team has been integrating 3D Slicer and Robot Operating System using OpenIGTLink to achieve the above goal
following [our first project](https://www.na-mic.org/wiki/2016_Winter_Project_Week/Projects/SlicerROSIntegration),
and recently received a grant from National Institutes of Health (2R01EB020667). In this year, we will focus on
transition to the new ROS platform (ROS2).

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Explore ROS2 as a potential platform for our study on image-guided model-driven needle placement robot.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Run ROS2 on a universal robot arm (UR-10) at JHU.
1. Prototype a new version of ROS-IGTL-Bridge
1. Display a 3D model of the UR-10 on 3D Slicer, and synchronize its posture with the robot by sending the transform of each link.
 
## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. First meeting (1:00pm on Discord)
  - Participants: Tamas, Junichi Pedro
  - 
1. Kick-off meeting (2:30pm on Discord)
  - Participants: Tamas, Lydia, Junichi, Simon
  - Confirm the goal of the project
  - Breakdown the tasks
    - Prototype ROS-IGTL-Bridge (Junichi)
    - Setup a remote environment for the the UR-10 computer at Dr. Krieger's lab at JHU
    - Install ROS2 on the UR-10 computer remotely
1. First implementation of ROS2-OpenIGTLink bridge
[![ROS2 OpenIGTLink demo]({image-url})]({https://www.dropbox.com/s/sq5amxkrfjvmvaz/ros2_igtl_bridge_July_1_2021.mov?dl=0} "ros2_igtl_bridge")
 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References
- Frank T, Krieger A, Leonard S, Patel NA, Tokuda J. ROS-IGTL-Bridge: an open network interface for image-guided therapy using the ROS environment. Int J Comput Assist Radiol Surg. 2017 Aug;12(8):1451-1460. doi: 10.1007/s11548-017-1618-1. Epub 2017 May 31. PMID: 28567563; [PMCID: PMC5543207](https://www-ncbi-nlm-nih-gov.ezp-prod1.hul.harvard.edu/pmc/articles/PMC5543207/).
- [ROS-IGTL-Bridge (for ROS 1)](https://github.com/openigtlink/ROS-IGTL-Bridge)
- [ros2_igtl_bridge (for ROS 2)](https://github.com/tokjun/ros2_igtl_bridge)
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

# Acknowledgement
This work is supported by NIH R01EB020667 (MPI: Tokuda, Krieger, Fuge, Leonard).
