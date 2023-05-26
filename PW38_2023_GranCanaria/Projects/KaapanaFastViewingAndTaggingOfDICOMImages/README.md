Back to [Projects List](../../README.md#ProjectsList)

# Fast viewing and tagging of DICOM Images

Kaapana tutorial for the 38th NA-MIC project week: 
https://drive.google.com/file/d/1A7-8Ru0uTJHFFa17rZtkBpvNhJao_F7x/view?usp=share_link

## Key Investigators

- Stefan Denner (German Cancer Research Center, Germany)
- Klaus Kades (German Cancer Research Center, Germany)
- Andrey Fedorov (Brigham and Women's Hospital, USA)
- Davide Punzo (Freelancer, France)
- Alireza Sedghi (Radical Imaging)

# Project Description

Creating a cohort or tagging DICOM images is a very time-consuming and error-prone procedure.
In this project, we are extending the functionality of the so-called Gallery View within Kaapana. 

![](https://github.com/NA-MIC/ProjectWeek/releases/download/project-week-resources/PW38__KaapanaFastViewingAndTaggingOfDICOMImages__NA-MIC.gif)

## Approach and Plan

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

- Upgraded Cornerstone to Cornerstone3D with the great help of Alireza and Davide
- Proof of Concept for creating segmentation thumbnails in the Gallery View
- Proof of Concept for multi select of items
- Proof of concept virtual scrolling to improve performance

TODO: 
- Cleanup and integrate into kaapana code base
- Add segmentation support to Cornerstone3D viewer
- Store segmentation thumbnails to S3 bucket to load them from there. 

# Illustrations

tbd

# Background and References

https://github.com/kaapana/kaapana
