---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/TrainingAiAlgorithmsOnIdcData/README.html

project_title: Training AI algorithms on IDC data
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Cosmin Ciausu
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/) provides publicly available cancer imaging data.

Previous works([IDC Prostate segmentation](https://github.com/ImagingDataCommons/idc-prostate-mri-analysis)) ([NLST-Body Part Regression](https://github.com/ImagingDataCommons/IDC-Tutorials/blob/master/notebooks/body_part_regression_with_structured_reports.ipynb)) demonstrated through several use cases inference and analysis of AI algorithms on IDC data.
Downloading IDC data, conversion between file imaging standards, cloud environment setup and imaging pre-processing steps were studied through these inference and analysis use cases.

During this project week, our goal is to develop use cases of training AI algorithms on IDC data. We welcome any Project Week participants that are interested in leveraging IDC data for training AI algorithms(or evaluation) to collaborate with us!

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Leverage IDC data for SOTA segmentation algorithm(nnUNet, MONAI)
2.  Collaborate with other members to study the feasibility of using IDC data for training AI algorithms.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Using nnUNet segmentation framework for prostate segmentation on IDC data([Prostatex/QIN collection](https://portal.imaging.datacommons.cancer.gov/explore/filters/?collection_id=Community\&collection_id=QIN\&collection_id=prostate_mri_us_biopsy\&collection_id=prostatex\&collection_id=qin_prostate_repeatability)) for training purposes.
2.  Expand AI training use cases beyond SOTA algorithms.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Leverage information gained by applying inference using nnUNet prostate segmentation on several prostate imaging collections, for training pipelines.
2.  Creation of whole prostate IDC training cohort: 45 T2W MRI scans and corresponding expert whole prostate annotations were used.
3.  Creation of Google Colab use case showing how to build this cohort and begin a nnUNet training experiment. 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![WORKFLOW](https://github.com/ccosmin97/ProjectWeek/assets/72577931/d9627a49-b6ca-4216-a564-4118c3b61e14)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
* [Google Colab use case for IDC training cohort and nnUNet training](https://colab.research.google.com/drive/1TmmhouNGeQ-DpGz2z83yiZh3KQ20a-1M?usp=sharing).
*   [PW37_2022_Virtual -- nnUnet - Prostate segmentation on Imaging Data Commons(IDC) data](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/IDCProstateSegmentation)
*   [AI Imaging analysis on IDC data](https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks#imaging-analysis-ai)
