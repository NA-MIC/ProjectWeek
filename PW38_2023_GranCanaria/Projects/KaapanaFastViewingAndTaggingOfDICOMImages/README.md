Back to [Projects List](../../README.md#ProjectsList)

# Fast viewing and tagging of DICOM Images

Kaapana tutorial for the 38th NA-MIC project week: 
https://drive.google.com/file/d/1A7-8Ru0uTJHFFa17rZtkBpvNhJao_F7x/view?usp=share_link

## Key Investigators

- Stefan Denner (German Cancer Research Center, Germany)
- Klaus Kades (German Cancer Research Center, Germany)
- Andrey Fedorov (Brigham and Women's Hospital, USA)

# Project Description

Creating a cohort or tagging DICOM images can be very time-consuming.
In this project, we are working on solutions to facilitate the process.

![](NA-MIC.gif)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Improving the Gallery view (see video above) in Kaapana in cooperation with other participants
2. Interacting native DICOM image support into the annotation tool [Doccano](https://github.com/doccano/doccano)
3. Discussion: DICOM Dashboard Setup (somewhat) related to this: in IDC we have been using Google DataStudio / Looker, and Apache Superset (to a lesser degree) - can discuss

Relate to:
- [Kaapana overall](https://github.com/NA-MIC/ProjectWeek/tree/master/PW38_2023_GranCanaria/Projects/Kaapana_overall)

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

The Gallery View is part of the kaapana open source toolkit and is based on open source tools such as 
OpenSearch, dcm4chee, dcmjs and Cornerstone.js.
So far, the Gallery View is a proof of concept for fast viewing and tagging of DICOM Images.

**We are actively looking for new use cases, in which the functionality of the Gallery View can be either applied or extended.**


Some use-cases we have in mind:
- Proper visualization of thumbnails for segmentation data
- More efficient/faster loading of DICOM Series in the detail view (on the right)
- Adding metadata to the DICOM Image viewer (similar to OHIF Viewer)
- Download of tags as CSV files

If you have any ideas in mind, please feel free to contact us (-> stefan.denner@dkfz-heidelberg.de).

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. tbd

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

tbd

# Background and References

tbd
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
