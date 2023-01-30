Back to [Projects List](../../README.md#ProjectsList)

# HOWTO: Detection of prostate cancer in IDC images using MONAI prostate_mri_anatomy model

## Key Investigators

- Cosmin Ciausu (Brigham and Women's Hospital, USA)
- Deepa Krishnaswamy (Brigham and Women's Hospital, USA)
- Patrick Remerscheid (Brigham and Women's Hospital, USA and Technical University Munuch, Germany)
- Tina Kapur (Brigham and Women's Hospital, USA)
- Sandy Wells (Brigham and Women's Hospital, USA)
- Andrey Fedorov (Brigham and Women's Hospital, USA)
- Khaled Younis (Philips, USA)

# Project Description

[MONAI Zoo] has a growing number of pre-trained models for solving a range of image analysis tasks. It is of interest to understand robustness of those models on independent datasets, evaluate their performance.

[NCI Imaging Data Commons (IDC)]() has a growing number of imaging datasets, most of which do not have accompanying annotations, complicating downstream analysis. 

In this project we will demonstrate how an existing pre-trained MONAI model packaged as a bundle can be applied to a suitable subset of data from IDC, and how existing annotations can be used to validate results produced by this model.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Develop an end-to-end documented example demonstrating the use of MONAI bundle on IDC prostae MRI.
1. Understand and quantify the performance of the model using ground truth annotations.
1. If applicable (results are of good quality), consider sharing the produced annotations within IDC.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Develop a Google Colab notebook that contains the following steps:\
    a. Install prerequisites and the [MONAI bundle](https://github.com/Project-MONAI/model-zoo/tree/dev/models/prostate_mri_anatomy).\
    b. Select applicable subset of MRI series from IDC (ProstateX and QIN-Prostate-Repeatability collections).\
    c. Convert images from DICOM to the format acceptable by the model.\
    d. Run inference.\
    e. Visualize results.\
    f. Perform quantitative evaluation of the results.\
    g. Convert results into DICOM representation, visualize in OHIF.\
2. Document performance of the model.
3. Consider sharing analysis results if they are of good quality.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Preliminary work applying the model in question to segment prostate anatomy : [use.case.ipynb](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/blob/main/main_monai_anatomy.ipynb)
1. Exploratory work on transfer of PC detection/localization on IDC data by creating a monai bundle : multi-modality input, custom transforms

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- [NCI Imaging Data Commons](ttps://portal.imaging.datacommons.cancer.gov/)
- [MONAI zoo prostate_mri_anatomy bundle](https://github.com/Project-MONAI/model-zoo/tree/dev/models/prostate_mri_anatomy)
