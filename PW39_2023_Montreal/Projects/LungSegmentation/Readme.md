---
layout: pw39-project

project_title: 3D Slicer Lung CT Segmentation and Analysis
category: Segmentation / Classification / Landmarking

key_investigators:
- name: Rudolf Bumm
  affiliation: KSGR
  country: Germany

- name: Steve Pieper
  affiliation: Isomics
  country: USA
  
- name: Andras Lasso
  affiliation: Queens University
  country: Canada
---

# Project Description

<!-- Add a short paragraph describing the project. -->
This is a follow-up to previous 3D Slicer lung CT segmentation PW projects. 


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
Our objective is to improve the LungCTAnalysis extenion Analysis in 3D Slicer.

- Improve vessel segmentation
- Implement emphysema and COPD analysis
- Develop a better concept for lung segment (sublobar) segmentation in 3D Slicer
- Fine-tune the workflow for surgical planning
- Work on current publication

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

The development of the extension has slowed down due to the lack of ideas how to handle vessel and subsegmental structure segmentation that would be crucial for surgical planning. 
To many it seems that the main limitation of the computational method it is highly sensitive to the chosen threshold values. This is indicated that just the small variance between well calibrated clinical CTs could cause measurable differences in the end result in about 20-30% of the cases. Probably the root cause of the problem is that thresholding with a hard value makes the classification very sensitive to the chosen threshold value. Andras Lasso suggested to reduce this sensitivity by using soft classifiers.

GPT-4 reponse: 
    It's correct that one of the limitations of thresholding methods in image processing is their sensitivity to the choice of threshold values. This is particularly problematic in medical imaging, where subtle variations in pixel values can make significant differences in diagnosis and treatment planning. 

    The issue with hard thresholding is that it treats every pixel above a certain value the same way, without considering the context or the distribution of values in the image. A pixel just above the threshold is treated the same as a pixel far above the threshold, which can lead to inaccuracies.

    Using a soft classifier, as you suggest, could be a good way to reduce this sensitivity. Soft classifiers do not make absolute decisions like hard classifiers. Instead, they provide a degree of membership, allowing a more flexible classification.

    For example, in fuzzy logic-based image processing, pixels can belong to multiple classes with varying degrees of membership. This is more in line with how a human expert might interpret a CT scan, recognizing that some areas may not clearly belong to just one category.

    A popular soft classifier is the Fuzzy C-Means (FCM) clustering algorithm, which can be used to segment an image into different classes, each representing a different tissue type. FCM is a method of clustering which allows one piece of data to belong to two or more clusters with a certain degree of membership. In the case of Lung CT images, it can be used to classify normally ventilated, infiltrated, and collapsed lung parenchyma as well as areas of emphysema.

    Another approach might be to use machine learning methods, such as convolutional neural networks (CNNs). These algorithms can learn to classify images based on a training set of labeled examples, potentially providing a more nuanced and accurate classification. They can also learn to incorporate spatial information, considering the context of each pixel in making the classification.

    Remember, these techniques may not be straightforward to implement and would require sufficient domain knowledge in image processing and machine learning. It's also worth mentioning that the accuracy of soft classifiers greatly depends on the quality and representativeness of the training data. The algorithm's performance should be rigorously evaluated using a validation dataset before clinical deployment.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->









