Back to [Projects List](../../README.md#ProjectsList)

# Integration of infrared, ultraviolet and hyperspectral sensors in Slicer via Plus Toolkit  and OpenIGTLink. 
## Key Investigators

- Francisco J. Marcano Serrano

# Project Description

<!-- Add a short paragraph describing the project. -->
Integration of a predefined set of sensors in the 3D Slicer platform,  via Plus Toolkit  and OpenIGTLink, for future use in clinical applications.
Several sensors/cameras operating in different electromagnetic ranges and using different communication standards (USB, CameraLink, GigE, GenICam) will be integrated.
The set of cameras to integrate includes (but not limited to): visible light USB cameras, PCO (ultraviolet, USB, several models), Thermal Expert (infrared, USB/CameraLink, several models), FLIR (infrared, GigE, several models), Specim (hyperspectral, GenICam, several models).


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Adding selected sensors as new devices in PTK.
2. Visualization and control of integrated sensors from Slicer. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Integration of at least one USB camera (sensor) as a  PTK device.
1. Integration of at least one CameraLink sensor as a  PTK device.
1. Integration of at least one GigE sensor as a PTK device.
1. Integration of at least one GenICam sensor as a PTK device.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
1. Environment configuration (Win10, Visual Studio 2019, Qt5, installation of PTK (https://plustoolkit.github.io) & cameras drivers + SDK's ).
2. Thermal Expert EV2 infrared camera added, following instructions from PTK site (plustoolkit.github.io/devicecode).  
3. PCO Ultraviolet camera added, following instructions from PTK site. Code modified to change camera exposure values from config file (XML).  
4. Simultaneous image acquisition from TE-EV2 & PCO UV tested from Slicer (OpenIGTLink, see figure).
5. Next steps: integration of CameraLink, GigE, GenICam cameras; interactive control of camera parameters.   

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
Fig. 1: Integration of Thermal Expert EV2 & PCO Ultraviolet Cameras (OpenIGTLink)
[TEEV2PCOUV-2.gif](https://github.com/NA-MIC/ProjectWeek/blob/master/PW38_2023_GranCanaria/Projects/MultiSpectralSensorIntegration/TEEV2PCOUV-2.gif)
<img src="TEEV2PCOUV-2.gif" width="652" height="356" class="center">></img>

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
1. Plus ToolKit. Adding a Device. URL: https://plustoolkit.github.io/devicecode (Last seen: 02/02/2023). 
