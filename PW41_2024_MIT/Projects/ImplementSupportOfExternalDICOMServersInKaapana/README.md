---
layout: pw41-project

permalink: /:path/

project_title: Implement support of external DICOM servers in Kaapana
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Vamsi Thiriveedhi
  affiliation: Brigham and Women's Hospital
  country: Boston
- name: Mikulas Bankovic
  affiliation: DKFZ
  country: Germany
- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: Boston

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The goal of this project is to enhance the capabilities of Kaapana, an open-source platform, by enabling it to work seamlessly with DICOM data stored in Google Cloud's HealthCare API DICOM stores. Currently, Kaapana relies on an internal dcm4chee DICOM, which means all of the data needs to be managed on the same VM as Kaapana itself, and in the situation where data already exists in an external DICOM store, it needs to be replicated to the Kaapana dcm4chee. We would like to make it possible to reuse existin Google Healthcare DICOM store without copying its content. Building upon the [previous](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/RunKaapanaOnGkeAndImproveConnectivityOfKaapanaToIdc/) project week's progress, we aim to further improve the connectivity and compatibility of Kaapana with Google's Healthcare API.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Build on the progress done by Miki from Kaapana team on the PR in progress 
2. Review GCP authentication's procedure currently implemented




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Evaluate the current state of the feature by building docker images from the outstanding PR
2. Impement GCP authentication by asking the user to upload a service account key file with necessary permissions 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


_No response_



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/RunKaapanaOnGkeAndImproveConnectivityOfKaapanaToIdc/](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/RunKaapanaOnGkeAndImproveConnectivityOfKaapanaToIdc/)

