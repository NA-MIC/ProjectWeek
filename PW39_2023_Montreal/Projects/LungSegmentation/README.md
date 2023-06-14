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

This is a follow-up to previous 3D Slicer lung CT segmentation PW projects. 


## Objective

To improve the LungCTAnalysis extension analysis in 3D Slicer, 

which is frequently used (40 runs per day) 

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/51840d88-e21f-489e-9943-e292ea8994b9)

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/ee0a6b06-9647-44b7-be68-84bbd04c4256)


the following steps could be taken:

1. Improve **vessel segmentation**:
   - Explore advanced image processing techniques, such as machine learning algorithms, to enhance the accuracy of vessel segmentation.
   - Incorporate vessel enhancement filters and vesselness measures to improve the detection and segmentation of pulmonary vessels.
   - Investigate the use of multi-modal imaging, such as combining CT angiography and conventional CT scans, to improve vessel segmentation accuracy.

2. Develop a better concept for lung **segment (sublobar) segmentation** in 3D Slicer:
   - Review the existing lung segmentation algorithms and identify areas for improvement.
   - Consider incorporating anatomical landmarks, such as fissures and vessel patterns, to refine the segmentation of lung sublobes.
   - Utilize machine learning techniques, such as deep learning algorithms, to automatically segment lung sublobes based on training data.

3. **Identify tumors** belonging to segments and consider safety margins:
   - Implement tumor detection algorithms that can identify and segment lung tumors within specific lung segments.
   - Incorporate safety margin calculations to ensure adequate coverage of tumors during segmentation.
   - Provide visual cues or annotations to clearly indicate tumor locations and **safety margins** in the 3D Slicer interface.

4. Suggest resection of segments which include nutritive vessel resection for **neighboring tumors**:
   - Develop algorithms that can analyze the relationships between lung segments and neighboring tumors to determine if resection of the nutritive vessels is necessary.
   - Provide automated suggestions for resection of segments that require removal due to the radicality of neighboring tumor resections.
   - Ensure clear visualization and communication of these suggestions to the medical professionals using 3D Slicer.

5. **Differentiate pulmonary arteries and veins** reliably:
   - Investigate advanced image analysis techniques (VMTK?), such as texture analysis and flow analysis, to differentiate pulmonary arteries and veins with higher reliability.
   - Explore the use of contrast-enhanced imaging techniques or dual-energy CT to improve the differentiation of arteries and veins.
   - Validate the accuracy and reliability of the differentiation algorithms through comprehensive evaluation and comparison with ground truth data.

6. Work on current **OpenSourceCOVID publication**:
   - Collaborate with domain experts to finalize the research findings and results.
   - Prepare the manuscript for publication, ensuring clear and concise communication of the developed techniques, methodologies, and results.
   - Conduct a thorough review of the existing literature to ensure the publication adds novel contributions and addresses any gaps in the field.
   - Seek feedback from colleagues and experts in the field to improve the manuscript before submission.
   - Consider presenting the research findings at relevant conferences or workshops to share knowledge and gather feedback from the scientific community.

## Approach and Plan

Work on a dedicated Angio-CT. 


## Progress and Next Steps

Lung CT Segmenter

The most expedient way to obtain a precise surgical planning result at the moment involves the use of combined airway segmentation and vessel volume rendering, utilizing the centerblock technique. This method requires minimal manual intervention. We have chosen to enhance the division of vascular structures within the vessel mask by eliminating the hilar structures, where there's a prominent overlay of vessels. Subsequently, we employ a 'grow-from-seeds' analysis which promises improved accuracy. The VMTK centerline analysis, however, appears to be a less preferable option. This is largely due to its lack of efficiency in differentiating between pulmonary arteries and vessels.

Lung CT Analyzer 

The primary constraint of the computational method appears to be its pronounced sensitivity to the selected threshold values. Evidence suggests that even minor variances in well-calibrated clinical CTs can lead to appreciable differences in the final outcome, affecting about 20-30% of cases. The likely source of this issue is the use of rigid threshold values, which inherently makes the classification highly responsive to the specific threshold set. Andras Lasso has proposed mitigating this sensitivity through the application of soft classifiers. We intend to pursue this approach, potentially augmenting it with AI pattern detection.

# Illustrations

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/a5b9aa50-3f4f-4a70-9edb-d90346a918c2)
Fig 1: Pulmonary vesselmask

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/8760d090-c003-4a67-a0be-bba3c17fc677)
Fig 2: Combined airway segmentation and vessel volume rendering, centerblock technique

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/c8e5f155-5c03-4b94-9983-0fb6850ae7a1)

Fig 3: Centerline analysis with VMTK

# Background and References

Lung CT Analyzer
https://github.com/rbumm/SlicerLungCTAnalyzer

From Voxels to Prognosis: AI-Driven Quantitative Chest CT Analysis Forecasts ICU Requirements in 78 COVID-19 Cases (preprint) 
https://doi.org/10.21203/rs.3.rs-3027617/v3










