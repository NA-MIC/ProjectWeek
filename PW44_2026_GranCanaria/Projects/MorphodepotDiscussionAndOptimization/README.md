---
layout: pw44-project

permalink: /:path/

project_title: MorphoDepot discussion and optimization
category: Infrastructure
presenter_location: 

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Murat Maga
  affiliation: Seattle Children's
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


As part of the [MorphoCloud](https://morphocloud.org/) project, we have developed a [MorphoDepot](https://github.com/MorphoCloud/SlicerMorphoDepot), as 3D Slicer extension that is already available and in use.

The goals are to help organize work related to 3D imaging, primarily for biological morphology applications.  Initial target is segmentation of microCT scans of animals. In the future it could expand to applications like landmarking and other annotation / analysis tasks.

The extension relies heavily on GitHub as the back-end, with each scan being associated with a repository, and segmentation tasks being managed by issues and pull requests. The system is working and is in the early stages of real-world usage and we are collecting feedback about usability.

The system uses the Github CLI, gh, to interact with Github but has some performance issues and sometimes the API is throttled due to quota restrictions.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Make the Project Week community aware of this extension
2. Gather feedback about possible other use cases for similar technology and explore possible collaborations
3. Get ideas about how to improve performance to scale up to more users and repositories.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


* Give demos to any interested parties
* Discuss github actions and other ways to optimize the gh data process 



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

