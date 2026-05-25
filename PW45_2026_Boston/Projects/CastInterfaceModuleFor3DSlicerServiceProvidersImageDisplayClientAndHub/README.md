---
layout: pw45-project

permalink: /:path/

project_title: 'Cast interface module  for 3D Slicer: Service Providers, Image Display client and
  Hub.'
category: Infrastructure
presenter_location: 

key_investigators:

- name: Martin Bellehumeur
  affiliation: Radical Imaging
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Cast interface Module for 3D Slicer: Service Providers, Image Display client and Hub.

Service Providers: Service providers subscribe to all user topics for dicom events and send back results to the user. Each service provider has its own onMessage script. The script handles producing the results from the DICOM files received and publishes a dicom-send event back to the user topic.

Image Display Client: The image display client provide a PACS client type interface to the 3D slicer viewer. Supported events should be ImagingStudy-open, Imaging-Study-close, dicom-send and request for sceneview. 

Hub: The hub is the server that distributes the messages and handles the data transfer requests over the websocket connection to each client. 





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


 - Provide cloud access to 3D slicer processing services to viewers without running 3D slicer in the cloud. Only the hub needs to be in the cloud. 3D Slicer can connect to the hub and provide the services from anywhere through the websocket connection.
 - Finish the request for SCENEVIEW started in project week 44 by adding an image display client to the 3D slicer viewer.
 - Support 3D Slicer developers who want to connect to cast / FHIRcast.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


 - Implement service providers with existing 3D slicer modules such as Total Segmentator or Skull Stripper.
 - Implement SCENEVIEW request in the Slicer client



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Online example:
<https://examples-vtkjs.d2pxx3mhr69djy.amplifyapp.com/examples/CastClient.html>




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


VolView using a segmentation service provider:


<iframe width="800" height="500" src="https://www.youtube.com/embed/hxk0FvQMyb8?si=d2dmwfyggzZY5NsB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Cast  Interface Module:

<img width="756" height="804" alt="image" src="https://github.com/user-attachments/assets/edaccdd0-3c25-4dce-b356-b375af9d97fd" />




Cast hub: 

<img width="1253" height="892" alt="image" src="https://github.com/user-attachments/assets/e99f55c1-0448-4bf9-97c4-55424eb3ca2d" />




# Background

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


What is Cast?
Cast is an offshoot of FHIRcast (<https://fhircast.hl7.org/>). FHIRcast is the standard replacing Epic’s file drop interface for integration with PACS and reporting systems. It provides a secure messaging infrastructure using a hub with websocket subscriptions.

Cast differs to FHIRcast in the following way:

Mission: 
Cast is focused on desktop integration of healthcare applications. It is not restricted to a specific data format.  Cast is also not restricted to a specific authentication mechanism; it expects that apps will authenticate with the customer's system. Cast aims to provide a general framework that can support all use cases by adding data types with verbs (events), for example, nifti-send.




Features: 
In addition to FHIRcast events, the cast hub allows the following:

 - Request data from applications such as worklist context, report content, DICOM instance, DICOM tag, JPEG/PNG screenshots, scene views, etc.

 - Support for binary files transfer; therefore payloads other than FHIR/JSON, such as DICOM, PNG, NIFTi, openEHR, OpenIGTLink.

 - Group topics for multi-user workflows, such as tumor boards or interventional procedures.
Support for IHE roles.

 - Support three additional subscription data: 
 -- subscriber.product.name, 
 -- subscriber.product.version,
 -- subscriber.actors
 
 - Support four additional event data: 
 -- subscriber.name
 -- subscriber.actor
 -- target.actor
 -- target.product.name


For testing and development, the hub provides a test mock auth endpoint that assigns a user  when none is provided.  A “single-user” mode is available for stand-alone applications that do not use authentication.   The hub mock auth endpoints are the same as keycloak to facilitate integration.



Hub availability and complexity are possibly  the main obstacle to the deployment of this technology; therefore the hub is kept as simple as possible and only handles message handling. The cast_api.py script used for  Volview server and 3D slicer is @2000 lines and the admin.html portal as well.


The cast hub does not support context management.  Context is to be retrieved from the relevant applications directly through the request mechanism.   In cast, the hub is a routing appliance only.  It does not look at event data; it has no storage or database;  only distribution logic.  
## Security Architecture Benefits

This architecture protects service providers by eliminating direct inbound internet exposure entirely.

Each service provider establishes only **outbound encrypted connections** to the Cast Hub, which functions exclusively as a lightweight **routing and session coordination appliance**. Because no inbound ports need to be opened on hospital or enterprise networks, the service providers remain protected behind existing firewalls and are never directly reachable from the public internet.

The Cast Hub maintains:

- No persistent storage
- No database
- No long-term data retention
- No exposed clinical infrastructure

This significantly reduces the overall attack surface and minimizes operational security risk.

<img width="1535" height="1024" alt="image" src="https://github.com/user-attachments/assets/9b6d7d2b-70db-487c-b01c-ad461d6ca5d7" />





The context management paradigm was tried 30 years ago with CCOW ( <https://en.wikipedia.org/wiki/CCOW> ).  We have to acknowledge that today all advanced radiology integrations function without it. They manage with a combination of file drops, postMessage, URL with parameter, exe with command-line parameters and socket to to socket.  

There is value being able to obtain real-time  information from applications in the workfow.  For example, knowing the "sceneview" status of an Image Display application or the actual current content of the report which can be different than what a FGHIRcast hub would know since it is relies on getting events which are not generated for each keystoke/click.  
<https://projectweek.na-mic.org/PW44_2026_GranCanaria/Projects/CastAStandardForRealTimeFrontEndIntegrationOfHealthcareApplication/>


VolView cast interface:

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/a2913844-0202-40bb-b52c-4cf45d26fc82" />

VTK-JS worklist cast client example:
 <iframe width="800" height="500" src="https://www.youtube.com/embed/MUagLJ5HHG0?si=ciSN9c_wLSfpc3X9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


# References

Total segmentation:
https://pubs.rsna.org/doi/10.1148/ryai.230024

Skull stripper:
Wasserthal J., Meyer M., , Hanns-Christian Breit H.C., Cyriac J., Shan Y., Segeroth, M.: TotalSegmentator: robust segmentation of 104 anatomical structures in CT images. https://arxiv.org/abs/2208.05868 



