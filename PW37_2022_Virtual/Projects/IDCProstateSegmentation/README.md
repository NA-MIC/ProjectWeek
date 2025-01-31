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
2. Inference on Qin-Prostate-Repeatability collection using a pre-trained nnUnet model on task05 imaging decathlon data :

   * 3d full-res model, T2 and ADC modalities, so there is a need to resample the input.

3. Inference on Qin-Prostate-Repeatability collection using a different pre-trained nnUnet model, task 24 promise.

   * Easier to corner the resampling problem since this pre-trained model has only one input modality -- T2

3. Obtained good dice scores results on the 15 PatientID divided into two studies each using this model.
4. Dealt with the Resampling/Converting issue -  slice spacing incorrect -- use of simpleITK instead of plastimatch

# Illustrations
Slicer visualisation of ground truth and predicted whole prostate segmentation mask, on PatientID01.
Red is ground truth and green is prediction from nnUnet.

![Slicer demo](slicer_idc_prostate_seg.gif)

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

* [Ipynb link](https://colab.research.google.com/drive/1len4_C1mzDi5kDqg120avexJ9g7sEiM9?usp=sharing)
* [Google slides link](https://docs.google.com/presentation/d/10A1zjISq8pcal4enwX48TTj3jgUvvzuboCShGGiI4FA/edit?usp=sharing)
* [nnUnet pre-trained models for download](https://zenodo.org/record/4003545#.Yr7DA-zMIrk)
* [nnUnet paper](https://www.nature.com/articles/s41592-020-01008-z)
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
