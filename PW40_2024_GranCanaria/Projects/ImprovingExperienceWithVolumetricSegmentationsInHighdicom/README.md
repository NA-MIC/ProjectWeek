---
layout: pw40-project

permalink: /:path/

project_title: Improving Experience with Volumetric Segmentations in Highdicom
category: DICOM
presenter_location: In-person

key_investigators:

- name: Chris Bridge
  affiliation: MGH
  country: Boston, USA

- name: David Clunie
  affiliation: PixelMed Publishing
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: Boston, USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

### Background

The DICOM Segmentation format is used to store image segmentations in DICOM format. Using DICOM Segmentations, which use the DICOM information model and can be communicated over DICOM interfaces, has many advantages when it comes to deploying automated segmentation algorithms in practice. DICOM Segmentations are especially flexible in many respects including the arrangement of the multiple frames that are present in the image. However, https://github.com/NA-MIC/ProjectWeek/issues/643 flexibility is sometimes criticized for making the processes of creating and parsing overly complex for "simple" cases, which are also typically the most commonly encountered.

In particular, the case of a "3D volume" is very commonly encountered within segmentations. By "3D volume" I refer specifically to a segmentation in which frames are parallel and regularly spaced along a vector normal to each frame, possibly with multiple segments and, subject to discussion, with empty frames omitted from the volume.

This topic was discussed as part of a broader discussion on possible improvements to the Segmentation IOD for the last project week on https://github.com/NA-MIC/ProjectWeek/issues/643#issuecomment-1582677841 issue and in particular this comment is relevant.

This issue has been raised as one of particular interest by the Imaging Data Commons team. @dclunie @fedorov @pieper
Proposal

The proposed project is to investigate to what extent these issues can be simplified for users on two fronts:

    By better tooling for working with segmentations, by adding special cases to the [highdicom](https://github.com/ImagingDataCommons/highdicom) python library to deal with 3D volumes.
    By determining, in consultation with other DICOM experts at project week, whether additions or clarifications within the standard may be warranted.

### Details

Here is my initial attempt to lay out some of the issues to consider (some is adapted from the thread mentioned above):

    A key goal is that a receiver of a DICOM segmentation object should be able to determine whether it is a volume without having to parse the per-frame metadata and perform calculations based on them. Additionally, in my opinion, it would be preferable to be able to determine the spacing between slices in all volume cases without needing to perform additional calculations.
    There is already a mechanism by which the creator can convey that planes are equally spaced in 3D space by setting the [DimensionOrganizationType](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.17.html#table_C.7.6.17-1) to '3D'. This helps a bit, but does not require that SpacingBetweenSlices attribute be present in the SharedFunctionalGroupsSequence, so the receiver in the general case still needs to calculate the spacing for themselves. Neither does it actually require the ImageOrientationPatient to be present in the SharedFunctionalGroupsSequence. Furthermore, it does not specify which order the frames are stacked in (there are two options, top to bottom or bottom to top), nor does it specify whether multiple segments are allowed and if so what the dimension organization should be (i.e. does frame position or segment change most quickly as the frame number increases?). And lastly it is entirely optional to have the DimensionOrganizationType at all. So really the '3D' DimensionOrganization still leaves too much unnecessary flexibility in my opinion and is largely "toothless" without clarification or associated requirements.
    The above is actually not specific to segmentations, but are general to all IODs that use multiple frames. The issues have been noted mostly with reference to segmentations perhaps because segmentations are one of the more widely used multiframe IODs. I mention this because any changes/clarifications to the standard would have wide-reaching effects.

As a minimum (assuming no changes to the standard), I would propose that for project week I would make the following improvements to the highdicom library:

    In the segmentation constructor, add logic to determine whether the input segmentation could be recorded as "3D", and if so, automatically store it as such with the maximum amount of useful information available to the receiver (i.e. include the SpacingBetweenSlices attribute).
    Add a mechanism for a user to pass a 3D numpy array with an affine matrix to the constructor and have it stored as a "3D" segmentation.
    Add a mechanism to determine whether a received segmentation is "3D", either using the DimensionOrganizationType, or if it is not present, by performing the required calculations on the metadata. If it is a volume, provide the user with a mechanism to access the affine matrix of the array, and retrieve a 3D numpy array of the segmentation with frames correctly sorted to match the affine matrix.
    Hopefully work with the slicer team to prototype integrating this into slicer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Implementation in highdicom of checks to determine when a segmentation is a "volume" and populate optional metadata accordingly
2.  Implementation in highdicom of mechanism to retrieve a spatially-sorted volumetric segmentation, along with its affine matrix, in a consistent way regardless of the way that the segmentation file is laid out.
3.  Discuss and determine with DICOM experts and other interested parties whether changes to the DICOM standard may have a part to play in addressing some of the issues outlined above.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Implement a PR to highdicom library to address the points above
2.  Hold a meeting with relevant investigators (and anyone else interested) to decide on next steps (if any) regarding the standard

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

### Changes To `highdicom` Library

See the associated [pull request](https://github.com/ImagingDataCommons/highdicom/pull/277) (currently a work in progress as a draft PR).

### Changes to the DICOM Standard

After discussing with @dclunie and @pieper, we have agreed that a correction proposal shall be drafted by @dclunie as a next step. Here are my notes on what this could include:

- Define DimensionOrganizationType value of “OTHER”. This will allow a receiver to know for sure that the image is *not* 3D (as opposed to simply not having the DimensionOrganizationType). Should this be “IRREGULAR” or something else?
- Precisely define what is meant by DimensionOrganizationType of “3D” in the case of the patient coordinate system:
    - All planes have the same ImageOrientationPatient. The ImageOrientationPatient shall be factored out into the SharedFunctionalGroupsSequence (and not appear in the PerFramesFunctionalGroupsSequence).
   - Planes shall be regularly spaced. The SpacingBetweenSlices must be found in the PixelMeasuresSequences within the SharedFunctionalGroups. All other pixel measures must also be shared between all frames.
   - ImageOrientationPatient values shall follow the following rules (using numpy-like indexing):

     ImagePositionPatient[n+1] = ImagePositionPatient[n] + SpacingBetweenSlices * NormalVector

     Where NormalVector is a unit vector found as the vector cross product of the two direction cosines:

     NormalVector = ImageOrientationPatient[:3] x ImageOrientationPatient[3:]

     Note that this does imply that only one of the two possible ordering of planes is valid.

   -	ImagePositionPatient must be used as the only dimension index.

Notes:
- The above DOES NOT allow for the creation of BINARY Segmentations with more than one segment, since the Referenced Segment Number would need to be included as a further dimension index and there would need to be further sets of frames for each segment, which would break the strict spatial ordering. We currently feel that this is okay given that we hope that LABELMAP will become the dominant segmentation, and allowing no further dimensions considerably simplifies things.
- If we are precisely defining "3D" for the patient coordinate system, we should probably give "3D_TEMPORAL" the same treatment. Presumably this would be as above, except that there would some standardized time dimension index too, and a specified ordering of frames along the two dimensions (3d position + time).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
