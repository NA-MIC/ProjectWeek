---
layout: pw40-project

permalink: /:path/

project_title: 'ALI: Automated Landmark Identification update'
category: Segmentation / Classification / Landmarking
presenter_location: Online

key_investigators:

- name: Jeanne Claret
  affiliation: University of Michigan
  country: USA

- name: Gaëlle Leroux
  affiliation: University of Michigan
  country: USA

- name: Lucia Cevidanes
  affiliation: UoM
  country: USA

- name: Juan Prieto
  affiliation: ' University of North Carolina'
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This is an update to a Slicer module developed during project week #37. The approach  reformulates anatomical landmark detection as a classification problem through a virtual agent placed inside a 3D Cone-Beam Computed Tomography (CBCT) scan. This agent is trained to navigate in a multi-scale volumetric space to reach the estimated landmark position. The agent movements decision relies on a combination of Densely Connected Convolutional Networks (DCCN) and fully connected layers. Automated Landmark Identification (ALI) is a tool available in the extension SlicerAutomatedDentalTool. This module aims to automatically identify landmarks on different type of scans (CBCT, IOS). The current CBCT models trained include the Cranial Base, Upper and Lower Bones of the face, and the teeth (Left, Right, Upper, and Lower).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Retrain the different landmarks models with new  and larger datasets annotated by clinicians, with particular focus on teeth on atypical or impacted position inside the bone.
2.  Hyperparameters fine tuning for maintenance  and improved accuracy on the previously available code.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Collected and preprocessed data
2.  Model Architecture: Review and improve the existing model architecture, which utilizes Densely Connected Convolutional Networks (DCCN) and fully connected layers.
3.  Hyperparameter Fine-Tuning: Conduct hyperparameter optimization to fine-tune the model for improved accuracy. This includes adjusting learning rates, batch sizes, and regularization techniques.
4.  Training and Validation
    Dataset Split: Divide the dataset into training, validation, and test sets to ensure proper model evaluation.
    Model Training: Train the models for automated landmark identification using the restructured dataset. Employ techniques such as data augmentation to improve generalization.
    Validation Metrics: Use appropriate evaluation metrics such as maximum, mean and standard deviation fo errors compared with gold standard annotations.
5.  Pull request of the updated models into the SlicerAutomatedDentalTool extension to enable improved automated landmark identification for CBCT scans.
6.  User Interface: Enhance the user interface to make it user-friendly and intuitive for clinicians.
7.  Testing and Quality Assurance: Thoroughly test the updated module to identify and resolve any bugs or issues. Ensure that the automated landmark identification module performs accurately and reliably on different types of scans.
8.  Documentation and Training: Create comprehensive documentation for users and developers, including instructions on how to use the module effectively.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Collected and preprocessed data
2.  Hyperparameter Fine-Tuning
3.  Training Dataset Split: Divide the dataset into training, validation, and test sets to ensure proper model evaluation.
4.  The evaluation metrics currently seems unreliable;  so I am seeking guidance on how to improve.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![SegTab](https://user-images.githubusercontent.com/46842010/180010603-37dce4c3-e7f8-4b3a-98a1-2874918320cb.png)

![Slicer screen](https://user-images.githubusercontent.com/46842010/174138265-66ab080e-e885-4f76-a150-7e4da3869aa0.png)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Link to the AutomatedDentalTool Github: <https://github.com/Jeanneclre/SlicerAutomatedDentalTools/tree/main>
