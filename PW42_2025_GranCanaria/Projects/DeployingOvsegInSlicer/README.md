---
layout: pw42-project

permalink: /:path/

project_title: Deploying OvSeg in Slicer
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Thomas Buddenkotte
  affiliation: University Medical Center HamburgEppendorf
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


[OvSeg](https://github.com/ThomasBudd/ovseg/) is a deep learning-based library for the segmentation of high-grade serous ovarian cancer on CT images. Right now, to obtain the segmentations the user has to write some lines of Python code, making the tool not directly usable by non-technical people. It would be great to expose this algorithm in Slicer to be used in a codeless manner.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Expose OvSeg in 3D Slicer in order to provide a scalar volume as input and obtain the segmentations as a segmentation node




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a Slicer extension
2. Let the extension to install OvSeg via pip
3. Let the extension pull the CT volume, run the inference, and push back the segmentations




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Ovseg can be successfully used in Slicer
2. The code can be downloaded from [this GitHub repository](https://github.com/pzaffino/SlicerOvseg)

3. We would like to include this extension in the Slicer Extension repository
4. We need a logo
5. We could decide to expose the extended ovseg version which provides more segmentations classes




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://raw.githubusercontent.com/NA-MIC/ProjectWeek/refs/heads/master/PW42_2025_GranCanaria/Projects/DeployingOvsegInSlicer/SlicerOvseg_screenshot.png)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. [https://github.com/ThomasBudd/ovseg/](https://github.com/ThomasBudd/ovseg/)
2. [https://www.repository.cam.ac.uk/items/d7d9011c-2518-4a7a-8b85-01b086d672fc](https://www.repository.cam.ac.uk/items/d7d9011c-2518-4a7a-8b85-01b086d672fc)
3. [https://eurradiolexp.springeropen.com/articles/10.1186/s41747-023-00388-z](https://eurradiolexp.springeropen.com/articles/10.1186/s41747-023-00388-z)
