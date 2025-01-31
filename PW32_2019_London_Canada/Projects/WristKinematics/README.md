Back to [Projects List](../../README.md#ProjectsList)

## Wrist Kinematics from 4D CT

## Key Investigators
- Puneet Kaur Ranota (Western University)
- Adam Rankin
- Andras Lasso (PerkLab, Queen's)

# Project Description
We are looking to investigate the distance between bones in the wrist from CT images.

## Objective
1. Load static CT into Slicer
1. Load 4D cine CT into Slicer
1. Segment bones

## Approach and Plan

1. Use multivolume importer plugin to load 4D kinematic CT into volume sequence
1. Experiment with Segment Editor module for segmentation

## Progress and Next Steps

1. MultiVolumeImporter patched to recognize GE Revolution 4D Cine sequence separator field (available in latest Slicer Preview version)
1. Segment editor tutorial for bone segmentation

# Illustrations

Videos of Extension and flexion of the wrist:
* [Volume rendered using bone preset](Media/ExtensionFlexion_CTBone.mp4)
* [Volume rendered using tissue preset](Media/ExtensionFlexion_CTTissue.mp4)
* [Volume rendered with slice views](Media/ExtensionFlexion_CTTissue_4up.mp4)
* [Volume rendered with slice views, looped](Media/ExtensionFlexion_CTTissue_4up_loop.mp4)
