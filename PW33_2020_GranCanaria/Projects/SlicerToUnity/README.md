Back to [Projects List](../../README.md#ProjectsList)

# Slicer to Unity Connection

## Key Investigators

- Thomas Muender (Uni Bremen)
- Anke Reinschluessel (Uni Bremen)
- Thomas Mildner (Uni Bremen)
- Adam Rankin
- Steve Pieper
- Andras Lasso

# Project Description

Developing a real time viewer showing image data (e.g., segmentations, 3D models, ...) from 3D Slicer in Unity, if possible allowing also for interaction in unity updating the slicer data (as a 2nd step)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Establish a streaming connection between unity and 3D slicer
2. Select Data that should be streamable (Meta data, dicom images, 3d models)
3. Integrate the streamed data into Unity application

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Get an overview about pre-existing solutions (Web server Http streaming, OpenITGLink)
2. Developing a slicer plug-in
  * create new plugin
  * integrate streaming technology
  * select data to be streamed
  * put data into streamable format
3. Developing the unity application
  * integrate streaming technology
  * transform data into unity data formats
4. Integrate data in the Unity application
  * Build Unity viewer

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Look at pre-existing solutions (Web server Http streaming, OpenITGLink)
  * OpenITGLink seems a bit too much for our goals
  * http streaming looks promising (https://github.com/pieper/SlicerWeb)
  * https://projectweek.na-mic.org/PW32_2019_London_Canada/Projects/KidneySegmentation/
  * AR/VR solutions with slicer: https://www.slicer.org/wiki/Documentation/Labs/Augmented_Reality_and_Virtual_Reality_support#Current_approaches
  * https://github.com/Lyla-M/UnityOpenIGTLink
2. Familiarize ourselfs with zmq
3. Set-up a Connector-class between Unity and 3D Slicer setting up three connections:
* one connection Unity -> Slicer for continuous data exchange
* one connection Slicer -> Unity for continuous data exchange
* one connection Unity -> Slicer using request to get volume data
4. wrote several data gathering functions
* getting mesh data
* getting volume data
* getting annotation data (fiducials, ROI, ruler)
5. implemented a automtic request on slicer data change
6. set up a Unity camera position visualizer in slicer 3D view


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
https://youtu.be/jXaJ5jVDjyg (Demonstration of the functionality)

# Background and References
* https://zeromq.org/get-started/
* https://github.com/thomasMuender/SlicerToUnity
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
