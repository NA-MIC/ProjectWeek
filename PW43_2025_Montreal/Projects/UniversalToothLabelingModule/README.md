---
layout: pw43-project

permalink: /:path/

project_title: Universal Tooth Labeling Module
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Enzo Tulissi
  affiliation: University of Michigan
  country: USA

- name: Lucia Cevidanes
  affiliation: University of Michigan
  country: USA

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

- name: Jonas Bianchi
  affiliation: University of Pacific
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The **Universal Tooth Labeling** module employs nnUNet to automatically label all teeth (including primary dentition) from CBCT scans.  
It aims to deliver robust, anatomically correct labels for each tooth.

Currently, some outputs exhibit left/right mirroring errors (e.g., both canines labeled as “right canine”).



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. **Resolve mirroring errors** in the labeling output.  
2. **Optimize nnUNet training** (patch size, batch size, learning rate) and augmentations.  
3. **Implement post‐processing checks** to verify and correct side‐specific labels.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Analyze cases with mirroring errors and identify their characteristics.    
2. Tune nnUNet hyperparameters for optimal label accuracy.  
3. Develop a post‐processing module to enforce correct left/right assignment.  
4. Evaluate performance (DSC, IoU) on a dedicated test set.  



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.
**Completed:**
- Initial nnUNet pipeline and label export implemented.  
- Prototype output integrated into 3D Slicer.

**Next Steps:**
- Fix mirroring bugs in output labels.  
- Conduct clinical validation and benchmarking.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![image](https://github.com/user-attachments/assets/5632a488-8b6d-45b3-946c-567c8d40b613)

*Figure 1: Example output from Universal Tooth Labeling*



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [Universal Tooth Labeling (in progress)](https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools/tree/main/BATCHDENTALSEG)

