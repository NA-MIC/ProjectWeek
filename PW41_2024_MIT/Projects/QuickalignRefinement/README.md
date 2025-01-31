---
layout: pw41-project

permalink: /:path/

project_title: QuickAlign Refinement
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Sara Rolfe
  affiliation: SCRI
  country: USA

- name: Murat Maga
  affiliation: SCRI
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


QuickAlign is a SlicerMorph module used to temporarily fix alignment in two 3D viewers. The user aligns the view in each viewer and then applies the linking. If the nodes are Markups, then joint editing of the point lists can be enabled. We plan to make usability improvements.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Address of issue object size/zoom
2. Assess implementations for transforming multiple nodes in scene
3. Discuss whether this may be a useful feature outside SlicerMorph




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop plan for correcting for object size/zoom
3. Discuss alternate implementations using camera transforms



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Implemented and tested alternative methods based on (a) camera event updates from camera instead of 3D view linking and (b) transforming the camera instead of the linked nodes.
2. Identified a more robust solution where camera positions are tracked and updated on interaction events applying a transform. This is likely the best solution if the feature will be integrated in the core and will support alignment of views with multiple nodes. Refer to Endoscopy and ViewPoint examples for camera update.
3. Identified a short-term solution for the SlicerMorph extension where an approximate zoom factor is calculated from the initial camera parameters and object position, then applied as a scaling factor to the aligned object node. The scale factor could be provided as a slider in the QuickAlign module so the zoom could be adjusted both jointly (in the scene) and independently (via the scaling factor).
4. [Zoom-factor solution](https://github.com/SlicerMorph/SlicerMorph/tree/QuickAlignRefinement) pushed to SlicerMorph repo for testing


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="866" alt="quickAlignedSkulls" src="https://github.com/NA-MIC/ProjectWeek/assets/43060230/95933056-1662-41ec-8992-0002720eb7bf">
<img width="1319" alt="unalignedSkulls" src="https://github.com/NA-MIC/ProjectWeek/assets/43060230/68d333ea-309d-4025-bf68-7bee7adf350d">






# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[Endoscopy example](https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L1080)

[ViewPoint example](https://github.com/SlicerIGT/SlicerIGT/blob/master/Viewpoint/Viewpoint.py)
