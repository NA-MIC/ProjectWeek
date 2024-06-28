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

- name: Csaba Pinter
  affiliation: Ebacinca, S.L.
  country: Spain
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

During project week we:
1. Created framework for saving 3D muscle and vertebral joint data as model creation information. 
2. Troubleshooting and confirmed muscle measurements from DL masks matched expected results.  
3. Established plan for defining OpenSim spine bodies and joints from segmentations
  1. Identifying endplates of vertebral bodies via clustering. 
  2. Use centroids of both full vertebral and vertebral body only segmentations to evaluate local vertebral orientation

Next steps: 
1. Finalize downstream model creation code.
2. Integration - multiple DL models + several measurement and model creation scripts 
3. Test on multiple input scans. 
4. Enable model creation in Slicer with an extension that will display key measurements to be used, and possibly have a method for editing /correcting obvious errors.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Picture1](https://github.com/NA-MIC/ProjectWeek/assets/49168951/81a8be1a-2648-49a7-ae30-c5043f56f677)

Model creation for the analysis of personalized patient spinal loading predictions.



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


•	[Evaluation of Load-To-Strength Ratios in Metastatic Vertebrae and Comparison With Age- and Sex-Matched Healthy Individuals](https://www.frontiersin.org/articles/10.3389/fbioe.2022.866970/full)

# Results

## Intervertebral centroid calculation

### 1. Seperate vertebral body from existing segmentation
   
![Screenshot 2024-06-27 215559](https://github.com/VyHong/ProjectWeek/assets/67245730/af1ea7cd-4eab-43ef-8fd9-945065a09774)
![Screenshot 2024-06-27 215504](https://github.com/VyHong/ProjectWeek/assets/67245730/c3dc9282-38e0-486d-ba76-9be863ada80f)

### 2. Convert volume to surface
![Screenshot 2024-06-27 223435](https://github.com/VyHong/ProjectWeek/assets/67245730/9d717ed2-cf1f-47e4-9e73-6fe34f40eb7a)
 
### 3. Cluster surface points to determine vertebral endplates
 <video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/67245730/f6469b36-f808-451c-827c-de0100745e9e"
   style="max-height:640px; min-height: 200px">
 </video>


<video
   controls muted
   src="https://github.com/VyHong/ProjectWeek/assets/67245730/f01e4596-3cd7-4d84-b45b-2801e850fdd2"
   style="max-height:640px; min-height: 200px">
 </video>

### 4. Calculate convex hull centroid between 2 endplates

![Screenshot 2024-06-27 234732](https://github.com/VyHong/ProjectWeek/assets/67245730/2c0d1065-1b19-4517-9b6a-542a10916cd6)

