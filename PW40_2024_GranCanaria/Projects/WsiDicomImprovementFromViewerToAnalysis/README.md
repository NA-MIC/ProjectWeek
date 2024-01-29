---
layout: pw40-project

permalink: /:path/

project_title: WSI-DICOM Improvement - From Viewer to Analysis
category: DICOM
presenter_location: In-person

key_investigators:

- name: Fabian Hörst
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Lukas Heine
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Moon Kim
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Fin H. Bahnsen
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

- name: Jens Kleesiek
  affiliation: Institute for Artificial Intelligence in Medicine (IKIM)
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Despite various existing solutions for the conversion of WSI data into DICOM, there is a distinct lack of conversion tools (vendor agnostic) that result in DICOM files. Current solutions fall short in generating DICOM files compatible with OpenSlide (4.0.0) and OHIF/SLIM-Viewer, including a PACS, impeding seamless integration and compromising overall performance.

Our objective is to 1. assess available conversion tools, 2. examine their seamless integration capabilities, and 3. enhance or develop our own solutions for WSI-DICOM conversion that integrates into PACS systems connected to web-based viewers (OHIF/SLIM), but also works locally with open-source Viewers such like QuPath (newest version 0.5.0). As automatic slide analysis with AI algorithms (mostly Python) is a cornerstone of computational pathology, OpenSlide integration is another necessary requirement.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

This project aims to test existing software solutions for vendor-agnostic WSI to DICOM conversion in digital pathology and deliver/develop an open-source, community-maintained software solution. The tool must adhere to established software design patterns, ensuring ease of contribution from the community.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Provide a testing suite for testing resulting DICOM files, consisting of PACS/Viewer/Analysis-Components
2.  Test existing WSI DICOM solutions and find shortcomings
3.  Develop/Improve WSI DICOM conversions
4.  Deliver key insights into shortcomings to push conversion forward

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

Next steps are to build the test suite in advance, prepare test data and begin to collect more tools

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![idea](https://github.com/NA-MIC/ProjectWeek/assets/67600643/ff39403e-8dc6-411e-9f78-31189f242ea0)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

### Current known solutions for the WSI-DICOM Conversion: 

**thanks to @dclunie**

1. bfconvert (BioFormats):
   Converting a file to different format — Bio-Formats 7.1.0 documentation. 
   Link: [https://bioformats.readthedocs.io/en/v7.1.0/users/comlinetools/conversion.html](https://bioformats.readthedocs.io/en/v7.1.0/users/comlinetools/conversion.html)
2. dicom_wsi
   Gu Q, Prodduturi N, Jiang J, Flotte TJ, Hart SN. Dicom_wsi: A Python Implementation for Converting Whole-Slide Images to Digital Imaging and Communications in Medicine Compliant Files. J Pathol Inform. 2021;12(1):21. doi:[10.4103/jpi.jpi_88_20](https://doi.org/10.4103/jpi.jpi_88_20)
  Link: [https://github.com/Steven-N-Hart/dicom_wsi](https://github.com/Steven-N-Hart/dicom_wsi)
3. GoogleCloudPlatform. WSI to DICOM Converter. 
  Google Cloud Platform; 2022. 
   Link: [https://github.com/GoogleCloudPlatform/wsi-to-dicom-converter](https://github.com/GoogleCloudPlatform/wsi-to-dicom-converter)
4. wsidicomizer. Sectra AB
   Sectra AB. wsidicomizer. imi-bigpicture; 2021. 
   Link: [https://github.com/imi-bigpicture/wsidicomizer](https://github.com/imi-bigpicture/wsidicomizer)
5. Jodogne S, Lenaerts É, Marquet L, Erpicum C, Greimers R, Gillet P, et al. Open Implementation of DICOM for Whole-Slide Microscopic Imaging: In: Proceedings of the 12th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications. Porto, Portugal: SCITEPRESS - Science and Technology Publications; 2017. p. 81–7. Available from: https://orbi.uliege.be/handle/2268/204498 doi:[10.5220/0006155100810087](https://doi.org/10.5220/0006155100810087)
6. Clunie D. com.pixelmed.convert.TIFFToDicom. 
   Link: [http://www.dclunie.com/pixelmed/software/javadoc/com/pixelmed/convert/TIFFToDicom.html](http://www.dclunie.com/pixelmed/software/javadoc/com/pixelmed/convert/TIFFToDicom.html)
7. Pocock J. wsic. 2023.
  Link: [https://github.com/John-P/wsic](https://github.com/John-P/wsic)
8. Orthanc WSI "Dicomizer"
  Link: [https://www.orthanc-server.com/static.php?page=wsi](https://www.orthanc-server.com/static.php?page=wsi)
  Documentation: [https://orthanc.uclouvain.be/book/plugins/wsi.html](https://orthanc.uclouvain.be/book/plugins/wsi.html)

### Background Information
DICOM-WSI: [https://dicom.nema.org/dicom/dicomwsi/](https://dicom.nema.org/dicom/dicomwsi/)

### Test Data

OpenSlide: [https://openslide.org/](https://openslide.org/)
Test data can be downloaded there for some vendors.

Imaging Data Commons has >23TB of DICOM WSI (converted from original SVS): [https://portal.imaging.datacommons.cancer.gov/explore/filters/?Modality_op=OR&Modality=SM](https://portal.imaging.datacommons.cancer.gov/explore/filters/?Modality_op=OR&Modality=SM)

NEMA ftp server including WG 26 Connectathon ECDP 2023 data from vendors (some have issues; older data is more variable in quality): ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG26/

### Other Resources
Test-Suite: TBD

Link to Lean Study Host: [https://github.com/TIO-IKIM/LeanStudyHost](https://github.com/TIO-IKIM/LeanStudyHost)

Validation tool (checks compliance with standard): [https://www.dclunie.com/dicom3tools/dciodvfy.html](https://www.dclunie.com/dicom3tools/dciodvfy.html)



