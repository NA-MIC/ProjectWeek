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
 
 
   <img width="273" height="208" alt="image" src="https://github.com/user-attachments/assets/9b4eff43-739f-4785-8ce1-3c0c1c3a8a53" />
 
   <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/fdccb08e-754d-4c26-902d-9fa34e3a48f9" />

   <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/e9f47e26-48c8-4fd5-9815-c7abdffc6ca9" />



3. Add a Cast client to slicer with a [AI prompt that generates the client service](https://github.com/mbellehumeur/cast/blob/main/cast-hub-ai-prompt).
   <img width="618" height="317" alt="image" src="https://github.com/user-attachments/assets/e70ff9da-32c3-453c-981f-f9d9638a0b09" />

   <img width="592" height="516" alt="image" src="https://github.com/user-attachments/assets/cc3eaa71-96a8-4e32-b34b-76731e14f55a" />

  


4. Implement events:
   *  patient-open/close
   *  imagingstudy-open/close
   *  annotation-update (measurements,markups,...)

  One user drving three applications:


  

   Three users working on the same annotation:

      <iframe width="800" height="400" src="https://youtube.com/embed/O-M0Y9JHcoQ" >
      </iframe>
  
  

6. Add a trame-slicer viewport to OHIF with trame-react and configure hanging protocol.
    * Have OHIF with trame-slicer hanging protocol open/close studies (PACS with advanced viewer scenario).

7. Have a multi-user session with OHIF and Slicer (tumor board or attending/resident scenario).
   
<!-- Describe here HOW you would like to achieve the objectives stated above. -->

# Cast
## A Standard for Real-Time Front-End Integration of Healthcare Application 


## Table of Contents

1. [Introduction](#introduction)
2. [Purpose and Scope](#purpose-and-scope)
3. [Architecture Overview](#architecture-overview)
4. [Core Concepts](#core-concepts)
5. [Protocol Specification](#protocol-specification)
6. [Event Types](#event-types)
7. [Data Formats](#data-formats)
8. [Security](#security)
9. [Implementation Guidelines](#implementation-guidelines)
10. [Examples](#examples)
11. [References](#references)

---

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

![Cast-conferencing 001](https://github.com/user-attachments/assets/f8c2c606-b43a-4c8e-9f2d-e29516a688b6)


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

**Cast Variants:**

- **FHIRCast**: Specialized for FHIR resource context management and synchronization
- **DICOMCast**: Specialized for DICOM data exchange and imaging workflow synchronization
- **NAVICast**: Specialized for surgical navigation and real-time guidance systems
- **Other Variants**: The Cast framework is extensible, allowing for domain-specific variants.

All Cast variants share the same core hub-based architecture, protocol, and infrastructure, but define specialized event types and payloads for their specific domains. This allows applications to participate in multiple Cast variants simultaneously, enabling comprehensive workflow integration across different healthcare domains.

---

## Purpose and Scope

### Purpose

Cast enables healthcare applications to:

- **Distribute Events**: Share events of any type across multiple applications in real-time
- **Support Multiple Data Formats**: Handle FHIR resources, DICOM data, OpenEHR, proprietary formats, legacy data structures, and other healthcare standards
- **Support User Interactions**: Broadcast user interaction events for coordinated UI behavior
- **Enable Low-Latency Interactions**: Support bi-directional WebSocket communication for  low-latency interactions, enabling immediate feedback and synchronized collaborative workflows
- **Support Collaborative Multi-User Workflows**: Enable the hub to group multiple users together in sessions, allowing them to share events and synchronize their applications in real-time for collaborative scenarios such as tumor review board meetings.
- **Enable Flexible Integration**: Provide hub-based connectivity where applications only need to connect to the hub (not to each other), enabling applications on different platforms (workstations, mobile devices, web browsers, servers) and locations to seamlessly participate in the same workflow

### Scope

This specification defines:

- The Cast protocol for event distribution and synchronization
- Event types and their payloads
- Subscription and notification mechanisms
- Security requirements
- Data format specifications
- Implementation guidelines

This specification does not define:

- Specific user interface implementations
- Business logic for individual applications
- Data storage or persistence mechanisms
- Network transport protocols (though recommendations are provided)

---

## Architecture Overview

Cast employs a **hub-based publish-subscribe architecture** with the following key components:

### Components

#### Cast Hub

The Cast Hub is a centralized service that:

- Manages subscriptions from applications
- Validates subscription requests
- Receives events from event publishers
- Broadcasts event notifications to all subscribed applications
- Maintains session state and manages connection lifecycle
- **Groups users together within sessions** to enable collaborative multi-user workflows, allowing multiple users to share events and synchronize their applications in real-time

The hub infrastructure provides significant flexibility for integration because **clients do not need to connect directly to each other**—they only need to establish a connection to the hub. This architectural pattern offers several key advantages:

- **Simplified Connectivity**: Applications don't need to know about or maintain direct connections to other applications in the workflow. Each application only needs to connect to the hub, and from there, all other applications in the session can be reached automatically.

- **Platform and Location Independence**: Applications can run on different computers, operating systems, and platforms. For example, a 3D Slicer application running on a workstation can seamlessly communicate with a mobile device application, a web-based viewer, or a server-based PACS system—all through the hub without requiring direct network connections between them.

- **Network Simplification**: The hub acts as a single point of connectivity, eliminating the need for complex peer-to-peer networking, port forwarding, or direct IP address management between applications.

- **Scalability**: New applications can join a workflow session by simply connecting to the hub, without requiring changes to existing applications or network configurations.

#### Event Publisher

An Event Publisher is an application that:

- Publishes events to the Cast Hub
- Can publish any type of event (user interactions, data changes, workflow events, etc.)
- Examples include EHR systems, PACS viewers, clinical applications, and any system that needs to broadcast events

#### Event Subscriber

An Event Subscriber is an application that:

- Subscribes to specific event types
- Receives event notifications from the Cast Hub
- Processes events and takes appropriate action (update UI, synchronize data, trigger workflows, etc.)
- Examples include clinical decision support tools, imaging viewers, documentation systems, and any application that needs to react to events

### Communication Flow

The hub-based architecture eliminates the need for direct peer-to-peer connections:

```
┌─────────────┐         ┌──────────┐         ┌─────────────┐
│   Event     │───────▶│   Cast   │────────▶│   Event     │
│  Publisher  │  Event  │   Hub    │  Event  │ Subscriber  │
│ (3D Slicer) │         │          │         │  (Mobile)   │
└─────────────┘         └──────────┘         └─────────────┘
                              │
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
    ┌────▼────┐         ┌─────▼─────┐        ┌────▼────┐
    │  Event  │         │   Event   │        │  Event  │
    │Subscriber│        │ Publisher │        │Subscriber│
    │  (Web)   │        │  (PACS)   │        │(Workstation)│
    └─────────┘         └──────────┘        └─────────┘
```

**Key Points:**
- All applications connect **only to the hub** (no direct connections between applications)
- Applications can run on **different platforms** (workstations, mobile devices, web browsers, servers)
- Applications can be on **different networks** and locations
- The hub routes events to all subscribed applications automatically

**Flow:**
1. **Subscription Phase**: Applications subscribe to the Cast Hub for specific event types (each app only needs to know the hub's address)
2. **Event Publication**: Event Publisher publishes an event to the Cast Hub
3. **Event Broadcast**: Cast Hub broadcasts the event to all subscribed applications in the session
4. **Event Processing**: Subscribers receive the event and process it according to their needs

This architecture enables flexible integration scenarios, such as:
- A 3D Slicer application on a workstation communicating with a mobile tablet viewer
- A web-based EHR system coordinating with a server-based PACS
- Multiple applications across different networks collaborating in a single session

---

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

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

