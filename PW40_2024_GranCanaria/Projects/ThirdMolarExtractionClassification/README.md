---
layout: pw40-project

permalink: /:path/

project_title: Third molar extraction classification
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Roberto Veraldi
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Amerigo Giudice
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Maria Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The classification of third molar extraction is a key factor in oral surgery. Developing a deep learning model to classify the difficulty score of extraction would be useful for surgeons and dentists.
This project aims to create a Slicer module that allows clinicians to obtain an extraction-difficulty grade by providing just the patient CT.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

To expose an already developed deep learning classifier in Slicer.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Identification of optimal classification parameters
2.  Expose weights into Slicer
3.  Generate extension

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

Done during this week:
1.  Obtained pth file with the model for deep learning classification.
2.  Implemented module extention in Slicer.
3.  Tested if the same label obtained in testing was the same that appeared in output in Slicer.

Future steps:
1.  Integrating weight files for the specific classification (maybe giving to the clinicians the possibility to download locally the right weights for their specific tasks).
2.  Specify what label score means.
3.  Other modifications for a general usage of the extention.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
<video
   autoplay muted loop
   src="https://github.com/NA-MIC/ProjectWeek/assets/112720518/b3aa2ef6-223c-4155-a0b5-d12a0b6b30d6"
   style="width:1000px">
</video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
1. GitHub Project Page: https://github.com/robsver/3DSlicerClassificator 
2. Classification score table for third molar extraction: Juodzbalys, Gintaras, and Povilas Daugela. "Mandibular third molar impaction: review of literature and a proposal of a classification." Journal of oral & maxillofacial research 4.2 (2013).
