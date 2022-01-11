Back to [Projects List](../../README.md#ProjectsList)

# Update the Chest Imaging Platform to support Slicer 5.0

## Key Investigators

- Rudolf Bumm  (KSGR)
- Andras Lasso (PerkLab)
- Steve Pieper (Kitware)

# Project Description

<!-- Add a short paragraph describing the project. -->
The Chest Imaging Platform (CIP) is an extension to 3D Slicer that integrates:

CIP functionality as a Toolkit exposing of the CLIs
Slicer specific modules to provide user-friendly chest CT quantitative solutions
Visualization of scale-space particles and labelmaps
Integrated workflows to end-to-end clinical evaluation

In the current preview versions of 3D Slicer (4.13.0) CIP fails to load the following CIP modules because Slicer's "Editor" module has been removed.    

CIP_CalciumScoring

CIP_RVLVRatio

CIP_LesionModel

CIP_Calibration

CIP_MIPViewer

CIP_BodyComposition

CIP_ParenchymaSubtypeTrainingLabelling

CIP_ParenchymaAnalysis

CIP_PAARatio

CIP_AVRatio

CIP_InteractiveLobeSegmentation

The CIP extension currently uses legacy editor module, and charts infrastructure (instead of Segment editor, Plots, and Tables modules).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Replace the usage of the "Editor" module in CIP by something different, preferably the SegmentEditor
Replace the charts infrastructure. 


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Resolve compatibility problems step by step 

There is no labelmap editor in Slicer 5. Is it possible to keep the Editor module and rename it to LabelmapEditor ? 


## Progress and Next Steps

01/06/22:

Removing the "Editor" related imports from "Scripted/CIP_/CIP/ui/__init__.py" results in a complete CIP-startup in Slicer 4.13.0 without initial error messages. 

A github search revealed that "Editor" calls are being made from three of the above modules:  

- CIP_Calibration
- CIP_ParenchymaSubtypeTrainingLabelling
- CIP_BodyComposition 

01/11/22: 

CIP_Calibration is probably outdated.

CIP_ParenchymaSubtypeTrainingLabelling is outdated, probably redundant. 

CIP_BodyComposition is needed, but probably much better realized with AI segmentation 





# Illustrations


# Background and References

https://chestimagingplatform.org/

https://discourse.slicer.org/t/exporting-csv-with-parenchyma-analysis-module/10697/58?u=rbumm



