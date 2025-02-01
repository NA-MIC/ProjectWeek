---
layout: pw42-project

permalink: /:path/

project_title: Development of a 3D Slicer Extension to Support Samsung Medical Center Protocol Based
  PreOperative Planning for Liver Transplantation and Liver Cancer Surgery
category: Infrastructure

key_investigators:

- name: Soyoung Lim
  affiliation: Samsung Medical Center
  country: Republic of Korea

- name: Hyejeong Hong
  affiliation: Samsung Medical Center
  country: Republic of Korea

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This extension will be developed for use at Samsung Medical Center to support their protocol-based pre-operative planning for liver transplantation and liver cancer surgery using 3D Slicer. The extension will generate accurate 3D patient models from medical imaging data and enable surgical planning and simulation. This will improve the efficiency of the 3D reconstruction process.

A recent study (Rhu et al., 2021) found that using 2D illustrations and 3D modeling of donor anatomy during living donor hepatectomy improved image guidance for liver transplantation procedures at Samsung Medical Center. The medical center has established a protocol for 3D reconstruction to generate accurate patient-specific 3D models from medical imaging data, enabling enhanced pre-operative planning and simulation.

Since the summer of 2023, the medical center's research team has been transitioning from MIMICS program to 3D Slicer as their primary segmentation tool. To streamline the repetitive tasks, they have been working to automate the workflow using custom scripts starting in early 2024. The goal of this project is to develop a specialized 3D Slicer extension that aligns with the established institutional protocols and automates the 3D modeling process.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. The goal is to develop 5–6 of the most frequently used features from the custom script currently connected to the slicer.rc file into a Slicer module, making it easier to maintain. This will help automate repetitive tasks in the data preparation process for long-term research. Planned features include tools for optimizing liver transplantation surgery segmentation, liver cancer segmentation, displaying dice score comparison tables and liver segment volume tables related to AI research, and exporting segmentation masks as NIfTI files for AI training.

2. Given that Slicer is a visualization tool, an additional goal is to implement features for customizing 3D view rendering materials and lighting settings. As someone with a background in design and medical illustration who frequently uses Blender 3D, I’ve always thought having a module for adjusting rendering options in 3D Slicer would be beneficial. This idea could be extended by creating optimized rendering presets for different organs, making it easier to apply tailored visual settings.

3. We also intend to improve the manual script currently used for volume and dice score tables. Enhancements will include allowing one-click copy-paste functionality and saving results directly as Excel files for easier review.

**[Project Proposal PPT ->](https://docs.google.com/presentation/d/1kLeWb436ZpJCnbPZJxa0f1xVZAY0btyB/edit?usp=drive_link&ouid=117843046046586749971&rtpof=true&sd=true)** 



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will start by following the [tutorial](https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g420896289_0251) for developing a 3D slicer extension.
2. Since we are researchers with a background in Medical Illustration rather than Computer Science, we plan to actively utilize Cursor.ai and Slicer documentation to develop our module during this hackathon.
3. We always welcome advice from other researchers who have experience developing Slicer modules! 😊




## Progress and Next Steps

Our workflow diagram for Liver Cancer Surgery 3D Images and AI data (before participating Project Week 2025)

<img width="3412" alt="Image" src="https://github.com/user-attachments/assets/7d81e77a-829c-4ef9-b257-2f9d18ed3410" />


Our workflow diagram for Living Donor Liver Transplantation Surgery 3D Images and AI data (before participating Project Week 2025)

<img width="3476" alt="Image" src="https://github.com/user-attachments/assets/e1f33145-b40b-4f9a-985e-a7fe96f677f9" />


[Day 1-2] Studied and studying tutorial documents on devleoping Slicer Extension. + Tested making modules with "Extension Wizard"
https://training.slicer.org/ 
https://slicer.readthedocs.io/en/latest/developer_guide/index.html



[Day 2-5] Began developing the Liver Volumetry module for LDLT, which calculates the Graft-to-Recipient Weight Ratio (GRWR) to assist in selecting the optimal liver donor among candidates. The GRWR is a key parameter in liver transplantation, ensuring that the donated liver graft is of adequate size to support the recipient’s metabolic needs.

![Image](https://github.com/user-attachments/assets/7efe841f-37a5-4b55-bd95-83baec421e62)

Studied and studying the [Bone Reconstruction Planner module from SlicerIGT](https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L423) for reference (thanks to Mauro I. Dominguez).

Tasks:
Designing the UI using Qt Designer
Implementing signal/slot connections


Next Steps
1. Finalize module logic for LDLT donor volumetry and test.
2. Finalize module UI for Liver Cancer Surgery module, logic and test.
3. After making the module, upload it to Slicer extension market. ((https://github.com/Slicer/ExtensionsIndex/tree/main)







# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://github.com/user-attachments/assets/76d91735-6e44-486a-84d2-0d2bb599a4cc)

https://github.com/user-attachments/assets/0776a062-2128-4773-84de-8c3174e869ed

![Image](https://github.com/user-attachments/assets/485e8a96-ff90-406a-a792-c2fc97408c78)

![Image](https://github.com/user-attachments/assets/576e7253-d77e-4f9b-8449-01b229c8e3e8)

![Image](https://github.com/user-attachments/assets/e5ef5fc4-5dd5-43d8-90d3-a04117170f58)

![Image](https://github.com/user-attachments/assets/e4a1f9c8-f0d3-4642-ae44-1b8baacc4e6a)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Rhu J, Choi GS, Kim MS, Kim JM, Joh JW. Image guidance using two-dimensional illustrations and three-dimensional modeling of donor anatomy during living donor hepatectomy. Clin Transplant. 2021 Jan;35(1):e14164. doi: 10.1111/ctr.14164. Epub 2020 Dec 12. PMID: 33222255. [https://pubmed.ncbi.nlm.nih.gov/33222255/](https://pubmed.ncbi.nlm.nih.gov/33222255/)


Oh, N., Kim, JH., Rhu, J. *et al.* Automated 3D liver segmentation from hepatobiliary phase MRI for enhanced preoperative planning. *Sci Rep* **13**, 17605 (2023). [https://doi.org/10.1038/s41598-023-44736-w](https://doi.org/10.1038/s41598-023-44736-w)

