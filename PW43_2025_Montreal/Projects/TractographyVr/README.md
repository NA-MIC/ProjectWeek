---
layout: pw43-project

permalink: /:path/

project_title: Tractography-VR
category: VR/AR and Rendering

key_investigators:

- name: Tina Nantenaina
  affiliation: ETS
  country: Canada

- name: Sylvain Bouix
  affiliation: ETS
  country: Canada

- name: Simon Drouin
  affiliation: ETS
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to work on VR interaction with tractograms in 3D Slicer. The goal is to develop tools that allow users to clean and annotate fiber bundles more accurately and efficiently in an immersive environment. This could support tasks such as cluster selection, labeling, or removal of outlier fibers during tractography analysis.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Improve VR interaction with tractography data
2. Objective B. Improve VR interaction with the ROI box




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Identify the source of the positional mismatch between the controller and the selected object
2. Fix VR laser-object interaction offset : Ensure the object follows the controller movement precisely without lag or offset




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Users can now select and resize the ROI box in VR using the controller, which enables manual cleaning of fibers by adjusting the region of interest.
1. Different bugs where identified
  1. It was determined that the ROI is only moved relative to the controller translation, which explain why the box is not following the laser. This could be fixed by taking into account the rotation of the controller
  2. Usability issues and rendering artifacts come from a very low framerate that results from an incompatibility between the new Markup system in Slicer and SlicerVirtualReality
1. The short-term solution to the bug is to use a simple polygonal model as a ROI for fiber clipping instead of a ROI markup.
2. A script that illustrates how this can be done in Python is available [here](https://gist.github.com/drouin-simon/e2b5ecf77d53697e2e20c1d8fd016ea3).

# Illustrations


 <video
   controls muted
   src="demo3red.mp4"
   style="max-height:640px; min-height: 200px">
 </video>





# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

