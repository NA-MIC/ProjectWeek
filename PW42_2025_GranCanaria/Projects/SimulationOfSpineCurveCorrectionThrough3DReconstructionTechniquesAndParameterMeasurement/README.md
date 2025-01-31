---
layout: pw42-project

permalink: /:path/

project_title: Simulation of Spine Curve Correction Through 3D Reconstruction Techniques and Parameter
  Measurement
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Cristina Soriano
  affiliation: Digital Anatomics SL
  country: Spain

- name: Maria Ordieres
  affiliation: Digital Anatomics SL
  country: Spain

- name: Javier Pascau
  affiliation: Universidad Carlos III de Madrid
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Digital Anatomics is a company focused on the devolpment of solutions in the field of personalized medical surgeries, specially in the area of the spine. In this project we would like to explore the reconstruction of personalized spine models from 2D imaging. We are currently developing a neural netkwork for this reconstruction task.
Using 3D Slicer as a tool for modeling and parameter measurement, we aim to apply the obtained information to perform precise patient curve measurements, simulate curve correction procedures, design detailed surgical plans, and assess post-operative outcomes. This approach will provide valuable insights to improve decision-making and enhance the precision of spinal surgeries.






## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Obtain DRR projections from CT scans for the obtention of paired training data
2. Obtain precision measurmets for the 3D reconstructions (specially focused on the pedicle region)
3. Automatize landmark indentification on the 2D image  for the Cobbs angle measurment and study the correlation with the reconstructed vertebrae curvature






## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
We would like to generate a slicer extension that allows us to visualize and study the correlation between the 2D and 3D images and automatically obtain spine curve measurements.






## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Generate a custom layout for the joint visualization of:

      a. Lateral XRay plus sagittal CT slices

      ![image](https://github.com/user-attachments/assets/4a94d739-baae-4e0f-b2ef-08d231fd27b4)


      b. AP XRay plus coronal CT slices
      ![image](https://github.com/user-attachments/assets/ec6dc6aa-eb9f-4d86-a75d-cb8a06fb59c1)


2. Automatically compute the landmarks for each vertebral segmentation

  ![image](https://github.com/user-attachments/assets/ca8b7702-8cd1-4ed8-b6ce-a505e49333ab)
3. Compute the curvature measurements and show them on the images: we have implemented the computation of 2D angles (Cobbs angle & Kyphosis/Lordosis curvature)

![image](https://github.com/user-attachments/assets/1e5bad4d-957c-4e4a-beae-cee2c337ef90)

![image](https://github.com/user-attachments/assets/be8dbc1a-2a2b-47a0-900d-15d31227847f)

Next steps:
 · Compute the 3D curvature by interpolating the vertebral centers of mass and study the correlation with the 2D curvatures



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



<!-- Uploading "image.png"... -->
![Image](https://github.com/user-attachments/assets/0a21a2ac-2506-4410-9938-ddb537aa870f)
**3D reconstruction from 2D X-rays**
<!-- Uploading "image.png"... -->

![Image](https://github.com/user-attachments/assets/b292a716-6661-47fd-aaaa-c36d0deb0b2a)
**Landmark detection and cobbs angle measurement**
<!-- Uploading "image.png"... -->

![image](https://github.com/user-attachments/assets/bf310de0-a58d-414e-8222-bec0a382281f)
**Curve correction simulation**

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_
