---
layout: pw40-project

permalink: /:path/

project_title: Current state of DICOMweb for pathology
category: DICOM
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

- name: André Homeyer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

DICOMweb™ defines a set of RESTful services for web-based medical imaging with DICOM. This project aims at getting a detailed understanding of the capabilities of available (Python) libraries and tools that implement DICOMweb and how they facilitate working with pathology whole-slide images (WSI) via DICOMweb services. The summarized knowledge will be the basis for discussions and help to decide what further work makes sense (e.g. new library, contributing specific functionality to an existing library etc.).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A: Have a document (document A) describing capabilities of available tools.
2.  Objective B: Have a document (document B) summarizing discussions and plans for further work.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Get practical experience with the libraries: wsidicom, dicomslide (both underlyingly using dicomweb_client).
2.  Set-up document A
3.  Set-up times to discuss during project week
4.  Summarize discussion in document B

## Progress and Next Steps

1.  Prepared small Jupyter notebook [here](https://colab.research.google.com/drive/1WxOVtLOGwt7xSOy7SghbOWxcDzG_XAD4?usp=sharing) on how to get started with wsidicom vs. dicomslide to access data via DICOMweb
2.  Summarized capabilities of both libraries beyond DICOMweb in a Google Doc [here](https://docs.google.com/document/d/1qWjzwneL4em7fQYdCfaP6RG6AtmAz23o5ZARfCo1Evs/edit?usp=sharing).

Both will be updated/extended after the project week as relevant work and discussions goes on.

# Illustrations

![Conceptual overview of DICOMweb](./dicomweb.png) \
*Conceptual overview of DICOMweb. Taken from: https://www.dicomstandard.org/using/dicomweb/capabilities.*

# Background and References

- Repository [dicomslide](https://github.com/ImagingDataCommons/dicomslide)
- Repository [wsidicom](https://github.com/imi-bigpicture/wsidicom)
- Repository [dicomweb-client](https://github.com/ImagingDataCommons/dicomweb-client)
