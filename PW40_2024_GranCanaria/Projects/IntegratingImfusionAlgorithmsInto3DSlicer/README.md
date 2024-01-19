---
layout: pw40-project

permalink: /:path/

project_title: Integrating ImFusion Algorithms into 3D Slicer
category: Other
presenter_location: In-person

key_investigators:

- name: Federico Gnesotto
  affiliation: ImFusion GmbH
  country: Germany

- name: Martin Matilla
  affiliation: ImFusion GmbH
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The ImFusionSDK (a collection of libraries) contains various algorithms that are applied on medical data such as MR, CT and Ultrasound. The algorithms range from calibration to image-registration, segmentation etc.

Our proposal is to create an extension in 3D-Slicer that exposes ImFusion algorithms to the data loaded in the 3D Slicer software. As a starting point, we will employ the existing [ImFusion extension for 3D-Slicer](https://github.com/ImFusionGmbH/public-demos/tree/release/SlicerExtension) which performs CPU and GPU-accelerated registration between single and multi modal images.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The project plan can be broken down into the following concrete objectives:

Plugin Infrastructure: Creation of Module/Plugin infrastructure for 3D Slicer ()

Data Interface: Handling and conversion of DataSets ( <-> )

Algorithm Interface: accessing ImFusion’s list of compatible algorithms

Algorithm Controller Integration: Integration of GUI and Logic for configuring algorithms () into 3D Slicer (, )

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

None

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![RegistrationModule powered by ImFusion Libraries in 3D Slicer](https://github.com/NA-MIC/ProjectWeek/assets/79929002/46c7efcb-990f-4e1e-b403-0a08c025e109)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

ImFusion's RegistrationModule for Slicer <https://github.com/ImFusionGmbH/public-demos/tree/release/SlicerExtension>
