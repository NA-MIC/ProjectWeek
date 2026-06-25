---
layout: pw45-project

permalink: /:path/

project_title: NousNav Project Updates
category: IGT and Training
presenter_location: 

key_investigators:

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Alex Golby
  affiliation: BWH
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->
The NousNav project is an initiative led by Dr Alex Golby to develop a low-cost neuronavigation system designed for use in low- and middle-income countries. We are developing a 3D Slicer based application focused on supporting segmentation, registration and navigation tasks.

The project will also include the development of open source hardware desgins for these applications.

This week will include continued development on the NousNav project, in preparation for work with new collaborators.  This includes new usability features, UI refinement and updating the guidance images for the patient registration.




## Objectives and Progress

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


- Generate installers for NousNav 1.1
    - In progress, pending IGSIO build fixes
- 1.2 tasks finished:
  - Add recenter views toolbar button — New toolbar button (Google Material "my_location" icon) next to the screenshot button that recenters all 2D slice views and resets 3D cameras.
  - Update registration guidance images — Updated images used during the registration workflow.
  - Fix picture layout image scaling to maintain aspect ratio — Replaced ctkThumbnailLabel with QLabel and added a resize event filter to scale images proportionally using KeepAspectRatio.
  - Fix tab bars to fit all tabs without scrolling — Disabled scroll buttons on primary and secondary tab bars, removed min-width: 200px from tab QSS rules, and zeroed spacer stretch factors so tabs share available space. Closes #322.
  - Reduce module panel width to give more space to central layout — Scaled down per-page widget sizes by ~5% (fonts, margins, min-heights) and set minimum size policy on the module panel.
  - Add user-settable RMSE error thresholds in settings dialog — Added a new "Error Thresholds" section to the settings dialog with spin boxes for pivot, spin, registration, initial registration, and conditional registration RMSE thresholds, persisted via QSettings.
  - Replace flake8 with ruff for pre-commit linting — Swapped flake8 for ruff (v0.15.17) in .pre-commit-config.yaml, created ruff.toml with equivalent rules adapted from Slicer, and auto-fixed 89 whitespace issues.
- Work on addressing licensing concerns from MGB




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
<img width="1922" height="1081" alt="Screenshot 2026-06-25 093911" src="https://github.com/user-attachments/assets/a4b338d6-cffc-467d-bc24-7fb97bf40cbf" />

<img width="1932" height="1087" alt="Screenshot 2026-06-25 093828" src="https://github.com/user-attachments/assets/812490c5-0213-45fd-86dd-ea734efcb55b" />



# Background and References

Previous Project Week Pages:
- [PW 35](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/NousNav/)
- [PW 36](https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/NousNav/)
- [PW 36 Skin Segmentation](https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/SkinSegmentation/)
- [PW 39](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/NousNavRelease/)
- [PW 39 Tracked Ultrasound](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/TrackedUltrasoundIntegrationIntoNousnavALowCostNeuronavigationSystem/)
- [PW 41 Skin Segmentation](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SkinSurfaceSegmentationForNousnav/)
- [PW 42](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/NousnavFuturePlansAndGrantBrainstorming/)

- [PW 44](https://projectweek.na-mic.org/PW44_2026_GranCanaria/Projects/NousnavBasedSlicerExtension/)


<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

