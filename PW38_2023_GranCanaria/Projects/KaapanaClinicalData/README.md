Back to [Projects List](../../README.md#ProjectsList)

# Integration of clinical data into medical imaging pipelines

## Key Investigators

- Philipp Schader (German Cancer Research Center, Germany)
- Andrey Fedorov (BWH)

# Project Description

Clinical data like age, blood type, diagnosis and other non-imaging biomarkers are highly relevant in medical image processing as they provide context for the analysis of imaging datasets. Incorporating this additional data layer into image processing tools facilitate the development of complex biomarkers. While platforms for medical image processing like Kaapana focus on the imaging layer they often lack for features to relate clinical data to it.

This projects aims to integrate clinical data better into the Kaapana medical image processing platform by using the FHIR standard. To facilitate this a FHIR server will be integrated in the platform and linked to the imaging data stored in the internal PACS. Additionally the workflow component will be extended to be able to store and retrieve FHIR objects from the internal server. This forms the basis to create import procedures allowing the import of clinical data from tabular data into the internal FHIR store. By extending the preexisting radiomics workflow of the platform to store its results in the FHIR server a first imaging biomarker is made available. In a last step a joint analysis using the Jupyter Lab service of the platform joining the clinical data with the imaging biomarkers from the radiomics analysis is performed.


## Objective

1. Integration of a data store for clinical data in the Kaapana Platform
2. Integration of clinical data retrieval and storage from processing pipelines (Try to store analysis results like radiomics reports in FHIR)
3. Establish import procedures for clinical data (e.g. for data formats available via TCIA or IDC - up for discussion)
4. Integration of the clinical data store into the analysis frameworks of the platform and example of a joint analysis

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Find a small collection of datasets including images, segmentations of pathologies and according clinical data
2. Decide on an open-source FHIR server (like HAPI FHIR) integrate it into Kaapana (and link it to the PACS if possible)
4. Creation of query / retrieve operators for FHIR objects within the workflow components
5. Create import workflow to import different clinical data fromats from the object store into the FHIR server and discuss which data formats to support (csv, Excel, RedCap, odm)
6. Represent the results of an workflow (maybe by extending the preixisitng radiomics workflow - feedback welcome) as FHIR objects and store them in the FHIR Server of the platform
7. Perform an example analysis using the workflow results and enriching them using other clinical data

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
- [Kaapana](https://github.com/kaapana/kaapana) the imaging platform to use
- [HAPI FHIR](https://hapifhir.io/) a potential open source FHIR server
- [CCE_DART](https://cce-dart.com/) a project using Kaapana to discover complex biomarkers
- Clinical data in IDC - start with [this tutorial](https://github.com/ImagingDataCommons/IDC-Examples/blob/master/notebooks/clinical_data_intro.ipynb)
