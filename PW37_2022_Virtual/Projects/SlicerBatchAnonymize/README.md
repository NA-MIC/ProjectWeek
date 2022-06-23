Back to [Projects List](../../README.md#ProjectsList)

# Updates to Batch Anonymizer
SlicerBatchAnonymize is a Slicer Extension that strips off metadata from dicom files, and converts them to various file formats. 
The work during project week will involve investigating and creating prototypes for defacing in medical images, support and single file dicom export.

## Key Investigators

- Hina Shah (UNC Chapel Hill)
- Juan Carolos Prieto (UNC Chapel Hill)

# Project Description

<!-- Add a short paragraph describing the project. -->
The very first step to make any medical data available to research community is it's anonymization. [SlicerBatchAnonymize](https://github.com/hina-shah/SlicerBatchAnonymize)
is a 3D Slicer extension to anonymize a batch of DICOM images by stripping most of metadata (image information stays intact). 
The tool currently provies a user-friendly UI, supports export to several popular research formats including DICOM series, and also generates a crosswalk files for future uses.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Support export to a single DICOM file. 
2. Investiage existing defacing methods
3. Come up with a prototype for defacing of CBCT images. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use either DICOMlib or pydicom for export to DICOM as a single file.
2. Get guidance from community on existing defacing methods, and lookup existing tools/literature available for defacing
3. Decide and implement a prototype for defacing of CBCT images

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. 
2. 
3.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![image](https://user-images.githubusercontent.com/22948571/149800624-b1468449-96a1-467c-ad49-7559e68fb74b.png)


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
1. [Source code in Github repository](https://github.com/hina-shah/SlicerBatchAnonymize)
