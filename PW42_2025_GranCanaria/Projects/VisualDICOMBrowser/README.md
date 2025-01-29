---
layout: pw42-project

permalink: /:path/

project_title: Visual DICOM browser
category: Infrastructure

key_investigators:

- name: Davide Punzo
  affiliation: freelancer, DNA-HIVE
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

1. Feedback has been collected:
  - #### **Leonard Nürnberg:**  
    - Add an option in settings to order series in the study widget by modality.  
    - Automatically load the source volume when loading a segmentation.  
    - Render SEG DICOM thumbnails (already a known issue).  
    - Improve UI clarity regarding querying PACS servers vs. filtering the local database (e.g., display a dialog explaining the difference when a user opens the visual DICOM browser for the first time).  

  - #### **Tina Kapur:**  
    - Add a button to enable full-screen mode in the Visual DICOM browser.  
    - Modify *Edit → Application Settings → DICOM → Thumbnail Size* (small, medium, large) to apply changes without requiring a restart.  
    - Address UI performance issues when importing large cohorts (e.g., 490 patients with 3,931 DICOM series).  
    - Implement support for ultrasound video visualization in the Visual DICOM browser (already a known issue, see [CTK issue #1162](https://github.com/commontk/CTK/issues/1162#long-termENH) and [Slicer Discourse thread](https://discourse.slicer.org/t/new-frame-set-table-in-the-dicom-database/35012)).  

1. The 2025 roadmap priorities will be evaluated following an assessment of current funding opportunities.


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


[PR CTK 1187](https://github.com/commontk/CTK/pull/1187) - [PR CTK 1191](https://github.com/commontk/CTK/pull/1191) - [PR Slicer 7676](https://github.com/Slicer/Slicer/pull/7676) - [PR CTk 1201](https://github.com/commontk/CTK/pull/1201) - [PR CTK 1202](https://github.com/commontk/CTK/pull/1202) - [PR CTK 1203](https://github.com/commontk/CTK/pull/1203) - [PR Slicer 7751](https://github.com/Slicer/Slicer/pull/7751) - [PR CTK 1206](https://github.com/commontk/CTK/pull/1206) - [PR CTK 1217](https://github.com/commontk/CTK/pull/1217) - [PR CTK 1218](https://github.com/commontk/CTK/pull/1218) - [PR Slicer 7811](https://github.com/Slicer/Slicer/pull/7811) - [PR Sliceer 7912](https://github.com/Slicer/Slicer/pull/7912) - [PR CTK 1221](https://github.com/commontk/CTK/pull/1221)

[PW40 Project](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerVisualDICOMBrowser/)

[PW38 Project](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerVisualDICOMbrowser/)


