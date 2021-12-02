Back to [Projects List](../../README.md#ProjectsList)

# AR in Slicer

## Key Investigators

- Alicia Pose Díez de la Lastra (Universidad Carlos III de Madrid, Madrid, Spain)
- Javier Pascau (Universidad Carlos III de Madrid, Madrid, Spain)
- Rafael Moreta Martínez (Universidad Carlos III de Madrid, Madrid, Spain)
- Gabor Fichtinger (PerkLab, Queen's University , Kingston , Canada)
- Andras Lasso (PerkLab, Queen's University , Kingston , Canada)
- Adam Rankin (Robarts Research Institute / Western University, Canada)
- Csaba Pinter (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Lucas Gandel (Kitware, France)
- Jean-Christophe Fillion-Robin (Kitware, USA)




# Project Description

Augmented Reality has increased its adoption in many areas with exciting benefits. Universidad Carlos III de Madrid (Madrid, Spain) has already worked in several medical projects
based on AR (see their progress in https://biig-igt.uc3m.es/augmented-reality/). On these studies, they usually export information from Slicer to an alternative software (Unity). 

The ultimate goal of this project is to develop a new 3D Slicer module that will allow to use augmented reality directly in 3D Slicer. With it, it will be possible
to centralize the working process, at the time of benefiting from all Slicer tools.

Ebatinca S.L. in Las Palmas de Gran Canaria (Spain), has already started this project in collaboration with Kitware (France) and Universidad Carlos III de Madrid (Spain) and
they all are currently developing OpenXR. 

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Create OpenXR, a code based on the currently existing OpenVR so that the new mixed reality version is compatible with VTK.


Some links of interest:
1. [Writing a Holographic Remoting remote app using the OpenXR API](https://docs.microsoft.com/en-us/windows/mixed-reality/develop/platform-capabilities-and-apis/holographic-remoting-create-remote-openxr)
2. [Slicer Documentation on Augmented Reality and Virtual Reality support](https://www.slicer.org/wiki/Documentation/Labs/Augmented_Reality_and_Virtual_Reality_support#Current_approaches)

## Approach and Plan

1. Develop a new Slicer extension that streams AR directly to HoloLens 2.

## Progress and Next Steps

1. OpenXR in VTK:

The WIP branch supporting Holographic remoting to stream VTK rendering inside the Hololens has been submitted [here](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8101).


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
Here below you can find some AR implementations in health by Universidad Carlos III de Madrid (Madrid, Spain) in the past years:

HoloLens 2 in Orthopedic Oncological Surgeries:

![HoloLens 2 in Orthopedic Oncological Surgeries](Figure_HoloLens2_OrthopedicOncologicalSurgery.png)

Smartphone app to communicate with the patient and help him/her understand his/her condition:

![Smartphone app to communicate with the patient and help him/her understand his/her condition](Figure_Smartphone_PatientCommunication.png)

Real-time guidance during Open Cranial Vault Remodeling using smartphone:

![Smartphone app to guide open cranial vault remodeling](Figure_Smartphone_CraniosynostosisSurgery.png)

Needle Insertion Guidance for Sacral Nerve Stimulation using smartphone:

![Smartphone app to guide needle insertion for sacral nerve stimulation](Figure_Smartphone_NeedleInsertion.png)




# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
