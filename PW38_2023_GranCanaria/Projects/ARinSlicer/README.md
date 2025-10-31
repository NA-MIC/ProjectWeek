Back to [Projects List](../../README.md#ProjectsList)

# AR in Slicer

## Key Investigators

- Alicia Pose Díez de la Lastra (Universidad Carlos III de Madrid, Madrid, Spain) - [Presenter]
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



## Background and References
Check out our app in [this GitHub repository](https://github.com/BIIG-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning).
This repository contains all the resources and code needed to replicate our work in your computer.

Transfer of geometrical transforms from HoloLens 2 to 3D Slicer:

![MovingSpine_GIF](https://user-images.githubusercontent.com/66890913/214097820-96b9f875-4651-4efd-879b-831eb88b7b07.gif)

Transfer of images from 3D Slicer to HoloLens 2:

![MovingCT_GIF](https://user-images.githubusercontent.com/66890913/214097469-17a1aa1a-2768-4f73-8c12-bb4ab7d393f0.gif)


## Outcomes
Use this system for multiple HL2 interaction:

![Interaction2HL2_Simon_GIF](https://user-images.githubusercontent.com/66890913/216575916-e37b6a07-aab1-4710-b709-21ce56271eeb.gif)

![Interaction2HL2_Leo_GIF](https://user-images.githubusercontent.com/66890913/216621686-27d7ec42-8ad3-400c-b90c-da59a2a92358.gif)

## Acknowledgements
Research supported by projects PI122/00601 and AC20/00102  (Ministerio de Ciencia, Innovación y Universidades, Instituto de Salud Carlos III, Asociación Española Contra el Cáncer and European Regional Development Fund / EU “Una manera de hacer Europa”), project PerPlanRT (under the frame of ERA PerMed), TED2021-129392B-I00 (MCIU/AEI/10.13039/501100011033 and European Union “NextGenerationEU”/PRTR).
<img width="4400" height="49" alt="image" src="https://github.com/user-attachments/assets/c4d375b1-db08-41b0-a5f2-e265484e07da" />

