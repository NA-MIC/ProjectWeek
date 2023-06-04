---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/README.html

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

Subsequently, I adhered to our outlined procedures for setting up MONAILabel from scratch. For those who need to refer to [these instructions](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html), they can be found on our Project Week webpage 1.

Then follow these guidelines until reaching the command to set the MONAILabel script paths:

    $Env:PATH += ";C:\Users\yourname\MONAILabel\monailabel\scripts"


After setting the paths, the next step was to installed Monai as recommended above:

    pip install monai==1.2.0rc6

After a “cd $home”, where the  MONAILabel folder is located, the start_server command can be  issued:

    monailabel start_server --app MONAILabel/sample-apps/monaibundle --studies c:/Data/Task06_Lung/imagesTr --conf models lung_nodule_ct_detection

After this command, the correct and requested model is automatically loaded from the [Monai Model Zoo](https://monai.io/model-zoo.html), which is a highly commendable feature.

Then proceeded to test the setup with the 3D Slicer and the MONAILabel extension using the CT Chest dataset. It is great to see that the AI successfully detects some nodules!

Sidenote: The process was implemented on an AWS EC2 Windows server instance with an A10G GPU (23 GB dedicated video RAM).


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->
     
Here is a list of the bundles from the MONAI Model Zoo page as of 5/23:

**Clara train COVID19 3D classification**: A pre-trained model for 3D COVID-19 classification using CT images【1†source】

**Clara train COVID19 3D segmentation**: A pre-trained model for 3D COVID-19 lung and infection segmentation from CT images【3†source】.

**COVID19 3D segmentation**: A pre-trained model for 3D COVID-19 lung and infection segmentation from CT images【5†source】.

**Decathlon BrainTumourSegmentation**: A 3D segmentation model pre-trained on the Brain Tumour Segmentation (BraTS) subset of the Medical Segmentation Decathlon dataset【7†source】.

**Decathlon HippocampusSegmentation**: A 3D segmentation model pre-trained on the Hippocampus subset of the Medical Segmentation Decathlon dataset【9†source】.

**Decathlon LiverTumourSegmentation**: A 3D segmentation model pre-trained on the Liver Tumour subset of the Medical Segmentation Decathlon dataset【11†source】.

**Endoscopic tool segmentation**: A pre-trained binary segmentation model for endoscopic tool segmentation【13†source】.

**Lung nodule ct detection**: A pre-trained model for volumetric (3D) detection of the lung lesion from CT image on LUNA16 dataset【17†source】.

**Mednist gan**: An example of a GAN generator that produces hand x-ray images like those in the MedNIST dataset【23†source】.

**Mednist reg**: An example of a ResNet and spatial transformer for hand x-ray image registration【25†source】.

**Pancreas ct dints segmentation**: Searched architectures for volumetric (3D) segmentation of the pancreas from CT image【29†source】.

**Pathology nuclei classification**: A pre-trained model for Nuclei Classification within Haematoxylin & Eosin stained histology images【33†source】.

**Pathology nuclei segmentation classification**: A simultaneous segmentation and classification of nuclei within multitissue histology images based on CoNSeP data【37†source】.

**Endoscopic Tool Segmentation:** A pre-trained binary segmentation model for endoscopic tool segmentation【13†source】.

**Lung Nodule CT Detection:** A pre-trained model for volumetric (3D) detection of lung lesions from CT images using the LUNA16 dataset【17†source】.

**MedNIST GAN:** An example of a GAN generator that produces hand X-ray images like those in the MedNIST dataset【23†source】.

**MedNIST REG:** An example of a ResNet and spatial transformer for hand X-ray image registration【25†source】.

**Pancreas CT Dints Segmentation:** A model for volumetric (3D) segmentation of the pancreas from CT images【29†source】.

**Pathology Nuclei Classification:** A pre-trained model for nuclei classification within haematoxylin & eosin-stained histology images【33†source】.

**Pathology Nuclei Segmentation Classification:** A model for simultaneous segmentation and classification of nuclei within multitissue histology images based on CoNSeP data【37†source】.

**Pathology Nuclick Annotation:** A pre-trained model for segmenting nuclei cells with user clicks/interactions【43†source】.

**Pathology Tumor Detection:** A pre-trained model for metastasis detection on the Camelyon16 dataset【47†source】.

**Prostate MRI Anatomy:** A pre-trained model for volumetric (3D) segmentation of the prostate from MRI images【51†source】.

**Renalstructures Unest Segmentation:** A transformer-based model for renal segmentation from CT images【53†source】.

**Spleen CT Segmentation:** A pre-trained model for volumetric (3D) segmentation of the spleen from CT images【57†source】.

**Spleen Deepedit Annotation:** A pre-trained model for 3D segmentation of the spleen organ from CT images using DeepEdit【61†source】.

**Swin Unetr BTCV Segmentation:** A pre-trained model for volumetric (3D) multi-organ segmentation from CT images【65†source】.

**Valve Landmarks:** A network used to find where valves attach to the heart to help construct 3D FEM models for computation. The output is an array of 10 2D coordinates【69†source】.

**Ventricular Short Axis 3label:** A network that segments full cycle short axis images of the ventricles, labelling LV pool separate from myocardium and RV pool【71†source】.

**Wholebody CT Segmentation:** A pre-trained SegResNet model for volumetric (3D) segmentation of the 104 whole body segments【75†source】.





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
     https://monai.io/model-zoo.html
     


