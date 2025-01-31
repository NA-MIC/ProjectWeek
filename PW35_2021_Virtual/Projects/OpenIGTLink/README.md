Back to [Projects List](../../README.md#ProjectsList)

# OpenIGTLink

## Key Investigators

- Junichi Tokuda

# Project Description

OpenIGTLink has been used to share data between software platforms (e.g., 3D Slicer, PLUS, ROS, etc..) in real-time for IGT applications. In this project, we will discuss new features that are potentially incoporated in the future versions of OpenIGTLink.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Identify missing features that are required in ongoing research projects.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. We will have a meeting at 1pm on Tuesday on the 'openigtlink' channel on Discord. (Confirmed attendees: Sarah, Sam, Tina, Junichi)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Discuss current status of OpenIGTLink and existing issues
  - We have been trying to minimize changes to the protocol to maintain the compatibility, and keep the protocol simple. There has been few protocol change in the past few years. Changes are mostly on the interface implementation.
  - OpenIGTLink is a 'low-level' messaging protocol. Applications need to define how the subsystems exchange messages (=messaging scheme).
  - Junichi has recieved a new funding to use OpenIGTLink for medical robotics projects. OpenIGTLink is used to brdige Robot Operating System (ROS) and 3D Slicer. ROS uses its own messaging system (Data Distribution Service: DDS).
  - Issues in Brainlab connectivity
    - Brainlab's IGTLink interface was designed before Protocol version 2. Some of the messages are not fully complient with the current protocol.
    - 3D Slicer's OpenIGTLink interface has been overhauled a few years ago. The old version had some workaround to handle non-complient messages from Brainlab.
    - The new version relies on an external library (IGSIO) to handle high-level messaging scheme, which makes it harder to implement the workaround. Also the new version of interface does not accept some of the message types that used to be supported by the old versions.
3. Zoom conference with Brainlab
  - BWH team (Sarah and Paxy) described the issues they are facing during clinical cases
  - Brainlab acknowledge one of the issues and could fix it. Another issue is related to the incomplient message format, and could be fixed without significant effort.
  - Potential new features e.g., DTI support etc. DTI support will require testing on the OpenIGTLink side, as it has never been used for such a purpose.
  -
# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
