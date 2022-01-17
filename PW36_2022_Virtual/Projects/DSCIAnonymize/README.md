Back to [Projects List](../../README.md#ProjectsList)

# Write full project title here
Tool to anonymize a dataset of medical images.

## Key Investigators

- Hina Shah (UNC Chapel Hill)
- Juan Carolos Prieto (UNC Chapel Hill)
- Fryderyk Kögl (BWH, TUM) 

# Project Description

<!-- Add a short paragraph describing the project. -->
The very first step to make any medical data available to research community is it's anonymization. While there are ways to anonymize a single DICOM/non-dicom image in 3D Slicer, there's no module to do this for a full dataset.

The proposed tool will:
- Anonymize a dataset of images by deleting any identifiable metadata information
- Have options to rename the files using either UUID or custom name. 
- Create a crosswalk to get the correspondence between anonymized and original files
- Work as a standalone app or a slicer extension

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Write tests
1. Objective B. Push the extension to Slicer Extension Index
1. Objective C. Find out what other features/enhancements can be added to this extension

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Identify existing anonymization pipelines for DICOM
2. Modify code to make the extension be available as an extension (not a standalone app), and push it to Slicer Extension Index
3. Within the community try to find out what other features would be useful to add to the extension.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. The extension has been written to work as a stand alone app, with the features written above

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![image](https://user-images.githubusercontent.com/22948571/149800624-b1468449-96a1-467c-ad49-7559e68fb74b.png)


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
1. [Source code in Github repository](https://github.com/hina-shah/DSCI_Anonymizer)
