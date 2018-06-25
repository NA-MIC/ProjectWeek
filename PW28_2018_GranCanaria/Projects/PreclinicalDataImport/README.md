Back to [Projects List](../../README.md#ProjectsList)

# Improve/Test multivolume preclinical MRI data import (DCE, DTI, ASL, T1 mapping). 

## Key Investigators

-	Sharon Peled (Brigham and Women’s, USA)
-	Andras Lasso (Queen’s University, Canada)
-	Lauren O’Donnell (Brigham and Women’s, USA)

# Project Description

Correct Slicer dynamic MRI DICOM frame data and DTI gradient data loading for Bruker preclinical MRI systems (Paravision version 6).


## Objective

1. Modify the multivolume importer to correctly display and represent preclinical DCE MRI DICOM data.
1. Modify the DTI loader.

## Approach and Plan

1. Collect examples of preclinical data.
1. The first correction for DCE is to make sure the frame time in DCE MRI is not merely copied from the 'RepetitionTime' field in the DICOM files. Instead, this should be multiplied by the number of phase encoding steps. 
1. Identify the Slicer format of DTI data.
1. Implement a Matlab Bridge module "LoadBruker" that correctly loads all the various Bruker data sets: DCE, ASL, T1 mapping, DTI (with the correct gradient directions).
1. Convert the Matlab Bridge module to Python/Slicer.

## Progress and Next Steps

1. Various preclinical data sets were collected, including DCE, DTI, T1 mapping, and cASL:

https://www.dropbox.com/sh/5qo2kay9w7bi92t/AADvQtsKR3SJBS2HlReN1q-Ma?dl=0


<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->
