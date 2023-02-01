Back to [Projects List](../../README.md#ProjectsList)

# Integration of desktop apps

Kaapana tutorial for the 38th NA-MIC project week:
https://drive.google.com/file/d/1A7-8Ru0uTJHFFa17rZtkBpvNhJao_F7x/view?usp=share_link

## Key Investigators

- Hanno Gao (German Cancer Research Center, Germany)
- Klaus Kades (German Cancer Research Center, Germany)
- Andrey Fedorov (Brigham and Women's Hospital, USA)
- Ralf Floca (German Cancer Research Center, Germany)

# Project Description

It could be useful for Desktop applications such as 3D slicer or MITK to run within a browser, for this a containerization of the application is necessary. Also it could be useful for Desktop applications to communicate with third-party endpoints to, for examples, run a model on images to get a segmentation. In this project, we focus on solution to containerize desktop applications and on communicating with third-party tools

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Desktop apps in containers (Slicer, MITK, OHIF, …), Improved Slicer integration
2. Desktop interaction with Kaapana (Slicer, MITK, ITK-SNAP …)

Relate to:
- [Kaapana overall](https://github.com/NA-MIC/ProjectWeek/tree/master/PW38_2023_GranCanaria/Projects/Kaapana_overall)
- [SlicerCloud](https://github.com/NA-MIC/ProjectWeek/tree/master/PW38_2023_GranCanaria/Projects/SlicerCloud)
- [OHIFSlicerBridge](https://github.com/NA-MIC/ProjectWeek/blob/master/PW33_2020_GranCanaria/Projects/OHIFSlicerBridge/README.md)


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Look at the current state of Slicer and MITK integration in Kaapana (container and client/server interaction)
![image](https://user-images.githubusercontent.com/49161877/215472354-28e8e2bd-60c4-4bc5-9b20-69c98de61a80.png)
2. Finish/adapt integration.
3. Improve desktop (running in a browser) streaming solutions - (noVNC, guacamole...) in the Kaapana kubernetes cluster. 
4. Create documented API for an interaction Kaapana with destop clients

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

* [branch](https://github.com/fedorov/kaapana/tree/develop-slicer) that attempts to integrate Slicer into Kaapana
* [MITK TaskList](https://phabricator.mitk.org/T29160)
