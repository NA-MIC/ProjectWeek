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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

