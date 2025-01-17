---
layout: pw42-project

permalink: /:path/

project_title: Kidney and tumor segmentation for surgery planning
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Sylvia Ladstatter
  affiliation: Children's National
  country: USA

- name: Kevin Cleary
  affiliation: Children's National
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Our [overall project](https://arpa-h.gov/research-and-funding/mission-office-iso/awardees#:~:text=SARRTS%3A%20Supervised%20Autonomous%20Robotic%20Renal%20Tumor%20Surgery) aims to help automate kidney surgery and requires a fast and accurate way to make detailed segmentations of renal structures.  Currently we can do this in 3D Slicer in a few hours using existing segmentation techniques.

We would like to test improved methods for this task, and also define a good terminology for it.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Have a supervised segmentation method that works well with standard pre-op clinical images (typically diagnostic CTs with contrast enhancement at 1mm or smaller pixel size).
2. The method should segment the following structures:
  * Aorta
  * Vena cava
  * Renal cortex
  * Renal artery (including accessories, inside and outside the kidneys)
  * Renal vein
  * Renal pyramids / medulla
  * Renal pelvis
  * Ureters
  * Tumors / masses
 3. Define a [good terminology](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/InfrastructureForCustomTerminologyAndColorTablesInSlicer/) and map it to SNOMED terms.
 4. The method should work well on a wide range of clinically realistic cases, such as noisy images and anatomical variants.
 5. Ideally a method should also work on non-contrast CT and MR as well



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Use test data from IDC ([KiTS data](https://kits-challenge.org/kits23/)) as a testbed.  See if there are other datasets we could use for testing.
2. Meet with experts to discuss state-of-the-art approaches and find out about any existing kidney segmentation models we can try
3. Experiment with [ScribblePrompt, MultiverSeg](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/DeployingScribblepromptAndMultiversegForInteractiveSegmentationAsA3DSlicerExtension/), and [Radiology Copilot](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/3Dand2DRadiologyCopilotIntegrationin3DSlicer/) for this task
4. Get input from the IDC team and others on terminologies for this task



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://github.com/user-attachments/assets/e64fc125-1cc5-4cd8-8e92-b27d5f070a3a)

![Image](https://github.com/user-attachments/assets/cb5f60f5-60ab-46c7-8e77-a3072e135934)

![Image](https://github.com/user-attachments/assets/28bad2d7-3476-4247-a899-563c18561099)



# Background and References

Example KiTS case from IDC:
[https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.6919.4624.135173370342136417423953641748](https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.6919.4624.135173370342136417423953641748)


