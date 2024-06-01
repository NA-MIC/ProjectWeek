---
layout: pw41-project

permalink: /:path/

project_title: Spinal musculoskeletal module for computing vertebral-specific loading in daily tasks
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Ron Alkalay
  affiliation: Beth Israel Deaconess Medical Center
  country: US

- name: Dennis Anderson
  affiliation: Beth Israel Deaconess Medical Center
  country: US

- name: Vy Hong
  affiliation: Technical University Munich
  country: Germany

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->


Musculoskeletal models of the spine allow insight into the complex loading states experienced by the human spine that cannot be measured in human subjects noninvasively. We have previously established models for such analyses within the open-source modeling software OpenSim, as well as developing methods and experience in personalizing models to represent individual human subjects and patients using a variety of data.  However, establishing personalized models from clinical imaging is complex and time-consuming, historically requiring manual segmentation of thoracic and abdominal vertebrae and spinal musculature using expensive commercial applications and custom scripting for data computation, curation, and assembling of model parameters.  

Over the last year, our group, in collaboration with members of the 3D Slicer community, has developed DL models for the segmentation of human thoracic and lumbar vertebrae and detailed segmentation of the torso and abdominal musculature in cancer patients. We have similarly ported our model creation, analysis, and and data management scripts to Python. We propose integrating these tools within the extension framework to enable the complete pipeline to assess spinal loading using our open-source spinal model in OpenSim. Having such an open-source model in 3d Slicer will significantly contribute to the scientific and clinical community for cancer patient research and to studying the effect of spinal loading on morbidity in elderly populations and surgical outcomes. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1.	Create an open-source Slicer extension to integrate vertebrae and musculature DL segmentation models (TS, AutoSeg, in-house) and our group's Python-based data analysis and management scripts to allow the preparation of a spinal model for analysis in OpenSim. 

2.	Discuss the possible integration of tools for running static and dynamic simulations and evaluating and presenting model results.  



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1.	Discuss the current analysis and management scripts pipeline. Is it ready for integration? What parts are missing? Integration of the DL-based masks for generating data for the pipeline. 
    1.	The key gap for integration of DL segmentation data is translating DL-based masks into model-relevant information.

2.	What issues must be solved for this integration within the extension mechanism? Build an integration plan emphasizing a framework for modularity and code expansion.

3.	Possible avenues for slicer module(s) creation (the very ambitious version)
    1.	Create Slicer module (s) from the Python scripts.
    2.	Create a Slicer module to run-extract information from the DL models
    3.	Create a Slicer module to assemble the data file for the OpenSim modeler
    4.	Create an extension containing the modules.

4.	Discuss methods of results presentation.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Established DL-based segmentation tools for vertebrae and spinal muscles
2. Converted the computation and data management scripts to Python
3. Created detailed documentation of the Python code
4. Extensively validated and published the OpenSim spinal musculoskeletal model.  The model is open-source.
5. will create a database of anonymized CT data from our cancer patient study



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Picture1](https://github.com/NA-MIC/ProjectWeek/assets/49168951/81a8be1a-2648-49a7-ae30-c5043f56f677)

Model creation for the analysis of personalized patient spinal loading predictions.



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


•	[Evaluation of Load-To-Strength Ratios in Metastatic Vertebrae and Comparison With Age- and Sex-Matched Healthy Individuals](https://www.frontiersin.org/articles/10.3389/fbioe.2022.866970/full)

