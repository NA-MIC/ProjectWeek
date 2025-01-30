---
layout: pw42-project

permalink: /:path/

project_title: 'MorphoDepot: Collaborative segmentation projects '
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Murat Maga
  affiliation: Seattle Children's
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: Inc., USA

- name: Andrey Fedorov
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

We are developing tools for segmentation of biological specimens (e.g. 3D microCT of fish or snakes).  The idea is that a Lab Director will define a project, such as what scan to segment, what anatomical structures to segment, the terminologies to use, etc.  Students or lab members would be assigned to segment subsets of the data.  We want to leverage existing data management tools, such as github for organizing issues and contributions, and jetstream2 for hosting data and computation.

There is a presentation about the ideas here: [https://morphocloud.github.io/MorphoDepotDocs/](https://morphocloud.github.io/MorphoDepotDocs/)

And there is an existing extension here: [https://github.com/MorphoCloud/SlicerMorphoDepot](https://github.com/MorphoCloud/SlicerMorphoDepot)

We are interested in facilitating collaborative segmentation, including dividing a whole project into tasks, managing allocation to tasks to segmenters, managing/merging contributions, etc. 

If you are interested in similar topics, please join our project!


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Networking: we would like to know how this fits with anyone else's projects and possibly collaborate
2. Talk with developers who are improving the terminologies and color modules about how to better structure our segmentations
3. Harden the infrastructure for Mac/Windows (install gh cli for users).
4. Work on MorphoDepotAccession module to make it easier to create segmentation task repositories (design ideas are here: https://github.com/MorphoCloud/SlicerMorphoDepot/issues/10)
5. Explore how to improve the GH tasks efficiency as querying through tags to find repos, issues and PRs can be slow and may not scale. 
6. Bonus: if time brainstorm tools for comparing segmentations / reviewing and merging segmentations from team members more effectively.
7. Extra Bonus: Come up with plans on how to use collaboratively segmented datasets to train AI models (and iteratively refine them)

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Define/create a JSON schema for the mandatory metadata for each MorphoDepot archive. These should include specimen metadata, and some key imaging metadata.
2. Explore how to create a staging area for data donors to upload their scenes (volume + segmentation, if exists) to be reviewed by MorphoDepot team (quality control, metadata check, etc).
   

## Progress and Next Steps
1. Extension is fully functional and has been used in classroom with multiple users for basic segmentation tasks. (e.g., go to https://github.com/muratmaga/pinecone/issues and open an issue for yourself to test).
2. Implement the MorphoDepotAccession

### During Project Week
* Chance to discuss MorpoDepot with the wider community and meet with our research group (Murat, Steve, and Jc)
* Agreement that Accession module will include the following technologies:
    * A Slicer module that relies on the `gh` github command line tool to simplify accessioning data
    * Use a JSON Schema to define accession metadata and create UI form: https://pieper.github.io/sites/schemaform/
    * Use the new colortable with coded concepts infrastructure to define the segmentation to be performed on the specimen
    * Create a service that will allow uploading of volume data of the specimen that is already in Slicer to an s3 bucket in zarr format by allocating a [presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) only to people whose github account has been previously approved as a MorphoDepot contributor.
    * Then create a github repo for the specimen that includes the color table and the URL to the zarr bucket for use with the MorphoDepot system.  The repo will be based on a repository template that has the correct setting, like the MorpoDepot label and other properties.


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![image](https://github.com/user-attachments/assets/09f94c3d-9d7c-4688-b9b4-f4d7b70a8e65)

MorphoDepot module lists pending issues assigned to this user and allows you to load/segment/commit them and then request review.

![image](https://github.com/user-attachments/assets/2d81e4f3-8d8b-49e4-97f4-f906053d375f)

MorphoDepotReview module lists pending pull requests and allows PI to accept edits or request changes.

![image](https://github.com/user-attachments/assets/9481ce0f-dc37-4900-9cdc-14bb0922df59)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Previous Project Week work:
* [https://projectweek.na-mic.org/PW41_2024_MIT/Projects/MorphodepotCollaborativeSegmentationProjects/](https://projectweek.na-mic.org/PW41_2024_MIT/Projects/MorphodepotCollaborativeSegmentationProjects/)
