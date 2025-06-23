---
layout: pw43-project

permalink: /:path/

project_title: Physics-informed neural networks to improve registration accuracy for image-guided
  neurosurgery
category: Quantification and Computation

key_investigators:

- name: Benjamin Zwick
  affiliation: University of Western Australia

- name: Mostafa Jamshidian
  affiliation: University of Western Australia

- name: Sajjad Arzemanzadeh
  affiliation: University of Western Australia

- name: Karol Miller
  affiliation: University of Western Australia

- name: Adam Wittek
  affiliation: University of Western Australia

- name: Paul Parizel
  affiliation: University of Western Australia

- name: Ron Kikinis
  affiliation: Harvard Medical School
  country: USA

- name: Michael Bynevelt
  affiliation: Department of Health WA
  country: Australia

- name: Alexandra Golby
  affiliation: Harvard Medical School
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Brain tumour surgery relies on preoperative images for planning and guidance. But during surgery the brain shifts, reducing navigation accuracy. This project will develop an artificial intelligence-based technique that combines biomechanics and machine learning in a physics-informed neural network to track brain shift during surgery. This will help surgeons remove tumours more precisely while preserving healthy tissue, reducing adverse effects and follow-up surgeries for better patient outcomes.

This project aims to develop a biomechanics-guided physics-informed neural network (PINN) to correct preoperative images for intraoperative brain shift, enhancing the precision, accuracy, and efficiency of neuronavigation in brain tumour surgery.

Surgical outcomes depend on precise navigation, but once surgery begins, the brain deforms due to cerebrospinal fluid drainage, gravity, and resection. This brain shift renders preoperative images inaccurate, compromising localisation of tumour boundaries and identification of critical neural structures.

Existing solutions are limited. Intraoperative imaging lacks the resolution of preoperative scans and can be costly, slow, or unavailable. Purely physics-based methods that predict brain shift using patient-specific biomechanical models require time-consuming geometry reconstruction and mechanical property description of brain tissues.  We propose a novel approach that integrates physics-based modelling with data-driven machine learning. Our specific aims are to:
1. develop and train a PINN to correct preoperative images for intraoperative brain shift
2. integrate the PINN into a non-rigid image registration framework using open-source software; and
3. evaluate the PINN’s performance against existing techniques.

The PINN will incorporate biomechanics-based constraints to ensure deformation fields conform to brain tissue mechanics. Training will use retrospective data from Harvard Medical School. Performance will be assessed by comparing predicted tumour and ventricle contours with actual positions identified on intraoperative magnetic resonance images.

By combining the strengths of physics-based and data-driven methods, the proposed PINN-based approach has the potential to provide intraoperative images with accuracy and resolution comparable to preoperative images.  This would enable more precise tumour localisation, reducing incomplete resections and preserving healthy tissue, and ultimately improving patient outcomes.

Ultimately, we aim to implement these methods into 3D Slicer extension.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Develop and validate a novel PINN-based non-rigid image registration technique that accurately tracks large brain deformations during surgery in real time.
2. Objective B. Perform validation using a dataset of clinical cases from the Advanced Multimodality Image Guided Operating (AMIGO) suite, demonstrating the technique's applicability in a clinical setting.
3. Objective C. Implement real-time brain shift correction by combining preoperative MRI images with intraoperative sparse imaging data, providing an adaptable system for various surgical scenarios.
4. Objective D. Demonstrate the scalability of the technique by applying it to a broader patient cohort and comparing its performance to existing rigid and non-rigid registration methods.
5. Objective E. Disseminate the developed algorithms via the widely used 3D Slicer medical imaging platform (https://www.slicer.org/), ensuring its availability for clinical and research purposes.
6. Objective F. Publish high-impact journal articles in leading medical and engineering journals, such as Medical Image Analysis and NeuroImage.
7. Objective G. Secure additional research funding through ARC Linkage and NHMRC applications, leveraging the project’s outcomes to support future clinical trials and the expansion of the research to other imaging modalities, such as intraoperative ultrasound.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Discuss current state-of-the-art registration techniques in 3D Slicer.
2. Develop a workflow for integrating PINNs-based registration into 3D Slicer.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


### SlicerCBM
We have previously developed the SlicerCBM “Computational Biophysics for Medicine in 3D Slicer” extension for biomechanics-based image registration. [SlicerCBM](https://github.com/SlicerCBM/SlicerCBM) is an extension for[ 3D Slicer](http://slicer.org/) that provides tools for creating and solving computational models of biophysical systems and processes with a focus on clinical and biomedical applications. Features include grid generation, assignment of material properties and boundary conditions, and solvers for biomechanical modeling and biomechanics-based non-rigid image registration.

