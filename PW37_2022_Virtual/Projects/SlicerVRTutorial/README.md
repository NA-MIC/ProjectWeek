Back to [Projects List](../../README.md#ProjectsList)

# SlicerVR Tutorial

## Key Investigators

- Mónica García-Sevilla (Universidad de Las Palmas de Gran Canaria, Spain)
- David García-Mato (EBATINCA, Spain)
- Csaba Pinter (EBATINCA, Spain)

# Project Description

SlicerVR is a nice tool for visualization of medical 3D data. It can be used in preoperative planning, surgical training and others. However, understanding how to interact with the images and models or getting used to move around the Slicer scene using the VR controllers can be difficult at the beginning. Therefore, a first steps tutorial could be useful for new users.

## Objective

The goal of this project is to develop a SlicerVR tutorial module to learn the basic actions needed to interact with objects and move around the 3D scene.


## Approach and Plan

1. Define the actions to train (fly, grab, transform scene...)
1. Decide how to train those actions (define target positions or actions)
1. Decide the tutorial workflow (how to change which action is being trained)
1. Implement the module
1. Test with different headsets (HTC Vive, Oculus Rift...)

## Progress and Next Steps

1. A module has been created for the tutorial which connects to the VR hardware and shows a virtual scenario.
1. The user is assigned an avatar (head and hands).
1. The tutorial includes a first task where users learn how to use the controllers to fly.

The task consists on reaching a target (yellow cylinder shown in the scene).

![part1-fly](https://user-images.githubusercontent.com/90038097/176720297-e1098bcd-1c5f-4b84-ba09-055b7855993a.gif)

When the target is reached, the user sees a message indicating “Success”.

Next steps:

1. Include more tasks to cover all the possible actions performed with the controllers.
1. When the in-VR widget is ready, the instructions and messages will be shown there.

# Illustrations
VR scenario

![VR scenario](https://user-images.githubusercontent.com/90038097/175922432-08bccf28-2e82-4203-9b0b-c77b83cc5831.gif)

Interaction with objects

![Object Interaction](https://user-images.githubusercontent.com/90038097/175923480-92620ad5-d286-4b04-8ea9-fd05016ba54a.gif)


# Background and References

Link to the source code repository: https://github.com/monicagsevilla/SlicerVRTutorial 
