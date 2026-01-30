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
5. Compare muscle segmentation with [MuscleMap](https://github.com/MuscleMap/MuscleMap) (also [SlicerMuscleMap](https://github.com/Eddowesselink/SlicerMuscleMap) for Slicer)
6. Side-project stretch goal: assemble a whole-body single volume image for Visible Human and prepare segmentations from various tools for the resulting image.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


### 1. Representative NLST Subset Selection
The representative subset selection was guided by an initial sampling strategy developed together with Claude AI. Based on this plan, a Python notebook was generated and iteratively refined. The notebook is available in the [**`nlst-exploration`**](https://github.com/fedorov/nlst-exploration/tree/main) repository.


**Dataset filtering:** We excluded all CT series without existing TotalSegmentator segmentations, as these had already been filtered out previously due to problematic acquisition parameters (e.g., invalid pixel spacing).

**Selection of relevant DICOM attributes:** Together with Claude AI, we discussed and defined a set of DICOM parameters that should be considered to capture relevant variability in acquisition, reconstruction, and scanner hardware.
The following attribute groups were selected: Spatial: 'SliceThickness', 'PixelSpacing', 'SpacingBetweenSlices'; Exposure: 'KVP', 'Exposure', 'CTDIvol'; Reconstruction: 'ConvolutionKernel'; Hardware': 'Manufacturer', 'ManufacturerModelName'; Geometry': 'PatientPosition', 'GantryDetectorTilt', 'SpiralPitchFactor';

The following attributes were found to be constant or empty across the dataset and were therefore excluded from further analysis: SpacingBetweenSlices, CTDIvol, PatientPosition, and GantryDetectorTilt.

At this stage, the selection focuses exclusively on series-level acquisition and reconstruction parameters.
Patient-related attributes (e.g. age, sex, or other clinical metadata) are not yet included in the sampling strategy and will be incorporated in a future iteration.

**Data reduction:** To reduce the combinatorial complexity of the parameter space we rounded continuous attributes as follows:
- *Slice thickness* was rounded to one decimal place.
- *Pixel spacing* was rounded to one decimal place.
- *KVP* was rounded to the nearest integer.
- *Exposure* values were rounded to the nearest 100 units.

**Dataset statistics (after filtering and data reduction):**
| Numerical Attribute             | Count  | Unique | Min  | Q25  | Median | Mean | Q75  | Max   | Std  |
|-----------------------|--------|----------|------|------|--------|------|------|-------|------|
| SliceThickness    | 133273 | 13       | 0.60 | 2.00 | 2.50   | 2.47 | 2.50 | 6.50  | 0.90 |
| PixelSpacing  | 133273 | 7        | 0.40 | 0.60 | 0.70   | 0.66 | 0.70 | 1.00  | 0.07 |
| KVP                   | 133273 | 7        | 80   | 120  | 120    | 121  | 120  | 140   | 5    |
| Exposure               | 133256 | 62       | 0    | 0    | 100    | 504  | 1000 | 9000  | 668  |
| SpiralPitchFactor     | 38629  | 9        | 0.75 | 1.38 | 1.50   | 1.47 | 1.50 | 1.75  | 0.15 |

| Categorical Attribute     | Count  | Unique | Most Frequent Value | Most Frequent (%) | Top 3 Values                                   |
|---------------------------|--------|----------|----------------------|-------------------|------------------------------------------------|
| Manufacturer              | 133273 | 4        | GE MEDICAL SYSTEMS   | 45.4 %            | GE MEDICAL SYSTEMS, SIEMENS, Philips            |
| ManufacturerModelName     | 133273 | 23       | Volume Zoom          | 20.8 %            | Volume Zoom, Sensation 16, LightSpeed QX/i      |
| ConvolutionKernel         | 133273 | 36       | STANDARD             | 29.9 %            | STANDARD, B30f, B50f                            |


**Clustering and sampling:** Based on the normalized attributes, Claude AI proposed a clustering strategy to group series with similar acquisition and reconstruction characteristics. The dataset was clustered into 14 distinct clusters. From each cluster, 3 representative CT series were selected, this resulted in a total of 48 CT series.
Post-hoc verification using summary statistics confirmed that the selected subset mostly reflects the global parameter distributions of the filtered NLST dataset, with most acquisition parameters covering the interquartile range Q25–Q75 of the full dataset.


| Numerical Attribute             | Min  | Median | Max   | 
|-----------------------|------|--------|-------|
| SliceThickness    | 1.0  | 2.5    | 5.0   |
| PixelSpacing | 0.64 | 0.665  | 0.72  | 
| KVP                   | 120  | 120    | 140   |
| Exposure               | 0    | 100    | 3000  |
| SpiralPitchFactor     | 0.75 | 1.5    | 1.5   | 

A CSV file listing all selected representative CT series is available in the [**`nlst-exploration`**](https://github.com/fedorov/nlst-exploration/tree/main)repository.

**Segmentation Generation:** Segmentation generation was initially planned using only the MOOSE model. However, based on results from a prior comparative analysis on the NLST dataset, CADS segmentations were additionally generated. Both models had previously shown the most consistent performance and did not show visible segmentation errors across the evaluated anatomical structures. Since it was not possible to determine which of the two models performs better on this dataset, both MOOSE and CADS were included in the analysis.

**Next Steps (Future Work)**
- Extract radiomic features from MOOSE and CADS segmentations using [Radiomics.jl](https://github.com/pzaffino/Radiomics.jl).
- Analyze feature distributions to identify potential segmentation outliers.
- Visually inspect identified outliers using [CrossSegmentationExplorer](https://github.com/ImagingDataCommons/CrossSegmentationExplorer) in 3D Slicer.
- Extend representative sampling by incorporating patient-related attributes.

### 2. Publish the CrossSegmentationExplorer extension in 3DSlicer
A Pull Request to include CrossSegmentationExplorer as a Tier 1 3D Slicer extension has been created.





# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- Project repository: [nlst-exploration](https://github.com/fedorov/nlst-exploration)
- Imaging Data Commons [documentation](https://learn.canceridc.dev/) [portal](https://portal.imaging.datacommons.cancer.gov/explore/)
- Preprint: ["In Search of Truth: Evaluating Concordance of AI-Based Anatomy Segmentation Models"](https://www.arxiv.org/pdf/2512.15921)
- 3DSlicer [CrossSegmentationExplorer](https://github.com/ImagingDataCommons/CrossSegmentationExplorer) extension
- BigQuery table ID for NLST series-level metadata: idc-external-031.nlst_capstone2025.series_level_characteristics
- This project is continuing earlier PW42 project [“Review of segmentation results quality across various multi-organ segmentation models”](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/ReviewOfSegmentationResultsQualityAcrossVariousMultiOrganSegmentationModels/) and PW43 project ["Evaluating concordance of AI-based anatomy segmentation models"](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/EvaluatingConcordanceOfAiBasedAnatomySegmentationModels/)
- [Radiomics.jl](https://github.com/pzaffino/Radiomics.jl)

