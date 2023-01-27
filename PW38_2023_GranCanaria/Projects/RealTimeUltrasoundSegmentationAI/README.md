Back to [Projects List](../../README.md#ProjectsList)

# Real-time ultrasound AI segmentation using Tensorflow and PyTorch models

## Key Investigators

- María Rosa Rodríguez Luque (Universidad de Las Palmas de Gran Canaria, Spain)
- Tamas Ungi (Queen’s University, Canada)
- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)

# Project Description

The module "Segmentation U-Net", from extension [SlicerAIGT](https://github.com/SlicerIGT/aigt), applies deep learning models on an ultrasound image stream to generate the predicted segmentation in real time. This is shown in the following example, where it is used to detect tumour tissue (highlighted in red) on breast images. That way, we can apply a live volume reconstruction on this prediction and visualize the complete region of interest (in this case, the area of the tumour). Another instance, using spine images, is shown in (Figure 1).

<p float="left">
 <img  src="https://user-images.githubusercontent.com/104084765/215089478-fe5647f6-fecf-4df0-9829-317ef4f49453.gif" width="350">
  &nbsp; &nbsp; &nbsp;&nbsp;  
 <img src="https://user-images.githubusercontent.com/104084765/215089556-23c865ec-e6c1-4dd5-aa9f-8deced1a0fb0.gif" width="350">
</p>


Currently, this module supports models trained with the TensorFlow ecosystem. However, in recent years, PyTorch has become an increasingly popular machine learning framework, especially in medical imaging applications (an example of this is the MONAI framework, which is based on PyTorch). 

We have developed a separate module to run the inference of PyTorch model for the segmentation of breast ultrasound images: [Breast Lesion Segmentation](https://github.com/EBATINCA/UltrasoundAI) (Figure 2). However, our module does not integrate parallel processing to enable real-time image segmentation.

In this project, we aim to adapt the current "Segmentation U-Net" module to enable the use of models trained with both ecosystems, PyTorch and TensorFlow, for real-time ultrasound image segmentation. 

In addition, we will discuss further improvements for this module. For instance, automatically visualize the prediction overlayed on the input ultrasound image and avoid changing to different modules to activate the visualization.

## Objective

1. Adapt the previous module to support models trained with PyTorch
2. Automatically display the AI segmentation overlayed on the input ultrasound image 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
1. ...
1. ...

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<p float="left">
 <img  src="https://user-images.githubusercontent.com/104084765/215072656-7325329f-34ee-4a05-8ada-1f7771fece43.gif" width="400">
  &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; 
 <img src="https://user-images.githubusercontent.com/104084765/215077686-813b26c0-c49e-434c-a849-aaf8150830d6.gif" width="350">
</p>

_**Figure 1. Real-time spine segmentation and volume reconstruction using the module "Segmentation U-Net"**_

 <img src="https://user-images.githubusercontent.com/104084765/215134745-a3ecddaf-4255-4128-b989-3bf921d8fda3.gif" width="550">
 
 _**Figure 2. Segmentation of breast ultrasound images using the module "Breast Lesion Segmentation"**_

# Background and References
This project is based on the previous **Segmentation Unet** and **Breast Lesion Segmentation** modules:
- **Segmentation Unet** admits Tensorflow models to develop the segmentation task on an ultrasound image stream:
    - GitHub repository: [Segmentation Unet](https://github.com/mrluque/aigt/tree/master/SlicerExtension/LiveUltrasoundAi) module.
    - The [tutorial](https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day2_2_SlicerIGT-U38_LiveAiRec.pptx) about how to use the previous module was shown during PerkLabBootcamp held virtually on May 24-26, 2022. 
     - The video tutorials of the [breast](https://youtu.be/WyscpAee3vw) and [spine](https://youtu.be/l0BcW8c9CnI) segmentation are also available.

- **Breast Lesion Segmentation** deploy deep learning models trained in PyTorch for segmentation of 2D Ultrasound images:
    - GitHub Repository: [Breast Lesion Segmentation](https://github.com/EBATINCA/UltrasoundAI) module.
    
Integration of PyTorch and Slicer:
* To use a deep learning model trained in PyTorch inside Slicer, we install the [PyTorch extension](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PyTorchIntegration/), presented during 35th Project Week held virtually June 28-July 2, 2021.
