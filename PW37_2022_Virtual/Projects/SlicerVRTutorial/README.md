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
1. Instructions on how to use the controllers for the most common devices are given.

![controllersInstructions](https://user-images.githubusercontent.com/90038097/176795986-34bcddee-0b15-4882-a091-586b22280a25.gif)

The tutorial includes a **first task** where users learn how to use the controllers to fly. The task consists on reaching a target (yellow cylinder shown in the scene).

1. First, the module shows the instructions on how to use the controllers for that specific action and the task to perform.

![Instructions](https://user-images.githubusercontent.com/90038097/176796116-4e752803-0fa2-4402-a3ae-d59f0f0d8813.png)

1. Then, the user performs the task.

![part1-fly](https://user-images.githubusercontent.com/90038097/176720297-e1098bcd-1c5f-4b84-ba09-055b7855993a.gif)

1. When the target is reached, the user sees a message indicating “Success”.

Started implementation of **two more tasks**:

1. The user has to grab a model of a skull and put it in the scale

![Move object](https://user-images.githubusercontent.com/90038097/176893946-de3241ca-018b-4373-a83b-1423384f1379.PNG)

2. The user has to move the model of the femur to match the target position (shown as a transparent femur)

![Move and rotate object](https://user-images.githubusercontent.com/90038097/176893988-a9f0cb25-73c3-4eef-8052-cd38fdacd795.PNG)

__Next steps__:

1. Finish the implementation of these tasks.
1. Include more tasks to cover all the possible actions performed with the controllers.
1. When the in-VR widget is ready, the instructions and messages will be shown there.

# Illustrations
VR scenario

![VR scenario](https://user-images.githubusercontent.com/90038097/175922432-08bccf28-2e82-4203-9b0b-c77b83cc5831.gif)

Interaction with objects

![Object Interaction](https://user-images.githubusercontent.com/90038097/175923480-92620ad5-d286-4b04-8ea9-fd05016ba54a.gif)


# Background and References

Link to the source code repository: https://github.com/monicagsevilla/SlicerVRTutorial 
