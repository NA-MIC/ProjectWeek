Back to [Projects List](../../README.md#ProjectsList)

# Real-time ultrasound AI segmentation using Tensorflow and PyTorch models

## Key Investigators

- María Rosa Rodríguez Luque (Universidad de Las Palmas de Gran Canaria, Spain)
- Tamas Ungi (Queen’s University, Canada)
- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)

# Project Description

The module "Segmentation U-Net", from extension [SlicerAIGT](https://github.com/SlicerIGT/aigt), applies deep learning models on an ultrasound image stream to generate the predicted segmentation in real time. This is shown in the following image, where it is used to detect tumour tissue (highlighted in red) on breast images. 

<img src="https://user-images.githubusercontent.com/104084765/213722945-46e5174e-65e0-4177-ab1c-f520170d2994.png" alt="drawing" width="650"/>

That way, we can apply a live volume reconstruction on this prediction and visualize the complete region of interest (in this case, the area of the tumour). 

<img src="https://user-images.githubusercontent.com/104084765/213723471-5018e772-874f-4582-bf65-330ea8e98512.png" alt="drawing" width="650"/>

Currently, this module supports models trained with the TensorFlow ecosystem. However, in recent years, PyTorch has become an increasingly popular machine learning framework, especially in medical imaging applications (an example of this is the MONAI framework, which is based on PyTorch). 

We have developed a separate module to run the inference of PyTorch model for the segmentation of breast ultrasound images: [Breast Lesion Segmentation](https://github.com/EBATINCA/UltrasoundAI). However, our module does not integrate parallel processing to enable real-time image segmentation.

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

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References
This project is based on the previous **Segmentation Unet** and **Breast Lesion Segmentation** modules:
- **Segmentation Unet** admits Tensorflow models to develop the segmentation task on an ultrasound image stream:
    - **GitHub repository**: [Segmentation Unet](https://github.com/mrluque/aigt/tree/master/SlicerExtension/LiveUltrasoundAi) module.
    - The [tutorial](https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day2_2_SlicerIGT-U38_LiveAiRec.pptx) about how to use the previous module was shown during PerkLabBootcamp held virtually on May 24-26, 2022. 
     - A [video demo](https://youtu.be/WyscpAee3vw) is also available

- **Breast Lesion Segmentation** deploy deep learning models trained in PyTorch for segmentation of 2D Ultrasound images:
    - **GitHub Repository**: [Breast Lesion Segmentation](https://github.com/EBATINCA/UltrasoundAI) module
    
Integration of PyTorch and Slicer:
* To use a deep learning model trained in PyTorch inside Slicer, we install the [PyTorch extension](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PyTorchIntegration/), presented during 35th Project Week held virtually June 28-July 2, 2021.
