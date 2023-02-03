Back to [Projects List](../../README.md#ProjectsList)

# Real-time ultrasound AI segmentation using Tensorflow and PyTorch models

## Key Investigators

- María Rosa Rodríguez Luque (Universidad de Las Palmas de Gran Canaria, Spain) [on site]
- Tamas Ungi (Queen’s University, Canada) [remote]
- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain) [on site]
- Chris Yeung (Queen’s University, Canada) [remote]

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

1. Adapt the current "Segmentation U-Net" module to support models trained with PyTorch
2. Automatically display the AI segmentation overlayed on the input ultrasound image 

## Approach and Plan

1. Integrate a TensorFlow/PyTorch model selector, so the module would automatically use the one give by the user
1. Develop the image pre-and post-processing required by the PyTorch model 
1. Record an ultrasound image stream and run the inference in real time using a PyTorch model
1. Apply the selected prediction transform on the output volume automatically 

## Progress and Next Steps

1. The module uses the file extension to know the model framework (.h5 for TensorFlow and .pth or .pt for PyTorch) and execute the corresponding actions in each case

<img src="https://user-images.githubusercontent.com/104084765/216464220-a88c58f6-99fc-4db8-b18f-6a92d04387f4.gif" width="450">

2. We have recorded a stream from a breast ultrasound phantom where an inclusion that simulates injured tissue is shown. A PyTorch model previously trained with the [Dataset BUSI](https://www.sciencedirect.com/science/article/pii/S2352340919312181) was used to run the inference for the real-time segmentation.

* Original stream recorded:

<img src="https://user-images.githubusercontent.com/104084765/216470636-3e6cfdce-5dbf-40fd-a7a6-b8c69b77143a.gif" width="500">


* Steps to run the inference and visualize the predicted segmentation with this new version of the "Segmentation U-Net" module:

<img src="https://user-images.githubusercontent.com/104084765/216473923-ef5ba058-0b96-42be-879e-ebf7c651acd3.gif" width="800">


* Lesion reconstruction using _Volume Reconstruction_ and _Volume Rendering_  modules:

<img src="https://user-images.githubusercontent.com/104084765/216473931-38878234-5e09-4376-8bdd-fa2f1dc853f2.gif" width="650">

3. When we the box "Use separate process for prediction" is not checked, we automatically apply the prediction transform selected and display the AI segmentation overlayed on the input ultrasound image (as it was shown before). When this box is checked, the input stream and the prediction have different frame rate and it is more convenient to visualize the prediction in a different view, so we should make it visible manually.


**Next Steps**

* Currently, it is required to define the PyTorch network and load only the trained weights. To make the module more flexible it is desired to directly load the complete model (as it is done in the case of TensorFlow).

* The pre-and post-processings steps have been defined according to the process carried out to train the PyTorch model used in this case. However, these steps should be more generalized to work with different models.

* PyTorch models are only supported when we use the same process for prediction (the check box is not selected), so it is necessary to improve this. 

# Illustrations
Previous work:

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
