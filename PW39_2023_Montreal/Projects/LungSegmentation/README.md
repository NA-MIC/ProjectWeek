---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/LungSegmentation/README.html

project_title: 3D Slicer Lung CT Segmentation and Analysis
category: Segmentation / Classification / Landmarking
presenter_location: Online

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
To improve the LungCTAnalysis extension analysis in 3D Slicer, which is frequently used, the following steps could be taken:

1. Improve vessel segmentation:
   - Explore advanced image processing techniques, such as machine learning algorithms, to enhance the accuracy of vessel segmentation.
   - Incorporate vessel enhancement filters and vesselness measures to improve the detection and segmentation of pulmonary vessels.
   - Investigate the use of multi-modal imaging, such as combining CT angiography and conventional CT scans, to improve vessel segmentation accuracy.

2. Develop a better concept for lung segment (sublobar) segmentation in 3D Slicer:
   - Review the existing lung segmentation algorithms and identify areas for improvement.
   - Consider incorporating anatomical landmarks, such as fissures and vessel patterns, to refine the segmentation of lung sublobes.
   - Utilize machine learning techniques, such as deep learning algorithms, to automatically segment lung sublobes based on training data.

3. Identify tumors belonging to segments and consider safety margins:
   - Implement tumor detection algorithms that can identify and segment lung tumors within specific lung segments.
   - Incorporate safety margin calculations to ensure adequate coverage of tumors during segmentation.
   - Provide visual cues or annotations to clearly indicate tumor locations and safety margins in the 3D Slicer interface.

4. Suggest resection of segments with nutritive vessel resection for neighboring tumors:
   - Develop algorithms that can analyze the relationships between lung segments and neighboring tumors to determine if resection of the nutritive vessels is necessary.
   - Provide automated suggestions for resection of segments that require removal due to the radicality of neighboring tumor resections.
   - Ensure clear visualization and communication of these suggestions to the medical professionals using 3D Slicer.

5. Differentiate pulmonary arteries and veins reliably:
   - Investigate advanced image analysis techniques (VMTK?), such as texture analysis and flow analysis, to differentiate pulmonary arteries and veins with higher reliability.
   - Explore the use of contrast-enhanced imaging techniques or dual-energy CT to improve the differentiation of arteries and veins.
   - Validate the accuracy and reliability of the differentiation algorithms through comprehensive evaluation and comparison with ground truth data.

6. Work on current OpenSourceCOVID publication:
   - Collaborate with domain experts to finalize the research findings and results.
   - Prepare the manuscript for publication, ensuring clear and concise communication of the developed techniques, methodologies, and results.
   - Conduct a thorough review of the existing literature to ensure the publication adds novel contributions and addresses any gaps in the field.
   - Seek feedback from colleagues and experts in the field to improve the manuscript before submission.
   - Consider presenting the research findings at relevant conferences or workshops to share knowledge and gather feedback from the scientific community.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

The development of the extension has slowed down due to the lack of ideas how to handle vessel and subsegmental structure segmentation that would be crucial for surgical planning. 
To many it seems that the main limitation of the computational method it is highly sensitive to the chosen threshold values. This is indicated that just the small variance between well calibrated clinical CTs could cause measurable differences in the end result in about 20-30% of the cases. Probably the root cause of the problem is that thresholding with a hard value makes the classification very sensitive to the chosen threshold value. Andras Lasso suggested to reduce this sensitivity by using soft classifiers.

### GPT-4 reponse: 


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









