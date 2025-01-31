---
layout: pw42-project

permalink: /:path/

project_title: Spinal musculoskeletal module for computing vertebral specific loading
category: Quantification and Computation

key_investigators:

- name: Csaba Pinter
  affiliation: Ebatinca S.L.
  country: Spain

- name: Ron Alkalay
  affiliation: Beth Israel Deaconess Medical Center
  country: USA

- name: Dennis Anderson
  affiliation: Beth Israel Deaconess Medical Center
  country: USA

- name: Vy Hong
  affiliation: Technical University Munich
  country: Germany

- name: Nils Rehtanz
  affiliation: Technical University Munich
  country: Germany

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

- name: Andras Lasso
  affiliation: Queen’s University
  country: Canada

- name: Ron Kikinis
  affiliation: Brigham and Women’s Hospital and Harvard Medical School
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Musculoskeletal models of the spine allow insight into the complex loading states experienced by the human spine that cannot be measured in human subjects noninvasively. We have previously established models for such analyses OpenSim, an open-source modeling software, and developed machine-learning approaches for segmenting cancer patients' spinal column and trunk musculature. However, establishing personalized models to represent individual human subjects is complex and time-consuming, requiring custom scripting for data computation, curation, and assembling of model parameters.
In the previous project week, our group ported our model creation, analysis, and data management scripts to Python and has worked on computing spinal inter-segment centroid and vertebral segment orientation necessary for adapting our generic female and male model to the patient anatomy and the spatial kinematic relationships of the modeled spine (individual vertebral size, inter-discal space, spinal curvature). For project week 42, we propose integrating these tools within the extension framework to enable automation of the segmentation process and visualization of the spine and muscle segmentation outcome, a complete pipeline to allow computing the input file required to model creation in Open sim from this segmentation and visualizing the force and moment values results at each vertebral level in 3Dslicer based on the Open sim model analysis.

Having such an open-source model in 3d Slicer will significantly contribute to the scientific and clinical community for cancer patient research and to studying the effect of spinal loading on morbidity in elderly populations and surgical outcomes.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1.	Create an open-source Slicer module integrating our group's
    a)	Vertebrae and musculature DL segmentation models
    b)	Python-based spinal musculoskeletal model preparation and management scripts
for establishing patient-specific spinal model input files for analysis in the OpenSim environment.
2.	Automate model creation in Open Sim based on the model input file.
3.	Create tools for visualizing and presenting model results at the model skeleton and muscle structures for static simulations.
4.	Discuss extending  objective 3 for visualizing dynamic simulations (gait, tasks)



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


TBD



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

**Progress**:
- **Landmark Identification**: Using segmentations of vertebrae, we identified critical points such as joint centroids and body centroids.
- **Local Coordinate Frames**: Defined subject-specific biomechanical models in OpenSim by creating local coordinate frames for vertebral bodies and intervertebral joints.
- **Integration into OpenSim**: Successfully exported the identified landmarks into OpenSim models, enabling personalized musculoskeletal analyses.

**Next Steps**:
1. Consider multiple methods for identifying the points and landmarks used.
2. Display resulting frames (joint centers and axes) within 3D Slicer along with spine segmentations, incorporating methods for viewing and correction before exporting to OpenSim.
3. Improve visualization and QA of OpenSim models:
   - Export vertebral segmentations into files and use them in the OpenSim visualizer.
   - Visualize OpenSim models in Slicer for side-by-side comparisons.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
![vertebra_segmentation_front](https://github.com/user-attachments/assets/4d27c9a9-fa4b-46c6-8981-77bffcbbfdec)
![vertebra_segmentation_side](https://github.com/user-attachments/assets/538d45be-a9cc-4c6a-9f15-cda61b96a3b7)
![subregion_segmentation_side](https://github.com/user-attachments/assets/78402110-338b-428d-b454-6d7ecac93315)
![poi_in_vertebra](https://github.com/user-attachments/assets/cc99a5de-fb5d-46c4-a859-364975daded0)
![open_sim_spine_model_front](https://github.com/user-attachments/assets/63c9c325-dd71-4cf2-b233-28eba349d7bf)
![open_sim_spine_model_side](https://github.com/user-attachments/assets/8fb7d50f-a84e-40e4-87c0-158c85f437bd)
![open_sim_fulll_body](https://github.com/user-attachments/assets/139b93c0-ff4d-46b2-957e-8bff813ebc84)


![PW42 project page Graphic](https://github.com/user-attachments/assets/767c0b03-0dcf-4e05-b179-b476099c2a68)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. [Evaluation of Load-To-Strength Ratios in Metastatic Vertebrae and Comparison With Age- and Sex-Matched Healthy Individuals](https://www.frontiersin.org/articles/10.3389/fbioe.2022.866970/full)
2. [Metastatic spine disease alters spinal load-to-strength ratios in patients compared to healthy individuals](https://www.medrxiv.org/content/10.1101/2025.01.06.25320075v1)
3. [Automated Segmentation of Trunk Musculature with a Deep CNN Trained from Sparse Annotations in Radiation Therapy Patients with Metastatic Spine Disease](https://www.medrxiv.org/content/10.1101/2025.01.13.25319967v1)
