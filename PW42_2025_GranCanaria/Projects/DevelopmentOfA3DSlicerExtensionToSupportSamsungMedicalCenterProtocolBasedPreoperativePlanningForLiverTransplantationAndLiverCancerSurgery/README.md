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




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We will start by following the [tutorial](https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g420896289_0251) for developing a 3D slicer extension.
2. Since we are researchers with a background in Medical Illustration rather than Computer Science, we plan to actively utilize Cursor.ai and Slicer documentation to develop our module during this hackathon.
3. We always welcome advice from other researchers who have experience developing Slicer modules! 😊




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://github.com/user-attachments/assets/c148b8cb-068c-46d9-8a8a-f4934c0a7ada)

![Image](https://github.com/user-attachments/assets/af809947-9b15-418e-811e-6534927ba75d)

![Image](https://github.com/user-attachments/assets/dec01856-0947-4d03-95a9-9d763a03b6d5)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Rhu J, Choi GS, Kim MS, Kim JM, Joh JW. Image guidance using two-dimensional illustrations and three-dimensional modeling of donor anatomy during living donor hepatectomy. Clin Transplant. 2021 Jan;35(1):e14164. doi: 10.1111/ctr.14164. Epub 2020 Dec 12. PMID: 33222255. [https://pubmed.ncbi.nlm.nih.gov/33222255/](https://pubmed.ncbi.nlm.nih.gov/33222255/)


Oh, N., Kim, JH., Rhu, J. *et al.* Automated 3D liver segmentation from hepatobiliary phase MRI for enhanced preoperative planning. *Sci Rep* **13**, 17605 (2023). [https://doi.org/10.1038/s41598-023-44736-w](https://doi.org/10.1038/s41598-023-44736-w)
