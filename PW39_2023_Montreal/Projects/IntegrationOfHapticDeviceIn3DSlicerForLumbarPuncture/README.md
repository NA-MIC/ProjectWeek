---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/IntegrationOfHapticDeviceIn3DSlicerForLumbarPuncture/README.html

project_title: Integration of Haptic Device in 3D Slicer for Lumbar Puncture
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Pablo Sergio Castellano Rodríguez
  affiliation: Universidad  de Las Palmas de Gran Canaria
  country: Spain

- name: Jose Carlos Mateo Pérez
  affiliation: Universidad de Las Palmas de Gran Canaria
  country: Spain

- name: Juan Bautista Ruiz Alzola
  affiliation: Universidad de Las Palmas de Gran Canaria
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The main objective of the project is to integrate the haptic device Touch 3D Systems into 3D Slicer through an OpenIGTLink connection with the Unity platform. Slicer To Touch is the 3D Slicer module that contains the scene with the 3D models of the spine and the needle. This module has an interface where the user can configure the number, position and value of the resistances to be exerted by the haptic device. These values will be included in a .json file that will later be transferred to Unity, which will process this data and configure the forces of the haptic device within the Unity environment. Finally, through the OpenIGTLink connection bridge, a real-time connection will be created, where the transformations and the resistances of the haptic device will be shared with the 3D Slicer scene. This idea comes from a project for a lumbar puncture training system that makes use of this device, but the body tissues, their location and thickness are generic. This way you can make a segmentation of a real patient's back with its own characteristics and practice the lumbar puncture before doing it with the patient. Due to the way it works, it could be used in other procedures.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Create a module that with the help of Unity and OpenIGTLink allows us to interact with a back model of a real patient obtained by segmentation of medical images. In this way we can train the lumbar puncture on the model of a real patient feeling the resistance in the body tissues.
2.  Automate the process of creating resistances on segmentation-generated models so that clinicians can easily perform lumbar puncture and other procedures with a sense of realism.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Creation of the 3D Slicer module with fields to enter the number of resistances, positions and values.
2.  Generate a .json file with all the information entered in the module.
3.  Create a Unity project with a script that reads the generated .json file and creates a scene with the resistances in that position and with those values.
4.  Connect Unity to 3D Slicer through OpenIGTLink to send the transforms and see the needle movements in 3DSlicer.
5.  Generate an executable application from the Unity project with a simple look and feel that does the procedure automatically so that the clinical user finds it easy to use and does not have to deal with the unity interface.
6.  Do a documentation search of other procedures to check that the project works correctly in them. We are looking for other clinical procedures for which this project may be useful and for which there is information a

## Progress and Next Steps


<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
Steps that are already done:

1.  Create a 3d model of a real patient back from segmentation of medical images.

![Screenshot (33)](https://github.com/NA-MIC/ProjectWeek/assets/117910171/98f78b7b-61c5-451c-9277-9b432ca00f41)

   
2.  Indicate with MarkUps the tissues which we want to feel.

![Screenshot (34)](https://github.com/NA-MIC/ProjectWeek/assets/117910171/b8117833-3df2-45f1-a7d4-f93dd315458c)

   
3.  Inlcude in SlicerToTouch module the number of resistances, posiitons and force value for each tissue. This module generates a json file with all the information.

![Screenshot (43)](https://github.com/NA-MIC/ProjectWeek/assets/117910171/988cbfc0-0ba2-4ea1-b11a-9f279c83adb8)

![configfile](https://github.com/NA-MIC/ProjectWeek/assets/117910171/a58ca86b-ffcc-413d-8638-8f1234e16c2e)


4.  Using Unity in the background we read that file and automatically a new scene is created with the haptic materials. Also, at the same time, it sends the transform of the haptic device to slicer by OpenIGTlink, so you can see a needle moving.

![2023-06-14-16-09-55-Trim](https://github.com/NA-MIC/ProjectWeek/assets/117910171/34822062-8a61-4ade-b346-e6e5a6d8dee3)
   


What we are actually working on:

1. Integration of Hololens 2 for the visualization of the scene:
![20230614-224421-HoloLens-Trim-Tr (1)](https://github.com/NA-MIC/ProjectWeek/assets/117910171/d66de98b-a539-4407-a489-fdf2aa398b0f)


Next steps: 

1. Include metrics in order to analyze the procedure.
2. Restrict the movement to just one axis once you are inside the back model.
# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

3D Slicer Module in which you enter the resistances (left) and the .json file with the information of these resistances (right)(Picture1.png)

![Picture1](https://github.com/NA-MIC/ProjectWeek/assets/134281471/02e28cdd-11dc-4f3c-b714-1c7164456f05)

Unity interface after reading the information from the .json file with the resistances created in the positions and the needle as a visual mesh of the haptic device (left) and script that makes it work (right) (Picture2.png)

![Picture2](https://github.com/NA-MIC/ProjectWeek/assets/134281471/e4ac4786-0ae6-442e-b068-8808591c1e99)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   Real-Time integration between Microsoft HoloLens 2 and 3D Slicer. (Alicia Pose Diez de la Lastra)
    <https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning>

*   OpenIGTLink-Unity.
    <https://github.com/franklinwk/OpenIGTLink-Unity>
