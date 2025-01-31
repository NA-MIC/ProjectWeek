Back to [Projects List](../../README.md#ProjectsList)

# 3D Slicer Lung CT Segmentation

## Key Investigators

*   Rudolf Bumm (KSGR)
*   Ron Kikinis (Brigham and Women's Hospital)
*   Raúl San José Estépar (Brigham and Women's Hospital)
*   Steve Pieper (Isomics)
*   Eserval Rocha jr. (University of Sao Paulo Medical School)
*   Andras Lasso (Perk Labs)
*   Curtis Lisle (KnowledgeVis)

# Project Description

This is a follow-up to previous 3D Slicer lung CT segmentation PW projects. 

## Objective

Our objective is to improve the lung CT segmentation and analysis processes in 3D Slicer.

*   Improve **vessel** segmentation
*   Implement **emphysema** and COPD analysis
*   Develop a concept for **lung segment** segmentation in 3D Slicer
*   Fine-tune the workflow for **surgical planning**
*   Work on possible **grant application**

## Specific Approach and Plan

*   make lung, lobe, and airway segmentation fully automatic (no manual intervention)
*   write a batch script that makes use of the LCTA logic
*   test the script on the OpenSourceCovidDatabase
*   evaluate results and compare them to radiology score 
*   discuss strategies for vessel segmentation and segment detection

## Progress and Next Steps

During the project week, we were able to apply SlicerLiver (with fantastic help of the liver team) to a working demo lung segmentation dataset, demonstrating that segment-oriented lung resection can be simulated in SlicerLiver using VMTK and dedicated software functions.
Furthermore, we talked with Jakob Wasserthal, the creator of TotalSegmentator, about how to incorporate pulmonary artery and vein segmentation into his deep-learning tool. Raoul San Jose Estbar agreed to provide the TotalSegmentator training dataset with ground truth data. We elaborated the skeleton of a grant application for vessel-based lung segment segmentation.

We ran LCTA over the complete dataset of the OpenSourceCovidDataset with great results and a good correlation between radiology expert and machine. 

![](https://user-images.githubusercontent.com/18140094/216458521-1df25eb4-63b2-4946-8b67-6881f8050024.png)

![](https://user-images.githubusercontent.com/18140094/216458649-a7862df4-4c2a-4518-a1f8-c1e0b441be9c.png)

# Illustrations

![](https://user-images.githubusercontent.com/18140094/216455289-bbf2d613-57f4-423f-8e17-0263a5cda126.png)

![](https://user-images.githubusercontent.com/18140094/216455423-5c2990be-b31d-4691-9bf9-1c3540366e4c.png)

# Background and References

[Lung CT Analyzer extension](https://github.com/rbumm/SlicerLungCTAnalyzer)

[Open Source COVID Database](https://www.mdpi.com/2306-5354/8/2/26)
