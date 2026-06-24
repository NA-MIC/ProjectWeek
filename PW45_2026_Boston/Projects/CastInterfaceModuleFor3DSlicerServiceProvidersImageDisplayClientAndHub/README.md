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


Try the new “Cast Interface” 3D slicer extension to integrate different AI engines with VolView and OHIF without a DICOM server.  

Cast is  an offshoot of FHIRcast (<https://fhircast.hl7.org/>)and is focused on desktop integration workflows for healthcare providers and researchers. It provides a secure event messaging infrastructure using a hub with websocket subscriptions.

The project also integrated with a new IDC MCP server to search for studies in the Imaging Data Commons repository and added cast to the Slim whole slide imaging viewer, VolView, OHIF and the 3D slicer viewer. 

The repository for the slicer extension is here: https://github.com/mbellehumeur/SlicerCastInterface





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


 - Develop standard based desktop integration of AI resources.
 - Add cast interface to Slim viewer
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



VolView desktop integration of AI subcortical segmentation of the brain 

<img width="1162" height="957" alt="image" src="https://github.com/user-attachments/assets/7c8aefc0-d697-4813-9193-53fe08944c99" />

<br><br>


Imaging worklist:

<img width="1278" height="772" alt="image" src="https://github.com/user-attachments/assets/76dbe891-9ef5-49c9-839c-827d4a13cc88" />

<br><br>

Cross-product scene views:


<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/2f7feceb-1e85-4918-9012-220daa5870b0" />

<br><br>

IDC MCP  integration in worlist


<img width="660" height="464" alt="image" src="https://github.com/user-attachments/assets/a1eab181-a5c8-45bf-a67d-182f80ec7bec" />



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



