---
layout: pw40-project

permalink: /:path/

project_title: 'Mauritanian Project '
category: Other
presenter_location: In-person

key_investigators:

- name: Ahmedou Moulaye IDRISS
  affiliation: Faculté de médecine de Nouakchott
  country: Université de Nouakchott, Mauritania

- name: Sonia Pujol
  affiliation: Brigham and Women’s Hospital and Harvard Medical School
  country: USA

- name: Fatimetou Mohamed-Saleck
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

- name: Moustapha Mohamed Saleck
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

- name: Mohamed Mahmoud Septy Mohamed bamba
  affiliation: Faculté de médecine de Nouakchott
  country: Université de Nouakchott, Mauritania

- name: Mohamed Abdellahi Sidi Mohamed Blal
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

- name: El Hacen Mohamed Soueilem
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

- name: Mohamedou
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

- name: Mohamed Boullah
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

- name: Fatimetou Hademine
  affiliation: Faculté des Sciences et Techniques
  country: Université de Nouakchott, Mauritania

---

# Project Description

<!-- Add a short paragraph describing the project. -->

The Mauritanian approach aims to make 3D Slicer accessible to a broader audience of users and researchers in the medical field. Various projects have been completed, initiated, or are currently under consideration, including:

- The anatomy atlases created by professors Idriss and Yahya in 2018 enabled medical students to visualize and quickly assimilate human body parts through the use of 3D Slicer.
- Other applications for generating 3D models of baby and expectant mother mannequins.
- Implementation and integration of three breast cancer segmentation methods by one of our researchers: An adaptive fuzzy C-means algorithm, An adaptive k-means algorithm, and an adaptive Otsu thresholding. Integration is underway.
- Processing and segmentation of medical images with 3D Slicer and Deep Learning in the context of an integrated approach for analyzing various medical data from Mauritania. This is the subject of an ongoing doctoral thesis.
- Other upcoming applications are planned.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

- Generate 3D models of baby and expectant mother mannequins.
- Contribute to enriching breast cancer segmentation methods by introducing and comparing user choices in 3D Slicer.
- Explore cutting-edge techniques in medical image processing and segmentation, especially those based on Deep Learning, implement them, and evaluate performance.
- Anticipate additional upcoming applications.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

- 3D Model of Baby and Expectant Mother
- Introduction of 3D Segmentation Methods:
- Segmentation of Medical Images from Mauritania:
- Other upcoming applications:


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

- Progress in generating 3D models of the baby and expectant mother.
- Progress in integrating the 3D segmentation methods.
- Progress of the doctoral thesis: Segmentation of Medical Images from Mauritania.
- Other upcoming projects.


# Illustrations

We have developed an extension for 3D Slicer to perform medical image (volume) segmentation using the K-Means algorithm. Specifically, we have implemented an adaptive version of K-Means, which allows segmentation based on pixel intensity.

We encountered several challenges during volume processing and rendering, as well as in finding alternatives to libraries like scikit-learn, NumPy, and OpenCV to integrate them into the 3D Slicer API.

Ultimately, we successfully segmented the images using both the adaptive K-Means and the classic K-Means methods. However, these results still require improvement and testing on various types of medical images to ensure their reliability


**Adaptive Algorithm Result**

[![Image 1](https://github.com/slicermauritanie/AdaptiveSegML/blob/main/result_images/apaptive_rim1_1.png)](https://github.com/slicermauritanie/AdaptiveSegML/blob/main/result_images/apaptive_rim1_1.png) [![Image 2](https://github.com/slicermauritanie/AdaptiveSegML/blob/main/result_images/apaptive_rim1_2.png)](https://github.com/slicermauritanie/AdaptiveSegML/blob/main/result_images/apaptive_rim1_2.png) [![Image 3](https://github.com/slicermauritanie/AdaptiveSegML/blob/main/result_images/apaptive_rim1_3.png)](https://github.com/slicermauritanie/AdaptiveSegML/blob/main/result_images/apaptive_rim1_3.png)


*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[Previous ProjectWeek Page](https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/AnatomicalAtlasesMauritania)
