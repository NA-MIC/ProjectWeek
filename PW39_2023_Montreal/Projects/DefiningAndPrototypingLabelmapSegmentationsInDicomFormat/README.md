---
layout: pw39-project

permalink: /:path/

project_title: Defining and Prototyping Labelmap Segmentations in DICOM Format
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Chris Bridge
  affiliation: MGH/Harvard
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: David Clunie
  affiliation: PixelMed
  country: USA

- name: Andrey Fedorov
  affiliation: BWH/Harvard
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The DICOM Segmentation format is used to store image segmentations in DICOM format. Using DICOM Segmentations, which use the DICOM information model and can be communicated over DICOM interfaces, has many advantages when it comes to deploying automated segmentation algorithms in practice. However, DICOM Segmentations are criticized for being inefficient, both in terms of their storage utilization and in terms of the speed at which they can be read and written. This is in comparison to other widely-used segmentation formats within the medical imaging community such as NifTi and NRRD.

While improvements in tooling may alleviate this to some extent, there appears to be an emerging consensus that changes to the standard are also necessary to allow DICOM Segmentations to compete with other formats. One of the major reasons for poor performance is that in segmentation images containing multiple segments (sometimes referred to as "classes"), each segment must be stored as an independent set of binary frames. This is in contrast to formats like NifTi and NRRD that store "labelmap" style arrays in which a pixel's value represents its segment membership and thus many (non-overlapping) segments can be stored in the same array. While the DICOM Segmentation has the advantage that it allows for overlapping segments, in my experience the overwhelming majority of segmentations consists of non-overlapping segments, and thus this representation is very inefficient when there are a large number of segments.

The goal of this project is to gather a team of relevant experts to formulate changes to the standard to address some issues with DICOM Segmentation. We will focus primarily on "Labelmap" style segmentations and issues surrounding frame compression. Other objectives for further discussion include simplifying per-frame metadata. Although we do not speak for the DICOM standards committee, we hope to put forward a complete proposal that can be considered by the committee. Ideally, the proposal will be backed by multiple interoperable implementations of the proposed objects and demonstrations of their value in reducing object size and complexity.

The proposal for this project received a considerable amount of constructive feedback from the community: [#643](https://github.com/NA-MIC/ProjectWeek/issues/643)

@pieper @fedorov @dclunie

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Put forward a proposal for changes to the DICOM Segmentation object that addresses the needs of the medical image computing community

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Gather relevant experts to discuss and appraise potential changes to the DICOM standard for Segmentations
2.  Compile a full proposal based on the resulting consensus from the team
3.  Implement prototypes of the new proposed objects in the highdicom (python) and dcmjs (javascript) libraries
4.  Use the prototype implementations to demonstrate the advantages of the proposed changes on realistic data (e.g. in terms of file size, read/write times)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Solicited feedback and items for discussion on proposal #643

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
