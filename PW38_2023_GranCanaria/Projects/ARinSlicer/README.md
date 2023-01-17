Back to [Projects List](../../README.md#ProjectsList)

# AR in Slicer

## Key Investigators

- Alicia Pose Díez de la Lastra (Universidad Carlos III de Madrid, Madrid, Spain)
- Javier Pascau (Universidad Carlos III de Madrid, Madrid, Spain)
- Gabor Fichtinger (PerkLab, Queen's University , Kingston , Canada)
- Andras Lasso (PerkLab, Queen's University , Kingston , Canada)
- Adam Rankin (Robarts Research Institute / Western University, Canada)
- Csaba Pinter (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Lucas Gandel (Kitware, France)
- Jean-Christophe Fillion-Robin (Kitware, USA)
- Simon Drouin (École de Technologie Supérieure , Montreal , Canada)

## Project Description
Up to date, there has been a lack of software infrastructure to connect 3D Slicer to any augmented reality (AR) device. This project presents a novel connection approach using Microsoft HoloLens 2 and OpenIGTLink.
This project has been developed in collaboration of [Universidad Carlos III de Madrid](https://biig-igt.uc3m.es/augmented-reality/) (Madrid, Spain) and Perk Lab in Queen's University.
The current solution is implemented in a 3 elements system. It is composed by A Microsoft HoloLens 2 headset, the Unity software, and the 3D Slicer platform. 

## Objective
Create a universal module in 3D Slicer that sends all types of messages via OpenIGTLink.


## Approach and Plan
1. 3D Slicer creates an OpenIGTLink server.
2. Unity, containing the AR application, creates an OpenIGTLink client that connects to the server.
3. When the application is executed in the Unity editor, it starts sending and receiving messages from 3D Slicer. Simultaneously, it wirelessly streams the app to Microsoft HoloLens 2 using Holographic Remoting. 



## Progress and Next Steps


We have already developed an application that transfers geometrical transform and image messages between the platforms.
It displays CT reslices of a patient in the AR device. The user wearing the glasses can manipulate the CT plane to see different perspectives.
The application was build for pedicle screw placement planning.

![20221213_161232_HoloLens](https://user-images.githubusercontent.com/66890913/212931527-035baf4c-4799-4d83-9c60-b8a0f839547e.jpg)


The final version will be able to transfer any type of messages.
To do so, we have to create necessary scripts in 3D Slicer and also in Unity (C#).



<!--## Background and References-->

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
