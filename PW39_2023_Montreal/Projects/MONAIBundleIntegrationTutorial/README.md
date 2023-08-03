---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/README.html

project_title: HOW TO use MONAI bundle to integrate models from MONAI model ZOO
category: Segmentation / Classification / Landmarking
presenter_location: Online

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

NVIDIA AI-assisted annotation (AIAA) is no longer actively maintained and MONAI bundle has been established to load a wide selection of pre-trained models for radiology and pathology. 


## Objective


Our objective is to provide a detailed step-by-step description on how to use MONAI bundle for this task.

## Step-by-Step Description

Setting up an AWS EC2 Windows server in the cloud: 
The detailed process [is described here](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/).

Install MONAILabel

Do a “cd $home”, to the place where the  MONAILabel folder will be created. 

Firstly, begin by uninstalling the existing MONAILabel and Monai installations, because as of 6/2023 we need a special MONAI version to make this word. 
This is accomplished by running the following commands in the terminal:

    pip uninstall monailabel
    pip uninstall monai

Then, follow to our outlined procedures for setting up MONAILabel from scratch. 
Please refer to [these instructions](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html), they can be found on our Project Week webpage 1.

Follow these guidelines until reaching the command to set the MONAILabel script paths:

    $Env:PATH += ";C:\Users\yourname\MONAILabel\monailabel\scripts"

After setting the paths, the next step is to install Monai in a special version (this may change in the future and will be adopted):

    pip install monai==1.2.0rc6

After a “cd $home”, where the  MONAILabel folder is located, the start_server command can be  issued:

    monailabel start_server --app MONAILabel/sample-apps/monaibundle --studies c:/Data/Task06_Lung/imagesTr --conf models lung_nodule_ct_detection


possible arguments for "conf models" are: 

lung_nodule_ct_detection
pancreas_ct_dints_segmentation
prostate_mri_anatomy
renalStructures_UNEST_segmentation
spleen_ct_segmentation
spleen_deepedit_annotation
swin_unetr_btcv_segmentation
wholeBody_ct_segmentation
wholeBrainSeg_Large_UNEST_segmentation

After this command, the correct and requested model is automatically loaded from the [Monai Model Zoo](https://monai.io/model-zoo.html), which is a highly commendable feature.

Then proceeded to test the setup with the 3D Slicer and the MONAILabel extension using the CT Chest dataset. 

It is great to see that the AI successfully detects some nodules!

Sidenote: The process was implemented on an AWS EC2 Windows server instance with an A10G GPU (24 GB dedicated video RAM).


## Approach and Plan

During the workshop, create the wholeBody_ct_segmentation MONAILabel model on an AWS EC2 Windows instance.

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/06d8146a-4d0e-4a6d-a7d3-59158f773647)

We'll attempt using the server simultaneously from various places while documenting the installation procedure. 

The IP address of the MONAILabel server is http://52.209.177.211:8000/. During the Project week (Monday through Wednesday), the server will be accessible daily from 2 p.m. to 4 p.m. local time. 

## Progress and Next Steps

We held three workshops during the conference with good success. In each of the workshops we were able to 

- reliably connect to the AWS server instance
- start MONAILabel
- use the monaibundle app
- load one of the two demonstrated models
- start 3D Slicer on the server
- perform inference with the preconfigured model
- demonstrate label adjustments
- submit labels
- work remotely on the AWS server instance
- answer first-timer questions


Here is a list of the bundles from the [MONAI Model Zoo page](https://monai.io/model-zoo.html) as of 5/23:

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

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/cdc7d159-2670-433a-945e-4c7000c21f80)


# Background and References
     
     https://docs.monai.io/en/stable/bundle_intro.html
     https://monai.io/model-zoo.html
     


