---
layout: pw44-project

permalink: /:path/

project_title: Revisit RawImageGuess extension
category: Infrastructure
presenter_location: 

key_investigators:

- name: Attila Nagy
  affiliation: University of Szeged
  country: Hungary

- name: Csaba Pintér
  affiliation: EBATINCA
  country: Spain

- name: Andras Lasso
  affiliation: Queen's
  country: Canada

- name: Steve Pieper
  affiliation: Isomics Inc
  country: Cambridge

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We created this extension not too long ago.
By using this extension you can find out the parameters of work file types and formats that Slicer doesn't handle out of the box. This way you can create an .nhdr with the parameters of the images(series), and then load them into Slicer.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Would like to collect use cases, refinement suggestions and new ideas.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Collect use cases, refinement suggestions and new ideas.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Ruined the original functionality :D
2. Began to implement new ideas an experiment with them. One is a 
3. Tried one, but didn't really work out as expected. It is a row continuity heuristic (super cheap, super effective)
Natural images (medical, microscopy, industrial) have strong horizontal continuity.
For a guessed X:
Interpret raw data as 1D array
Split into rows of length X
Compute:
mean(|row[i] - row[i+1]|)
Do this for several rows.
Maybe needs some refinement.

The implementation of further ideas is coming.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



<img width="1920" height="1030" alt="RawImageGuess_enh_1" src="https://github.com/user-attachments/assets/fed718c2-cf5e-4888-a136-fd898548d2b9" />

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Project week from 2018:
https://projectweek.na-mic.org/PW28_2018_GranCanaria/Projects/RawImageGuess/

And 2019:
https://projectweek.na-mic.org/PW30_2019_GranCanaria/Projects/RawImageGuess/

