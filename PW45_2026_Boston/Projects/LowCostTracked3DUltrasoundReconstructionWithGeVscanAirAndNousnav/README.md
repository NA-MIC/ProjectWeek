---
layout: pw45-project

permalink: /:path/

project_title: Low-Cost Tracked 3D Ultrasound Reconstruction with GE Vscan Air and NousNav
category: IGT and Training
presenter_location: 

key_investigators:

- name: Amirali Azimi
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Alexandra Golby
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Colin Galvin
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Intraoperative brain shift reduces the accuracy of neuronavigation systems that rely on preoperative imaging. Updated intraoperative imaging can help restore navigation accuracy, but technologies such as intraoperative MRI and conventional cart-based ultrasound systems are not available in many surgical environments.

We are developing a lower-cost workflow for tracked three-dimensional ultrasound reconstruction using the wireless GE Vscan Air CL ultrasound probe and NousNav, an open-source neuronavigation platform implemented in 3D Slicer. During an ultrasound sweep, NousNav uses an optical tracking system to record the position and orientation of both the ultrasound probe and a patient reference frame. The goal is to associate each two-dimensional ultrasound frame with the corresponding tracking transform, position the frames correctly in three-dimensional space, and reconstruct them as a navigable three-dimensional ultrasound volume.

A proof-of-concept reconstruction has already been performed using ultrasound images acquired through the Vscan Air mobile application and tracking data transmitted using the PLUS Toolkit and SlicerIGT. However, the current workflow relies on screen-recorded ultrasound video, which reduces image quality and makes precise synchronization between ultrasound frames and tracking data difficult. Several additional components remain unresolved, including calibration of the ultrasound image plane relative to the tracked probe, registration of the reconstructed ultrasound volume to the patient coordinate system using the tracked reference frame, and integration of the current Python-based NIfTI reconstruction process directly into the 3D Slicer environment.

During Project Week, we aim to develop and evaluate a more reliable and integrated workflow for ultrasound image acquisition, timestamp synchronization, probe calibration, patient registration, three-dimensional reconstruction, and visualization within 3D Slicer and the broader open-source image-guided therapy ecosystem.

<img width="439" height="323" alt="Image" src="https://github.com/user-attachments/assets/12452a63-c54c-45cb-b8a9-0aba551dcd86" />

<img width="666" height="374" alt="Image" src="https://github.com/user-attachments/assets/3d86af47-6143-4b76-9d00-d9efafb4a308" />



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement and validate ultrasound probe calibration and patient-coordinate registration, enabling each ultrasound frame to be placed accurately within the navigation coordinate system.
2. Integrate the current Python-based 3D reconstruction pipeline into 3D Slicer to generate and visualize a navigable three-dimensional ultrasound volume without relying on a separate offline NIfTI-generation process.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Review and organize the existing proof-of-concept pipeline, including the Vscan Air screen-recorded ultrasound data, PLUS Toolkit tracking stream, probe and reference-frame transforms, and the current Python-based NIfTI reconstruction code.
2. Develop a frame-extraction and timestamping workflow for the ultrasound video, and evaluate methods for matching each ultrasound frame with the closest corresponding probe and reference-frame tracking transform.
3. Implement ultrasound probe calibration to determine the spatial relationship between the tracked probe marker and the ultrasound image plane, and evaluate the calibration using a phantom or known target geometry.
4. Establish the complete transformation chain between the ultrasound image, tracked probe, reference frame, patient, and 3D Slicer coordinate systems so that each ultrasound frame can be positioned correctly in the navigation space.
5. Transfer the current Python reconstruction process into the 3D Slicer environment, either as a Python scripted module or an integrated processing workflow, to reduce dependence on external offline processing.
6. Reconstruct the synchronized ultrasound frames into a 3D volume and visualize the resulting volume together with the patient imaging and tracked instruments in 3D Slicer.
7. Evaluate the reconstructed volume for spatial consistency, image orientation, dimensions, frame placement, and alignment with the phantom or patient reference coordinate system.
8. Document the complete acquisition, synchronization, calibration, registration, reconstruction, and visualization workflow, including remaining limitations and requirements for future real-time integration with the GE Vscan Air system.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Developed an initial proof-of-concept application for recording Vscan Air ultrasound video and NousNav tracking data during the same acquisition.
2. Implemented collection of ultrasound probe and reference-frame tracking transforms through PLUS and OpenIGTLink.
3. Created an initial workflow for extracting ultrasound frames from the recorded video and approximately matching them with tracking timestamps.
4. Developed a preliminary Python-based reconstruction method for placing ultrasound frames in 3D space and exporting the result as a NIfTI volume.
5. Generated early proof-of-concept reconstructions that can be viewed in 3D Slicer, but the spatial accuracy and reliability of the workflow have not yet been validated.

<img width="1056" height="578" alt="Image" src="https://github.com/user-attachments/assets/f22242e4-e021-48a3-a82d-bdb00ddfd357" />
<img width="1118" height="559" alt="Image" src="https://github.com/user-attachments/assets/5172f187-588a-4f4a-872a-edb60e255742" />



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

