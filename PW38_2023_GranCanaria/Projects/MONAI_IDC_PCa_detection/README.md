Back to [Projects List](../../README.md#ProjectsList)

# HOWTO: Detection of prostate cancer in IDC images using MONAI prostate_mri_anatomy model

## Key Investigators

- Cosmin Ciausu (Brigham and Women's Hospital, USA)
- Deepa Krishnaswamy (Brigham and Women's Hospital, USA)
- Patrick Remerscheid (Brigham and Women's Hospital, USA and Technical University Munuch, Germany)
- Tina Kapur (Brigham and Women's Hospital, USA)
- Sandy Wells (Brigham and Women's Hospital, USA)
- Andrey Fedorov (Brigham and Women's Hospital, USA)

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

1. Develop a Google Colab notebook that contains the following steps:
  
  1. Install prerequisites and the MONAI bundle https://github.com/Project-MONAI/model-zoo/tree/dev/models/prostate_mri_anatomy.
  
  1. Select applicable subset of MRI series from IDC (ProstateX and QIN-Prostate-Repeatability collections).
  
  1. Convert images from DICOM to the format acceptable by the model.
  
  1. Run inference.
  
  1. Visualize results.
  
  1. Perform quantitative evaluation of the results.
  
  1. Convert results into DICOM representation, visualize in OHIF.

2. Document performance of the model.

3. Consider sharing analysis results if they are of good quality.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Preliminary work applying the model in question to segment prostate anatomy.
1. Created bundle segmenting prostate tumors
1. [Minimum working example on training data sample](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/blob/main/cancer_bundle_train_prostate158.ipynb)
3. Examination of results on pre-trained model training data : prostate158
4. Multi-modal input : T2,ADC, DWI, understand acquisition process of DWI used for training
5. Bundle creating thoughts : More extensive documentation about required parameters in inference.json and the relation between anatomy.json and inference.json should be provided.
6. Document process of creating bundle, difficulties encountered
8. Next steps : Confirm DSC results on prostate158 and evaluate on IDC data(DWI acquisition parameters -- QIN Prostate repeatability similar to prostate158 ?)       

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

<img width="1092" alt="Screen Shot 2023-02-03 at 1 10 45 PM" src="https://user-images.githubusercontent.com/72577931/216611849-d148840f-997a-46ce-998a-4c59f2111651.png">


# Background and References

- [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/)
- **[Minimum working example of pc segmentation on training sample prostate158](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/blob/main/cancer_bundle_train_prostate158.ipynb)**
- **[Minimum working example of pc segmentation on QIN-Prostate-Repeatability collection sample](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/blob/main/MONAI_prostate158_cancer_qin_prost_rep.ipynb)**
- [MONAI zoo prostate_mri_anatomy bundle](https://github.com/Project-MONAI/model-zoo/tree/dev/models/prostate_mri_anatomy)
- [MONAI PC segmentation custom bundle](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/tree/main/pcDetectionBundle)
- [PC segmentation model paper](https://www.sciencedirect.com/science/article/pii/S0010482522005789?via%3Dihub#kwrds0010)
