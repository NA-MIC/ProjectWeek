---
layout: pw41-project

permalink: /:path/

project_title: Virtual plate placement for orbital surgery
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Chi Zhang
  affiliation: Texas A&M University School of Dentistry
  country: USA

- name: Kyle Sunderland
  affiliation: Queen's University, Canada

- name: Rafael Palomar
  affiliation: Oslo University Hospital / NTNU, Norway 

- name: Braedon Gunn
  affiliation: Texas A&M University School of Dentistry
  country: USA

- name: Andrew Read-Fuller
  affiliation: Texas A&M University School of Dentistry
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We are developing a Slicer module to simulating registering titanium plate to orbital fracture sites to aid surgical planning and investigating the fitness of different commercial preformed plates across a large sample of patients.





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Make a module to allow the plate to properly sits above the bone at the orbital fracture site


<img width="350" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/33c83ae5-5634-4f11-9a25-2a2b0e8f9087">





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


See below.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


I have complied existing methods in Slicer and VTK into one preliminary module [https://github.com/chz31/surgical_plate_registration](https://github.com/chz31/surgical_plate_registration) to do the semi-automatic registration:

<img width="300" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/ea8a640f-883f-4ad7-98b9-aee000c6d327">

1. An initial fiducial registration and a refined registration based on only allowing the plate to rotate while pivoting on the posterior stop, an important landmark for place the nail.

**2. Use `VTKCollisionDetector()` and intersect marker to detect collision and mark the intersection** 
<img width="500" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/447f572c-8fa9-4deb-998d-7b6b469b1802">

**3. Use `Probe Volume with Model ` to paint both the orbit and the plate to mark the overlapping areas.**
<img width="300" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/9dd2ac18-bde5-433c-a675-5460aeb4a324">

**4. Use the new Interaction Transform Handle to manually fine tune the position**
<img width="500" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/efbf149c-71ac-43a1-8608-710dceacdf09">

**7. Update new intersection and overlapping areas until they ar minimized.**
<img width="500" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/19532437-d6d5-4678-a60e-944e2b4641ab">


**Next steps:**
1. Improving the use of the Interaction Transform Handle and intersection marker to more efficiently adjust plate position so that it sits just above the bone. Converting transform matrix into standard descriptor: yaw, roll, and pitch.
<img width="300" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/6ebf2b69-7a9c-4f8f-a3eb-1c236615f390">
(from https://doi.org/10.1371/journal.pone.0150162)

3. Design measurements to quantify plate fitness. Comparing the shape of the plate with the unfractured orbit.

4. Automated segmentation for segmenting fractured orbit.

5. Explore methods such as reinforcement learning and SOFA for actual simulating how the plate is placed.


## PW Progress
Being able to use interaction handle to rotate the plate and real-time update colomap to highlight intersection and report intersection. This can provide visual aid for manual adjustment of plate position

<img width="300" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/4f25bd9b-df51-4a84-b289-3a8032b90525"> <img width="250" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/3f5562b5-eaa5-4f5b-82ad-6b57a6cfa6e0">
<img width="300" alt="image" src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/1ce948e5-0ac3-4b0f-a095-d216dc4d733b">

# Video demo:
<video
  controls muted
  src="https://github.com/NA-MIC/ProjectWeek/assets/80793828/93b2d951-ac39-47e4-8613-d1f427291667"
  style="max-height:640px; min-height: 200px">
</video>

https://youtu.be/4no8vEyKo5s


## Next steps
1. Refine color-map and details for visual aid
2. Working with Rafael for using Slicer-SOFA:
   - Deforming the plate:
   - Simulating plate failure (e.g. the bone area for screwing the plate damaged and plate became loose; adapting/bending poor fitted plate introduces metal fatigue)
   - Including soft-tissue
3. Segmentation of fractured orbit?



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

The repo for the current module: [surgical_plate_registration](https://github.com/chz31/surgical_plate_registration)
Other studies using commercial software iPlan from BrainLab, which should still be based on manual adjustment: [Schreur et al. 2017](https://doi.org/10.1371/journal.pone.0150162) and [Schreur et al. 2021](https://doi.org/10.1016/j.cxom.2020.10.003)

