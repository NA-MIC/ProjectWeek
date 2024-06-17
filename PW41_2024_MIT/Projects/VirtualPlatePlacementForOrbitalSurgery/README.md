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
1. Improving the use of the Interaction Transform Handle and intersection marker to more efficiently adjust plate position so that it sits just above the bone.
2. Design measurements to quantify plate fitness.
3. Deep learning-based segmentation for segmenting fractured orbit.
4. Explore methods such as reinforcement learning and SOFA for actual simulating how the plate is placed.






# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

