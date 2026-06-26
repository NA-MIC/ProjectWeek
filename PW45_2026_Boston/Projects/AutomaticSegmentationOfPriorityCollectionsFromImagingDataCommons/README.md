---
layout: pw45-project

permalink: /:path/

project_title: Automatic segmentation of priority collections from Imaging Data Commons
category: Cloud / Web
presenter_location: 

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Kyle Sunderland
  affiliation: Queen's
  country: Canada

- name: Vamsi Thiriveedhi
  affiliation: MGH
  country: USA

- name: Paolo Zaffino
  affiliation: Magna Graecia U. of Catanzaro
  country: Italy

- name: Lalith Kumar Shiyam Sundar
  affiliation: LMU
  country: Germany

- name: Michael Onken
  affiliation: OpenConnections GmbH
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

**Questions? Want to participate remotely? Join our project [Discord channel](https://discord.gg/TTFGUYGdsZ)!**

The goal of this project is to further increase availability of anatomic segmentations and accompanying radiomics features for the images available in Imaging Data Commons.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Volumetric segmentations of the anatomy for selected images in IDC.
2. Radiomics features for the segmented labels.
3. Interface to explore the resulting data.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop Terra workflow wrapping selected MOOSE, VIBESegmenator and TotalSegmentator models
2. Extract radiomics features using Radiomics.jl
3. Saving resulting segmenations and radiomics features into DICOM using dcmqi
4. Test on a representative sample from IDC (prioritize processing of Cancer Moonshot Biobank and CPTAC images)
5. Apply to a larger cohort
6. Develop review interface, examine results, investigate possible issues
7. Apply workflow to the APOLLO5 dataset (embargoed)



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
This week we made progress on debugging/fixing/imporoving segmentation workflow and the associated tools.

1. Refined post-processing component of the workflow - improved/fixed generation of DICOM SEG.
2. Fixed handling of deflate transfer syntax in dcmqi, which was broken on windows (which was also broken in Slicer) [https://github.com/QIICR/dcmqi/pull/549](https://github.com/QIICR/dcmqi/pull/549)
3. Adding SNOMED mapping upstream to the MOOSE segmentator [https://github.com/ENHANCE-PET/MOOSE/pull/241](https://github.com/ENHANCE-PET/MOOSE/pull/241)
4. Started working on making the segmentation workflow applicable to segmentation of non-IDC data (via private Google bucket access)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="776" height="499" alt="Image" src="https://github.com/user-attachments/assets/5a146049-09b6-4aea-8298-4f8d79b7e5eb" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- <https://portal.imaging.datacommons.cancer.gov/>
- <https://terra.bio/>
- <https://github.com/ENHANCE-PET/MOOSE>
- <https://github.com/robert-graf/VIBESegmentator>
- <https://github.com/pzaffino/Radiomics.jl>
- <https://github.com/QIICR/dcmqi>
- <https://github.com/wasserth/totalsegmentator>
- <https://doi.org/10.1117/1.JMI.13.6.062204>

