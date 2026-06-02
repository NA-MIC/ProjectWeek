---
layout: pw45-project

permalink: /:path/

project_title: 'Cast interface extension for 3D Slicer: Hub,  Resource Servers and Image Display client.'
category: Infrastructure
presenter_location: 

key_investigators:

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Cast interface Module for 3D Slicer: Resource Servers, Image Display client and Hub.

Resource servers: Resource servers subscribe to all user topics for dicom/nifti events and send back results to the user throuh the hub. Each server has its own onMessage script. The script handles producing the results from the DICOM files received and publishes a dicom-send event back to the user topic.

Image Display Client: The image display client provide a PACS client type interface to the 3D slicer viewer. Supported events should be ImagingStudy-open, Imaging-Study-close, dicom-send and request for sceneview. 

Hub: The hub is the server that distributes the messages and handles the data transfer requests over the websocket connection to each client. 





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


 - Provide cloud access to 3D slicer processing services to viewers without running 3D slicer in the cloud. Only the hub needs to be in the cloud. 3D Slicer can connect to the hub and provide the services from anywhere through the websocket connection.
 - Finish the request for SCENEVIEW started in project week 44 by adding an image display client to the 3D slicer viewer.
 - Support 3D Slicer developers who want to connect to cast / FHIRcast.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


 - Implement reource servers with existing 3D slicer modules such as Total Segmentator or Skull Stripper.
 - Implement SCENEVIEW request in the Slicer client



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

Extension repository:
https://github.com/mbellehumeur/SlicerCastInterface/


Online 3D Slicer Hub for project week:
[Slicer Hub](https://slicerhub-azejffgnb7dve8es.canadaeast-01.azurewebsites.net/api/hub/admin)



# Illustrations

<img width="1324" height="857" alt="image" src="https://github.com/user-attachments/assets/a64ed683-e556-45a0-8727-50116f1c9ed1" />

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


VolView using a segmentation resource server:

<!-- should be https://youtu.be/AXadJl0u8g8  -->
<iframe width="800" height="500" src="https://www.youtube.com/embed/AXadJl0u8g8?si=d2dmwfyggzZY5NsB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



# References

Total segmentation:
https://pubs.rsna.org/doi/10.1148/ryai.230024

Skull stripper:
Wasserthal J., Meyer M., , Hanns-Christian Breit H.C., Cyriac J., Shan Y., Segeroth, M.: TotalSegmentator: robust segmentation of 104 anatomical structures in CT images. https://arxiv.org/abs/2208.05868 



