# RadOncSegmentor Segmentation for Radiation Treatment Planning

## Key Investigators
- [Harini Veeraraghavan](https://github.com/harveerar) (MSKCC)
- Aditya P. Apte, (MSKCC)
- [Eve M. LoCastro] (https://github.com/locastro) (MSKCC)
- Jue Jiang (MSKCC)
- Sharif Elguindi (MSKCC)
- Aditi Iyer (MSKCC)
- Joseph Deasy (MSKCC)

# Project Description

RadOncSegmentor contains methods for 3D segmentation of CT and MRI images to generate volumetric segmentation of tumors and organs at risk to radiotherapy. The open-source implementation of these methods is available as singularity containers through [CERR](https://github.com/cerr/CERR/wiki/Auto-Segmentation-models).

## Objective
The goal for this project is to present to people about the various deep learning segmentation applications available through CERR for tumor and normal organs for radiation oncology applications. We will also show how these methods are currently used in our clinical workflow for radiation therapy treatment planning at MSK.

## Approach and Plan

1. Create project page that provides an overview of the project
1. 5-minute presentation and demo of the CERR-XNAT open-source library as well as (time permitting) our MIM-CERR- workflow used for routine clinical processing
1. Get feedback from people and hopefully find collaborators to work with.

## Progress and Next Steps

1. Made the project page
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

1. Reference publications:
- Lung tumor segmentation from CT: Jiang J, Hu Y.C, Liu C.J, Halpenny D, Hellmann M.D, Deasy J.O, Mageras G, Veeraraghavan H, "Multiple resolution residually connected feature streams for automatic lung tumor segmentation from CT images", IEEE Trans. Med Imaging, 38(1): 134-144, 2019.
- Lung organs segmentation:
  - [Um H, Jiang J, Thor M, Rimner A, Luo L, Deasy J.O, Veeraraghavan H, "Multiple resolution residual network for automatic thoracic organs at risk segmentation from CT"] (https://arxiv.org/abs/2005.13690), in MIDL 2020.
  - Haq R, Hotca A, Apte A, Rimner A, Deasy J.O, Thor M, "Cardio-pulmonary substructre segmentation of radiotherapy computed tomography images using convolutional neural networks for clinical outcomes analysis", phiRO, 2020
- Head and neck organs:
  - [Jiang J, Elguindi S, Um H, Berry S, Veeraraghavan H, "Local block-self attention for normal organ segmentation"] (https://arxiv.org/abs/1909.05054)
  - [Iyer A, Thor M, Haq R, Deasy J.O, Apte A](https://www.biorxiv.org/content/10.1101/772178v2.full)
- Prostate organs:
  - Elguindi S, Zelefsky M, Jiang J, Veeraraghavan H, Deasy J.O, Hunt M, Tyagi N, "Deep learning-based auto-segmentation of targets and organs-at-risk for magnetic resonance imaging only planning for prostate radiotherapy", phiRo 2019.
