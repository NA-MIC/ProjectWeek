---
layout: pw45-project

permalink: /:path/

project_title: AI model development for lung ultrasound analysis
category: Lung Ultrasound
presenter_location: 

key_investigators:

- name: Alexandre Banks Gadbois
  affiliation: BWH
  country: USA

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Dave Dinh
  affiliation: BWH
  country: USA

- name: Matt McCormick
  affiliation: Fideus Labs
  country: USA

- name: Tina Kapur
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


One of the primary indicators of acute heart failure is the presence of pulmonary congestion. To detect fluid build up quickly in the emergency room, lung ultrasound exams are taken of the patient. Clinicians look for hyperechoic artifacts (B-lines) that appear in the image, where the more they see the more congested the patient is. 

Unfortunately, manual detection of these B-lines is difficult due to the image quality, which depends on the type of transducer and the expertise of the clinician. Therefore, AI models have started to be developed to quickly detect these B-lines. Our group, over the past few years, has developed multiple methods [1], [2], [3]. One of the drawbacks though, is that existing models do not compute the pleural percentage, the ratio of the B-line sectors to the pleural line sectors, which is strongly associated with extravascular lung water and consistent with other semi-quantitative clinical scores [4]. 

Therefore, we have started to develop detection models to automatically find pleural lines and B-lines and compute the percentage pleura. Our goal for this project week is to train and validate keypoint detection models such as ViTPose++, [5], and HRNet with UDP, [6], and talk to clinicians about the performance. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Develop a dataloader to read in and pre-process US scans from different sites, patients, and probes.
2.  Train and validate keypoint detection models such as ViTPose++ and HRNet (with UDP) for pleural line and B-line (endpoint) detection.
3.  Show and discuss our results with clinicians. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop a dataloader to efficiently handle pre-processing and different data distributions.
2. Develop 1-2 models for pleural line and B-line keypoint detection. 
3. Make our model/code publicly available. 
4. Talk to clinicians.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We have trained some preliminary YOLO models for bounding box detection. We trained one oriented bounding box YOLO model for pleural lines, and another axis-aligned box YOLO model for B-lines. 
2. We calculated the percent pleura and compared it to the experts.
3. Implemented and validated a data preprocessing script: 1) parses data and formats into COCO-styled repository, 2) enables sector-to-scanline conversions, 3) enables filtering by metadata (_site, annotator, lung zone, patients, before/after diuretic, transducer type, transducer manufacturer_)
4. Implemented a dataloader that allocates equal proportions of different metadata tags to train/vali/test datasets. Implemented k-fold validation and inclusion of data by various metadata tags.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Ground truth boxes in scanline space: oriented bounding box for the pleural line (left), and axis-aligned bounding box for the B-lines. 
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/e2c235c9-7abe-4a63-a6a0-512143757eb2" />

YOLO results after performing pleural line detection and B-line detection, and conversion back to the sector space, compared to the ground truth: 
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/22010591-075d-4910-9e31-184b91568813" />

Percent pleura for one test lung zone - x = frame #, and y = percentage. We see that the AI predicted 
<img width="455" height="333" alt="Image" src="https://github.com/user-attachments/assets/ac226669-a7e1-40dd-b479-cb7cb14a95f0" />

**Data Exploration (During Project Week)**

Overview of different metadata of lung ultrasound dataset:
<img width="1653" height="993" alt="LungUSDataOverview" src="https://github.com/user-attachments/assets/e046e100-d5e3-4aaa-8ee9-0dd1a1b5f8d0" />

Overview of original data structures:
```
+---Andrew/
|   +---Andrew-0561119268/
|   |       0561119268_08109698.andrew.json
|   |       0561119268_08109698.dcm
|   |       ...
|   +---Andrew-1835608883/
|   +---Andrew-3594442829/
|   +---Andrew-5476058456/
|   +---Andrew-5982622832/
|   ...
|   +---Andrew-CARVD_123_Day_0/
|   +---Andrew-CARVD_124_Day_0/
|   +---Andrew-CARVD_125_Day_0/
|   ...
|   +---Andrew-CARVD_134_Day_0/
|   +---Andrew-Lahey_001_T0_Transverse/
|   +---Andrew-Lahey_029_T0_Transverse/
|   +---Andrew-Lahey_032_T0_Transverse/
|   ...
+---Arjun/
|   ...
+---Frances/
|   ...
+---Lao/
|   ...
+---Nick/
|   ...
+---Nicole/
|   ...
+---Peter/
|   ...
+---Sandra/
|   ...
+---Sandra-old/
    ...
```

Overview of new data structure:
```
COCO_Data
+---annotations/
|   +---scanline/
|   |       <Annotator>_<clipid>.json
|   |       <Annotator>_<clipid>.json
|   |       ...
|   +---sector/
|           <Annotator>_<clipid>.json
|           <Annotator>_<clipid>.json
|           ...
+---images/
    +---scanline/
    |       <Annotator>_<clipid>_<framenum>.png
    |       <Annotator>_<clipid>_<framenum>.png
    |       ...
    +---sector/
            <Annotator>_<clipid>_<framenum>.png
            <Annotator>_<clipid>_<framenum>.png
            ...
```


Standardized JSON Metadata:

<img width="600" alt="image" src="https://github.com/user-attachments/assets/70d1a7a3-a83f-4b3e-9629-e7fa67848f1f" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [1] Lucassen RT, Jafari MH, Duggan NM, Jowkar N, Mehrtash A, Fischetti C, Bernier D, Prentice K, Duhaime EP, Jin M, Abolmaesumi P. Deep learning for detection and localization of B-lines in lung ultrasound. IEEE journal of biomedical and health informatics. 2023 Jun 5;27(9):4352-61.

- [2] Asgari-Targhi A, Ungi T, Jin M, Harrison N, Duggan N, Duhaime E, Goldsmith A, Kapur T. Can Crowdsourced Annotations Improve AI-Based Congestion Scoring for Bedside Lung Ultrasound?. InInternational Conference on Medical Image Computing and Computer-Assisted Intervention 2024 Oct 7 (pp. 580-590). Cham: Springer Nature Switzerland.[3] MICCAI 2026 submission. 

- [3] MICCAI 2026 acceptance. AI-Driven Pulmonary Congestion Assessment for Lung Ultrasound via Segmentation-Guided Transformers.
  
- [4] Brusasco C, Santori G, Bruzzo E, et al. Quantitative lung ultrasonography: a putative new 
algorithm for automatic detection and quantification of B-lines. Crit Care. 2019;23(1):288. 

- [5] [https://github.com/ultralytics/ultralytics](https://github.com/vitae-transformer/vitpose#Updates)

- [6] [https://github.com/HuangJunJie2017/UDP-Pose](https://github.com/HuangJunJie2017/UDP-Pose)

