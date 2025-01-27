---
layout: pw42-project

permalink: /:path/

project_title: Evaluation of interoperability between DICOM WSI Infrastructure components within Kaapana
category: DICOM

key_investigators:

- name: Maximilian Fischer
  affiliation: German Cancer Research Center
  country: Heidelberg

- name: Marco Nolden
  affiliation: German Cancer Research Center
  country: Heidelberg

- name: Klaus Maier-Hein
  affiliation: German Cancer Research Center
  country: Heidelberg

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: David Clunie
  affiliation: Pixelmed Publishing
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Kaapana is an open-source research platform for radiological imaging, featuring a range of infrastructure components. While some of these components natively support DICOM WSI (Whole Slide Imaging), others do not, necessitating the integration of alternative solutions to enable the processing of DICOM WSI data within the platform. The currently integrated components were selected based on their ability to provide fundamental functionality for DICOM WSI data processing, with a focus on being open-source and ensuring high interoperability.

Since the initial integration, newer tools and technologies have been developed that may better meet Kaapana's requirements. The objective of this project is to reassess the existing components and evaluate whether additional or alternative components should be incorporated. This evaluation aims to enhance the overall processing capabilities for WSI data within Kaapana and further improve the interoperability of the system.

Some components, such as the integrated PACS (dcm4che), are predefined as they form the foundation of the entire platform. Other components, such as the SlimViewer, were integrated on top because it was one of the first viewers capable of connecting to a DICOMweb PACS system.

Goal of this project is to evaluate all exchangeable components to ensure optimal support of DICOM WSI and interoperability with other systems (e.g. for generated analysis results of WSI within the platform).



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Identification of available alternatives to visualize DICOM WSI files
2. Test integration possibilities in Kaapana
3. Document results 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Bind other viewing components like QuPath to the data storage in Kaapana
2. Run dl-based analysis of DICOM WSI data with different reading libraries (openslide vs. wsidicom)
3. Visualize exported results (e.g. heatmaps as StructuredReport) with external DICOM WSI viewers. 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

* Conversion routines for SR, ANN and fractional SEG developed by Chris Bridge / IDC: https://github.com/ImagingDataCommons/idc-sm-annotations-conversion/tree/main for the dataset available in https://zenodo.org/records/14041167
* Tutorials created by Daniela in IDC for ANN and SR: https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/pathomics (ANN) and https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/collections_demos/rms_mutation_prediction (SR)
* Support of external PACS (eg, Googe Healthcare DICOM stores) in Kaapana: https://codebase.helmholtz.cloud/kaapana/kaapana/-/merge_requests/415, https://codebase.helmholtz.cloud/kaapana/kaapana/-/issues/1191
<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

