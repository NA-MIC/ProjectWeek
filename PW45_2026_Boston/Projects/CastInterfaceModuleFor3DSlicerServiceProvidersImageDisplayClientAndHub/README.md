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

- name: Renzo Phellan Aro
  affiliation: Lunenfeld-Tanenbaum Research Institute, Sinai Health
  country: Canada

- name: Ahmed Rekik
  affiliation: École de technologie supérieure
  country: Canada

- name: Jarrett Rushmore
  affiliation: Center for Morphometric Analysis, Massachusetts General Hospital, Boston
  country: USA

- name: Sylvain Bouix
  affiliation: École de technologie supérieure
  country: Canada
  

---

# Project Description

<!-- Add a short paragraph describing the project. -->



Cast interface Module for Slim and  3D Slicer: Resource Servers, Image Display client and Hub.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


 - Add cast interface to Slim viewer
 - Develop standard desktop integration of AI resources.
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


  Two project week teams integrated their AI resource with VolView and OHIF for lung cancer screening and brain cortex segmentation.
  




# Illustrations

Imaging worklist:

<img width="1278" height="772" alt="image" src="https://github.com/user-attachments/assets/76dbe891-9ef5-49c9-839c-827d4a13cc88" />






Cross-product scene views:


<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/2f7feceb-1e85-4918-9012-220daa5870b0" />









IDC MCP  integration in worlist


<img width="660" height="464" alt="image" src="https://github.com/user-attachments/assets/a1eab181-a5c8-45bf-a67d-182f80ec7bec" />



VolView desktop integration of TotalSegmentator 

<img width="1145" height="891" alt="image" src="https://github.com/user-attachments/assets/e41cd703-b5cd-4a5a-86e9-a547dfcc51ce" />


<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


VolView using a segmentation resource server without DICOM archive:

<!-- should be https://youtu.be/AXadJl0u8g8  -->
<iframe width="800" height="500" src="https://www.youtube.com/embed/AXadJl0u8g8?si=d2dmwfyggzZY5NsB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



# References

Lung cancer screening:
https://projectweek.na-mic.org/PW45_2026_Boston/Projects/ExtractingDeepLearningFeaturesFromCtImagesOfTheThoracicRegionForLungCancerApplications/

Subcortical segmentation:
https://projectweek.na-mic.org/PW45_2026_Boston/Projects/Vox2SeglamProtocolGuidedSubcorticalSegmentationIn3DSlicer/

Total segmentator:
https://pubs.rsna.org/doi/10.1148/ryai.230024
Wasserthal J., Meyer M., , Hanns-Christian Breit H.C., Cyriac J., Shan Y., Segeroth, M.: TotalSegmentator: robust segmentation of 104 anatomical structures in CT images. https://arxiv.org/abs/2208.05868 


 [Cast interface extension repository](https://github.com/mbellehumeur/SlicerCastInterface/)


Online imaging worklist with Slim/OHIF/VolView for project week:
[Imaging worklist with cast interface](https://slicerhub-azejffgnb7dve8es.canadaeast-01.azurewebsites.net/worklist-client/examples/CastClient.html)



