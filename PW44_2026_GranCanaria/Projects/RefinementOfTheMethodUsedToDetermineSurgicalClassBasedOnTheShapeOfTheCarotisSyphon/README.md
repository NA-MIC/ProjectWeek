---
layout: pw44-project

permalink: /:path/

project_title: Refinement of the method used to determine surgical class based on the shape of the
  carotis syphon
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Attila Tanács
  affiliation: University of Szeged
  country: Hungary

- name: Attila Nagy
  affiliation: University of Szeged
  country: Hungary

- name: Ferenc Dezső Bakó
  affiliation: University of Szeged
  country: Hungary

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This is an [ongoing project from last year](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/DeterminationOfSurgicalClassBasedOnTheCurvatureAndShapeOfTheCarotidSyphon/).

Stroke is a leading cause of death worldwide of which ischaemic stroke is the more common. Mechanical thrombectomy involves inserting a catheter into the cerebral vasculature to remove blood clot. Catheter devices with different parameters are available to perform the procedure of which the correct one must be selected beforehand to avoid blockage. Clinical experience suggests that large lumen aspiration catheters were most commonly stuck at the anterior curvature of the carotid syphon.

We categorised 53 studies into four groups. Previously, we extracted nine features based on vessel geometry for classification purposes.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Our main objective is to refine the extracted attribute values in order to enhance the classification results.
2. Objective B. Vessel segmentation is also part of the process that is performed manually currently. We are trying to make it automatic.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Using Weka, figure out what features and classification method provide the best result.
2. We plan to gather CT and ground truth data for MONAI Auto3dSeg segmentation training.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Absolute distance values were normalized by computing the ratio of distance relative to the distance along the centreline of the vessel.
2. Starting from the first cross section, difference values were computed from absolute vessel cross section area values.
3. Attributes were inspected using Weka functions.

Results: Even the new attributes are not really a good descriptor of best choice available as ground truth.

Next steps: Ground truth should be considered in a different way. Instead of opting for one single choice, a percentage value could be assigned to each intrumentation. From the recorded surgical log data, we know which devices were tested and which were unsuccessful. These unsuccessful instrument applications could also be used to train the classification method.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="749" height="792" alt="Image" src="https://github.com/user-attachments/assets/02e5d8ea-f072-4fb6-81f0-b8f5f7336ed7" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

