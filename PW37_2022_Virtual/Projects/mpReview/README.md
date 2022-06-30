Back to [Projects List](../../README.md#ProjectsList)

# mpReview - 3DSlicer module for multiparametric annotation of the prostate

## Key Investigators

- Deepa Krishnaswamy (Brigham and Women's Hospital)
- Andrey Fedorov (Brigham and Women's Hospital)

# Project Description

The 3DSlicer module mpReview (part of the SlicerProstate extension) was previously developed to assist with manual annotation of the prostate and other related anatomical regions. 
The current state of the module does not use the latest SegmentEditor, and requires that the data be organized and preprocessed in a specific manner on the user's local machine. 
The overall goal is to update the module to be more streamlined, and later have the ability to be extended to other regions of the body. 

Currently, we have modified the module to allow data to be loaded from the local Slicer database, or from a remote GCP server. The DICOMweb client is used to retrieve studies/series/instances 
of the user-selected GCP DICOM store. The resulting segments are saved as a DICOM SEG file (user-specific) and uploaded to the server. Using our own instance of the OHIF viewer, the data and the corresponding segmentations can be viewed. 

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Separate the location of the raw DICOM data and the DICOM SEG files. 
1. Objective B. Brainstorm easier ways for multiple users to view their annotations. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Implement the selection of two DICOM stores, where one will contain the raw DICOM data and the other the DICOM SEG files. 
1. Discuss how to best view annotations from multiple users. 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. The user can select to use the local DICOM database or the remote GCP server. 
2. Annotations are saved as DICOM SEG files to the server. 
3. We can create a second DICOM datastore to store only the segmentations, but cannot yet read the latest saved segmentation DICOM file from it. 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

Select to use either the local Slicer database or a remote (GCP) server. 

![image](https://user-images.githubusercontent.com/59979551/173397241-97def393-7434-4d8d-978f-9ca695cf6efc.png)

Create annotations of the prostate and other anatomical regions of interest, and upload the segmentation DICOM files to the server. 

![image](https://user-images.githubusercontent.com/59979551/173397664-c3a7f567-d5f2-4214-a366-7cef1344860c.png)

Use our instance of the OHIF viewer to see the updated annotations.

![ohif_mpreview](https://user-images.githubusercontent.com/59979551/176763073-ac96d7cf-d490-4946-bb2a-4ed073e80b47.JPG)



# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

[Code is here](https://github.com/deepakri201/mpReview/tree/seg_editor)
