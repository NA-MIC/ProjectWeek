---
layout: pw45-project

permalink: /:path/

project_title: AI model development for lung ultrasound analysis
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Alexandre Banks Gadbois
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Deepa Krishnaswamy
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Dave Dinh
  affiliation: Consultant for Brigham and Women's Hospital
  country: USA

- name: Matt McCormick
  affiliation: Fideus Labs
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


One of the primary indicators of acute heart failure is the presence of pulmonary congestion. To detect the fluid build up quickly the in emergency room, lung ultrasound exams are taken of the patient. Clinicians look for hyperechoic artifacts (B-lines) that appear in the image, where the more they see, the more congested the patient is. 

Unfortunately, the manual detection of these B-lines is difficult due to the image quality, which depends on the type of transducer and the expertise of the clinician. Therefore, AI models have started to be developed to quickly detect these B-lines. Our group, over the past few years, has developed multiple methods [1], [2], [3]. One of the drawbacks though, is that the models do not compute the pleural percentage, which is the ratio of the B-line sectors to the pleural line sectors. 

Therefore, we have started to investigate using object detection models for automatically finding the pleural lines and B-lines. Our goal for this project week is to train and validate detection models such as YOLO, [4] and talk to clinicians about the performance. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Train and validate YOLO  models for pleural line and B-line detection. 
2. Train and validate other state-of-the-art methods, such as [RF-DETR](https://github.com/roboflow/rf-detr) [5]
3. Show and discuss our results with clinicians. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop models for pleural line and B-line detection. 
2. Make our model/code publicly available. 
3. Talk to clinicians 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. We have trained some preliminary YOLO models. We trained one oriented bounding box YOLO model for pleural lines, and another axis-aligned box YOLO model for B-lines. 
2. We calculated the percent pleura and compared it to the experts. 




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Ground truth boxes in scanline space: oriented bounding box for the pleural line (left), and axis-aligned bounding box for the B-lines. 
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/e2c235c9-7abe-4a63-a6a0-512143757eb2" />

YOLO results after performing pleural line detection and B-line detection, and conversion back to the sector space, compared to the ground truth: 
<img width="800" alt="Image" src="https://github.com/user-attachments/assets/22010591-075d-4910-9e31-184b91568813" />

Percent pleura for one test lung zone - x = frame #, and y = percentage. We see that the AI predicted 
<img width="455" height="333" alt="Image" src="https://github.com/user-attachments/assets/ac226669-a7e1-40dd-b479-cb7cb14a95f0" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [1] Lucassen RT, Jafari MH, Duggan NM, Jowkar N, Mehrtash A, Fischetti C, Bernier D, Prentice K, Duhaime EP, Jin M, Abolmaesumi P. Deep learning for detection and localization of B-lines in lung ultrasound. IEEE journal of biomedical and health informatics. 2023 Jun 5;27(9):4352-61.

- [2] Asgari-Targhi A, Ungi T, Jin M, Harrison N, Duggan N, Duhaime E, Goldsmith A, Kapur T. Can Crowdsourced Annotations Improve AI-Based Congestion Scoring for Bedside Lung Ultrasound?. InInternational Conference on Medical Image Computing and Computer-Assisted Intervention 2024 Oct 7 (pp. 580-590). Cham: Springer Nature Switzerland.[3] MICCAI 2026 submission. 

- [3] MICCAI 2026 acceptance. AI-Driven Pulmonary Congestion Assessment for Lung Ultrasound via Segmentation-Guided Transformers. 

- [4] https://github.com/ultralytics/ultralytics

- [5] https://github.com/roboflow/rf-detr

