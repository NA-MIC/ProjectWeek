---
layout: pw41-project

permalink: /:path/

project_title: Methods for self-supervised depth estimation and motion estimation in colonoscopy under deformation
category: Quantification and Computation
presenter_location: In-person

key_investigators:
- name: Megha Kalia
  affiliation: Brigham and Women’s Hospital, Harvard Medical School
  county: USA

---

# Project Description

Estimating Depth and localizing endoscope in surgical environment is critical in many tasks such as, intra-operative registration, augmented reality, surgical automation, among many others. Monocular self-supervised depth and pose estimation methods can estimate depth and camera pose without requiring labels. However, how do these methods perform in presence of deformation while endoscope moves through the lumen is not known. Therefore, through this project we want to evaluate the effect of addition of primarily two modules on depth and pose estimation accuracy. These modules are TransUnet and Optical Flow Module. Optical Flow can capture the image intensity changes in the scene because of deformation. And TransUnet can potentially capture the temporal correlations between the image frames to give better pose and depth predictions. For the project open sources dataset and github codes will be utilized.  


## Objective


1. Objective A. To build and run and train the flowNet on colonoscopy dataset
1. Objective B. To integrate the flowNet module in the Monodepth2 framework
1. Objective C. To integrate and evaluate TransUnet blocks in Monodepth2 framework. 

## Approach and Plan


1. Run the Monodepth2 on the colonoscopy dataset. 
1. Train the optical flow network on the colonoscopic dataset
1. 

## Progress and Next Steps

1. Run the model on the colonoscopic dataset. 
2. Self-supervised training with supervision from scale-invariant depth loss.
3. Hosting the model on Huggingface

Next Steps:
creating a 3D mesh from generated depth values. 

# Illustrations

Left : Ground Truth, Right : The 3D Depth prediction (Purple - Yellow : Farther - Close)

 <iframe width="420" height="315" src="https://youtu.be/PwY5dyqEEQA">
 </iframe>

HuggingFAce link: https://huggingface.co/spaces/mkalia/DepthPoseEstimation

Simple Upload and Predict 
<img width="273" alt="upload_model" src="https://github.com/meghakalia/ProjectWeek/assets/64866412/048cae19-68f7-4f46-a11f-124668894be0">

<img width="289" alt="depth_image_huggingface" src="https://github.com/meghakalia/ProjectWeek/assets/64866412/4c5ca604-b47f-483f-ac74-cb4c64973191">


# Background and References

- [Dataset](http://cmic.cs.ucl.ac.uk/ColonoscopyDepth/Data/)
- [https://data.mendeley.com/datasets/cd2rtzm23r/1](https://data.mendeley.com/datasets/cd2rtzm23r/1)
- [Monodepth2](https://github.com/nianticlabs/monodepth2)
- [TansUnet](https://github.com/Beckschen/TransUNet/tree/main/networks)

<img width="389" alt="images_combined" src="https://github.com/NA-MIC/ProjectWeek/assets/64866412/9791afc8-7b19-456f-84a5-b04ac13a8b4f">

