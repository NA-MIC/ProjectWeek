---
layout: pw40-project

permalink: /:path/

project_title: 'Evaluation of AI methods for prostate cancer segmentation '
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Patrick Remerscheid
  country: Switzerland

- name: Cosmin Ciausu
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Brianna Burton
  affiliation: 3D Side SA
  country: Belgium

- name: Laura Levy
  affiliation:
  country: Switzerland

- name: Bálint Kovács
  affiliation: DKFZ
  country: Germany

- name: Umang Pandey
  affiliation: Universidad Carlos III de Madrid
  country: Spain  

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA



---

# Project Description

<!-- Add a short paragraph describing the project. -->

When it comes to evaluating AI methods, it's important to have reproducible code and methods. We are interested in evaluating state-of-the-art AI methods for prostate cancer segmentation on data in Imaging Data Commons. Additionally, we have a non-public BWH internal dataset that we would like to use for evaluation.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  We first need to identify a set of publicly available AI methods that we can use for prostate cancer segmentation.
2.  We then need to identify datasets in IDC that we can use for evaluation, preferably ones with expert delineated segmentations.
3.  Then, we will run inference using those methods, convert our output to a standard format (hopefully DICOM SEG) and visualize in OHIF and Slicer.
4.  We will make our code and results publicly available in GitHub.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  We will do a literature/code repo search of the methods.
2.  We will search for  appropriate data in IDC using the portal/BigQuery.
3.  We will create a sample set of data from multiple prostate imaging collections, including T2, DWI, ADC and ground truth segmentations.
4.  We will run inference using the 4 methods on these sample data sets and visualize in Slicer.
5.  If possible we will perform quantitative evaluation. 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. We have identified two major branches of methods we can use, baseline methods from the [PICAI challenge](https://pi-cai.grand-challenge.org/) and two methods using MONAI. 

    - PICAI has two baseline methods we can run: supervised nnUNet, semi-supervised nnDetection
    - MONAI has two methods we can run: a [MONAI bundle](https://github.com/kbressem/prostate158) and a [MONAI Deploy MAP](https://github.com/Project-MONAI/research-contributions/tree/main/prostate-mri-lesion-seg) 

2. We have identified two datasets in IDC that can be used for evaluation: 

    - [QIN-Prostate-Repeatability ](https://portal.imaging.datacommons.cancer.gov/explore/filters/?collection_id=qin_prostate_repeatability)
    - [Prostate-MRI-US-Biopsy ](https://portal.imaging.datacommons.cancer.gov/explore/filters/?collection_id=prostate_mri_us_biopsy)

3. We have started evaluation of the PICAI supervised nnUNet baseline model and the MONAI Deploy MAP on their training data.
4. We will take [Cosmin's work from PW38](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/tree/main/pcDetectionBundle/configs) on the MONAI bundle for prostate cancer segmentation. We'll make sure it works, and evaluate it on publicly available datasets including IDC data (continuation of [this](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis/blob/main/MONAI_prostate158_cancer_qin_prost_rep.ipynb) notebook).
5. We have evaluated the two PICAI models on almost all of the 3 subsets of data.
6. We've run the MONAI bundle on a subset of the 3 collections.
7. We've also run the MONAI deploy MAP on a subset of the 3 collections. 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*** PICAI nnUNet supervised *** 

ProstateX: The ground truth lesion is in green, and the predicted lesion in red. 
<img width="387" alt="PICAI_nnUNet_ProstateX" src="https://github.com/NA-MIC/ProjectWeek/assets/59979551/aefe3d66-0a6e-4717-b074-0040031fa215">

*** PICAI nnDetection semi-supervised *** 

ProstateX: The ground truth lesion is in green, and the predicted bounding box in white. 
<img width="387" alt="PICAI_nnDet_ProstateX" src="https://github.com/NA-MIC/ProjectWeek/assets/59979551/bd1f7eb6-2641-4c2e-9450-65d9aeb9d75a">

QIN-Prostate-Repeatability: The ground truth lesion is in green, and the predicted bounding box in white.
<img width="708" alt="nnunet_bounding_box" src="https://github.com/NA-MIC/ProjectWeek/assets/59979551/c91a256a-01c3-4660-90ef-c30a7f99b719">

*** MONAI Deploy MAP *** 

Using the MONAI Deploy MAP pre-trained model for prostate and lesion segmentation on a patient from Prostate-MRI-US-Biopsy.
The ground truth lesion segmentation is on the left, and the predicted prostate gland segmentation and lesion segmentations are on the right.
![](https://github.com/NA-MIC/ProjectWeek/assets/59979551/c55ff897-e1e8-485c-b17f-0bd104f95a4e)

Scrolling through slices of same patient as above: 

![](https://github.com/NA-MIC/ProjectWeek/assets/59979551/8fc9b45d-48ce-443d-a951-0345b6f913ea)

Using the MONAI Deploy MAP pre-trained model for prostate and lesion segmentation on a patient from ProstateX. 
The ground truth lesion segmentation is on the left, and the predicted prostate gland segmentation and lesion segmentations are on the right.

![monai_deploy_prostatex_0000](https://github.com/NA-MIC/ProjectWeek/assets/59979551/af44b9d3-74dd-4b3e-90fd-80daf8685850)

*** MONAI bundle *** 

Using the MONAI bundle and pretrained prostate158 model, on patients from ProstateX. The grountruth lesion is in green, and the predicted in red.

<img width="708" alt="monai_bundle_prostatex1" src=https://github.com/NA-MIC/ProjectWeek/assets/32570021/cc641bb6-2b6a-4bdf-b2cd-9dfd82a4c758>
<img width="708" alt="monai_bundle_prostatex2" src=https://github.com/NA-MIC/ProjectWeek/assets/32570021/ddc12fd3-3881-4a33-9eaf-8f2ac6a0e10b>
<img width="708" alt="monai_bundle_prostatex3" src=https://github.com/NA-MIC/ProjectWeek/assets/32570021/42128aad-e6c5-4064-beda-c0e93e69b037>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Our github repo with notebooks (WIP): https://github.com/deepakri201/prostateSeg

This is a continuation of the work that Cosmin did at PW38: https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/MONAI_IDC_PCa_detection/  

IDC getting started tutorials: https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/getting_started

*No response*
