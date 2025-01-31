---
layout: pw42-project

permalink: /:path/

project_title: Determination of surgical class based on the curvature and shape of the carotid syphon
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Attila Tanács
  affiliation: University of Szeged
  country: Hungary

- name: Ferenc Dezső Bakó
  affiliation: University of Szeged
  country: Hungary

- name: Attila Nagy
  affiliation: University of Szeged
  country: Hungary

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Stroke is a leading cause of death worldwide of which ischaemic stroke is the more common. Mechanical thrombectomy involves inserting a catheter into the cerebral vasculature to remove blood clot. Catheter devices with different parameters are available to perform the procedure of which the correct one must be selected beforehand to avoid blockage. Clinical experience suggests that large lumen aspiration catheters were most commonly stuck at the anterior curvature of the carotid syphon.

In literature Waihrich et al. proposed to use 2D X-Ray to measure angles of vessel segments for classification. In our prevcious work we extended this approach to 3D measuring the minimal angle along the centerline of the carotid syphon. Based on 49 studies classified manually into 5 surgical classes by a medical expert, it turned out that this angle alone is not a good indicator of surgery class.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Determine the vessel cross section area/diamater at given vessel centerline points.
2. Objective B. Figure out what other numerical parameters could be extracted for classification.
3. Obecjtive C. What methods could be used for classification taking into account the low number of studies.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. We'd like to extend our Slicer extension module to produce the numbers for classification.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


- Generating vessel cross-section tables for all studies using VMTK.
- Sampling vessel cross-section values at 9 given centerline points
around the middle point.
- 9 centerline points determine 8 line sections that determine 7 angles.
- Table is generated for all 49 studies containing 9 + 8 features.
- Next step is to use this values for classification (possibly using SVM
and fully connected shallow neural network).




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Vessel parts of the carotid syphon. 

<img width="809" alt="Image" src="https://github.com/user-attachments/assets/3931d350-55c3-4286-a6af-d0bc249e2e96" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

