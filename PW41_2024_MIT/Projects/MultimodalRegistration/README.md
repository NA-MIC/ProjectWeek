---
layout: pw41-project

permalink: /:path/

project_title: Multimodal Registration MR2CBCT
category: Quantification and Computation
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

- name: Allemang David
  affiliation: Kitware
  country: USA

- name: Prieto Juan Carlos
  affiliation: University of North Carolina
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to develop a novel Slicer tool that combines machine learning with image processing technique with image processing techniques to automatically register MRI to CBCT images, enabling enhanced visualization and analysis of the TMJ complex.  By integrating MRI soft tissue information with CBCT bony details, this automated technique provides clinicians with a more comprehensive patient-specific 3D model of the TMJ to improve diagnostic accuracy and treatment planning. 
Temporomandibular joint (TMJ) disorders affect a significant portion of the population and can cause chronic pain and disability. Accurate diagnosis is crucial for effective treatment planning, but can be challenging due to the complex anatomy and limited visibility of soft tissue structures on Cone Beam CT (CBCT) scans. MRI provides superior soft tissue contrast including the articular disc, but requires separate acquisition and manual registration with CBCT for detailed bone degeneration assessments. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


The “Multimodal Registration MR2CBCT Project” aims to develop a sequennce of image anlaysis preprocessing steps prior to accurately aligning and overlaying CBCT and MRI multimodal images, using Elastix registration tools.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. **Dataset Collection:**
   - Compile a comprehensive dataset consisting of MRI and CBCT files.
   - Perform manual approximation to align MRI and CBCT images initially.
   - Perform manual segmentation of the MRI.

2. **Image Registration Strategy:**
   - The primary goal is to achieve precise registration between MRI and CBCT images. To accomplish this, we are exploring two main approaches:

#### First Approach:
   - **Image Transformation Model:** 
     - Develop and train a model to transform MRI images into CBCT-like images.
   - **CBCT Registration:**
     - Utilize existing tools to register the transformed CBCT images with actual CBCT images.

#### Second Approach:
   - **Manual Segmentation:**
     - Conduct automated segmentation of CBCT images as an initial step.
   - **Automated MRI Segmentation:**
     - Train a model to automate the segmentation process of MRI images.
   - **Elastix-Based Registration:**
     - Use Elastix to do the registration between MRI and CBCT images based on the segmentation.
           - Invert MRI to facilitate the registration process with Elastix.
           - Normalized MRI and CBCT
3. **Validate:**
   - Validate the best method accuracy through rigorous testing against established benchmarks.
   - Create the Slicer module interface
   - Write documentationsand examples 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

### Progress

1. **Dataset Collection:**
   - We compiled a comprehensive dataset consisting of MRI and CBCT files.
   - Performed manual approximation to initially align MRI and CBCT images.

2. **Image Registration Strategy:**
#### Second Approach:
   - **Manual Segmentation:**
     - Conducted automated segmentation of CBCT images as an initial step.
   - **Image Preprocessing:**
     - Invert the gray scale level of the MRI
     - Normalize the MRI and the CBCT 
   - **Elastix-Based Registration:**
     - Working to use Elastix to do the registration between MRI and CBCT images using the manual segmentation. The MRI has been inverted to facilitate the registration process with Elastix.

### Next Steps
2. **Image Registration Strategy:**
#### First Approach:
   - **CBCT Registration:**
     - Develop and train a model to transform MRI images into CBCT-like images.
     - After finalizing the transformation model, utilize existing tools to register the transformed CBCT images with actual CBCT images.

#### Second Approach:
   - **Automated MRI Segmentation:**
     - Train a model to automate the segmentation process.

3. **Validate:**
   - Validate the best method accuracy through rigorous testing against established benchmarks.
   - Create the Slicer module interface
   - Write documentationsand examples





# Illustrations
#### Manual Segmentation of the Cranial Base on an MRI
![Manual Segmentation of the Cranial Base on an MRI](https://github.com/NA-MIC/ProjectWeek/assets/91245687/a4a73f38-5e28-4d32-a5ad-816cad73b118)

#### Invertion of an MRI
![Invertion of an MRI](https://github.com/NA-MIC/ProjectWeek/assets/91245687/7b8e4f61-90cf-45e8-99de-7e461fc1365b)

#### Manual Manual Approximation of an MRI on a CBCT
![Manual Manual Approximation of an MRI on a CBCT](https://github.com/NA-MIC/ProjectWeek/assets/91245687/5c4211ce-e930-4bf0-b9d8-a1193a29ea0a)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

