---
layout: pw44-project

permalink: /:path/

project_title: Defacing head and neck CT scans while preserving lymph nodes
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: Inc., USA

- name: Ron Kikinis
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


For the Lymph Node Quantification project we want to analyze and share head and neck scans but don't want to share PHI.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Use generic segmentation tools (CADS, SuperSynth, etc.)
2. Identify facial feature landmarks.  Find existing models or examples that identify features like corners of eyes and mouth
3. Figure out which features can be reliably detected that define a reasonable identity removal but leaving the nodes in the cheeks and jaw
4. Decide what bluring or removal to do in the identified face area



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


* Figure out if existing MR defacing tools can be used for this, perhaps by mapping the CT to MR
* Explore the state of the art in [Facial animation systems](https://research.nvidia.com/labs/amri/projects/gaia/)
* A more recent paper referencing the Milchenko paper [Deidentification of CT head images](https://pmc.ncbi.nlm.nih.gov/articles/PMC10406725/pdf/12021_2023_Article_9631.pdf)


## Progress and Next Steps

* Created mockups of the areas to be obscured
* Discussed the core issues with several project week attendees (Thank you Andras, David, Alexandra!)
* Created plan to test the nnU-Net based landmark detection system on the lymph node preserving face and ear definition
    * Help test the new extension on private data
* Test existing public data on David's Zenta defacing model for CT data
* Consider a custom version of Zenta's model that preserves lymph nodes (submandibular and submental)
  
### Mockups

### Area to be defaced

* Closed curve snapped to model surface

<img width="1008" height="377" alt="image" src="https://github.com/user-attachments/assets/bb1f2597-e68e-416f-a87f-619629f95674" />

* Dynamic modeling applied to suface wrap solidfy model

<img width="440" height="476" alt="image" src="https://github.com/user-attachments/assets/95876794-4d8e-414b-8e9e-f9361d6fe97a" />

* Facial blur

<img width="798" height="508" alt="image" src="https://github.com/user-attachments/assets/b3c02fc2-2d83-4b3d-b2ce-e89b3186f67a" />

* Extra blur

<img width="677" height="481" alt="image" src="https://github.com/user-attachments/assets/acb70748-22ba-45fd-a85e-954d9ac39d9c" />


### Open Questions

* What are the state-of-the-art definitions for facial deidentitication and how do they intersect with our requirements?
* What primitives exist in the Slicer ecosystem that can be used as building blocks, such as landmark detection, image manipulation, and segmentation to make a robust pipeline.
* Can we use exising infrastructure or is it better to build something custom.





# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="500" height="349" alt="Image" src="https://github.com/user-attachments/assets/b93bf4ce-485d-46c6-af8b-bda41197eb1b" />

We will use the [CTHead](https://drive.google.com/file/d/1a0tt9_Uu7whrYs2VKbBezwKi7gJGG823/view?usp=sharing) sample data for experiments.

<img width="1005" height="904" alt="image" src="https://github.com/user-attachments/assets/86c88b58-2874-435f-90ef-111bb53fb808" />


# Background and References



* [Facial lymph nodes - Wikipedia](https://en.wikipedia.org/wiki/Facial_lymph_nodes)
* [Paper describing defacing by adding variable thickness epidermis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3538950/pdf/nihms407349.pdf)

## Inspirations

### "Phantom of the Opera" deidentification:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/9cf6fd85-43c6-4e12-9de7-a7ded3f9c485" />

### "Venetian Masquerade" deidentification:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/c7aad156-f783-47bb-8e3a-125bbb1edb97" />

### "Traditional medical publication" deidentification:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/f6d69bb7-3356-4334-813b-e6eea7862bb4" />






