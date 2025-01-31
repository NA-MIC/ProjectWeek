---
layout: pw41-project

permalink: /:path/

project_title: 'MorphoDepot: Collaborative segmentation projects '
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: Inc., USA

- name: Murat Maga
  affiliation: Seattle Children's
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We are developing tools for segmentation of biological specimens (e.g. 3D microCT of fish or snakes).  The idea is that a Lab Director will define a project, such as what scan to segment, what anatomical structures to segment, the terminologies to use, etc.  Students or lab members would be assigned to segment subsets of the data.  We want to leverage existing data management tools, such as github for organizing issues and contributions, and jetstream2 for hosting data and computation.

We are interested in facilitating collaborative segmentation, including dividing a whole project into tasks, managing allocation to tasks to segmenters, managing/merging contributions, etc.

If you are interested in similar topics, please join our project!



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Networking: we would like to know how this fits with anyone else's projects and possibly collaborate
2. Exploration: test the use of github for managing segmentations and zarr with s3 back end for large data
3. Refine: based on what we learn, iterate on the concepts and implementation options



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Try [zarr on ceph in jetstream2](https://www.zonca.dev/posts/2022-04-04-zarr_jetstream2) and [zarr in Slicer](https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a).
2. Try storing seg.nrrd files in github repos
3. Try skeleton Slicer module




## Progress and Next Steps

1. Talked with several other project week participants about common interests in collaborative segmentation but did not learn of any existing work that we can build on directly.  A more common use case is large number of similar cases divided among annotators rather than annotators all working on a single large scan.
2. Confirmed that all packages are working correctly in Slicer
    1. git: confirmed that it's possible to create a git repo and commit seg.nrrd files from Slicer python
    2. github: confirmed that operations like creating pull requests can be done from Slicer python
    3. ome_zarr: can save any volume in zarr format (with pyramid), can also load, but slowly
    4. s5cmd: can be used to transfer data to/from s3-compatible buckets on Jetstream2 (ceph object store running in openstack)
    5. tensorstore: can load zarr from s3-compatible buckets very quickly
3. Tested performance on a Jetstream VM:
    1. Load volume (2110 x 677 x 666, 1.8 GB) from JS2 object store in about 5 seconds
    2. Same code works on non-JS2 machines, but more slowly



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

Experiments: [https://github.com/pieper/SlicerMorphoDepot/tree/main/Experiments](https://github.com/pieper/SlicerMorphoDepot/tree/main/Experiments)
