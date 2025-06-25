---
layout: pw43-project

permalink: /:path/

project_title: 'Slicer-SOFA: Next Steps'
category: Infrastructure

key_investigators:

- name: Rafael Palomar
  affiliation: Oslo University Hospital and NTNU
  country: Norway

- name: Paul Baksic
  affiliation: Inria
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware Inc.
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Sam Horvath
  affiliation: Kitware Inc
  country: USA
  
- name: Naomi Catwell
  affiliation: ÉTS
  country: Canada
  
- name: Chi Zhang
  affiliation: Texas A&M School of Dentistry
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The SlicerSOFA project has already been integrated as a Slicer extension, providing core functionality including python bindings and many examples.
We'd now like to take the next steps to determine default funcationality and determine how we want to enable applications that use the extension. In addition we will tackle some of the issues that need a fix, most notably, the MacOS extension packaging which to date is not available.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Define what SOFA plugins should be enabled for the extension and update the packaged SOFA to the lastest possible version (SOFA is currently in v25.06, while SlicerSOFA still uses v24.06).

2. Objective B. See if we can build a template for SlicerSOFA-based extensions that can provide custom C++ SOFA plugins.
This would allow the SOFA community to leverage Slicer's existing infrastructure for cross-platform testing and distribution.

3. Objective C. Discuss/prototype parallel processing architectures to optimize overlap of simulation and rendering for best interactive performance.
 
4. Objective D. Bug fixing ([#44](https://github.com/slicer/slicersofa/issues/44)) and MacOS package fixing

5. Objective E. Discuss other topics of interest to potential SlicerSOFA users.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Meet to review existing SlicerSOFA build configuration and options.

2. Discuss and possibly prototype a C++ SOFA plugin in a SuperBuild extension that depends on SlicerSOFA

3. Discuss various client/server and message passing options, such as an http-based protocol, RPyC, or others.
   
4. Improve the SlicerSOFA (and possibly SOFA) CMake infrastructure to enable MacOS packaging. Review SlicerSOFA python infrastructure in connection with the SoftTissueSimulation and [#44](https://github.com/Slicer/SlicerSOFA/issues/44) 

6. Reach out to other Project Week attendess who express interest.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

- Point 4:
  - One PR has been opened on SOFA to globally specify OUTPUT_DIRECTORY for runtime, archive and library material https://github.com/sofa-framework/sofa/pull/5558
  - One PR has been opened on SOFA to globally specify the RELOCATION path for plugins, applications and projects https://github.com/sofa-framework/sofa/pull/5562

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [SlicerSOFA GitHub Repository](https://github.com/Slicer/SlicerSOFA)
- [SOFA Framework](https://www.sofa-framework.org/)
- [3D Slicer](https://www.slicer.org/)
- [SlicerSOFA PW 42 Project](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/SlicerSofaIntegrationOfSofaWith3DSlicerForAdvancedMedicalSimulations/)
- [Slicer-SOFA PW 41 Project](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SlicerSofa/)
- [Slicer-SOFA PW 40 Project](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerSofaIntegration/)
