---
layout: pw44-project

permalink: /:path/

project_title: Orbital fracture surgery simulation using SlicerSOFA
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M University College of Dentistry
  country: USA

- name: Rafael Palomar
  affiliation: NTNU / OUH
  country: Norway

- name: Paul Baksic
  affiliation: INRIA
  country: France

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Using SlicerSOFA to simulate orbital fracture repair using titanium plate.

Virtual planning in oral and maxillofacial surgery (OMFS) is primary based on static models using proprietary software for implant customization design and surgical navigation. Soft tissue behaviors were usally unknown. However, physics simulation has not been widely adopted in OMFS virtual planning. One reason is simulation is complex. SlicerSOFA can bridge this gap by integration Slicer and SOFA.

![](https://github.com/user-attachments/assets/b8f775ea-4360-415b-9279-d44d7ecadbd2)
![](https://github.com/user-attachments/assets/da97f07b-c505-4d63-92de-7eeb9a6d89c6)
![](https://github.com/user-attachments/assets/7fe6a8b3-3b5f-45d2-8959-00356edbb846)

[Image source](https://surgeryreference.aofoundation.org/cmf/trauma/midface/orbit-floor/reconstruction#general-considerations)



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Create a demo scene for future development and gathering feedback from surgeons
2. Plan for a grant proposal resubmission.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Work on two separate scenes:

**1. Soft tissue retraction:**
- Goal: move the retractor to create a gap sufficient to insert the plate
- Challenges: collision in a confined space; proper mechanical models of different tissue types
- Creating a single multi-material model

![](https://github.com/user-attachments/assets/8ef946f4-00ff-4e3d-b0ce-126b367299fc)
![](https://github.com/user-attachments/assets/5aa60cab-99d4-48c3-9d09-7eeef7470867)


**2. Plate bending and fixation**
- Meshed plate is geometrically complicated; using shell model as a proxy


**3. Run a demo scene in SlicerSOFA**
- How to integrate Slicer methods to facilitate mechanical model preparation and interaction, such as controller

- Demo scene "tap the eyeball"

 <video
   controls muted
   src="https://github.com/user-attachments/assets/0b93f9aa-dabe-4870-8e73-00c9a834fc28"
   style="max-height:300px; min-height: 200px">
 </video>


**4. Planning for benchmarking and validation: what is considered as "success" at this stage?**




## Progress and Next Steps

### Multimaterial model
1. Create a union model of orbital soft tissue and convert into a tetrahedron mesh.
2. Using the SOFA 'MeshROI' method to use the eyeball-musle polygon model as an ROI to select tetrahedra fell within it, and assign different materials to tets in and out the ROI (i.e., orbital fat).

![](https://github.com/user-attachments/assets/ad88a41a-5459-4bd2-bff5-4f71f3cb65f0)

 <video
   controls muted
   src="https://github.com/user-attachments/assets/80c8c60b-ea99-44da-8d90-975b2f684990"
   style="max-height:500px; min-height: 200px">
 </video>

### Using SlicerSOFA infrastructure and vtkProbeFilter() & grid transform for mesh & image deformation

 <video
   controls muted
   src="https://github.com/user-attachments/assets/a18fb59e-1751-46a9-b317-718834077e70"
   style="max-height:500px; min-height: 200px">
 </video>

### Next step: work on the collision model issue between the retractor and the soft tissue

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Orbital fracture repair introduction: [AO Surgery Reference - Orbital Floor Reconstruction](https://surgeryreference.aofoundation.org/cmf/trauma/midface/orbit-floor/reconstruction#general-considerations)

Related previous PW pages: [Evaluate the fit of preformed plates in orbital surgery
](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/EvaluateTheFitOfPreformedPlatesInOrbitalSurgery/) and [Simulate orbit surgery using SlicerSOFA](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/SimulateOrbitSurgeryUsingSlicersofa/)
