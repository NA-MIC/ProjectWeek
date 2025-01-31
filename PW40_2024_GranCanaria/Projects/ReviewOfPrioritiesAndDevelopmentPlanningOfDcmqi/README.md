---
layout: pw40-project

permalink: /:path/

project_title: Review of priorities and development planning of dcmqi
category: DICOM
presenter_location: Remote

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Michael Onken
  affiliation: OpenConnections
  country: Germany

- name: Joost van Griethuysen
  affiliation: NKI
  country: Netherlands

- name: Ralf Floca
  affiliation: DKFZ
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[dcmqi](https://github.com/QIICR/dcmqi) (DICOM for Quantitative Imaging) is a free, open source C++ library for conversion between imaging research formats and the standard DICOM representation for image analysis results.

This library has been around for quite some time, and gained some adoption, but has not been actively developed for the past few years, but with the efforts of @michaelonken development restarted.

The goal of this project would be to discuss what, if anything, could be done to make it more usable and address any of the needs that users might have.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Review any outstanding and new topics and feature requests
2.  Review issue tracker
3.  Review documentation

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  discuss with @jcfr any topics related to the possible integration with [ITK-Wasm dicom package](https://github.com/InsightSoftwareConsortium/itk-wasm/tree/main/packages/dicom)
2.  revisit basic python wrapping, similar to [pyplastimatch](https://github.com/AIM-Harvard/pyplastimatch) done by @denbonte
3.  clean up issue tracker
4.  discuss support of enhanced multiframe as SEG reference images and confirm understanding of the level of support of enhanced multiframe in Slicer/ITK (@michaelonken tried and failed to load any such images in Slicer)
5.  revisit documentation
6.  discuss interoperability testing with highdicom and dcmjs and maybe other tools.
7.  Help @JoostJM with possible integration into CaseIterator
8.  Discuss the use case for running conversion in absence of source image DICOM files, per request from @rfloca and as discussed in <https://github.com/QIICR/dcmqi/issues/390>.
9.  Discuss the process and schedule of upgrading dcmqi in MITK (@rfloca I did submit a PR, but not sure if those are reviewed? <https://github.com/MITK/MITK/pull/279>)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
1. Discussed revisions to API with Ralf, agreed on addressing https://github.com/QIICR/dcmqi/issues/390
2. Revisited the topic of encoding background voxels, further discussions with David C will be needed https://github.com/QIICR/dcmqi/issues/490
3. Confirmed with Ralf that github PRs to MITK is the proper mechanism for updating dcmqi version, current PR will be addressed
4. Spent some time cleaning up issue tracker.
5. Started revising documentation. Need further discussions with adopters (Cosmin, Leo, Dennis) to make further progress.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [dcmqi](https://github.com/QIICR/dcmqi)
