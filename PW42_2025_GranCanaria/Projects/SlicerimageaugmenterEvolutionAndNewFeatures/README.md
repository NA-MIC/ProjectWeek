---
layout: pw42-project

permalink: /:path/

project_title: 'SlicerImageAugmenter : evolution and new features'
category: Quantification and Computation

key_investigators:

- name: Ciro Benito Raggio
  affiliation: Karlsruhe Institute of Technology
  country: Germany

- name: Paolo Zaffino
  affiliation: Magna Græcia University of Catanzaro
  country: Italy

- name: Maria Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


[ImageAugmenter](https://github.com/ciroraggio/SlicerImageAugmenter) is a 3D Slicer extension that provides a simple interface to apply over 20 simultaneous MONAI transforms (spatial, intensity, etc.) to medical image datasets without programming. 

It makes medical image augmentation more accessible, allowing a wider range of users to improve the performance of DL models in medical image analysis by increasing the number of samples available for training. 

Since the extension is officially available in the Extension Manager since version 5.7.0 (current Preview Release), the idea is to fix known bugs, improve various aspects and add new features before the extension will be available in the stable release of 3D Slicer.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Faster loading of the interface on first start
2. Improve error handling and view management of 3D Slicer
3. Improving the application of some transformations
4. Possibility to select the sample to be used for the preview function
5. Make the community aware of the extension and release it in the stable release of 3D Slicer



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Check all GUI components and/or dynamically load some components
2. Better handling of generic exceptions by preventing the interface from crashing and requiring a manual restart
3. Analyze MONAI documentation regarding available transformations for better interpretation of parameters 
4. Added a drop-down menu in preview mode to select the sample to which the selected transformations will be applied and previewed
5. Networking with other people during the PW



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


- [SlicerImageAugmenter Repository](https://github.com/ciroraggio/SlicerImageAugmenter)
- [SlicerImageAugmenter Journal Article - Software X, Volume 28, December 2024](https://doi.org/10.1016/j.softx.2024.101923)
- [SlicerImageAugmenter Website](https://ciroraggio.github.io/SlicerImageAugmenter/)

