---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/MpreviewDevelopmentOfAStreamlinedSlicerModuleForManualImageAnnotation/README.html

project_title: mpReview Development of a streamlined Slicer module for manual image annotation
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: BWH

- name: Nadya Shusharina
  affiliation: MGH

- name: Andrey Fedorov
  affiliation: BWH

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The 3DSlicer module mpReview (part of the SlicerProstate extension) was previously developed to assist with manual annotation of the prostate and other related anatomical regions. In previous project weeks, we have streamlined the extension [here](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/mpReview/) and updated the module to use the latest SegmentEditor, and incorporated the use of Google Cloud Platform [here](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/mpReview/).

However, there are improvements that can be made in terms of functionality. For instance, we would like to allow the user to access multiple types of servers, and perform annotation of body parts other than the prostate.

In this project week we'll focus on using a JSON file as input, which will allow users to customize the module to their annotation needs. Our goal will be to streamline the user's interaction with the module, allowing them to annotate large datasets efficiently and quickly using both the cloud (e.g. GCP and Kaapana) or a local DICOM database.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Discuss the current [multiple_server](https://github.com/deepakri201/mpReview/tree/multiple_server) branch of the module.

2.  Brainstorm the JSON format specification necessary for streamlining the annotation workflow. Generate examples of JSON files for different use cases: local Slicer DICOM database, Google Cloud Platform, Kaapana, etc.

3.  Define the steps that are needed to accomplish the changes.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  We will discuss the state of the current branch, and identify the needs of users.
2.  After talking to researchers and clinicians and their annotation needs/concerns, we will develop JSON format specifications for a variety of use cases.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  We have started discussing the  shortcomings of the current module.
2.  We have started to draft possible JSON file specifications.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Current screenshot of the module

![image](https://user-images.githubusercontent.com/59979551/173397664-c3a7f567-d5f2-4214-a366-7cef1344860c.png)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

We have worked on this during multiple project weeks, [PW35](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/mpReview/) and [PW37](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/mpReview/). The code from PW37 is available [here](https://github.com/deepakri201/mpReview/tree/multiple_server).
