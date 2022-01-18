Back to [Projects List](../../README.md#ProjectsList)

# Update the Chest Imaging Platform extenstion to support Slicer 5

## Key Investigators

- Rudolf Bumm  (KSGR)
- Raul San Jose Estepar (Brigham)
- Andras Lasso (PerkLab)
- Steve Pieper (Kitware)

# Project Description

<!-- Add a short paragraph describing the project. -->
The Chest Imaging Platform (CIP) is an extension to 3D Slicer. 

![image](https://user-images.githubusercontent.com/18140094/149629677-6bea2a6f-835d-4ae8-8955-71995e7e716d.png)

It integrates: 
- chest image processing functionality as a toolkit by exposing the CLIs
- Slicer specific modules to provide user-friendly chest CT quantitative solutions
- Visualization of scale-space particles and labelmaps
- Integrated workflows to end-to-end clinical evaluation

In the current preview versions of 3D Slicer (4.13.0) parts of CIP fail to load the following CIP modules because Slicer's "Editor" module has been removed.    

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

- Replace the usage of the "Editor" module in CIP by something different, preferably the SegmentEditor. 
- Replace labelmaps with segmentations
- Replace outdated fiducial calls (exceptions) 
- Replace the charts infrastructure


## Approach and Plan

A fork and branch of SlicerCIP was created at https://github.com/rbumm/SlicerCIP/tree/Branch_CIPCompatSlicer5 to be used as the source base, all changes will later be included in a PR to https://github.com/acil-bwh/SlicerCIP.   

Resolve compatibility problems step by step 

Deactivate non-working or outdated modules in Slicer 5

## Considerations 

## Progress and Next Steps

01/06/22:

Removing the "Editor" related imports from "Scripted/CIP_/CIP/ui/__init__.py" results in a complete CIP-startup in Slicer 4.13.0 without initial error messages. 

A github search revealed that "Editor" calls are being made from three of the above modules:  

- CIP_Calibration
- CIP_ParenchymaSubtypeTrainingLabelling
- CIP_BodyComposition 

01/11/22: 

- CIP_Calibration is probably outdated.
- CIP_ParenchymaSubtypeTrainingLabelling is outdated, probably redundant. 
- CIP_BodyComposition is needed, but probably much better realized with AI segmentation 

01/11/22: 12pm Meeting with Raul, Andras, Steve

- Incompabilities between 4.13 and CIP seem to be caused by CIPLibrary 
- CIP, it's CLI functions and their history were demonstrated by @Raul
- CIP_Calibration is not outdated.
- CIP_ParenchymaSubtypeTrainingLabelling should be kept. 
- CIP_BodyComposition is needed and should be kept
- CIP Toolkit functions should be included in a future SlicerCIP release
- A CIPLibrary compatibility branch "4.13" or "5.0" will be created 
- CIP GitHub write access was requested for @Andras to support merging, @Raul agreed 
- As labelmaps are used throughout CIP in nearly every module we will discuss a Slicer-based solution for that problem tomorrow 
  


# Illustrations


Body Composition module:

![image](https://user-images.githubusercontent.com/18140094/148948731-bdb76667-9380-4f0c-b98a-7eaf27aa942b.png)



Calibration module:

![image](https://user-images.githubusercontent.com/18140094/148948945-9c7d710c-add3-46ba-b774-4bcf35a05f51.png)



Parenchyma Subtype Training:

![image](https://user-images.githubusercontent.com/18140094/148949201-7de68dd3-9794-4f79-b323-d2ed02b4db12.png)



Parenchyma Subtype Training Labelling:

![image](https://user-images.githubusercontent.com/18140094/148949387-28de3db1-1323-44a8-8d01-c298a20661f1.png)





# Background and References

https://chestimagingplatform.org/

https://discourse.slicer.org/t/exporting-csv-with-parenchyma-analysis-module/10697/58?u=rbumm



