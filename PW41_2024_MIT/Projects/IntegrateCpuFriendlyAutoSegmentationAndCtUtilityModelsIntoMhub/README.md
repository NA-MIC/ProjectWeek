---
layout: pw41-project

permalink: /:path/

project_title: Integrate CPU friendly auto segmentation and CT utility models into mhub
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Suraj Pai
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Leonard Nürnberg
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Andriy Fedorov
  affiliation: Brigham and Women's Hospital
  country: Boston

- name: Hugo Aerts
  affiliation: Brigham and Women's Hospital
  country: Boston

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project will aim to integrate two categories of models into [mhub.ai](mhub.ai)

**1. CPU friendly (whole-body) auto-segmentation models**

**2. CT utility model for image QA**



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Working example of a CPU-friendly (whole-body) auto-segmentation model through the `mhub.ai` platform
2. Working example of a QA pipeline using CT utility tools through `mhub.ai` platform




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


**CPU-friendly auto-seg**
Several auto-segmentation models have been integrated into slicer recently through [https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults](https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults)

While the quick version of these models run fast on CPU, the slower versions take a couple of mins. It would be interesting to explore if CPU related optimizations would work to increase the speed and reduce memory of the full resolution versions while making the quick versions even faster. 

Some initial thoughts on optimization techniques could include,
1. Converting models to OpenVINO format for optimized inference on CPU ([https://docs.openvino.ai/2024/home.html](https://docs.openvino.ai/2024/home.html), [https://docs.openvino.ai/2024/omz_demos_3d_segmentation_demo_python.html](https://docs.openvino.ai/2024/omz_demos_3d_segmentation_demo_python.html)). This could provide faster inference and make models more lightweight offering a better user experience as well. 

2. For a majority of these auto-seg models, sliding window inferer implementation results in major differences in memory (with higher batch-size) and inference time (with larger overlap ratios). Is there an optimal configuration to save memory and increase speed? 
3. Another ticket item is that the the memory consumption largely increases when predicting more output classes in the softmax, is there a way to efficienlty address this issue as well. Perhaps a more restrictive implementation of the sliding window inferer with a accuracy-efficiency trade-off?
4. Distilling models to smaller ones that run faster (might be something that takes longer than PW): [https://github.com/VaticanCameos99/knowledge-distillation-for-unet](https://github.com/VaticanCameos99/knowledge-distillation-for-unet)


**CT utility models**
Implementing CT image inspection utility models, namely, body part regression - [https://github.com/MIC-DKFZ/BodyPartRegression](https://github.com/MIC-DKFZ/BodyPartRegression). This model allows determining the body part examined and if there are anomalies in certain slices in the processed image (nifti). 


Integrating this into Mhub would allow users to perform this QA by providing DICOM inputs directly




## Progress and Next Steps

### CPU friendly auto-seg
Tested the abdominal-organs-v2.0.0 segmentation as the reported times on CPU were approx ~6 mins.

![New Note](https://github.com/NA-MIC/ProjectWeek/assets/10467804/0d9be486-dbf4-45fe-965c-15ad2b6053ae)



#### Default CPU version:
<img width="1624" alt="Screenshot 2024-06-27 at 19 40 24" src="https://github.com/NA-MIC/ProjectWeek/assets/10467804/62d1830c-99b6-4832-bdf4-864787115af9">


#### OpenVINO compiled model (most significant gain) + Reducing overlap ratio:
<img width="1624" alt="Screenshot 2024-06-27 at 18 54 49" src="https://github.com/NA-MIC/ProjectWeek/assets/10467804/e2eed2fd-c216-481d-bb57-05152cd11288">

PS: OpenVINO models are FP16 compressed and are half the size. 

### Body part regression
![BPREG](https://github.com/NA-MIC/ProjectWeek/assets/10467804/11ec7e93-c747-46e3-a86e-049aba5c82d3)


### Next Steps

- Current conversion to OpenVINO is manually done for the abdominal model. This can be automated across models in a script and pushed to Github for download.
- CPU benchmarked on is AMD, benchmark on Intel and ARM. 
- Implement Mhub models for CPU friendly autoseg. and interface with Andras' SlicerMONIAAutoSeg3D extension (work on some slicer extension specifics). 
- Complete conribution workflow for Bpreg - model is ready to go!

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



BPREG:

![image](https://github.com/NA-MIC/ProjectWeek/assets/10467804/db57f0d3-6e36-4bb1-85a8-93089f158f68)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. [https://github.com/lassoan/SlicerMONAIAuto3DSeg](https://github.com/lassoan/SlicerMONAIAuto3DSeg)
2. [https://docs.openvino.ai/2024/home.html](https://docs.openvino.ai/2024/home.html)
3. [https://github.com/MIC-DKFZ/BodyPartRegression](https://github.com/MIC-DKFZ/BodyPartRegression)
4. [https://mhub.ai](https://mhub.ai)

