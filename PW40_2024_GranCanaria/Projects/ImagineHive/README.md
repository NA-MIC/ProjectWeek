---
layout: pw40-project

permalink: /:path/

project_title: ImagineHive
category: Cloud / Web
presenter_location: In-person

key_investigators:
- name: Davide Punzo
  affiliation: Freelancer, DNA HIVE 
  country: France   

- name: Mauro Domínguez
  affiliation: Freelancer, DNA HIVE
  country: Argentina

- name: Andras Lasso
  affiliation: Perk Lab, Queen's University 
  country: Canada

- name: Vahan Simonyan
  affiliation:  DNA HIVE 
  country: USA

- name: Aram Petrosyan
  affiliation: DNA HIVE 
  country: USA

- name: Jeffrey W Milsom
  affiliation: Weill Cornell Medicine
  country: USA

- name: Bradley B Pua
  affiliation: Weill Cornell Medicine
  country: USA

- name: Art Sedrakyan
  affiliation: Weill Cornell Medicine
  country: USA


---

# Project Description

![image](https://github.com/NA-MIC/ProjectWeek/assets/7985338/dc3f2fbf-9057-4caf-9fb9-66d42e6394bd)

[ImagineHive](https://www.dnahive.com/) is a data management and analytics platform for hospital environments consisting of:

1. Web frontend to navigate, filter and edit patients data.
1. HIVE server backend for storing and sharing data and run data analytics and processing workloads. HIVE is a massively parallel distributed computing environment where the distributed storage library is linked with computational.
1. SlicerHIVE, a Slicer-based app that shows up in the web browser and offers 3D image visualization and analysis:
   * Browse and retrieve data from hospital PACS.
   * Viewer and markup tools for enhanced teamwork.
   * Automated segmentation tools.

ImagineHive is currently used at the Weill Cornell Medicine/Presbyterian NY hospital (**CI3: center for intelligent image guided interventions at New York Presbyterian Hospital, New York, NY, USA**) for clinical pre-operation review and planning.

## Objective

1. Present ImagineHive. Get feedback.
1. Learn about user needs.
1. Foster collaborations with potential users and similar development efforts.

## Approach and Plan

1. Have a meetings/demos with people interested.

## Progress and Next Steps

1. Update of Slicer's DICOM browser to be more friendly for patient-oriented clinical workflows (visual appearance, better responsiveness - see [details](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerVisualDICOMBrowser/).
2. We had a meeting on Tuesday where we discussed the integration of customized 3DSlicer into web applications.
3. We presented a demonstration of ImageHIVE on Thursday and collected feedback.

# Illustrations

### HIVE front-end:

| Patient selection | Imaging |
| --- | --- |
| <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/0cd01923-2efe-4141-aefc-84d9716851cf" width="500"> | <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/9568cd8b-ec41-4b57-8541-ca3142707085" width="500"> |

### SlicerHIVE:

| Workspace selector | Visual DICOM browser |
| --- | --- |
| <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/06dec4f2-7e12-4b6e-8f08-feb2525749d2" width="500"> | <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/ca8c7182-dad0-4e4f-90e3-b508f690bc72" width="500"> |

| Segmentation tools | Viewer |
| --- | --- |
| <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/47fd127e-bdf0-48c4-88a2-dd55ab088d52" width="500"> | <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/bda9f033-1105-4333-8501-6add25476281" width="500"> |

### HIVE back-end:

<p align="center">
   <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/bbeee3db-c1c6-455f-8036-a41539809d64" width="500">
</p>
<p align="center"><i><a href="https://doi.org/10.1093/database/baw022">source: Vahan et al. 2016</a></i></p>

# Background and References
- [HIVE paper](https://doi.org/10.1093/database/baw022) 
- [HIVE FDA](https://github.com/FDA/fda-hive)
