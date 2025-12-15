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


1. Real-time integration of OHIF, Slicer , 6DOF controllers, navigation controllers.
2. Multi-user workflows.




## Approach and Plan

1. Add the Cast hub api to the Slicer Web Server module.
     * Collaborate on a AI prompt that generates the hub.
2. Add an entry for the Cast hub in the Web Server static page for hub admin page.
3. Update the "DICOM Database Browser"  OHIF client with the Cast client extension in the Web Server static page.
    * [OHIF Cast extension](https://github.com/mbellehumeur/fhircast) 
4. Add a Cast client to Slicer and controller devices.
5. Have a multi-user (party line) session with OHIF and Slicer.
   
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
DICOM, DICOMweb, FHIR and HL7v2 are server to server and client to server protocols. Client to client protocols differ because they often deal with temporary objects such as user interactions.  Even when FHIR or DICOM data exchange is exchanged, it is usually to refer an existing object or initiate a new object that may or may not be saved to the server.  For example, a DICOM annotation can be communicated but may or may not become part of a DICOM structured report.

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

**Cast Variants:**

- **FHIRCast**: Specialized for FHIR resource context management and synchronization
- **DICOMCast**: Specialized for DICOM data exchange and imaging workflow synchronization
- **NAVICast**: Specialized for surgical navigation and real-time guidance systems
- **Other Variants**: The Cast framework is extensible, allowing for domain-specific variants such as:
  - LabCast (laboratory workflows)
  - PharmCast (pharmacy workflows)
  - Any other specialized Cast implementation

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

## Core Concepts

### Events

**Events** are notifications that represent any occurrence of interest in a healthcare application. Events have:

- **Event Type**: A string identifier (e.g., `patient-open`, `user-click`, `dicom-study-received`, `workflow-task-assigned`)
- **Timestamp**: When the event occurred
- **Source**: The application that generated the event
- **Payload**: Event-specific data (format varies by event type and use case)

Events can represent:
- User interactions (clicks, keyboard input, navigation)
- Data changes (patient records, imaging studies, documents)
- Workflow events (task assignments, status updates)
- System events (errors, notifications, state changes)
- Custom domain-specific events

### Sessions

A **Session** represents a logical grouping of applications and users working together. All applications in a session can publish and subscribe to events within that session. 

Sessions enable **collaborative multi-user workflows** where the Cast Hub groups multiple users together, allowing them to share events and synchronize their applications in real-time. For example, in a tumor review board meeting, multiple radiologists and clinicians can join the same session, and when one participant navigates to a specific DICOM study or makes a measurement, all other participants' viewers are automatically synchronized to the same view and measurement.

Sessions can be:
- **Single-user sessions**: One user with multiple applications
- **Multi-user sessions**: Multiple users collaborating together, with the hub coordinating event distribution to all participants

### Subscriptions

A **Subscription** is a request from an application to receive notifications for specific event types. Subscriptions include:

- **Event Types**: Which events the application wants to receive
- **Callback URL**: Where to send notifications (for HTTP-based subscriptions)
- **Authentication**: Credentials for secure communication

---

## Protocol Specification

### Transport

Cast supports multiple transport mechanisms:

- **WebSockets**: For real-time, bidirectional communication (recommended). Unlike FHIRcast, Cast fully supports bi-directional WebSocket connections, enabling low-latency "gaming style" interactions where applications can publish and receive events simultaneously with minimal overhead. This is essential for use cases requiring immediate feedback, such as collaborative viewing, synchronized navigation, and interactive workflows.
- **HTTP/HTTPS**: For RESTful API interactions
- **Server-Sent Events (SSE)**: For unidirectional event streaming

### Base URL Structure

```
https://{hub-host}/cast/{version}/
```

Example:
```
https://cast.example.com/cast/v1/
```

### API Endpoints

#### Subscribe to Events

```
POST /cast/v1/subscribe
```

**Request Body:**
```json
{
  "eventTypes": ["patient-open", "study-view"],
  "callbackUrl": "https://app.example.com/cast/callback",
  "sessionId": "session-12345"
}
```

**Response:**
```json
{
  "subscriptionId": "sub-67890",
  "expires": "2024-12-31T23:59:59Z"
}
```

#### Unsubscribe from Events

```
DELETE /cast/v1/subscribe/{subscriptionId}
```

#### Publish Event

```
POST /cast/v1/event
```

**Request Body:**
```json
{
  "eventType": "patient-open",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "ehr-system",
  "sessionId": "session-12345",
  "payload": {
    "patientId": "pat-001",
    "patientName": "John Doe",
    "mrn": "MRN-12345"
  }
}
```

### WebSocket Protocol

Cast's WebSocket protocol supports **full bi-directional communication**, enabling applications to both publish and receive events over the same connection. This is a key differentiator from FHIRcast, which does not support bi-directional WebSockets. The bi-directional capability enables low-latency "gaming style" interactions where events can be exchanged with minimal delay, supporting real-time collaborative workflows.

For WebSocket connections, the protocol uses JSON messages:

**Subscribe Message:**
```json
{
  "action": "subscribe",
  "eventTypes": ["patient-open", "study-view"],
  "sessionId": "session-12345"
}
```

**Publish Event Message (Client to Hub):**
```json
{
  "action": "publish",
  "eventType": "patient-open",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "ehr-system",
  "sessionId": "session-12345",
  "payload": {
    "patientId": "pat-001",
    "patientName": "John Doe"
  }
}
```

**Event Notification Message (Hub to Client):**
```json
{
  "eventType": "patient-open",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "ehr-system",
  "sessionId": "session-12345",
  "payload": {
    "patientId": "pat-001",
    "patientName": "John Doe"
  }
}
```

Applications can simultaneously send events to the hub and receive events from other applications over the same WebSocket connection, enabling true real-time bidirectional communication with minimal latency.

---

## Event Types

Cast defines a set of standard event types, but also supports custom event types for extensibility. Unlike FHIRcast, which focuses on FHIR context events, Cast supports any type of event including user interactions, data exchanges, and workflow events.

### Standard Event Types

#### User Interaction Events

- **`user-click`**: A user clicked on an element
- **`user-navigate`**: A user navigated to a different view or page
- **`user-input`**: A user entered data in a form or field
- **`ui-state-change`**: The UI state changed (e.g., panel opened/closed, tab switched)

**Payload Example:**
```json
{
  "elementId": "patient-search-button",
  "elementType": "button",
  "coordinates": {"x": 150, "y": 200},
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### Patient Events
The exiuting FHIRcast events are:
- **`patient-open`**: A patient record has been opened
- **`patient-close`**: A patient record has been closed


**Payload Example:**
```json
{
  "patientId": "pat-001",
  "patientName": "John Doe",
  "dateOfBirth": "1980-01-15",
  "mrn": "MRN-12345",
  "identifiers": [
    {
      "system": "http://hospital.example.com/mrn",
      "value": "MRN-12345"
    }
  ]
}
```

### Custom Event Types

Applications can define custom event types using the format:

```
{domain}:{event-name}
```

Examples:
```
radiology:worklist-update
pharmacy:medication-review
user:mouse-move
workflow:task-completed
dicom:image-annotation-added
```

The Cast Hub will attempt to provide data in the preferred format, falling back to available formats if necessary.

---

## Security

Security is paramount in healthcare applications. Cast implements multiple security measures to protect Protected Health Information (PHI).

### Authentication

Cast  authentication:

1. Applications authenticate with the enterprise authentication server
2. Access tokens are required for all API calls
3. Tokens are validated on each request
4. Token refresh mechanisms are supported

### Authorization

Authorization is enforced at multiple levels:

- **Subscription Authorization**: Only authorized applications can subscribe to events
- **Event Authorization**: Applications can only publish events they are authorized to publish

### Transport Security

All communications must use:

- **HTTPS**: For HTTP-based communications (TLS 1.2 or higher)
- **WSS**: For WebSocket connections (WebSocket Secure)
- **Certificate Validation**: Proper certificate validation must be implemented

### Data Protection

- **Encryption in Transit**: All data is encrypted during transmission
- **Encryption at Rest**: Cast Hub implementations should encrypt stored data
- **Audit Logging**: All events and access attempts should be logged
- **PHI Minimization**: Only necessary data should be included in events

### Compliance

Cast implementations should comply with:

- **HIPAA**: Health Insurance Portability and Accountability Act
- **HITECH**: Health Information Technology for Economic and Clinical Health Act
- **GDPR**: General Data Protection Regulation (where applicable)
- **Local Regulations**: Applicable regional healthcare data protection laws

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

