---
layout: pw40-project

permalink: /:path/

project_title: Implement new DICOM Label Map Segmentation Supplement
category: DICOM
presenter_location: In-person

key_investigators:
- name: Michael Onken
  affiliation: Open Connections GmbH
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA
  
- name: David Clunie
  affiliation: PixelMed (IDC)
  country: USA
  
---

# Project Description

DICOM has a new Supplement underway (Supp 243: Label Map Segmentation) which is currently
in status "Public Comment". DICOM already has support for Segmentations, mainly through
the Segmentation Storage SOP Class. While it is very efficient for storing densely packed
overlapping segmentations, typical medical segmentations are non-overlapping and each
segment not covering large portions of the pixel space and the Segmentation Storage SOP
Class wastes lots of space compared to the ITK-enabled formats like NRRD when storing these.

Slicer uses the dcmqi library to convert between DICOM Segmentations and ITK formats, and
dcmqi itself relies on the dcmseg library from DCMTK.

In the PW, we want to build DICOM Label Map support into DCMTK, dcmqi and
finally Slicer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Add Label Map support to DCMTK, dcmqi and Slicer.
2. Identify issues with the current Supplement text and provide comments to DICOM Committee.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. (Optional: Move OverlapUtil code from dcmqi to upstream DCMTK). During the last months
we added support for overlapping segment detection to dcmqi which enhances export to
DICOM Segmentations in their current version. This code should go to DCMTK which has jus
been released in version 3.6.8 and is open again for new features.
2. Add DICOM Label Map support to DCMTK's dcmseg API.
3. The code will not go upstream (in DCMTK) unless the Supplement has been progressed to Final Text.
It could make sense to move the code to dcmqi classes first and mark it as experimental, also in the API. Or,
keep it in a separate branch and wait for the merge until the Supplement is finalized.
4. Add DICOM Label Map support to dcmqi, using the updated dcmseg API.
5. Add DICOM Label Map support to Slicer, to make use of the new dcmqi segmentation converter version.

Let's see how far we can get in one week, but the goal is to have at least a first working
Label map implementation for DCMTK and then start with dcmqi support with Slicer to follow.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- DICOM Supplement 243 "Label Map Segmentation": [PDF Download](https://dicom.nema.org/medical/dicom/Supps/Drafts/sup243_02_LabelMapSeg.pdf)
- DCMTK: [Homepage](https://www.dcmtk.org) and [GitHub](https://github.com/DCMTK/dcmtk/)
- dcmqi: [Guide](https://qiicr.gitbook.io/dcmqi-guide/) and [GitHub](https://github.com/QIICR/dcmqi/)
- Slicer: [Homepage](https://www.slicer.org/) and [GitHub](https://github.com/Slicer/Slicer)
