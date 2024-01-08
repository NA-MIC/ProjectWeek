---
layout: pw40-project

permalink: /:path/

project_title: virtual metal plate registration for orbital fracture
category: Other
presenter_location: Online

key_investigators:

- name: Chi Zhang, PhD
  affiliation: Texas A&M University School of Dentistry
  country: USA

- name: Andrew Read-Fuller, MD, DDS
  affiliation: Texas A&M University School of Dentistry
  country: USA

- name: Braedon Gunn
  affiliation: Texas A&M University School of Dentistry
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Orbital fracture usually involve large areas in the floor and medial wall of the orbit. During surgery, surgeons usually remove cracked floor and medial wall of the orbit and use the plate to reconstruct the orbit. Thus, we aim to develop a module for register 3D model of preformed metal plates to orbital fracture sites for surgical planning and measuring the adaptability of plates to patients. **The registered plate should sit just above the unfractured bone of the orbit.**
![Screenshot 2024-01-07 at 7 15 58 PM](https://github.com/NA-MIC/ProjectWeek/assets/80793828/57ac9554-c731-4469-ae0d-96c396b80331)

![Screenshot 2024-01-07 at 7 49 41 PM](https://github.com/NA-MIC/ProjectWeek/assets/80793828/1d87c9e6-fddc-40d8-96d7-eb1703b8ddf4)

(MatrixORBITAL™ Preformed Orbital Plates)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Simulate the process of how surgeons would place the plate to fracture sites: 

    - Plate can only rotate as it is fixed at the landmark "posterior stop, which marks the orbital process of the palatine bone. This area is usually preserved in orbital fracture cases and the most important landmark to screw the plate.
    - ![image](https://github.com/NA-MIC/ProjectWeek/assets/80793828/ce362a75-ca3b-4953-94ff-20015473d77a)
    - ![image](https://github.com/NA-MIC/ProjectWeek/assets/80793828/5c795578-a7ad-4dc7-9ff8-6d9774f17ed2)


    - Allow the plate sit above the unfractured area of the orbit rather than being superimposed with the orbit.
  
      
2.  Interactive tool for fine tuning the plate registration, such as adding an interactive handler for the 3D model.

3.  Automated segmentation of the fractured orbit as a future goal.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Using Fiducial Registration Wizard to do a pre-registration of the plate to the fractured orbit, then further registration the posterior stop landmark on the plate to the actual posterior stop on the orbit.
2.  Improved registration based on only allow the plate to rotate around the posterior stop: select more surgical landmarks at the peripheral areas of the orbit and the plate. Register the plate again with it pivoted on the posterior stop.
3.  Further refined registration to allow the plate to sit above the unfractured bone of the orbit.
4.  Add an interactive handler for adjusting the plate manually.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Currently making the landmark set of the plate to allow it only rotates around the posterior stop until the squared error with the orbital landmark set is minimized.
2.  The challenging is to further rotate the plate until it sits above the unfractures bone of the orbit.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Previous studies rely on commercial software BrainLab iPlan, and appears to be manual adjustment in a virtual environment: e.g., Schreurs et al. 2017: <https://doi.org/10.1371/journal.pone.0150162>

*No response*
