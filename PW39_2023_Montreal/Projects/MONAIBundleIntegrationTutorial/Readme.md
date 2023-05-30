---
layout: pw39-project

project_title: HOW TO use MONAI bundle to integrate models from MONAI model ZOO
category: Segmentation / AI

key_investigators:
- name: Rudolf Bumm
  affiliation: KSGR
  country: Germany

- name: Andres Dias-Pinto 
  affiliation: NVIDIA
  country: USA
  
- name: Andras Lasso
  affiliation: Queens University
  country: Canada
---

# Project Description

<!-- Add a short paragraph describing the project. -->
NVIDIA AI assisted annotation (AIAA) is no longer actively mainatined and MONAI bundle has been established to load a wide selection of pretrained models for radiology and pathology. 


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
Our objective is to provide a detailed step by step description on how to use MONAI bundle for this task. 

Firstly, begin by uninstalling the existing MONAILabel and Monai installations. This was accomplished by running the following commands in the terminal:

    pip uninstall monailabel
    pip uninstall monai

Subsequently, I adhered to our outlined procedures for setting up MONAILabel from scratch. For those who need to refer to [these instructions]([url](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html)), they can be found on our Project Week webpage 1.

I followed these guidelines until I reached the command to set the MONAILabel script paths:

$Env:PATH += ";C:\Users\yourname\MONAILabel\monailabel\scripts"
After setting the paths, the next step was to installed Monai as recommended above:

pip install monai==1.2.0rc6
After a “cd $home”, where my MONAILabel folder is located, the start_server command was issued:

monailabel start_server --app MONAILabel/sample-apps/monaibundle --studies c:/Data/Task06_Lung/imagesTr --conf models lung_nodule_ct_detection
After this command, the correct and requested model was automatically loaded from the [Monai Model Zoo]([url](https://monai.io/model-zoo.html)), which is a highly commendable feature.

I then proceeded to test our setup with the 3D Slicer and the MONAILabel extension using the CT Chest dataset. It was great to see that the AI successfully detected some nodules!

Sidenote: The process was implemented on an AWS EC2 Windows server instance with an A10G GPU (23 GB dedicated video RAM).



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/cdc7d159-2670-433a-945e-4c7000c21f80)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
     
     https://docs.monai.io/en/stable/bundle_intro.html
     


