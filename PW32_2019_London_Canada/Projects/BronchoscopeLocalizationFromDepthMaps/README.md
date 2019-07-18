Back to [Projects List](../../README.md#ProjectsList)

# Bronchoscope Localization From Depth Maps

## Key Investigators
- Franklin King (BWH)
- Shelly Liu (Concord Academy)
- Jonah Berg (The Rivers School)

# Project Description

<!--   -->
The goal is to localize a bronchoscope through the use of depth maps generated from bronchoscopy images using neural networks. With work already progressing on the depth map generation via neural network, the next goal will be to translate it into a realtime (or semi-realtime) tracking/localization method implemented in 3D Slicer.

## Objective

<!-- What we would like to achieve in this project is to be able to localize bronchoscopy images to the CT scan of the lung. -->

1. Produce some ground truth depth maps from model to perform tracking/localization with.
2. Develop Slicer module that loads in a feed of depth maps and registers to localize the position of the camera.

## Approach and Plan

1. Develop ground truth depth maps via Unity from phantom airway model.
2. Convert depth maps to point clouds.
3. Assuming a known starting position for the tracking, perform a boolean intersect operation around the area of the camera in order to limit the area of the model to register to.
4. Boolean operation may be performed using VTK polygon boolean filters, but if they don't work out then calling Blender via Python should work.
5. Perform registration of point cloud to intersected model of airway and adjust transform accordingly.

## Progress and Next Steps

1. Depth map general via neural networks: https://github.com/NA-MIC/ProjectWeek/tree/master/PW31_2019_Boston/Projects/BronchoscopeLocalizationFromDepthMaps
2. Ground truth depth maps specifically for the realtime registration testing generated using Unity.
3. Registration done using ICP registration (Surface Registration module from CMFreg)
4. Boolean operations to limit ICP registration to target area (plane cuts would probably be more reliable, but the boolean operations were performed using an instance of Blender imported into Slicer as a Python module)
5. Module created in Slicer 

## Installing and Importing Blender within Slicer

In Windows:
1. /(SlicerInstallPath)/bin/SlicerPython.exe -m pip install future-fstrings, bpy
2. Move /(SlicerInstallPath)/lib/Python/Scripts/2.79/ to /(SlicerInstallPath)/bin/2.79/
3. Just "import bpy" within Slicer
4. Example script for performing a Boolean operation using Blender: https://github.com/SNRLab/Slicer-DepthMapTracking/blob/master/Models/BlenderBooleanExample.py

## Images
![Point cloud of airway generated from depth map](https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW31_2019_Boston/Projects/BronchoscopeLocalizationFromDepthMaps/Example1.png)

![Registration to segment of airway model](https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW31_2019_Boston/Projects/BronchoscopeLocalizationFromDepthMaps/Example3.png)

# Background and References

1. https://github.com/NA-MIC/ProjectWeek/tree/master/PW31_2019_Boston/Projects/BronchoscopeLocalizationFromDepthMaps
