---
layout: pw44-project

permalink: /:path/

project_title: Using automatic AI segmentation tools for Imaging Data Commons data enrichment
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Lena Giebeler
  affiliation: RWTH Aachen
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Lalith Kumar Shiyam Sundar
  affiliation: LMU
  country: Germany

- name: Ron Kikinis
  affiliation: BWH
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project builds on work carried out during [PW43](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/EvaluatingConcordanceOfAiBasedAnatomySegmentationModels/)  and on the work ["In Search of Truth: Evaluating Concordance of AI-Based Anatomy Segmentation Models"](https://www.arxiv.org/pdf/2512.15921).

Our overall goal is to enrich images available in [Imaging Data Commons](https://learn.canceridc.dev/) with segmentations and quantitative features.

In this work, we developed a practical workflow to compare AI-based anatomy segmentation models in the absence of ground truth annotations. Segmentation outputs from different models were harmonized into a standardized representation, enabling structure-wise comparison and efficient visual review. Using this framework, we evaluated six open-source segmentation models, TotalSegmentator 1.5, TotalSegmentator 2.6, Auto3DSeg, MOOSE, MultiTalent, and CADS, on 18 CT scans from the NLST dataset hosted by the [Imaging Data Commons](https://learn.canceridc.dev). While agreement varied across anatomical structures, MOOSE and CADS showed consistent results across all evaluated structures and did not show visible segmentation errors during visual comparison. In contrast, the other four models produced visible segmentation errors or deficiencies in rib and vertebrae structures.

The goal of this Project Week is to select a representative subset of the NLST dataset, run the MOOSE segmentation model on it, and use radiomic features to identify and visually inspect potential segmentation outliers to confirm robustness of the model. Stretch goal is to process all of the CTs in NLST (or even beyond NLST) with MOOSE to generate segmentations and radiomics features, for the subsequent ingestion into Imaging Data Commons.

In addition, the 3DSlicer [CrossSegmentationExplorer](https://github.com/ImagingDataCommons/CrossSegmentationExplorer) extension described in the preprint should be finished and published as an extension for 3D Slicer.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Evaluate how the MOOSE segmentation model performs on a representative subset of the NLST dataset, as the previously analyzed subset did not capture all relevant dataset characteristics.
2. Publish the CrossSegmentationExplorer extension in 3DSlicer
3. Identify any new segmentation models known in the community that might be suitable for automatic segmentation tasks.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Define criteria for NLST subset selection
2. Run MOOSE on that subset and extract radiomic features
3. Analyze feature distributions to detect outliers
4. Visually review outlier cases in Slicer
5. Compare muscle segmentation with https://github.com/MuscleMap/MuscleMap (also https://github.com/Eddowesselink/SlicerMuscleMap for Slicer)
6. Side-project stretch goal: assemble a whole-body single volume image for Visible Human and prepare segmentations from various tools for the resulting image.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- Imaging Data Commons [documentation](https://learn.canceridc.dev/) [portal](https://portal.imaging.datacommons.cancer.gov/explore/)
- Preprint: ["In Search of Truth: Evaluating Concordance of AI-Based Anatomy Segmentation Models"](https://www.arxiv.org/pdf/2512.15921)
- 3DSlicer [CrossSegmentationExplorer](https://github.com/ImagingDataCommons/CrossSegmentationExplorer) extension
- This project is continuing earlier PW42 project [“Review of segmentation results quality across various multi-organ segmentation models”](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/ReviewOfSegmentationResultsQualityAcrossVariousMultiOrganSegmentationModels/) and PW43 project ["Evaluating concordance of AI-based anatomy segmentation models"](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/EvaluatingConcordanceOfAiBasedAnatomySegmentationModels/)

