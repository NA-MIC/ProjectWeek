---
layout: pw42-project

permalink: /:path/

project_title: DICOM WSI Interoperability with Kaapana
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



1. Setup of public Kaapana server in preparation of the DICOM conectathon at: 172.16.17.47
2. Some progress in containerizing QuPath within Kaapana to serve as viewer from Objectstorage (NOT from PACS)
3. Evaluating [https://github.com/huangch/openremoteslide](https://github.com/huangch/openremoteslide) as additional extension for communication with external server
4. Testing some interoperability components for Zeiss WSI files. 




# Illustrations

<img width="1512" alt="Screenshot 2025-01-31 at 11 02 27" src="https://github.com/user-attachments/assets/43a43144-2570-46a9-87c4-2dc2489d084a" />



_No response_



# Background and References

* Conversion routines for SR, ANN and fractional SEG developed by Chris Bridge / IDC: [https://github.com/ImagingDataCommons/idc-sm-annotations-conversion/tree/main](https://github.com/ImagingDataCommons/idc-sm-annotations-conversion/tree/main) for the dataset available in [https://zenodo.org/records/14041167](https://zenodo.org/records/14041167)
* Tutorials created by Daniela in IDC for ANN and SR: [https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/pathomics](https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/pathomics) (ANN) and [https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/collections_demos/rms_mutation_prediction](https://github.com/ImagingDataCommons/IDC-Tutorials/tree/master/notebooks/collections_demos/rms_mutation_prediction) (SR)
* Support of external PACS (eg, Googe Healthcare DICOM stores) in Kaapana: [https://codebase.helmholtz.cloud/kaapana/kaapana/-/merge_requests/415](https://codebase.helmholtz.cloud/kaapana/kaapana/-/merge_requests/415), [https://codebase.helmholtz.cloud/kaapana/kaapana/-/issues/1191](https://codebase.helmholtz.cloud/kaapana/kaapana/-/issues/1191)
<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

