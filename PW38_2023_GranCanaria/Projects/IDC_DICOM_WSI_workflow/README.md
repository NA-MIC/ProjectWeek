Back to [Projects List](../../README.md#ProjectsList)

# Write full project title here

## Key Investigators

- Maximilian Fischer (German Cancer Research Center, Germany)
- Andrey Fedorov (Brigham and Women’s Hospital, USA)
- Marco Nolden (German Cancer Research Center, Germany)
- Philipp Schader (German Cancer Research Center, Germany)
- David Clunie (PixelMed Publishing, USA)
- Daniela Schacherer (Fraunhofer MEVIS, Germany)
- André Homeyer (Fraunhofer MEVIS, Germany)


# Project Description

<!-- Add a short paragraph describing the project. -->
The Imaging Data Commons (IDC) portal is a cloud based repository of public cancer imaging data, and inclludes access to histopathological image data in the DICOM standard. In recent years increasingly more automated image analysis algorithms for pathology data emerged. However they are mainly developed for proprietary WSI vendor file formats and not for the standardized DICOM WSI file format as input. In this project a tumor classification algorithm shall be developed for DICOM WSI files as input file format. 
The aim of this project is to develop an end to end Google Colab notebook to define a data cohort from the IDC database. The selected cohort is retrieved in the DICOM WSI standard and an examplary deep learning based image analysis algorithm is applied on the selected DICOM studies. As a use case task we select a classification algorithm, which is a common downstream task in computational pathology. The algorithm generates for the selected DICOM WSI files a tumor heatmap and provides the analysis result as DICOM parametric map, which can be visualized together with WSI image in the interoperable web-based slide microscopy viewer and annotation tool (SLIM), which is fully integrated in the IDC database. 
A basis of this project provides the DICOM WSI support in the Kaapana platform, which also shall be improved in this project. The custom DICOM conversion pipeline for WSI files, which is integrated in the platform shall be improved and further applications with DICOM WSI data integrated in the platform. 






## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. An analysis pipeline to visualize the analysis results for IDC digital pathology data 
2. Deploy a deep learning based tumor classification algorithm via Google Colab
3. Develop further pathology applications in the Kaapana platform

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Define Query/Retrieve operations to define a data cohort from IDC portal
2. Test several image analysis algorithms for tumor classification
3. Store the result in a DICOM WSI file format 
4. Integrate workflow in Google Colab

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

- worfklow used by IDC to create DICOM WSI: [https://github.com/ImagingDataCommons/idc-wsi-conversion](https://github.com/ImagingDataCommons/idc-wsi-conversion)
- Colab notebooks with examples of using DICOM WSI in analysis workflows: [https://github.com/ImagingDataCommons/IDC-Examples/tree/master/notebooks/pathomics](https://github.com/ImagingDataCommons/IDC-Examples/tree/master/notebooks/pathomics)
- [https://github.com/GoogleCloudPlatform/wsi-to-dicom-converter](https://github.com/GoogleCloudPlatform/wsi-to-dicom-converter)
