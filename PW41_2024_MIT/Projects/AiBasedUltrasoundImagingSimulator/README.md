---
layout: pw41-project

permalink: /:path/

project_title: AI-based ultrasound imaging simulator
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Junichi Tokuda
  affiliation: BWH

- name: Xihan Ma
  affiliation: WPI

- name: Simon Leonard
  affiliation: JHU

- name: Laura Connolly
  affiliation: Queen's

- name: Haichong
  affiliation: Kai) Zhang (WPI

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We will discuss strategies to integrate AI-based ultrasound imaging simulators in multiple platforms for medical robotics and IGT, including the Gazebo dynamic simulator and PLUS.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. **Model** Improve the model - make the simulated ultrasound image more realistic
2. **Architecture** Explore the fast way to package the model into applications.


## Approach and Plan

1. Model improvement
   - The current model doesn't take account of tissue attenuation properties. Explore the use of CT segmentation data (or total segmentator).
   - To use the neuron network to accelerate the computation speed. (The current version is physics-based)
2. Architecture
   - Create an independent library for CT-ultrasound conversion. This library takes a 2D resampled CT data that is aligned to the (virtual) ultrasound probe, and generate a corresponding simulated ultrasound image.
   - Integration with existing platforms, including Gazebo, Slicer, PLUS (to be discussed with the community)
   - 



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


_No response_

