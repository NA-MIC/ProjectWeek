---
layout: pw44-project

permalink: /:path/

project_title: Hands-on tutorials extension
category: IGT and Training
presenter_location: 

key_investigators:

- name: Alejandro Rodríguez Moreno
  affiliation: Ebatinca SL
  country: Spain

- name: Csaba Pinter
  affiliation: Ebatinca SL
  country: Spain

- name: Interested people welcome!
  affiliation: Andriy
  country: Tina, Andras?

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Unfortunately the issue of useful and up-to-date tutorials is quite difficult, because
- Slide-based tutorials need to be updated manually (see that many tutorials are pre-5.0 in the [training material](https://training.slicer.org))
- Video tutorials are impossible to update
- In the above two cases it is next to impossible to offer them in different languages
- In-repo markdown files are quite limited in format and usefulness

We have developed a tutorials infrastructure and some basic tutorials for a commercial project, which could be repurposed for Slicer core. Basically it consists of a curriculum that is described by a JSON file, with dependencies among the tutorials, and a set of hands-on tutorials that can be started from this home screen.

The hands-on tutorials guide the users through a certan sequence of steps using targeted tooltips and a mechanism detecting if the current step has been completed successfully. This way we could offer some basic tutorials for Slicer core in multiple languages, which is easier to maintain than the current modalities. Of course maintenance will remain an issue, because if API changes the tutorials will break, but the basic functions of Slicer has not really changed in the last decade, and hopefully there won't be much maintenance necessary.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A: Reach a common understanding about the necessity of this in general
2. Objective B: Get started with the extension



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Discuss the proposal, hopefully in a breakout session, but in any case involving the interested people
    a. Decide if the basics are sensible, feasible, and useful, or not
    b. Define an initial set of tutorials
2. Start to adapt the tutorials infrastructure to the proposed goals



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="1642" height="595" alt="Image" src="https://github.com/user-attachments/assets/92e1aa2e-c6ab-4ed5-affc-285a2336cb72" />
Part of the curriculum tree in the commercial app that we propose to adapt to Slicer core



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* The commercial app in question: https://ebatinca.com/productos/start
* The current training material for Slicer core: https://training.slicer.org/

