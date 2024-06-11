---
layout: pw41-project

permalink: /:path/

project_title: Multimodal registration
category: Other
presenter_location: In-person

key_investigators:

- name: Leroux Gaelle
  affiliation: University of Michigan
  country: USA

- name: Claret Jeanne
  affiliation: University of Michigan
  country: USA

- name: Cevidanes Lucia
  affiliation: University of Michigan
  country: USA

- name: Allemand David
  affiliation: Kitware
  country: USA

- name: Prieto Juan Carlos
  affiliation: University of North Carolina
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The “Multimodal Registration Project” aims to develop a system capable of aligning different medical imaging modalities to enhance diagnostic accuracy and patient outcomes. By focusing on the registration of Cone Beam Computed Tomography (CBCT) with Magnetic Resonance Imaging (MRI), we seek to create a unified imaging model that offers comprehensive insights into patient anatomy and pathology.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. The objective is to register MRI images with CBCT data accurately.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


## Approach and Plan
1. **Dataset Collection:**
   - Compil a comprehensive dataset consisting of MRI and CBCT files.
   - Perform manual approximation to align MRI and CBCT images initially.

2. **Image Registration Strategy:**
   - The primary goal is to achieve precise registration between MRI and CBCT images. To accomplish this, we are exploring two main approaches:

#### First Approach:
   - **Image Transformation Model:** 
     - Develop and train a model to transform MRI images into CBCT-like images.
   - **CBCT Registration:**
     - Utilize existing tools to register the transformed CBCT images with actual CBCT images.

#### Second Approach:
   - **Manual Segmentation:**
     - Conduct manual segmentation of MRI images as an initial step.
   - **Automated MRI Segmentation:**
     - Train a model to automate the segmentation process of MRI images.
   - **Elastix-Based Registration:**
     - Use Elastix to train a model specifically for the registration between MRI and CBCT images based on the segmentation.
3. **Validate:**
   - Validate the best method accuracy through rigorous testing against established benchmarks.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


## Progress and Next Steps

### Progress

1. **Dataset Collection:**
   - We compiled a comprehensive dataset consisting of MRI and CBCT files.
   - Performed manual approximation to initially align MRI and CBCT images.

#### First Approach:
   - **Image Transformation Model:** 
     - Developing and training a model to transform MRI images into CBCT-like images.

#### Second Approach:
   - **Manual Segmentation:**
     - Conducted manual segmentation of MRI images as an initial step.

### Next Steps

#### First Approach:
   - **CBCT Registration:**
     - After finalizing the transformation model, utilize existing tools to register the transformed CBCT images with actual CBCT images.

#### Second Approach:
   - **Automated MRI Segmentation:**
     - Once manual segmentation is complete, train a model to automate the segmentation process.
   - **Elastix-Based Registration:**
     - Use Elastix to train a model specifically for the registration between MRI and CBCT images.





# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

