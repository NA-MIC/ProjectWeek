Back to [Projects List](../../README.md#ProjectsList)

# Updating Batch Anonymizer
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
1. Add support for exporting CBCT images to a single DICOM file. 
2. Add support for keeping certain metadata fields (example: age and gender) intact during anonymization process
3. Improve current defacing algorithm

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. CBCT export to dingle file DICOM images will need some exploration into DICOM standards to be careful that correct modailities are assigned correct SOP IDs. Ask experts what is the right way to convert a multi-file DICOm images to a single file.
2. Will be using inspiration from existing metadata anonymization tools to implement "selective" metadata stripping, with initial options of keeping gender and age intact. This is per the request of our clinicians who will be the primary users of this tool.
3. Current defacing approach creates noise in the back of the head, and is not robust to intensity changes. We'll work on implementing frontal region detection, and make the algorithm robust to intensities. Community is welcome to add their own/other standard defacing algorithms in the 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
