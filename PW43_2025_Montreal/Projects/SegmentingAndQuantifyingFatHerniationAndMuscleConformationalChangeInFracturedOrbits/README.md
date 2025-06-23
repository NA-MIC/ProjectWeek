---
layout: pw43-project

permalink: /:path/

project_title: 'Segmenting and quantifying fat herniation and muscle conformational change in fractured
  orbits '
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M College of Dentistry

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Segmentation of orbital soft tissue and bones are difficult because the structures are small and thin, boundaries of muscles, nerves, and fat tissue are not clear and highly sensitive to the quality of CT images. Orbital fracture poses unique challenges due to conditions including orbital floors and medial walls cracking like egg shells, muscle conformations and size changes (e.g., entrapment), altered globe positions (e.g., enophthalmos), and orbital fat and soft tissue herniation into sinuses. 

Manual segmentation is very time consuming and requires a high level of understanding of radiology and anatomy. Therefore, it is difficult to recruit enough labor to prepare for the ground truth and training dataset.

TotalSegmentator is the only ready-to-use module that incorporate segmenting extraocular muscles. However, there is no citation and validation of the accuracy. The literatures are also scarce. and virtually no study focuses on multi-structure segmentation for the fractured orbit.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Find a repeatable solution to manual segmenting orbital soft tissue for ground truth, particularly fractured orbit. 
2. Find a repeatable way to determine the anterior boundary of orbital fat, which usually continuous with the eyelid and is blurred. Accurately quantifying orbital fat volume has its clinical significance for inferring trauma, herniation, inflammation, etc. Retracting orbital fat is also critical in orbital fracture repair.
3. Find a repeatable way to represent thin orbital floor, which is sometimes only marked by the boundary between maxillary sinus & orbital soft tissue.
4. Initially deep learning segmentation training by incorporating fractured orbit to augment the training dataset. Locating open-source images of good orbital scans.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. For extraocular muscles, perhaps first focus on muscles that usually show changes (e.g., entrapment, enlargement, etc.) associated with fractures, such as medial & inferior rectus.
2. Currently using grow from seeds to segment overall soft tissue and herniation. Extraocular muscles retouched from TotalSegmentator results. Orbital fat is from using overall orbital content subtract the extraocular muscles and the globe.




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

