---
layout: pw39-project

permalink: /:path/

project_title: Docker based system to assess challenge submissions
category: Infrastructure
presenter_location: Online

key_investigators:

- name: Roya Khajavibajestani
  affiliation: Brigham and women’s hospital
  country: USA
  
- name: Erik Ziegler
  affiliation: Yunu
  country: Netherland
  
- name: Ron Kikinis
  affiliation: Harvard Medical School
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Project Description:

Our project is focused on developing a Docker-based submission mechanism for challenge participant. To maintain fairness and make sure that the test set is not used in the training process, the test set will not be released to the participants. Instead, participants will be required to containerize their methods using Docker and submit their Docker containers for evaluation.

Docker provides an excellent solution for running algorithms in isolated environments known as containers. In our project, we will leverage Docker to create a container that replicates the participants' pipeline requirements and executes their inference script. By encapsulating the entire environment within a container, we can ensure consistent execution and reproducibility.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Create a sample docker container for submission
Create an evaluation mechanism on the challenge website
Create documentation, guidelines, and tutorial for participants

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

Design the docker container, input/output mechanism, requirements, and methods to perform inference using a subset of the validation set.
Create an evaluation mechanism on the challenge website
Create a sample submission docker for the test phase and test it on the challenge website
Create documentation to publish in phase 2 of the challenge.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
