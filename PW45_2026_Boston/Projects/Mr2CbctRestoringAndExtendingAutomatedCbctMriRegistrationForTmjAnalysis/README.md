---
layout: pw45-project

permalink: /:path/

project_title: 'MR2CBCT: Restoring and Extending Automated CBCT-MRI Registration for TMJ Analysis'
category: DICOM
presenter_location: 

key_investigators:

- name: Eduardo Duarte Caleme
  affiliation: University of North Carolina
  country: USA

- name: Lucia Cevidanes
  affiliation: University of North Carolina
  country: USA

- name: Paul Dumont
  affiliation: University of North Carolina
  country: USA

- name: Alex Buisson
  affiliation: University of North Carolina
  country: USA

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Gaelle Leroux
  affiliation: CPE Lyon
  country: France

- name: Juan Prieto
  affiliation: University of North Carolina
  country: USA

- name: Alban Gaydamour
  affiliation: CPE Lyon
  country: France

---

# Project Description

<!-- Add a short paragraph describing the project. -->


MRI-to-CBCT registration remains a pressing challenge in medical imaging. Simultaneous visualization of hard and soft tissue structures benefits both clinicians and patients in the diagnosis of temporomandibular degenerative joint disease. Challenges remain in accurately registering these two modalities due to differences in intensity distributions that complicate mutual information optimization, as well as the necessity for initial manual alignment, which can prove unintuitive and challenging for clinicians using current 3D Slicer tools.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Fix issues with the current registration pipeline that impede it from producing appropriate outputs.
2. Implement clinician-friendly manual registration tools.
3. Expand options in both fully automated and clinician-in-the-loop workflows for multi modal registration between MRI and CBCT.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Present the restored MR2CBCT pipeline and validated results to the community.
2. Explore improved Elastix parameter strategies to increase the capture range beyond the current limits.
3. Present, test, and optimize the new clinician-friendly manual registration tools.
4. Discuss validation framework design.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Fixed a critical bug in AREG_MRI.py where process_images() was never called.
2. Fixed naming convention restrictions throughout the pipeline that proved unintuitive for clinicians.
3. Fixed a mask size mismatch crash in apply_mask.py and a left/right label swap in TMJ crop side detection.
4. Implemented clinician-friendly manual approximation tools, featuring options to freely translate the volume by dragging in slice views, rotate by dragging the circle edge, set a custom center of rotation, and center the MRI at the CBCT center of mass for extremely distant cases. This makes registration significantly easier and more accessible to clinicians and students.
5. Successfully ran the registration pipeline on 25 cases outside of the initial validation sample, yielding clinically satisfying results.
6. *Next Steps:* Robust automated approximation, increased Elastix capture range, and quantitative validation utilizing Target Registration Error (TRE).



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


No response



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


<video
  controls muted
  src="https://github.com/user-attachments/assets/560a90e5-ccc9-4ec8-be45-7606dc6c3080"
  style="max-width:800px">
</video>

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/6ff6b1e8-a796-4fd8-8bec-5be64b6bd389" />

Initial images

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/849362f2-ee53-43a8-8d8a-786ce34f3f90" />

Center MRI on CBCT function

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/f8aa1b2d-785f-422d-9fc3-d4350c1f5b37" />

Clinician manual registration

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/eae12ffd-e920-4a57-8eea-9da554c7894a" />

Elastix Refinement

