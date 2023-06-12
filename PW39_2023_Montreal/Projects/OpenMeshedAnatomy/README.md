---
layout: pw39-project

permalink: /:path/

project_title: Open Meshed Anatomy
category: Segmentation and Visualisation
presenter_location: In-person

key_investigators:
- name: Andy Huynh
  affiliation: The University of Western Australia
  country: Australia
  
- name: Michael Halle
  affiliation: Surgical Planning Lab (SPL)
  country: United States

- name: Benjamin Zwick
  affiliation: The University of Western Australia
  country: Australia

---

# Project Description

Open Meshed Anatomy (OMA) is a PhD project, in collaboration with the [Open Anatomy Project](https://www.openanatomy.org/) (OAP), aiming to facilitate and improve computational simulations of human body parts using free and open atlases available from OAP. By leveraging these existing segmented and labeled atlases, OMA streamlines the creation of computational grids/meshes for researchers and integrates valuable spatial anatomy information for a better understanding and visualization of simulation results. Similar to OAP's goals, the project will offer these resources and visualization tools via an open web platform or 3D Slicer, fostering global collaboration and research among the scientific community.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Determine the optimal way to assign labels to mesh elements/nodes describing structural names from the atlas.

2. Objective B. Improve SlicerAtlasEditor functionalities and merge to SlicerOpenAnatomy extension. Refer to Figure 1 and 2.

3. Objective C. Implement contextual visualisation of results from computational simulations. Refer to Figure 3.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Objective A:
1. What file extension to use (e.g. VTK?) or to use external file.
2. Labelling via tags for better querying functionalities (Mike Halle's idea)

Objective B:
1. Add option to download via URL the different atlas label maps that Open Anatomy Project offers, including its hierarchy structure json files within 3D Slicer or extension.
2. Fix non-manifold/corrupt labeled voxels in the label map. This will be useful for generating a clean surface mesh for visualization or volumetric meshing. Refer to Figure 2.

Objective C:
1. Have options to query different computational results based on different anatomy (from atlas). This may be done via tags or using the structure json files. Refer to Figure 3.
2. Use [SlicerCBM](https://github.com/SlicerCBM/SlicerCBM) as a sample application of this.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
-->

![Simplifying Open Anatomy Project's Brain Atlas to ROI](https://github.com/andy9t7/SlicerAtlasEditor/blob/main/img/merge-roi.png?raw=true)
**Figure 1: Simplifying Open Anatomy Project's Brain Atlas to ROI using SlicerAtlasEditor**

![Fixing non-manifold voxels in atlas label map](https://github.com/andy9t7/SlicerAtlasEditor/blob/main/img/fix-non-manifolds.png?raw=true)
**Figure 2: Fixing non-manifold voxels in atlas label map. [1]**

![Query and visualize simulation results](https://github.com/andy9t7/SlicerAtlasEditor/blob/main/img/query-and-visualise.png?raw=true)
**Figure 3: Query and visualize simulation results on ROI**

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

The Open Anatomy Project website: https://www.openanatomy.org/.  
Open Anatomy Project's Brain Atlas: https://github.com/mhalle/spl-brain-atlas.  
SlicerOpenAnatomy: https://github.com/PerkLab/SlicerOpenAnatomy.  
SlicerAtlasEditor: https://github.com/andy9t7/SlicerAtlasEditor.  
SlicerCBM: https://github.com/SlicerCBM/SlicerCBM.  

[1] S. J. Owen, M. L. Staten, and M. C. Sorensen, “Parallel hexahedral meshing from volume fractions,” _Engineering with Computers_, vol. 30, no. 3, pp. 301–313, Jul. 2014, doi: [10.1007/s00366-012-0292-8](https://doi.org/10.1007/s00366-012-0292-8).
