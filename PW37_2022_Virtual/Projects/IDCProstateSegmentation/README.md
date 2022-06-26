Back to [Projects List](../../README.md#ProjectsList)

# nnUnet - Prostate segmentation on Imaging Data Commons(IDC) data

## Key Investigators

- Cosmin Ciausu (Brigham and Women's Hospital)
- Andrey Fedorov (Brigham and Women's Hospital)

# Project Description

Inference on prostate IDC data using [nnUnet](https://github.com/MIC-DKFZ/nnUNet) segmentation framework.  
This framework provides an end to end segmentation pipeline, from pre-processing, data augmentation, hyper-parameter selection to post-processing, with variants of an Unet segmentation model.
The Imaging Data Commons platform provides both labelled and unlabelled prostate scans collections.

## Objective

1. Augment existing and applicable IDC collections with prostate segmentations obtained from nnUnet pre-trained models. 
2. Investigate/analyze nnUnet framework generalizability to IDC data. 

## Approach and Plan

1. Use nnUnet models pre-trained on prostate data to get predictions results on labelled IDC collections first, [PROSTATEx](https://portal.imaging.datacommons.cancer.gov/explore/filters/?access=Public&collection_id=Community&collection_id=prostatex) or [qin-prostate-repeatability](https://portal.imaging.datacommons.cancer.gov/explore/filters/?access=Public&collection_id=QIN&collection_id=qin_prostate_repeatability) for example.
2. Evaluate performance on labelled data, followed by inference on unlabelled IDC collections.

## Progress and Next Steps

1. Verification of nnUnet claimed results on prostate decathlon data, used for available pre-trained models.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
