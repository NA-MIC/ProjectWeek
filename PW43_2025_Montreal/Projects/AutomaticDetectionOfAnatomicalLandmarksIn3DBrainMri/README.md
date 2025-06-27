---
layout: pw43-project

permalink: /:path/

project_title: Automatic Detection of Anatomical Landmarks in 3D Brain MRI
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Ahmed Rekik
  affiliation: École de Technologie Supérieure
  country: Canada

- name: Sylvain Bouix
  affiliation: École de Technologie Supérieure
  country: USA

- name: Jarrett Rushmore
  affiliation: 'Boston University Medical '
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project aims to automate the detection of 12 anatomical landmarks in T1-weighted brain MRI volumes using deep learning techniques. These landmarks assist neuroanatomists in the manual segmentation of complex brain regions, reducing the time and variability involved in manual annotation.





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Develop and validate a deep learning model capable of accurately localizing 12 anatomical landmarks in 3D T1w MRI, with the goal of supporting expert-guided neuroimaging annotation.





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


- Validate a ground truth dataset consisting of 12 manually annotated anatomical landmarks on 3D T1-weighted brain MRIs.

- Adapt the PIN (Patch-based Iterative Network) model .

- Build a statistical shape model using Principal Component Analysis (PCA).

- Adapt and implement a Global-to-Local approach as an alternative method for landmark detection.

- Compare the predictions and performance of PIN and the Global-to-Local model.

- Validate the final selected model using an external dataset containing a different set of landmarks to assess generalizability.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


**Progress so far:**

> Assembled a dataset of 100 T1-weighted brain MRI volumes with 12 manually annotated landmarks per subject.

>  Converted the data to the format required by the PIN pipeline (normalized volumes, voxel-based coordinates).

>  Adapted key components of the PIN codebase: input_data.py, train.py, infer.py, and shape_model_func.py.

>  Built a shape model using PCA and verified shape vector consistency.

> `Trained the PIN model with uncertainty-weighted loss; training loss steadily decreased to ~8000.

> Debugged inference issues related to patch cropping and out-of-bounds landmarks.

**Next steps:**

>  Improve robustness during prediction.

>  Implement and adapt the Global-to-Local approach for our 12-landmark dataset.

>  Compare landmark prediction accuracy between PIN and Global-to-Local models.

>  Validate the chosen model on an external landmark dataset with different anatomical structures.

>  Visualize landmark predictions and generate error metrics to support discussion with neuroanatomy experts.





# Illustrations

![1](https://github.com/user-attachments/assets/a0b3aefa-b304-4f8b-9c72-2bf83dd4564c)

![2](https://github.com/user-attachments/assets/23996352-97ab-4291-9e17-6f8a5d8505ce)


![3](https://github.com/user-attachments/assets/90b751d8-47e8-4321-a439-3081f8ed08ec)


![4](https://github.com/user-attachments/assets/81c5257a-f68b-45f1-911a-43705a197ce5)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


> PIN – Patch-based Iterative Network
Li, Y., et al. (2018). Fast Multiple Landmark Localisation Using a Patch-Based Iterative Network. In Frangi, A., Schnabel, J., Davatzikos, C., Alberola-López, C., Fichtinger, G. (Eds.), MICCAI 2018, LNCS, vol. 11070. Springer, Cham.
[https://doi.org/10.1007/978-3-030-00928-1_64](https://doi.org/10.1007/978-3-030-00928-1_64)

> Global-to-Local Landmark Detection
Noothout, J. M. H., et al. (2020). Deep Learning-Based Regression and Classification for Automatic Landmark Localization in Medical Images. IEEE Transactions on Medical Imaging, 39(12), 4011–4022.
[https://doi.org/10.1109/TMI.2020.3009002](https://doi.org/10.1109/TMI.2020.3009002)

> CABLD Dataset – Cortical and subcortical Annotation of Brain Landmarks Dataset
Salari, S., Harirpoush, A., Rivaz, H., & Xiao, Y. (2023). CABLD: Contrast-Agnostic Brain Landmark Detection with Consistency-Based Regularization.
Department of Computer Science and Electrical Engineering, Concordia University, Montréal, Canada.
[https://doi.org/10.48550/arXiv.2411.17845](https://doi.org/10.48550/arXiv.2411.17845)

