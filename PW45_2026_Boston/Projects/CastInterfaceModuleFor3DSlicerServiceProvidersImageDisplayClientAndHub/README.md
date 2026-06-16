---
layout: pw45-project

permalink: /:path/

project_title: 'Cast interface extension for  Slim and 3D Slicer: Hub,  Resource Servers and Image Display client.'
category: Infrastructure
presenter_location: 

key_investigators:

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->



Cast interface Module for Slim and  3D Slicer: Resource Servers, Image Display client and Hub.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


 - Add cast interface to Slim viewer
 - Develop standard desktop integration of AI resources like Total Segmentator.
 - Finish the request for SCENEVIEW started in project week 44 by adding an image display client to the 3D slicer viewer.
 - Support 3D Slicer developers who want to connect to cast / FHIRcast.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


 - Implement resource servers concept. 
 - Implement SCENEVIEW request in the Slicer image display client
 - Implement cast interface in Slim



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

 [Cast interface extension repositoty](https://github.com/mbellehumeur/SlicerCastInterface/)


Online imaging worklist (vtk.js IO module cast interface example) with Slim/OHIF/VolView for project week:
[Imaging worklist with cast interface](https://slicerhub-azejffgnb7dve8es.canadaeast-01.azurewebsites.net/worklist-client/examples/CastClient.html)



# Illustrations

Imaging worklist:


<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/a6e46b10-97ae-4558-a802-ab067317bf54" />





Cross-product scene views:


<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/2f7feceb-1e85-4918-9012-220daa5870b0" />






VolView desktop integration of TotalSegmentator 

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/18fc3eda-44bf-47e1-84cc-9e988e3b568d" />


<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


VolView using a segmentation resource server without DICOM archive:

<!-- should be https://youtu.be/AXadJl0u8g8  -->
<iframe width="800" height="500" src="https://www.youtube.com/embed/AXadJl0u8g8?si=d2dmwfyggzZY5NsB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



# References

Total segmentator:
https://pubs.rsna.org/doi/10.1148/ryai.230024

Wasserthal J., Meyer M., , Hanns-Christian Breit H.C., Cyriac J., Shan Y., Segeroth, M.: TotalSegmentator: robust segmentation of 104 anatomical structures in CT images. https://arxiv.org/abs/2208.05868 



