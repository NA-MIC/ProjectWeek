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

- name: Joël Spaltenstein
  affiliation:  Agora Care SA
  country: Switzerland

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

1. DCMTK: Updated (templated) pixel data structures to also accept 16 bit
1. DCMTK: Updated all dependent classes (also some outside the segmentation code) to accept that as well
3. DCMTK: Prepare code for labelmap support
   1. Changed bookkeeping and access mechanism for segments (allow sparse numberings, allow 0)
   2. Mitigate checks where necessary
   3. Implemented missing attribute "Spatial Locations Preserved"
4. DCMTK: Successfully tested roundtrip for MONOCHROME2 Labelmaps produced by highdicom
5. dcmqi:
   1. Modified to handle the concept of multiple segmentations per frame.
   2. Added search in each frame to find what segments are on the frame for `LABELMAP`s.
   3. Modified to become tolerant of non-monotonically increasing `SegmentNumber`s and accept a
      segment with `SegmentNumber` of `0`.
   5. Adapted to updated DCMTK pixel data and segment access API

Next steps:
1. DCMTK:
   1. Test support for 16 bit segmentation pixel data (added but not tested yet)
   2. Add support for PALETTE COLOR model (palette is not imported / exported yet)
   3. Add unit tests for all color model / bit depth combinations
2. dcmqi:
   1. Actualy link it against the new DCMTK run it and test it...
   2. Performance can propably be improved significanly by not making a bunch of function
      calls within tight loops.
   4. Set up tests with LabelMap segmentation objects.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- DICOM Supplement 243 "Label Map Segmentation": [PDF Download](https://dicom.nema.org/medical/dicom/Supps/Drafts/sup243_02_LabelMapSeg.pdf)
- DCMTK: [Homepage](https://www.dcmtk.org) and [GitHub](https://github.com/DCMTK/dcmtk/)
  - DCMTK version with labelmap enhancements: [Michael's GitHub](https://github.com/michaelonken/dcmtk/tree/Labelmap)
- dcmqi: [Guide](https://qiicr.gitbook.io/dcmqi-guide/) and [GitHub](https://github.com/QIICR/dcmqi/)
  - dcmqi with labelmap enhancements: [WIP PR on GitHub](https://github.com/QIICR/dcmqi/pull/491)
- Slicer: [Homepage](https://www.slicer.org/) and [GitHub](https://github.com/Slicer/Slicer)
