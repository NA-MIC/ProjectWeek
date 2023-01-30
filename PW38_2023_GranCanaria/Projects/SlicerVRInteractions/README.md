Back to [Projects List](../../README.md#ProjectsList)

# SlicerVR - Restore Interactions

## Key Investigators

- Csaba Pintér (EBATINCA, Spain)
- Simon Drouin (ÉTS Montréal, Canada)
- Andrey Titov (ÉTS Montréal, Canada)
- Lucas Gandel (Kitware)
- Jean-Christophe Fillion-Robin (Kitware)

# Project Description

<!-- Add a short paragraph describing the project. -->

The main controller interactions in SlicerVR have been broken for about a year, some interaction types even longer. It would be crucial for keeping SlicerVR usable to make the interactions work again.

Kitware and Robarts (Jean-Christophe Fillion Robin, Lucas Gandel, Sankhesh Jhaveri, Adam Rankin) have been investing resources and effort in rehauling the AR/VR backend in VTK for a while, thus now we have a new OpenXR backend and restructured libraries SlicerVR is built on. The goal is to give a small push to their efforts in terms of SlicerVR interactions during the project week, towards restoring at least the previous feature set.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Fix the main controller interactions
    * Flying (joystick forward-backward)
    * Grab and move objects (trigger down and move)
    * Two-controller world move/zoom (i.e. 3D pinch) 
2. Customization of controller buttons. Either via the
    * Method in-place (functions integrated [here](https://github.com/KitwareMedical/SlicerVirtualReality/pull/87), see also [here](https://github.com/KitwareMedical/SlicerVirtualReality/pull/83))
    * Json manifest files (see [here](https://github.com/Kitware/VTK/tree/master/Rendering/OpenVR))

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Continuous coordination with Kitware / Robarts about our potential to help during the week
    * Make sure the absolutely necessary core VTK changes are in place by the start of the week (RecognizeComplexGesture virtual etc.)
3. Set up VR workstations at the hotel to be able to test and develop
4. Make sure event pipeline reaches the SlicerVR functions handling the events
5. Fix interactions: fly, grab, pinch3D

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

[![SlicerVR example](https://i.ytimg.com/an_webp/F_UBoE4FaoY/mqdefault_6s.webp?du=3000&sqp=CN7D_50G&rs=AOn4CLDzwAi5yXSmiMEkmmgMkmwYpQJY3Q)](https://www.youtube.com/watch?v=F_UBoE4FaoY&t=153s&ab_channel=PerkLabResearch)

[![SlicerVR collaborative example](https://i.ytimg.com/an_webp/Sw3JyKfvW6Q/mqdefault_6s.webp?du=3000&sqp=CJy8_50G&rs=AOn4CLDkH1pgzs3NCJqno3cJrc5lz8Oq-Q)](https://www.youtube.com/watch?v=Sw3JyKfvW6Q&ab_channel=EbatincaS.L.)
 
![In-VR widget example](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerVRInfrastructure/VRWidget.gif)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

Past project week pages
* [Project week #37 page](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerVRInfrastructure)
* [Project week #35 page](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SlicerVR/)
* [Project week #34 page](https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/SlicerVR/)

Pinter, C., Lasso, A., Choueib, S., Asselin, M., Fillion-Robin, J. C., Vimort, J. B., Martin, K., Jolley, M. A. & Fichtinger, G. (2020). SlicerVR for Medical Intervention Training and Planning in Immersive Virtual Reality. IEEE Transactions on Medical Robotics and Bionics, vol. 2, no. 2, pp. 108-117, May 2020, doi: 10.1109/TMRB.2020.2983199.
