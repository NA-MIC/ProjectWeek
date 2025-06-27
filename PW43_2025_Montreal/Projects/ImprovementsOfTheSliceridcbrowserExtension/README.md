---
layout: pw43-project

permalink: /:path/

project_title: Improvements of the SlicerIDCBrowser extension
category: Infrastructure

key_investigators:

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[SlicerIDCBrowser](https://github.com/ImagingDataCommons/SlicerIDCBrowser) is a 3D Slicer extension for exploring and downloading over 85TB of freely available image data from [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/explore). This project is about updating and improving this extension to make it more usable and easier to maintain.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Plan refactoring of the extension
2. Improve features: add download progress reporting, simplify download by automatically detecting whether identifier specified by the user is collection/patient/study/series, support automatic loading of the images.
3. A discussion with Ben Zwick resurrected earlier ideas about embedding [IDC portal explore page](https://portal.imaging.datacommons.cancer.gov/explore/) in Slicer directly, and injecting functionality to trigger Slicer open directly from that embedded page. Will prioritize development of that feature, see https://github.com/ImagingDataCommons/SlicerIDCBrowser/issues/52.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Discuss with Kyle overall organization of the extension, estimate effort.
2. Meet with the users to collect feedback.
3. Prioritize development and start working on implementation.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Andrey and Kyle discussed plans for improving the extension and defined priorities for the immediate development in [https://github.com/ImagingDataCommons/SlicerIDCBrowser/milestone/1](https://github.com/ImagingDataCommons/SlicerIDCBrowser/milestone/1).
3. Kyle contributed improvements to reduce delays to the startup of the extension in [https://github.com/ImagingDataCommons/SlicerIDCBrowser/pull/51](https://github.com/ImagingDataCommons/SlicerIDCBrowser/pull/51).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<video
   controls muted
   src="https://github.com/user-attachments/assets/522087f9-99e5-4c0b-80c9-f5ab940aa19c"
   style="max-height:640px; min-height: 200px">
 </video>



(video from [https://www.youtube.com/watch?v=m_jfSTWIYvc](https://www.youtube.com/watch?v=m_jfSTWIYvc))

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://portal.imaging.datacommons.cancer.gov/](https://portal.imaging.datacommons.cancer.gov/)

