# Affordable IGT Simulators with Slicer IGT + PLUS
3D Slicer affordable (low cost) navigated ultrasound system for training purpose description for the 27th NA-MIC Project Week at Boston.

Back to [Projects List](../../FIXME.md#ProjectsList)

# Affordable IGT Simulators with Slicer IGT + PLUS
## Key Investigators

- Guillermo Socorro (ULPGC - GTMA - MACbioIDi)
- Carlos Luque (ULPGC - GTMA - MACbioIDi)
- Abián Hernández (ULPGC - GTMA - MACbioIDi)
- Juan Ruiz (ULPGC - GTMA - MACbioIDi)

# Project Description

<!-- Presentation: https://medtec4susdev.github.io/FIXME -->

In this project we aim to create and integrate an Image Guided Therapy (IGT) ultrasound training system in 3D Slicer. Specifically, the main objective is the implementation of an affordable navigated ultrasound simulator based on ArUco low cost optical trackers. The ultrasound simulator already implemented in the PLUS Toolkit is used as reference and new geometrical models will be included.

## Objective

1. Track ultrasound probe with low cost optical trackers.
2. Integrate the tracked probe in an ultrasound simulator already implemented in PLUS Toolkit.
3. Improve the pose accuracy to make it suitable for training purpose.
4. Allow customization of the simulated geometrical models to a prescribed training lecture.

## Approach and Plan

1. Define a proper ArUco optical tracker system (web camera and markers selection and distribution).
2. Program the integration of the tracked probe in the ultrasound simulator device included in PLUS Toolkit. 
3. Implement strategies for track accuracy improvement.
4. Replace the default model simulated in the PLUS device with a custom arm model.
5. Test and verify the overall system.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<img src="https://github.com/medtec4susdev/FIXME.jpg" width="340" height="120">

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

+ 3D Slicer Tutorials: http://www.slicer.org/wiki/Documentation/4.8/Training

+ Plus Toolkit ultrasound simulator device documentation: http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceUsSimulator.html

+ ArUco optical trackers project site: http://www.uco.es/investiga/grupos/ava/node/26

<!--Link for editing page when displayed in GitHub pages-->
<a href="https://github.com/NA-MIC/ProjectWeek/edit/master/PW27_2018_Boston/Projects/FIXME.md">Edit this page on GitHub</a>
