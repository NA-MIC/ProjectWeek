---
layout: pw43-project

permalink: /:path/

project_title: 'Interpretable Deep Learning for the Detection and Classification of Impacted Canines
  and severity of root resorption '
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


The **CLIC** module uses a Mask R-CNN segmentation model to locate and classify impacted canines in CBCT scans.  
This project extends CLIC by developing a supervised model to automatically classify the severity of root resorption in teeth adjacent to impacted canines.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. **Segment impacted canines** using the existing CLIC module.  
2. **Extract adjacent teeth** volumes for analysis.  
3. **Assemble an annotated dataset** of adjacent teeth with clinician‐provided resorption severity scores.  
4. **Train a classification model** to predict root resorption severity from segmented volumes.  
5. **Integrate and visualize** segmentation plus severity scores within 3D Slicer.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Run CLIC across the CBCT dataset to isolate impacted canines.  
2. Combine CLIC masks to extract volumes of adjacent teeth.  
3. Annotate each extracted tooth volume with a severity label (mild, moderate, severe).  
4. Extract geometric and morphological feature sets from each volume.  
5. Train a classifier on these features.  
6. Extend CLIC or create a new Slicer module for real‐time severity classification.  
7. Validate model performance (accuracy, recall, precision) and integrate into the 3D visualization workflow.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


**Completed:**
- CLIC module validated.  
- Prototype pipeline for adjacent tooth extraction established.

**Next Steps:**
- Clinician annotation of extracted tooth volumes.  
- Feature engineering and model training.  
- UI design for severity score display in Slicer.  
- Performance evaluation and final documentation.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![image](https://github.com/user-attachments/assets/6f588a90-3e77-440c-b5c9-9ef0c9550150)

*Figure 1: Impacted canine segmentation results from CLIC*



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

