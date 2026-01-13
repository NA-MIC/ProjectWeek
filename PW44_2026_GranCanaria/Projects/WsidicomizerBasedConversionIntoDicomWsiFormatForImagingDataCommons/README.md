---
layout: pw44-project

permalink: /:path/

project_title: wsidicomizer-based conversion into DICOM WSI format for Imaging Data Commons
category: DICOM
presenter_location: 

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: David Clunie
  affiliation: PixelMed Publishing
  country: USA

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project is motivated by the operational needs of the [Imaging Data Commons](https://learn.canceridc.dev/) to have a sustainable mechanisms supported by open-source software for harmonizing various slide microscopy images in vendor-specific representations into DICOM Whole Slide Imaging format. Our current procedures is not sustainable, since they rely on the PixelMed tools by David Clunie, which are based on a coding style and build process that has not changed since initiated over 20 years ago, unfortunately have "bus factor" of 1, and are not open for community contributions. We started using [`wsidicomizer`](https://github.com/imi-bigpicture/wsidicomizer) as a replacement, but there are gaps in the functionality to be remedied, and additional testing that needs to be done before we can consider operational switch.

This project is the continuation of the [earlier project at PW42 2025](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/EvaluationOfImiBigpictureWsidicomizerAsAToolForConversionIntoDicomWholeSlideImagingFormat/). 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement routing of the DICOM metadata.
2. Evaluate extensibility of the conversion approach to various input types.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Improve the conversion script developed for the HMS SARDANA sample to handle metadata.
2. Evaluate conversion of the .czi samples.
3. Evaluate metadata routing in the Mirax conversion script



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

