Back to [Projects List](../../README.md#ProjectsList)

# DICOMweb Projects

## Key Investigators

- Michael Kelm (Siemens Healthineers)
- Steve Pieper (Isomics/NAMIC/OHIF)
- Erik Ziegler (OHIF)
- Marco Nolden (DKFZ/MITK)
- Jonas Scherer (DKFZ/MITK)
- Tina Kapur (BWH)

## Participating Remotely
- Andrey Fedorov (BWH)

# Project Description

## Objective

* Explore DICOMweb integration with various infrastructures and programming environments
  * OHIF
  * teamplay
  * CTK / MITK / Slicer
* Review existing implementations
  * dcm4chee
  * orthanc
  * teamplay
* Review enabling software / tools
  * dcmjs
  * cornerstone, cornerstoneTools

## Approach and Plan

* Review current implementations
* Review clinical applications and supportable workflows
  * General annotation (segmentation and measurements)
  * Orthopedic workflows
* Try some experimental connections with real data
  * QIDO/WADO of instances
  * STOW of derived instances
* Work on creating correct derived objects
  * SEG
  * SR
  * PR
  * SC


Here's an example endpoint for testing:

```curl quantome.org:8080/dcm4chee-arc/aets/DCM4CHEE/rs/patients```


## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations
<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [DICOMweb offical site](https://www.dicomstandard.org/dicomweb/)
- [OHIF](ohif.org)
- [CTK](commontk.org)
- [Example docker compose for OHIF + dcm4chee](https://github.com/OHIF/integration-examples/tree/master/ohif-dcm4chee-nginx)
- [dcm4chee REST api endpoints](http://petstore.swagger.io/index.html?url=https://raw.githubusercontent.com/dcm4che/dcm4chee-arc-light/master/dcm4chee-arc-ui2/src/swagger/swagger-dicom.json)
- [Example OHIF installation with dcm4chee back end](http://ohifviewer-staging.herokuapp.com/studylist)
