---
layout: pw45-project

permalink: /:path/

project_title: Slicer Chest Imaging Platform Reboot
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Kalysta Makimoto
  affiliation: Brigham and Women's Hospital
  country: United States

- name: Axel Masquelin
  affiliation: Brigham and Women's Hospital
  country: United States

- name: Raúl San José Estépar
  affiliation: Brigham and Women's Hospital
  country: United States

---

# Project Description

<!-- Add a short paragraph describing the project. -->

`The Chest Imaging Platform (CIP)` is an open-source software suite developed by the `Applied Chest Imaging Laboratory (ACIL)` at Brigham and Women's Hospital (Harvard Medical School). Slicer CIP is designed for quantitative chest CT analysis, helping clinicians and researchers identify and measure phenotypes for Chronic Obstructive Pulmonary Disease (COPD), Interstitial Lung Disease (ILD), Acute Lung Injury (ALI), Pulmonary Vascular Pruning, and Lung Cancer.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

To develop new modules for the Slicer Chest Imaging Platform (CIP)[1]. The first module aims to simplify CT feature extraction for skeletal rib biomarkers. The second module aims to implement SYBIl[2], a deep-learning model for lung cancer outcome predictions. 


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

**Rib Analysis Module**

*Input Data:* Chest CT Images and TotalSegmentator [3] segmentations are required as inputs. If existing segmentations are not available, the TotalSegmentator slicer module wil be used to generate the segmentations.

*Module Development:* Quantitative CT metrics (Mass, Volume, and Density) will be extracted based on the definitions in the CIP Parenchyma Analysis module [1]. The feature quantifications will be modified to reflect the methodlogy performed in our research project [4]. Briefly, Mass and Volume will be extracted form all rib segmentations, then for each rib level the right and left sides will be aggregated. Using the level-aggregated metrics, Density (Mass divided by Volume) will be computed for each rib level. Finally, averaged metrics for Mass, Volume, and Density will be computed for three anatomical regions: True Rib Region (levels 2-7), False Rib Region (levels 8-10), and Floating Rib Region (levels 11-12). Rib level 1 was excluded due to inconsistent segmentations from varying FOV. Based on our results, the most stable CT Rib metrics was CT Rib Density extracted from the True Rib Region, which will be considered the main metric. 

*Module Outputs:* The quantified CT Rib biomarkers will be displayed in a results table, a 3D reconstruction hgihlight the rib levels included in the main metric (CT Rib Density), and bar graphs to illustrate the averaged metrics (Mass and Density) from the anatomical regions. 

**SYBIL Module**

*Input Data:* DICOM Chest CT Images. 

*Module Development:* Leveraged CIP blank module template to create CIP Sybil module. Module searchers for either downloaded SYBIL repository in module directory or pip installs Sybil repository for users (will require restart on first use). Metrics follow SYBIL standard approaches and extracts the latent of the model, along with generating 6-year prediction and heatmap for the view. 

*Module Outputs:* Extracts latent features and exports as .pkl file. Also, exports the six lung cancer predictions as a .json file. Further, generates heatmaps for the regions of interest, shown in the viewer. 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
     
Progress
1. Reviewed the current SlicerCIP modules to identify which modules could be used as a template.
2. Installed the TotalSegmentator extension and tested to ensure segmentations are generated.
3. Developed the CIP Rib Analysis Module to align with the developed methodology.
4. Tested the CIP Rib Analysis Module with an existing segmentation and a segmentation generated using the slicer TotalSegmentation module.
5. Developed the CIP SYBIL Module.
6. Tested the CIP SYBIL Module in the most recent Slicer version. 

Next Steps
1. Update the CIP Rib Analysis Module to accept segmentations from additional methods (e.g. MOOSE).

Issues
1. SYBIL is dependent on torch 1.13 (2 years old) with no plans to update to newer torch versions due to lightening inferance issues. CIP SYBIL Module is dependent on Slicer version 5.8 or lower. 


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Overview of the new Slicer CIP modules (CIP Rib Analysis and CIP SYBIL).
<img width="3471" height="1900" alt="OverviewFigure" src="https://github.com/user-attachments/assets/821d8abe-1044-4bcf-a92c-3ab0d0e98efd" />

Demo of the CIP Rib Analysis Module.
<video
   controls muted
   src="https://github.com/user-attachments/assets/144faf2f-5e67-43bf-acec-71224aa947de"
   style="max-width:800px">
 </video>

Demo of the CIP SYBIL Module. 
<video
   controls muted
   src="https://github.com/user-attachments/assets/c4b99953-1b9e-42df-818c-9f5f9b287c71"
   style="max-width:800px">
 </video>


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

1. [Chest Imaging Platform](https://chestimagingplatform.org/)
2. Mikhael, P. G., Wohlwend, J., Yala, A., Karstens, L., Xiang, J., Takigami, A. K., ... & Barzilay, R. (2023). Sybil: a validated deep learning model to predict future lung cancer risk from a single low-dose chest computed tomography. Journal of Clinical Oncology, 41(12), 2191-2200.
3. Wasserthal, J., Breit, H. C., Meyer, M. T., Pradella, M., Hinck, D., Sauter, A. W., ... & Segeroth, M. (2023). TotalSegmentator: robust segmentation of 104 anatomic structures in CT images. Radiology: Artificial Intelligence, 5(5), e230024.
4. Makimoto, K., Iturroz Campo, M., San José Estépar, R. & San José Estépar, R. (2026). Computed tomography rib density is associated with cross-sectional outcomes and mortality in COPD. European Respiratory Journal. (Submitted). 
