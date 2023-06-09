---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/TutorialsOnWorkingWithDicomAnnotationsInPathologyWholeSlideImages/README.html

project_title: Tutorials on working with DICOM annotations in pathology whole-slide images
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: Chris Bridge
  affiliation: MGH
  country: USA

- name: David Clunie
  affiliation: PixelMed
  country: USA

- name: Curtis Lisle
  affiliation: KnowledgeVis
  country: USA

- name: Maximillian Fischer
  affiliation: DKFZ
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to create tutorials on how to work with DICOM annotations in pathology whole-slide images (WSIs).
At first, we will focus on nuclei annotations stored as DICOM Microscopy Bulk Simple Annotations and compute nuclei density (cellularity) on tile-level from them. The computed cellularity values are then stored as DICOM parametric maps.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A: Have a Colaboratory notebook ready that at least reads DICOM Microscopy Bulk Simple Annotation files (currently from a Google Storage bucket, ideally later from the IDC directly) and computes cellularity values.
2.  Objective B: Encode computed cellularity values as DICOM parametric map that can be stored back to the IDC.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Testing and documentation of the current capabilities
    * Establish a repository of test samples that will contain standard-compliant examples of bulk annotations (different number of points, 2D vs 3DSCOORD), segmentations (binary and fractional) and parametric maps (floating point and integer).
    * Share code samples that were used to generate the examples above
    * Test different combinations of Slim viewer, DICOMweb backend (Google, dcm4chee, orthanc) and test samples to understand what is supported by various components (i.e., perhaps only 3DSCOORD is supported by Slim, there may be limits on maximum size of SQ in Google Healthcare)
2.  Investigate nuclei annotations for plausibility
3.  Read nuclei annotations
4.  Efficiently compute cellularity values
5.  Encode cellularity values as DICOM parametric maps

## Progress and Next Steps

1.  Have prepared re-use of existing Google Cloud platform (GCP) project with the ID: idc-external-031
2.  Have given key investigators access to the GCP project
    * If anyone else is interested in being added, please send me an e-mail to daniela.schacherer@mevis.fraunhofer.de.
3. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![Overview DICOM annotations: Segmentation IOD, Microscopy Bulk Simple Annotations IOD. Taken from https://doi.org/10.1038/s41467-023-37224-2.](./overview_annotations.png)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

* link to test objects storage bucket
* Github page [Slim viewer](https://github.com/ImagingDataCommons/slim)
* [Slim deployment tutorial](https://docs.google.com/document/d/1857jb_wKHqyGOd49UirujDDrFE8fUPfimZPXJ19zSF4/edit?usp=sharing) - seek feedback from Max and Curt
* TODO: link to the repo with conversion from Chris B
* Some example [Parametric DICOM Maps](https://www.dropbox.com/scl/fo/yrbm7v2iyx6fh9jgsae1w/h?dl=0&rlkey=hxiagbbp486o3nj480skx0yw7) and the [conversion code as Docker container](https://github.com/maxfscher/DICOMwsiWorkflow/tree/main) from Max Fischer.
* 
