---
layout: pw42-project

permalink: /:path/

project_title: Improved automated segmentation of dental CBCT images with Auto3DSeg
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Csaba Pinter
  affiliation: EBATINCA
  country: Spain

- name: Daniel Palkovics
  affiliation: Semmelweis University
  country: Hungary

- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Majority of currently available deep learning (DL) cone-beam computed tomography (CBCT) segmentation models were trained on data of healthy, completely dentated patients. These models might not produce accurate segmentations of datasets with dentoalveolar hard tissue defects. Our group has perviously developed a Deep Learning-based model for the automatic segmentation of dental cone-beam computed tomography (CBCT) scans which was trained on CBCT images with dentoalveolar pathological processes [1][2]. The current model uses a two-staged SegResNet-based architecture from MONAILabel. Despite of the relatively low sample training data it produced sufficient accuracy (93% compared to semi-automatic segmentation). However, the model's robustness has to be improved. Using the MONAI Auto3DSeg framework and an enlarged training database the project aims to develop an improved model for the automatic segmentation of dental CBCT scans present with dentoalveolar pathological processes. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Develop an improved and robust automatic segmentation model for dental CBCT scans 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Established and enlarged training database with uniformly annotated CBCT data.
2. Decide for an adequate network framework and architecture (MONAI Auto3DSeg?)
3. Come up with an initial configuration of the chosen architecture (stages, options, pre- and post-processing)
4. Perform preliminary training on the available data



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


We have previously trained a two-stage SegResNet-based model for the automatic segmentation of dental CBCT scans. The project was initiated at the 36th project week.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



![Fig1 copy](https://github.com/user-attachments/assets/f681cb64-609c-47dc-8f33-08205141bd6a)
Two-stage SegResNet architecture


![Preop](https://github.com/user-attachments/assets/fb5ac395-64c0-4eb2-ad31-7a70a0a65769)
A: semi-automatic segmentation, B: deep learning segmentation



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


1. Hegyi, A., Somodi, K., Pintér, C., Molnár, B., Windisch, P., García-Mato, D., Diaz-Pinto, A., & Palkovics, D. (2024). Mesterséges intelligencia alkalmazása fogászati cone-beam számítógépes tomográfiás felvételek automatikus szegmentációjára [Automatic segmentation of dental cone-beam computed tomography scans using a deep learning framework]. Orvosi hetilap, 165(32), 1242–1251. [https://doi.org/10.1556/650.2024.33098](https://doi.org/10.1556/650.2024.33098)
2. Palkovics, D., Hegyi, A., Molnar, B., Frater, M., Pinter, C., García-Mato, D., Diaz-Pinto, A., & Windisch, P. (2025). Assessment of hard tissue changes after horizontal guided bone regeneration with the aid of deep learning CBCT segmentation. Clinical oral investigations, 29(1), 59. [https://doi.org/10.1007/s00784-024-06136-w](https://doi.org/10.1007/s00784-024-06136-w)

