---
layout: pw40-project

permalink: /:path/

project_title: Advancing SlicerHub - open issues and vision as part of a virtual hospital
category: Cloud / Web
presenter_location: Online

key_investigators:
- name: Rafael Nebot Medina
  affiliation: Instituto Tecnológico de Canarias (ITC)
  country: Spain

- name: Juan Ruiz Alzola
  affiliation: Universidad de Las Palmas de Gran Canaria

- name: Paula Moreno Fajardo
  affiliation: ITC

---

# Project Description

From the experience of developing SlicerHub (present at 38th edition of NA-MIC) within OpenDx28 project, using Teide HPC infrastructure, open issues and future vision should be discussed to 
define work for the forthcoming project, the Virtual Hospital.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Talk with experts present at the workshop to gather information to formulate possible solutions to having multiple Kubernetes pods using OpenGL in the same node.
2. Open discussion to define and take note of vision and specific desirable features of having SlicerHub in a virtual hospital. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Showcase the current implementation to interested people.
2. Explain the issues. Specially focus on executing Slicer multiple times in the same Kuberntes node.
3. Take note of possible approaches or solutions for the issues.
4. Explain ideas for SlicerHub in the Virtual Hospital to interested people. From resource profiles, to preconfigured sessiones, etc.
5. Document new ideas or modify existing ones.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- OpenDx28 project, just finished, allowed to experiment in deployment and integration of services related to health. OpenDx28 Github organization is at [https://github.com/OpenDx28](https://github.com/OpenDx28)
- The specific repository for SlicerHub at [https://github.com/OpenDx28/3dslicerhub](https://github.com/OpenDx28/3dslicerhub)
- The Docker image spawned by SlicerHub at [https://github.com/OpenDx28/docker-slicer](https://github.com/OpenDx28/docker-slicer)
- This image depends on another, at [(https://github.com/OpenDx28/docker-vnc-base](https://github.com/OpenDx28/docker-vnc-base)
