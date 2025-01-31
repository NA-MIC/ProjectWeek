---
layout: pw41-project

permalink: /:path/

project_title: New Radiology and Pathology Deep Learning Models into MHub.ai
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Curtis Lisle
  affiliation: KnowledgeVis
  country: USA

- name: Leonard Nürnberg
  affiliation: Brigham and Women's Hospital
  country: Boston

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The MHub.ai project at Harvard has developed methods to execute machine learning models on medical images in an easy to use and standardized way.  There is already a Slicer plugin for running MHub.ai format models.  For this project, we propose to add two models of different types to the MHub library.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A.  Test a MONAI-based deep learning model in MHub and validate the instructions for new developers to follow.

2. Objective B. Evaluate how well the MHub approach works for supporting pathology models in addition to radiology models.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Step 1. Port one of the pre-trained MONAIAutoSeg3D radiology models developed at Queens (by Andros Lasso et al.) for execution using the MHub framework as a docker container.  Test the MHub I/O converters to read a  DICOM image and reformat as needed from the input.   Write out a DICOM segmentation object as the result.

Step 2. Start converting a published pathology DNN model (Rhabdomyosarcoma segmentation) for the MHub framework.  This will Evaluate how well the MHub approach works for supporting pathology models in addition to radiology models.  For example, can the same base Docker image work for pathology?



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We selected two of the MONAIAutoSeg3D models from the Slicer Extension and wrapped them using the MHub.ai framework as an exercise to learn the MHub approach.  As part of this process, we wrote a converter to produce the class descriptions used by MHub to describe model outputs from the original model descriptions. This approach could be used to convert other models later.

2. We started adapting a trained Rhabdomyosarcoma pathology model for MHub. the first part of the MHub pipeline works in our prototype but we arent processing the model ooutputs correctly yet.

3. We completed a prototype implementation of the RMS model inside MHub.ai.  This demonstrated that the MHub approach can be used for pathology as well as radiology models.  Some cleanup is needed yet, but this was a lot of progress this week.


# Illustrations

Below is a Slicer screenshot showing a segmentation created by an MHUb.ai model.  For this example, we took the low-res MONAIAutoSeg3D thoractic segmentation model from Andras' Slicer Extension and ported it to execute inside an MHub.ai workflow.  Others of the pre-trained AutoSeg models could also be ported with minimal effort. This model uses the SegResNet DNN from the MONAI project:


<img width="953" alt="MONAIAutoSeg-in-MHub-result-thoracic" src="https://github.com/NA-MIC/ProjectWeek/assets/2152950/8de4f75b-a46e-4e4e-9e38-d80a4816b2e3">

Here is a rendering of a Fractional DICOM segmentation superimposed over the source image.  The segmentation was created by a trained model executing inside the MHub.ai environment.  This model was ported during the project week.

![fractional_mhub_1](https://github.com/NA-MIC/ProjectWeek/assets/2152950/acd54257-d668-4026-b113-2c89f7f5b1b4)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


MONAI AutoSeg3D: [https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg](https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg)

Slicer Extension: [https://github.com/lassoan/SlicerMONAIAuto3DSeg](https://github.com/lassoan/SlicerMONAIAuto3DSeg)

pathology model: [https://github.com/knowledgevis/rms-infer-code-standalone](https://github.com/knowledgevis/rms-infer-code-standalone)
