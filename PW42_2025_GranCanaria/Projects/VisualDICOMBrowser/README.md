---
layout: pw42-project

permalink: /:path/

project_title: Visual DICOM browser
category: Infrastructure

key_investigators:

- name: Davide Punzo
  affiliation: freelance, DNA-HIVE
  country: France

- name: Andras Lasso
  affiliation: Queens University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The visual DICOM browser provides a new user interface for quick viewing and retrieval of patient images stored on remote DICOM servers. The new tool is optimized for clinical workflows where the focus is on all the images of a single patient - as opposed to the existing DICOM browsing experience, which was more suitable for bringing together images from many patients.

Both server and local content are located at the same place and are visualized by thumbnails. All data is retrieved in the background using classic DIMSE networking (most commonly used protocols in hospitals), in multiple concurrently running threads. The currently supported operations are:

- Browsing and filtering with thumbnails of content of local DICOM database and multiple remote DICOM servers.
- Query/Retrieve data from servers (DIMSE `C-FIND`, `C-GET`, `C-MOVE` SCU). All the operations are done in background and in parallel. Downloaded data is automatically cached in the local DICOM database. A unique feature is the possibility to retrieve images using C-GET protocol (suitable for cases when many Slicer instances are running in docker containers) with a clinical PACS that only supports C-MOVE protocol (most clinical PACS), via a proxy server (such as the free Orthanc).
- Import data from local files.
- Receive data sent from remote PACS (DIMSE `C-STORE` SCP).
- Send data to remote PACS (DIMSE `C-STORE` SCU).
- Quick browsing of all DICOM metadata and pixel data.
- Remove data from local database (not from server).

The widget is currently an experimental feature in Slicer (DICOM module). Current Roadmap is at [link](https://github.com/commontk/CTK/issues/1162).

**Over the past year, improvements have been made to the performance and stability of the widget (full references in [Background and References](#background-and-references)). 
As a result, the widget is now prepared for broader testing and feedback from both users and developers.**

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Get feedback from users/developers.
1. Prioritize the long term ENH based on the community need/interest. For example:
	- Add support for DICOMweb
  - Add support for DICOM frame set
  - redesign the patient selection widget (currently a tab widget)
  - ...


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Have a meeting/demo with people interested for colletting feedback.  
1. Prioritize/coordinated any future development based on the feedback.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
 


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


screenshots:

|Visual DICOM Browser | Jobs and Settings|
|--- | ---|
|<img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/86088d74-650b-4139-8e1f-66d0794b73f7" width="1000"> | <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/971d3b2e-5fc6-422c-b57e-eb1c37e1b8b6" width="500">  <img src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/00c4bf23-961b-407b-8730-085d54244a53" width="500">|


video:

<video
   autoplay muted loop
   src="https://github.com/NA-MIC/ProjectWeek/assets/7985338/9bf4aa20-9c24-4673-8cc6-55039411bf68"
   style="width:1000px">
</video>

UML Diagram:

<img src="https://github.com/user-attachments/assets/7dbf8191-806e-4af9-871c-a578dd1e6051" width="1000">

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[PR](https://github.com/commontk/CTK/pull/1187)

[PR](https://github.com/commontk/CTK/pull/1191)

[PR](https://github.com/Slicer/Slicer/pull/7676)

[PR](https://github.com/commontk/CTK/pull/1201)

[PR](https://github.com/commontk/CTK/pull/1202)

[PR](https://github.com/commontk/CTK/pull/1203)

[PR](https://github.com/Slicer/Slicer/pull/7751)

[PR](https://github.com/commontk/CTK/pull/1206)

[PR](https://github.com/commontk/CTK/pull/1217)

[PR](https://github.com/commontk/CTK/pull/1218)

[PR](https://github.com/Slicer/Slicer/pull/7811)

[PR](https://github.com/Slicer/Slicer/pull/7912)

[PR](https://github.com/commontk/CTK/pull/1221)

[PW40 Project](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerVisualDICOMBrowser/)

[PW38 Project](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerVisualDICOMbrowser/)


