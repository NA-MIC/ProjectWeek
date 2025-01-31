Back to [Projects List](../../README.md#ProjectsList)

# Histology Data and Models Into IDC

## Key Investigators

- Curtis Lisle (KnowledgeVis)
- Andrey Fedorov (BWH)
- Maximilian Fischer (DKFZ)
- David Cllunie (PixelMed)
- others welcome


# Project Description
I am working on a histology project with NCI, which is producing whole-slide images and deep-learning segmentation and analysis models. Our images are of a rare pediatric cancer called Rhabdomyosarcoma.

Our group is in discussion with the IDC core team to import our images and models into IDC for others to use.  This Project Week project is about the process of converting a whole slide image (WSI) into DICOM for import and learning how to run models on histology images already managed by IDC.

It is our hope that this will prepare us for converting our analytic models and submitting them to IDC later, after Project Week has completed.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Run the IDC-recommended DICOM conversion process for a pyramidal input image
1. Execute existing analysis models (already in IDC) in Collab sessions
1. Learn about analysis models can access different levels/tiles in a pyramidal DICOM file so we can modify our models to run within the IDC environment.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Acquire an anonymized WSI image, suitable for testing during Project Week
1. Explore existing Histology collections in IDC. [See existing collections here](https://portal.imaging.datacommons.cancer.gov/explore/filters/?access=Public&Modality_op=OR&Modality=SM)
1. Learn how to convert and submit a WSI image into the IDC
1. Study how analysis models loaded in IDC access pyramidal DICOM files. Study existing models: [See Existing Model Examples](https://github.com/ImagingDataCommons/IDC-Examples/tree/master/notebooks/pathomics)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Acquire a set of anonymized WSI images from our project.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

[David Clunie's DICOM Import process](https://github.com/ImagingDataCommons/idc-wsi-conversion)

[Google's WSI to DICOM converter](https://github.com/GoogleCloudPlatform/wsi-to-dicom-converter)
