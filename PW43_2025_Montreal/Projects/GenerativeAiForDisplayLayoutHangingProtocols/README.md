---
layout: pw43-project

permalink: /:path/

project_title: Generative AI for Display layout/ Hanging protocols
category: Infrastructure

key_investigators:

- name: Martin Bellehumeur
  affiliation: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Generative AI / LLMs can today produce a good draft of report impressions based on learning the report history of the radiologist.
 We believe that GenAI could today produce reasonably valid hanging protocols if it had enough training data.

 Therefore, we   propose to standardized  hanging protocol Gen AI training data.  
 This data would be used by PACS viewers or AI agents to infer the appropriate display of the images available. 


 Because of standardization, radiologists would no longer have to train/configure each viewer they encounter.  
 They (or their PACS admin) would instead provide access to their personal training data repository to the viewer software. 


Ideally, the viewers would not only use the data for display but also provide the ability to add new hanging protocol training cases to the user's repository.

We believe that having the full study/series/image metadata, in addition to the thumbnails, could allow AI to compete with rule based systems.  Especially when those systems cannot be constantly maintained by highly skilled individuals.  

Gen AI would also enable personal hanging protocols which is almost impossible today because of maintenance costs.  



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Raise interest in the radiology reporting community in the standardization of hanging protocol training data.

Create proof of concept training data by adding the functionality to an open-source viewer.
This exercise should allow to refine the training data format required and could support an IHE standard request/grant request.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
This week we will add a prototype extension to the OHIF viewer that will save display layout training data and load it.
Ideally, we would do the same in 3DSlicer and demonstrate interoperability.


### Criterias
1. The training data should be human readable.  Therefore we would use DICOMweb/JSON encoding instead of DICOM binary.
 
2. The training data should be portable. The size of the data should be small enough that radiologist can keep their own backup copy, modify it manually if they wish and create multiple repositories if they need to.


### Example training data format

Each stored hanging protocol training data point would be composed of a folder containing:
1. A screenshot of the layout with privacy mode on.
2. A [hanging protocol DICOM information object](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.23.html) defining the layout and which series was assigned to which viewport (and other details).  This object would not try to define rules for the hanging protocol but just store what the user selected.  Also of interest is the work in [section V](https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_V.html).  THe hard work of defining monitor geometry, layouts, viewport types, viewport linking, ect, all that is already existing in the DICOM standard.
3. Separate folder for each study of the patient containing the metadata of each study/series/image(object) of the patient in [static DICOMweb](https://github.com/RadicalImaging/Static-DICOMWeb) format.  Therefore each display set will also include a thumbnail image. Patient level information and bulk data (DICOM image data) would not be stored.
4.  A way to identify which study was the current.


### Viewer support

Viewers would at a minimum need to support reading the hanging protocol object and assign the series specified by the AI to the layout.  Viewers that already support the existing hanging protocol DICOM standard object would be advantaged as they should be.

The request for the hanging protocol object would be done by the worklist or the viewer.  They would provide the same study/series metadata that is in the training data and the AI agent would return the most appropriate hanging protocol from your training data and assign series to the defined viewports in the hanging protocol object. 


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


I did not make progress on the original project but worked on a volume cropping (clipping?)  tool for Cornerstore3D/OHIF that was requested by a customer.
The customer wants the tool to be given back to open source so it will be available shorthly:

![image](https://github.com/user-attachments/assets/5f316009-dcb1-4f82-895a-da06a19f5e1d)

Next step I will attend Eusomii conference in October and try to find radiologist interested in GenAI for hanging protocols.

I will attend the next NA-MIC in Las Palmas and prototype something beforehand.

# Illustrations

A hanging protocol AI agent could, using the studies and series level metadata of the current and prior studies, find the most appropriate layout. 

## How Hanging Protocol AI Agents Work


```
+-----------------------------------+         +---------------------+         +-------------------+
|                                   |         |                     |         |                   |
|   PACS Viewer                     +-------->+  Hanging Protocol   +-------->+   Display Layout  |
| (current & prior study metadata   |         |    AI Agent         |         | (images assigned  |
|  and thumbnails)                  |         | (selects protocol   |         |   to viewports)   |
|                                   |         |  and assigns series |         |                   |
+-----------------------------------+         +---------------------+         +-------------------+
```
*The PACS viewer sends current and prior study metadata and thumbnails to the AI agent, which selects the best hanging protocol and returns the layout for display.*
*The PACS viewer sends study metadata and images to the AI agent, which selects the best hanging protocol and returns the layout for display.*




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[hanging protocol DICOM information object](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.23.html)

[section V](https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_V.html) 

[static DICOMweb](https://github.com/RadicalImaging/Static-DICOMWeb)  




 




