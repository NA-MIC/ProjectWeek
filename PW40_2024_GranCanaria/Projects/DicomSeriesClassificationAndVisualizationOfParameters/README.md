---
layout: pw40-project

permalink: /:path/

project_title: DICOM series classification and visualization of parameters
category: DICOM
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Bálint Kovács
  affiliation: DKFZ
  country: Germany

- name: Stefan Denner
  affiliation: DKFZ
  country: Germany 

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

To use and develop AI methods, significant data curation is required. In some cases like prostate cancer segmentation, clinicians often use multiple MRI sequences for diagnosis such as T2, diffusion-weighted series, and derived maps.

Unfortunately, the information describing the sequences is often missing or incorrect, as it's prone to errors from technicians. The proper sequence could be analyzed visually, but this is cumbersome if thousands of scans need to be analyzed. Therefore, automatic methods for determining the right series are of interest.

We propose methods to aid in the curation of DICOM data, as well as aids to help in vizualization of DICOM parameters.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

We would like to develop approaches for aiding in the curation of data. The first will be the development of visualization tools to understand DICOM parameters used in scanning. Secondly, we will develop AI methods for classifying MRI scans, with a focus on prostate cancer.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Use packages such as [hiplot ](https://ai.meta.com/blog/hiplot-high-dimensional-interactive-plots-made-easy/) to visualize DICOM scanning parameters across different collections and modalities in IDC.
3.  Develop approaches for data curation using AI - e.g. determine the scan sequence, or if endorectal coil is present, etc.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Started [repo here](https://github.com/deepakri201/DICOMTagViz/) for initial [hiplot](https://github.com/facebookresearch/hiplot) exploration of DICOM tags of T2 weighted axial series of prostate imaging collections from IDC 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
Hiplot vizualization of T2 weighted axial parameters from 5 different prostate cancer imaging collections in IDC

![hiplot_t2_recording_01_23_24_2](https://github.com/NA-MIC/ProjectWeek/assets/59979551/420c4733-c27e-4ef8-87a9-ebc35bb8e224)


# Background and References

[GitHub repo](https://github.com/deepakri201/DICOMTagViz/)

Some earlier work with parallel coordinates plots in Slicer:
* https://github.com/pieper/SlicerMultiMapper
* https://www.youtube.com/watch?v=Y4MyThyeIPs
