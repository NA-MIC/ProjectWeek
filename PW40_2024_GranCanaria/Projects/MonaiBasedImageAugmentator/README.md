---
layout: pw40-project

permalink: /:path/

project_title: MONAI based image augmentator
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Ciro Benito, Raggio
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Paolo, Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Maria Francesca, Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

MONAI and PyTorch based medical image augmentation tool that can be integrated in Slicer.
The project aims to be a low-code version of the tool: <https://github.com/ciroraggio/AugmentedDataLoader>.

It's designed to operate on a dataset of medical images and apply a series of specific transformations to each image. This process augments the original dataset, providing a greater variety of samples for training deep learning models.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Creating an intuitive graphic interface for the module
2.  Parallelising the augmentation process to optimally utilise resources

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Create the extension
2.  Implement the augmentation process
3.  Try to parallelise the process so that it takes as little time as possible on large data sets

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Implemented graphic interface for loading images and masks, choosing transformations and saving images.
2.  Implemented and tested MONAI spatial transformations such as Rotation, RandRotation, Flip, Resize.
3.  Partially implemented input validation and MONAI intensity transformations, it will be completed in the future.
4.  Partially implemented "Preview" feature, which allows the output of transformations to be viewed directly in the scene before saving them in the OS, will be completed in the future.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![main](https://github.com/NA-MIC/ProjectWeek/assets/96300975/4f8e8daf-88e2-483b-9849-e19899fb9260)
![filled](https://github.com/NA-MIC/ProjectWeek/assets/96300975/cc595232-fb44-4ff3-84eb-4a5ef52ec10c)

Files are saved as follows:
![output_folder](https://github.com/NA-MIC/ProjectWeek/assets/96300975/f69f0408-d680-4e60-8675-dfac3e0ac5ed)

Example of image after transformation in the scene:
![output_scene](https://github.com/NA-MIC/ProjectWeek/assets/96300975/4a06470e-8a1a-4b6b-87ed-82913aecc528)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
GitHub Project: <https://github.com/ciroraggio/SlicerAugmentator>
