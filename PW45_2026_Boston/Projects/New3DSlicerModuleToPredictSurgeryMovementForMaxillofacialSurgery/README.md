---
layout: pw45-project

permalink: /:path/

project_title: New 3D Slicer Module to predict surgery movement for maxillofacial surgery
category: IGT and Training
presenter_location: 

key_investigators:

- name: Alexandre Buisson
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Paul Dumont
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Juan Carlos Prieto
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Lucia Cevidanes
  affiliation: University of North Carolina at Chapel Hill
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Mauro I. Dominguez (I added me if that's ok)
  affiliation: Independent
  country: Argentina


---

# Project Description

<!-- Add a short paragraph describing the project. -->


Predicting surgical movements and bone displacement vectors in virtual surgical planning software remains an expert-intensive task, requiring surgeons to simulate osteotomies and manually adjust bone segments. Although statistical shape models and deep learning regression networks have been explored to automate this phase, they output dense deformation fields that lack the geometric interpretability needed to guide clinical or surgical decisions.

This project introduces a dedicated 3D Slicer module driven by a Machine Learning Stacking model, trained on a robust dataset of 1,496 patients. The module simplifies the clinical workflow by allowing users to upload an input file (e.g., Excel/CSV containing clinical parameters) and instantly receive accurate, data-driven predictions of the required maxillofacial bone movements.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Embed a pre-trained Stacking ML model into the 3D Slicer environment to leverage multi-patient surgical data.
- Enable seamless parsing of input files (Excel/CSV) to extract patient-specific features.
- Generate and display precise bone movement recommendations directly within the Slicer interface based on the model's inference.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Develop the input file parser (Excel/CSV) to clean and prepare patient data for the model.
- Integrate the pre-trained Stacking ML model into a Python-based 3D Slicer scripted module.
- Design a user-friendly Slicer UI that allows clinicians to load patient files, trigger the prediction, and visualize the recommended bone displacements.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


The core Stacking ML model has been successfully trained and validated using a dataset of 1,496 patient cases.

During the project week we'll build an interactive UI and backend pipeline within 3D Slicer to handle file inputs and run the model's prediction pipeline.
Also, we'll verify the accuracy of the outputs within the Slicer environment and explore intuitive ways to display the predicted movements to the user.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1728" height="695" alt="Screenshot 2026-06-25 at 10 29 58 AM" src="https://github.com/user-attachments/assets/40e31807-6507-4743-b3e6-e130736a4ab1" />




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Github link: https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools
This work was supported by the National Institute of Dental and Craniofacial Research (NIDCR) of the National Institutes of Health under Award Number R01DE024450.

