---
layout: pw42-project

permalink: /:path/

project_title: Review of segmentation results quality across various multi-organ segmentation models
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Ron Kikinis
  affiliation: BWH
  country: USA

- name: David Clunie
  affiliation: Pixelmed Publishing
  country: USA

- name: Steve Pieper
  affiliation: Isomics Inc
  country: USA

- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK

- name: Tamaz Amiranashvili
  affiliation: University of Zurich
  country: Switzerland

- name: Murong Xu
  affiliation: University of Zurich
  country: Switzerland

---

# Project Description

<!-- Add a short paragraph describing the project. -->


When initially released, TotalSegmentator was perceived to produce superior results, in comparison to the state-of-the-art at the time, anyway.

Over time, some of the deficiencies in the segmentations produced by TotalSegmentator have been identified. Further, new multi-organ segmentation models have been introduced.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Review segmentation results for a sample of images from IDC NLST collection, documenting the problems, across the publicly available multi-organ segmentation models. 





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


For any model to be evaluated, we need to have segmentation results available for the specific set of CT images from NLST. 

At this moment, we have those for
* TotalSegmentator v1
* MOOSE

We are hopeful to also get segmentations for those selected specific cases for the following (given the list of participants in PW):
* OMAS (@aTamaz will you help?)
* AutoSeg3D (@diazandr3s can you help?)

We plan to use the SegmentationVerification extension developed by @cpinter in the PW41 earlier for the review (see [https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SegmentationVerificationModuleForFinalizingMultiLabelAiSegmentations/](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SegmentationVerificationModuleForFinalizingMultiLabelAiSegmentations/)).

We plan to summarize the results of the review in a publicly available document.



## Progress and Next Steps

1. Instructions for downloading initial sample of images:

`pip install --upgrade idc-index`

```python
test_series = \
['1.2.840.113654.2.55.195946682403058845904768502826466194287', \
 '1.2.840.113654.2.55.221581533879834196356530174246594024639', \
 '1.2.840.113654.2.55.71263399928421039572326605504649736531', \
 '1.2.840.113654.2.55.79318439085250760439172236218713769408', \
 '1.2.840.113654.2.55.191661316001774647835097522264785668378', \
 '1.2.840.113654.2.55.304075689731327662774315497031574106725', \
 '1.2.840.113654.2.55.283399418711252976131557177419186072875', \
 '1.2.840.113654.2.55.21461438679308812574178613217680405233', \
 '1.2.840.113654.2.55.97114726565566537928831413367474015470', \
 '1.2.840.113654.2.55.122344168497038128022524906545138736420', \
 '1.2.840.113654.2.55.229650531101716203536241646069123704792', \
 '1.2.840.113654.2.55.257926562693607663865369179341285235858', \
 '1.3.6.1.4.1.14519.5.2.1.7009.9004.135383252566920035150987356231', \
 '1.3.6.1.4.1.14519.5.2.1.7009.9004.315696884435641630605419115484', \
 '1.3.6.1.4.1.14519.5.2.1.7009.9004.230644512623268816899910856967', \
 '1.3.6.1.4.1.14519.5.2.1.7009.9004.330739122093904668699523188451', \
 '1.3.6.1.4.1.14519.5.2.1.7009.9004.690272753571338193252806012518', \
 '1.3.6.1.4.1.14519.5.2.1.7009.9004.310718458447911706151879406927']

from idc_index import IDCClient 

c= IDCClient()

c.download_from_selection(downloadDir=".",seriesInstanceUID=test_series)
```





# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

