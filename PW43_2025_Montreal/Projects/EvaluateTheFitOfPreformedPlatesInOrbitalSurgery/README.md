---
layout: pw43-project

permalink: /:path/

project_title: Evaluate the fit of preformed plates in orbital surgery
category: VR/AR and Rendering

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M College of Dentistry

- name: Braedon Gunn
  affiliation: Texas A&M College of Dentistry

- name: Andrew Read-Fuller
  affiliation: Texas A&M College of Dentistry

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Orbital fracture repair commonly used preformed/contoured plates. ProprietaryVirtual Surgical Planning (VSP) soft focused on customized plate manufacture and placement guidance but does not allow comparing the fit of plates across vendors. The goal of this project is to allow surgeons to interactively try different ways of placement or different plates and compare the fit to find the more suitable implant. I created a customized extension [orbiSurgerySim](https://github.com/chz31/orbitSurgerySim).

**Current procedures:**
1. Alignment using the Interaction Transform Handle: rotate around the "posterior stop" landmark until the plate sits just above the. Real-time heatmap using Probe Model with Volume module and VTK collision detector can mark intersections to aid plate position adjustment.

<p>
<img src="https://github.com/user-attachments/assets/b79071c2-5518-418f-9c8e-99d3b005ab35" width="200"/>
<img src="https://github.com/user-attachments/assets/89116733-eb03-4823-b2d5-d836432187d1" width="200"/> <br>
<img src="https://github.com/user-attachments/assets/76affefe-9e47-48c7-aa54-53a65f05f13f" width="200"/>
<img src="https://github.com/user-attachments/assets/50178264-6ab7-4bf8-b596-24dfd9344a5f" width="200"/> <br>
</p>

2. Reconstructing the fractured orbit using the mirror of the contralateral side: use DentalSegmentator to segment the bone. I created a module to streamline reconstruction by using the mirrored contralateral side to rigidly register to fracture side followed by a warping. 

<p>
<img src="https://github.com/user-attachments/assets/bf411572-7a98-462c-ba84-7f8d65859229" width="200"/> 
<img src="https://github.com/user-attachments/assets/790efb9d-8838-4b48-bbd1-0f714eed0da6" width="200"/> 
<img src="https://github.com/user-attachments/assets/65be864e-4556-4bdd-af5b-68371d8c752d" width="200"/> 
<img src="https://github.com/user-attachments/assets/3bebb56c-b7c0-495d-84e1-c5ee6255ee52" width="200"/> 
</p>


3. Measuring fit by projecting fiducial points on plate edges to the reconstructed orbit. Fit is based on overall distances. Overall distance map can also be used. These distances can also be used to highlight largest deviation.

<p>
<img src="https://github.com/user-attachments/assets/62e02a60-b94d-4ddd-9cdb-55e9ffc53cea" width="250"/> 
<img src="https://github.com/user-attachments/assets/c94f156f-c6a8-4570-ac2d-0b20a9021761" width="250"/> <br>
<img src="https://github.com/user-attachments/assets/649076d2-9c08-48e0-8a12-1ce0cead75b6" width="250"/> 
<img src="https://github.com/user-attachments/assets/ed204c08-2bb0-49c4-bd27-f8745a78a337" width="280"/> 
<img src="https://github.com/user-attachments/assets/854b8d7d-04f1-44c4-8173-61de3bc9162f" width="330"/> 
</p>



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The current workflow is tedious. My goal is to simplify the process.
1. Design UI and workflow to streamline the processes
2. Alternative methods for plate registrastion to ensure the plate sits at the surface of the bone (e.g., methods from SlicerHeart).
3. Improve and design additional metrics for measuring the fit of different plates and their ways of placement.
4. Explore additional or improved methods for orbit reconstruction (e.g., using SlicerAntsPy for image deformable registration).


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Same as objectives
2. Simplify segmentation workflows for thin orbital bones. In some cases, the orbital floor and medial wall are too thin, and only a boundary between the sinus and orbit is visible. I segmented maxillary sinus, expand it, and create a shell to fix the orbit. Perhaps models used in DentalSegmentator or TotalSegmentator can be tuned to depict the boundary between sinus & orbit.
<p>
<img src="https://github.com/user-attachments/assets/da70f728-1d4a-45ac-9f0b-5922ba5e4307" width="200"/> 
<img src="https://github.com/user-attachments/assets/176ebcb4-1e35-426e-ae73-d39c4757808f" width="200"/> 
</p>

<p>
<img src="https://github.com/user-attachments/assets/27016320-ba74-433b-a5bb-8e988c395ab5" width="220"/> 
<img src="https://github.com/user-attachments/assets/a65a172e-12f7-47da-ad43-84c3a44dfa7d" width="200"/> 
</p>



## Progress and Next Steps

1. Demonstrated for workflow and collected suggestions for further improvement and simplification
2. Add instant distant map during plate position adjustment. Tried texture map alignment.
3. Add more visual support to highlight differences between different plates
4. Start to collect data from plates from two vendors and prepare for manuscript.





# Illustrations

Johnson&Johnson DePuy Synthesis preformed titanium plate: <br>
<img src="https://github.com/user-attachments/assets/f1402cf8-5581-4835-a829-133c03cfc594" width="300"/>
<img src="https://github.com/user-attachments/assets/8b631448-c285-4c72-8609-75d3190db24f" width="300"/>

<p>
<img src="https://github.com/user-attachments/assets/5c46f298-f059-4c4c-8114-4f21906f9dd2" width="200"/>
</p>
Surgical Guidance using MatrixOrbital preformed plates from DePuy (see below for reference).

<p>
<img src="https://github.com/user-attachments/assets/66a054ca-7751-4fe7-8c82-94ab1da61509" width="200"/>
</p>
Transconjunctival approach for retracting orbital tissue. From: [https://surgeryreference.aofoundation.org/cmf/pediatric-trauma/midface/orbital-floor/reconstruction](https://surgeryreference.aofoundation.org/cmf/pediatric-trauma/midface/orbital-floor/reconstruction)



# Background and References

Initial Project Week version [https://projectweek.na-mic.org/PW41_2024_MIT/](https://projectweek.na-mic.org/PW41_2024_MIT/)

Github for the customized rbitSurgerySim extension: [https://github.com/chz31/orbitSurgerySim](https://github.com/chz31/orbitSurgerySim)

Surgical Guidance using MatrixOrbital preformed plates from DePuy Synthesis: [https://www.jnjmedtech.com/en-US/product/matrixorbital-preformed-orbital-plates](https://www.jnjmedtech.com/en-US/product/matrixorbital-preformed-orbital-plates)

Orbital floor and wall fracture repair guidance: [https://surgeryreference.aofoundation.org/cmf/pediatric-trauma/midface/orbital-floor/reconstruction](https://surgeryreference.aofoundation.org/cmf/pediatric-trauma/midface/orbital-floor/reconstruction)

