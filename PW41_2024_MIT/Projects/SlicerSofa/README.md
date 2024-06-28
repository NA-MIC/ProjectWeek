---
layout: pw41-project

permalink: /:path/

project_title: 'Slicer-SOFA '
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Rafael Palomar
  affiliation: Oslo University Hospital / NTNU
  country: Norway

- name: Paul Baksic
  affiliation: INRIA
  country: France

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Naomi Catwell
  affiliation: ETS Montreal
  country: Canada

- name: Chi Zhang
  affiliation: Texas A&M School of Dentistry
  country: USA

- name: Ron Alkalay
  affiliation: Beth Israel Deaconess Medical Center
  country: USA

- name: Quinn Williams
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Slicer-SOFA was born during [PW40](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerSofaIntegration/) with the aim to support the use of the SOFA simulation library within 3D Slicer. This project will continue the development of the extension.

<img src="https://github.com/NA-MIC/ProjectWeek/assets/1978682/bb53dde9-7baa-45cc-87df-aabd6d6ef35d" alt="slicer-sofa-logo" width=200px/>

<video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/1978682/9d34a012-14c7-4480-89ff-265b74b054c5"
   style="max-height:640px; min-height: 200px">
 </video>






## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Engage with the community to understand the needs and possibilities
2. Establish a roadmap for future development of the Slicer-SOFA extension
  - Extension architecture to support simulation modules [RafaelPalomar/Slicer-SOFA#15](https://github.com/RafaelPalomar/Slicer-SOFA/issues/15)
  -  Distribution of third-party libraries [RafaelPalomar/Slicer-SOFA#14](https://github.com/RafaelPalomar/Slicer-SOFA/issues/14)
  - ...



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Meetings with the community, the SOFA and 3D Slicer developers.
2. Add new example modules
3. Add documentation
4. Bug fixes and extension release



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

* Modifications towards the binary distribution of SlicerSOFA as an extension (rafaelpalomar/SlicerSOFA#22) by Jean-Christophe Fillion-Robin
* Tested Slicer-SOFA extension on mac os build
    * Requires a local slicer build (tested on debug, see notes below for details)
    * Issues
    	* Turning off Qt and OpenGL dependencies doesn't seem to work - it would be best to build just the core simulation and python wrapping.
     	* Building in release mode didn't recognize libaries
 * Added a reset simulation functionality (rafaelpalomar/SlicerSOFA#23) by Quinn Williams
      



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

# Notes

## Mac OS build
    * Configure and make:
      ```
      cmake \
	      -DCMAKE_BUILD_TYPE:STRING=Debug \
	      -DSlicer_DIR:PATH=${SLICER_BUILD} \
      	-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=11.0 \
      	../Slicer-SOFA

      make -j50 |& tee log
      ```
  * Launch:
    ```
    export SLICERSOFA_DIR=/Users/pieper/slicer/latest/SOFA
    export SLICER_DIR=/opt/s
        SOFA_ROOT=${SLICERSOFA_DIR}/Slicer-SOFA-build/SOFA-build \
        ${SLICER_DIR}/Slicer-build/Slicer \
        --launcher-additional-settings ${DIR}/Slicer-SOFA-build/inner-build/AdditionalLauncherSettings.ini
    ```
  * Then paste a [script like this](https://github.com/pieper/Slicer-SOFA/blob/main/Experiments/lung.py) into the python console.

