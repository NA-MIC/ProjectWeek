---
layout: pw40-project

permalink: /:path/

project_title: MR Image Normalization
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Michela Destito
  affiliation: University Magna Graecia of Catanzaro
  country: Italy

- name: Paolo Zaffino
  affiliation: University Magna Graecia of Catanzaro
  country: Italy

- name: Maria Francesca Spadea
  affiliation: Institute of Biomedical Engineering
  country: KIT - Karlsruher Institut für Technologie, Germany

- name: Petros Koutsouvelis
  affiliation: Maastricht University
  country: Netherlands
---

# Project Description

<!-- Add a short paragraph describing the project. -->

A key step in medical image processing, particularly in MRI images, is normalization of gray level intensities. This normalization is important to ensure that images have a consistent intensity scale, facilitating any future analysis. The purpose is to create a targeted extension for normalization of MR images in Slicer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

*   The aim of the project will be to provide an extension to normalize the intensities of MRI images
*   It will be possible to choose different normalization methods.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Create an extension in which three normalization methods can be chosen: Zscore, WhiteStripe and Nyul.
2.  To be able to compare the different gray levels of images normalized by multiple methods.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. In this week I created the Extension for Normalization MRI Images with three normalization methods.
2. In the created extension you can choose which method to use.
3. Considering the first two proposed methods (Z-score and WhiteStripe) only the MRI image needs to be loaded and is normalized.
4. Considering the third method (Nyul) one must load in addition to the image to be Normalized, the MRI dataset and only then is the image normalized.
5. Future developments will be to implement new normalization methods proposed in the literature.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
<video
   autoplay muted loop
   src="https://github.com/NA-MIC/ProjectWeek/assets/77610678/5bb87958-e7b0-4252-9d91-29e74fd91be6"
   style="width:1000px">
</video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. https://github.com/Micheladestito/ImageNormalizationSlicer
2. https://github.com/jcreinhold/intensity-normalization
