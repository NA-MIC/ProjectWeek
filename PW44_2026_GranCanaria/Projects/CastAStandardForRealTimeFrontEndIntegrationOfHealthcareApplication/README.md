---
layout: pw44-project

permalink: /:path/

project_title: Cast - A Standard for Real-Time Front-End Integration of Healthcare Application
category: Infrastructure
presenter_location: 

key_investigators:

- name: Martin Bellehumeur
  affiliation: Bellehumeur Engineering
  country: Germany

- name: Steve Pieper
  affiliation: Isomics
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Standardize  Real-Time Front-End Integration of Healthcare Application 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Continue the development front-end integration of OHIF and Slicer.
2. Use the standard FHIRcast  websocket hub  messaging infrastructure for non-FHIR related data/events and real-time front-end intergration.
3. Enable multi-user workflows.


## Approach and Plan

1. Add  Cast hub API to Slicer Web Server with a [AI prompt that generates the hub](https://github.com/mbellehumeur/cast/blob/main/cast-hub-ai-prompt).

2. Add a Cast client to slicer with a [AI prompt that generates the client service](https://github.com/mbellehumeur/cast/blob/main/cast-hub-ai-prompt).

3. Implement events:
   *  patient-open/close
   *  imagingstudy-open/close
   *  annotation-update (measurements,markups,...)
   *  scene-update

4. Do some scene mirroring using scene-update OHIF/OHIF and OHIF/3DSlicver

5. Have a multi-user session with OHIF and Slicer (tumor board or attending/resident scenario).
   *  Use [OHIF client for  Project Week 44](https://white-hill-0dd101903.6.azurestaticapps.net/)  
   
<!-- Describe here HOW you would like to achieve the objectives stated above. -->


## Introduction

Cast is a standard protocol for real-time client to client event communication across healthcare applications. Built upon the foundational architecture of FHIRCast, Cast extends beyond FHIR-specific data and context management to support a wide range of healthcare data formats, user interactions, controller inputs and event types.
DICOM, DICOMweb, FHIR and HL7v2 are server to server and client to server protocols. 

Cast is a client to client protocol. Client to client protocols differ because they often deal with temporary objects such as user interactions.  Even when FHIR or DICOM data exchange is exchanged, it is usually to refer an existing object or initiate a new object that may or may not be saved to the server.  For example, a DICOM annotation can be communicated but may or may not become part of a DICOM structured report.

Cast serves as an umbrella standard that encompasses specialized variants such as FHIRCast (for FHIR context management), DICOMCast (for DICOM data exchange), NAVICast (for surgical navigation), and other domain-specific implementations. All variants share the same core infrastructure while defining specialized event types for their domains (see [Cast Ecosystem](#cast-ecosystem) below).


### Background

Healthcare environments sometimes involve multiple specialized applications working together to support clinical workflows. These applications need to communicate and coordinate in real-time, sharing events such as user interactions, data exchanges, state changes, and workflow transitions.  A typical scenario is radiology reporting where a worklist, viewer, reporting and EMR integrate to produce the diagnostic report. This workflow is defined in the IHE Integrated Reporting Applications profile.

FHIRcast provides a solid foundation for FHIR-based context management, focusing specifically on synchronizing FHIR resource context across applications. However, the healthcare ecosystem includes many non-FHIR data formats, such as DICOM, openEHR and use cases that extend beyond context management such has navigation controllers, VR controllsers, joysticks and footswitches.  Cast addresses this by providing a flexible, extensible framework that supports:

- **User Interaction Events**: Mouse clicks, keyboard input, 6DOF controller input,  navigation, UI state changes
- **Data Exchange Events**: FHIR, DICOM data synchronization (potentially called DICOMCast), HL7 V2 messages, proprietary formats
- **Workflow Events**: Task assignments, status updates, notifications
- **Any Custom Event Types**: Domain-specific events defined by applications

Cast supports **bi-directional WebSocket communication**. This enables low-latency, "gaming style" interactions where applications can exchange events in real-time with minimal delay, supporting use cases such as collaborative viewing, synchronized navigation, and interventional workflows that require immediate feedback and coordination.

Cast also supports **collaborative multi-user workflows** through the hub's ability to group users together within sessions. The hub can coordinate multiple users, allowing them to share events and synchronize their applications in real-time. This enables scenarios such as tumor board meetings, where multiple radiologists and clinicians can simultaneously view and interact with the same DICOM study, with measurements, annotations, and navigation synchronized across all participants own viewers.


The hub-based architecture provides **flexible integration** because applications do not need to connect directly to each other—they only need to reach the hub. This enables applications running on different platforms and locations to seamlessly participate in the same workflow. For example, a 3D Slicer application running on trame in the cloud can communicate with a mobile device application, a web-based viewer, or local camera control , all through the hub without requiring direct network connections between them.

### Cast Ecosystem

Cast serves as an umbrella standard that encompasses specialized "Cast" variants for different healthcare domains and use cases:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                          │
│                                    Cast                                                  │
│                              (Core Standard)                                             │
│                                                                                          │
│  ┌──────────────────┐  ┌──────────────────────┐  ┌──────────────────┐  ┌────────────┐    │
│  │                  │  │                      │  │                  │  │            │    │
│  │   FHIRCast       │  │     DICOMCast        │  │    NAVICast      │  │   Other    │    │
│  │                  │  │                      │  │                  │  │   Cast     │    │
│  │ FHIR Context     │  │ DICOM Data Exchange  │  │   Surgical       │  │ Variants   │    │
│  │   Management     │  │    (Front-end)       │  │   Navigation     │  │            │    │
│  │                  │  │                      │  │                  │  │(Extensible)│    │
│  └──────────────────┘  └──────────────────────┘  └──────────────────┘  └────────────┘    │
│                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```


## References

### Related Standards

- **FHIRcast**: [http://hl7.org/fhir/fhircast.html](http://hl7.org/fhir/fhircast.html) - The foundational standard upon which Cast is based. Note: FHIRcast focuses on FHIR context management, while Cast extends beyond context to support any type of event including user interactions and DICOM data exchange (DICOMCast).
- **HL7 FHIR**: [http://hl7.org/fhir/](http://hl7.org/fhir/) - Fast Healthcare Interoperability Resources
- **WebSocket**: [RFC 6455](https://tools.ietf.org/html/rfc6455) - The WebSocket Protocol
- **DICOM**: [https://www.dicomstandard.org/](https://www.dicomstandard.org/) - Digital Imaging and Communications in Medicine









## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.




# Illustrations
   <img width="273" height="208" alt="image" src="https://github.com/user-attachments/assets/9b4eff43-739f-4785-8ce1-3c0c1c3a8a53" />
   <img width="1558" height="482" alt="image" src="https://github.com/user-attachments/assets/9f6109fd-287b-4951-86a7-0aa6951591c3" />
<img width="1545" height="1194" alt="image" src="https://github.com/user-attachments/assets/5e6b77d3-3400-4efd-a271-f42863ff115f" />

<img width="1555" height="1188" alt="image" src="https://github.com/user-attachments/assets/4f7a6121-2864-47f2-a877-81f18eb501a2" />

<img width="652" height="891" alt="image" src="https://github.com/user-attachments/assets/0b7894dd-697a-4444-8d47-5f8ebd92d950" />





  One user driving three applications:

  Three users working on the same annotation:

  <iframe width="800" height="400" src="https://youtube.com/embed/O-M0Y9JHcoQ" ></iframe>
  
   
<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

