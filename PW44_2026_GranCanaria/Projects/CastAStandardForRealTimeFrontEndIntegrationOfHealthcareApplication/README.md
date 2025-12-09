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


1. Real-time integration of OHIF and Slicer 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
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

Cast is a standard protocol for enabling real-time event synchronization and communication across multiple healthcare applications. Built upon the foundational architecture of FHIRcast, Cast extends beyond FHIR-specific data and context management to support a wide range of healthcare data formats, user interactions, and event types.

It serves as an umbrella standard that encompasses specialized variants such as FHIRCast (for FHIR context management), DICOMCast (for DICOM data exchange), NAVICast (for surgical navigation), and other domain-specific implementations. All variants share the same core infrastructure while defining specialized event types for their domains (see [Cast Ecosystem](#cast-ecosystem) below).

The primary goal of Cast is to enable seamless, real-time coordination between disparate healthcare applications through a flexible event-driven architecture that supports diverse use cases beyond traditional CCOW based context synchronization.

### Background

Healthcare environments typically involve multiple specialized applications working together to support clinical workflows. These applications need to communicate and coordinate in real-time, sharing events such as user interactions, data exchanges, state changes, and workflow transitions.

FHIRcast provides a solid foundation for FHIR-based context management, focusing specifically on synchronizing FHIR resource context across applications. However, the healthcare ecosystem includes many non-FHIR data formats, such as DICOM, proprietary systems, legacy applications, and use cases that extend beyond context management. Cast addresses this by providing a flexible, extensible framework that supports:

- **User Interaction Events**: Mouse clicks, keyboard input, navigation, UI state changes
- **Data Exchange Events**: DICOM data synchronization (potentially called DICOMCast), HL7 messages, proprietary formats
- **Workflow Events**: Task assignments, status updates, notifications
- **Any Custom Event Types**: Domain-specific events defined by applications

Unlike FHIRcast, Cast is not limited to context management or FHIR data. It provides a general-purpose event distribution mechanism that can be used for any type of real-time communication between healthcare applications.

A key technical differentiator is Cast's support for **bi-directional WebSocket communication**, which FHIRcast does not provide. This enables low-latency, "gaming style" interactions where applications can exchange events in real-time with minimal delay, supporting use cases such as collaborative viewing, synchronized navigation, and interactive workflows that require immediate feedback and coordination.

Cast also supports **collaborative multi-user workflows** through the hub's ability to group users together within sessions. The hub can coordinate multiple users, allowing them to share events and synchronize their applications in real-time. This enables scenarios such as tumor review board meetings, where multiple radiologists and clinicians can simultaneously view and interact with the same DICOM study, with measurements, annotations, and navigation synchronized across all participants' viewers.

The hub-based architecture provides **flexible integration** because applications do not need to connect directly to each other—they only need to reach the hub. This enables applications running on different platforms and locations to seamlessly participate in the same workflow. For example, a 3D Slicer application running on trqane in the cloud can communicate with a mobile device application, a web-based viewer, or local camera control , all through the hub without requiring direct network connections between them.

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
- **Support Multiple Data Formats**: Handle FHIR resources, DICOM data, proprietary formats, legacy data structures, and other healthcare standards
- **Enable Interoperability**: Facilitate seamless communication between diverse healthcare systems
- **Support User Interactions**: Broadcast user interaction events for coordinated UI behavior
- **Enable Data Exchange**: Support real-time data synchronization, such as DICOM data exchange (potentially called DICOMCast)
- **Enable Low-Latency Interactions**: Support bi-directional WebSocket communication for "gaming style" low-latency interactions, enabling immediate feedback and synchronized collaborative workflows
- **Support Collaborative Multi-User Workflows**: Enable the hub to group multiple users together in sessions, allowing them to share events and synchronize their applications in real-time for collaborative scenarios such as tumor review board meetings
- **Enable Flexible Integration**: Provide hub-based connectivity where applications only need to connect to the hub (not to each other), enabling applications on different platforms (workstations, mobile devices, web browsers, servers) and locations to seamlessly participate in the same workflow
- **Enhance Workflow Efficiency**: Enable real-time coordination and reduce manual data entry and synchronization

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

- **`patient-open`**: A patient record has been opened
- **`patient-close`**: A patient record has been closed
- **`patient-select`**: A patient has been selected from a list

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

#### DICOM Events (DICOMCast)

Cast can be used for DICOM data exchange and synchronization, potentially called DICOMCast. These events support real-time DICOM data sharing:

- **`dicom-study-received`**: A new DICOM study has been received
- **`dicom-study-view`**: An imaging study is being viewed
- **`dicom-study-select`**: An imaging study has been selected
- **`dicom-series-view`**: A DICOM series is being viewed
- **`dicom-instance-view`**: A DICOM instance is being viewed
- **`dicom-data-update`**: DICOM metadata has been updated

**Payload Example:**
```json
{
  "format": "dicom",
  "studyId": "study-456",
  "studyInstanceUID": "1.2.840.113619.2.55.3.1234567890",
  "modality": "CT",
  "bodyPart": "CHEST",
  "studyDate": "2024-01-15",
  "patientId": "pat-001",
  "dicomAttributes": {
    "PatientName": "DOE^JOHN",
    "PatientID": "12345",
    "Modality": "CT",
    "StudyDescription": "CHEST CT"
  }
}
```

#### Document Events

- **`document-open`**: A clinical document has been opened
- **`document-select`**: A document has been selected
- **`document-close`**: A document has been closed

**Payload Example:**
```json
{
  "documentId": "doc-789",
  "documentType": "progress-note",
  "title": "Progress Note - 2024-01-15",
  "author": "Dr. Smith",
  "date": "2024-01-15T10:00:00Z",
  "patientId": "pat-001"
}
```

#### Order Events

- **`order-select`**: An order has been selected
- **`order-view`**: An order is being viewed
- **`order-update`**: An order has been updated

**Payload Example:**
```json
{
  "orderId": "order-321",
  "orderType": "laboratory",
  "status": "active",
  "orderedDate": "2024-01-15T09:00:00Z",
  "patientId": "pat-001"
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

Note: While FHIRcast focuses on FHIR context events, Cast supports any event type, making it suitable for user interactions, DICOM data exchange (DICOMCast), workflow events, and any custom domain-specific events.

---

## Data Formats

Cast is designed to support multiple data formats, not limited to FHIR.

### Supported Formats

#### FHIR Resources

When working with FHIR data, Cast uses standard FHIR resource formats:

```json
{
  "resourceType": "Patient",
  "id": "pat-001",
  "name": [{
    "family": "Doe",
    "given": ["John"]
  }],
  "birthDate": "1980-01-15"
}
```

#### Proprietary Formats

Cast supports proprietary data formats through a flexible payload structure:

```json
{
  "format": "proprietary",
  "system": "legacy-ehr",
  "data": {
    "patient_number": "12345",
    "last_name": "Doe",
    "first_name": "John"
  }
}
```

#### Legacy Formats

For legacy systems, Cast can wrap data in a standardized envelope:

```json
{
  "format": "legacy",
  "system": "mainframe-system",
  "data": "BASE64_ENCODED_LEGACY_DATA",
  "metadata": {
    "encoding": "EBCDIC",
    "recordType": "patient"
  }
}
```

#### DICOM

For imaging data, Cast supports DICOM attributes:

```json
{
  "format": "dicom",
  "studyInstanceUID": "1.2.840.113619.2.55.3.1234567890",
  "seriesInstanceUID": "1.2.840.113619.2.55.3.1234567890.1",
  "sopInstanceUID": "1.2.840.113619.2.55.3.1234567890.1.1",
  "attributes": {
    "PatientName": "DOE^JOHN",
    "PatientID": "12345",
    "Modality": "CT"
  }
}
```

### Format Negotiation

Applications can negotiate data formats during subscription:

```json
{
  "eventTypes": ["patient-open"],
  "preferredFormats": ["fhir", "proprietary"],
  "callbackUrl": "https://app.example.com/cast/callback"
}
```

The Cast Hub will attempt to provide data in the preferred format, falling back to available formats if necessary.

---

## Security

Security is paramount in healthcare applications. Cast implements multiple security measures to protect Protected Health Information (PHI).

### Authentication

Cast uses **OAuth 2.0** for authentication:

1. Applications authenticate with the Cast Hub using OAuth 2.0
2. Access tokens are required for all API calls
3. Tokens are validated on each request
4. Token refresh mechanisms are supported

### Authorization

Authorization is enforced at multiple levels:

- **Subscription Authorization**: Only authorized applications can subscribe to events
- **Event Authorization**: Applications can only publish events they are authorized to publish
- **Data Authorization**: Access to specific patient data is controlled by authorization policies

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

## Implementation Guidelines

### Hub Implementation

When implementing a Cast Hub:

1. **Scalability**: Design for horizontal scaling to handle multiple concurrent sessions
2. **Reliability**: Implement redundancy and failover mechanisms
3. **Performance**: Optimize for low-latency event delivery
4. **Monitoring**: Implement comprehensive logging and monitoring
5. **Error Handling**: Provide clear error messages and recovery mechanisms

### Event Publisher Implementation

When implementing an Event Publisher:

1. **Event Timing**: Publish events immediately when they occur
2. **Event Completeness**: Include all relevant data in event payloads
3. **Error Recovery**: Handle hub unavailability gracefully
4. **Session Management**: Properly manage session lifecycle
5. **Event Type Design**: Design event types that clearly represent the occurrence

### Event Subscriber Implementation

When implementing an Event Subscriber:

1. **Subscription Management**: Subscribe to events during application initialization
2. **Event Processing**: Process events asynchronously to avoid blocking the UI
3. **Data Validation**: Validate received event data before processing
4. **Fallback Behavior**: Handle missing or invalid event data gracefully
5. **Reconnection Logic**: Implement automatic reconnection if connection is lost
6. **Idempotency**: Design event handlers to be idempotent when possible

### Best Practices

- **Idempotency**: Design event handlers to be idempotent
- **Versioning**: Use versioned APIs to support evolution
- **Testing**: Implement comprehensive testing, including integration tests
- **Documentation**: Document custom event types and data formats
- **Error Handling**: Implement robust error handling and user feedback

---

## Examples

### Example 1: Patient Event Synchronization

**Scenario**: An EHR system opens a patient record, and a clinical decision support tool needs to update its display.

**Step 1: Subscriber Subscribes**
```http
POST /cast/v1/subscribe HTTP/1.1
Host: cast.example.com
Authorization: Bearer {token}
Content-Type: application/json

{
  "eventTypes": ["patient-open"],
  "callbackUrl": "https://cds.example.com/cast/callback",
  "sessionId": "session-12345"
}
```

**Step 2: Source Publishes Event**
```http
POST /cast/v1/event HTTP/1.1
Host: cast.example.com
Authorization: Bearer {token}
Content-Type: application/json

{
  "eventType": "patient-open",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "ehr-system",
  "sessionId": "session-12345",
  "payload": {
    "patientId": "pat-001",
    "patientName": "John Doe",
    "dateOfBirth": "1980-01-15",
    "mrn": "MRN-12345"
  }
}
```

**Step 3: Hub Notifies Subscriber**
```http
POST /cast/callback HTTP/1.1
Host: cds.example.com
Content-Type: application/json

{
  "eventType": "patient-open",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "ehr-system",
  "sessionId": "session-12345",
  "payload": {
    "patientId": "pat-001",
    "patientName": "John Doe",
    "dateOfBirth": "1980-01-15",
    "mrn": "MRN-12345"
  }
}
```

### Example 2: DICOM Data Exchange (DICOMCast)

**Scenario**: A radiologist selects a CT study in a PACS viewer, and a reporting system needs to load the corresponding report. This demonstrates DICOM data exchange using Cast.

**Event Publication:**
```json
{
  "eventType": "study-select",
  "timestamp": "2024-01-15T11:00:00Z",
  "source": "pacs-viewer",
  "sessionId": "session-12345",
  "payload": {
    "format": "dicom",
    "studyId": "study-456",
    "studyInstanceUID": "1.2.840.113619.2.55.3.1234567890",
    "modality": "CT",
    "bodyPart": "CHEST",
    "studyDate": "2024-01-15",
    "patientId": "pat-001"
  }
}
```

### Example 3: Bi-Directional WebSocket Implementation

**Connection with Low-Latency Bi-Directional Communication:**
```javascript
const ws = new WebSocket('wss://cast.example.com/cast/v1/ws');

ws.onopen = () => {
  // Subscribe to events
  ws.send(JSON.stringify({
    action: 'subscribe',
    eventTypes: ['patient-open', 'study-view', 'user-click'],
    sessionId: 'session-12345'
  }));
};

// Receive events from other applications (low-latency)
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  if (message.eventType === 'patient-open') {
    updatePatientDisplay(message.payload);
  } else if (message.eventType === 'user-click') {
    handleUserInteraction(message.payload);
  }
};

// Publish events to other applications (bi-directional)
function publishEvent(eventType, payload) {
  ws.send(JSON.stringify({
    action: 'publish',
    eventType: eventType,
    timestamp: new Date().toISOString(),
    source: 'my-application',
    sessionId: 'session-12345',
    payload: payload
  }));
}

// Example: Publish user interaction in real-time
document.getElementById('button').addEventListener('click', () => {
  publishEvent('user-click', {
    elementId: 'button',
    coordinates: { x: 150, y: 200 }
  });
});
```

This example demonstrates Cast's bi-directional WebSocket capability, enabling low-latency "gaming style" interactions where applications can both publish and receive events simultaneously over the same connection, unlike FHIRcast which does not support this capability.

### Example 4: User Interaction Event

**Scenario**: A user clicks a button in one application, and other applications need to respond to this interaction.

**Event:**
```json
{
  "eventType": "user-click",
  "timestamp": "2024-01-15T12:00:00Z",
  "source": "ehr-system",
  "sessionId": "session-12345",
  "payload": {
    "elementId": "print-report-button",
    "elementType": "button",
    "coordinates": {"x": 150, "y": 200},
    "user": "dr-smith"
  }
}
```

### Example 5: Custom Event Type

**Scenario**: A pharmacy system wants to notify other systems when a medication review is completed.

**Event:**
```json
{
  "eventType": "pharmacy:medication-review-complete",
  "timestamp": "2024-01-15T12:00:00Z",
  "source": "pharmacy-system",
  "sessionId": "session-12345",
  "payload": {
    "patientId": "pat-001",
    "reviewId": "review-789",
    "reviewer": "Dr. Pharmacist",
    "reviewDate": "2024-01-15T12:00:00Z",
    "findings": {
      "drugInteractions": 2,
      "dosingIssues": 0,
      "allergyWarnings": 1
    }
  }
}
```

### Example 6: Collaborative Multi-User Workflow - Tumor Review Board Meeting

**Scenario**: Multiple radiologists and clinicians participate in a tumor review board meeting. The Cast Hub groups all participants into the same session, enabling synchronized viewing of DICOM studies and measurements across all participants' viewers.

**Setup**: All participants join session `tumor-review-2024-01-15`:

**Participant 1 (Dr. Smith) navigates to a DICOM study:**
```json
{
  "eventType": "dicom-study-select",
  "timestamp": "2024-01-15T14:00:00Z",
  "source": "pacs-viewer-dr-smith",
  "sessionId": "tumor-review-2024-01-15",
  "userId": "dr-smith",
  "payload": {
    "format": "dicom",
    "studyInstanceUID": "1.2.840.113619.2.55.3.1234567890",
    "modality": "CT",
    "bodyPart": "CHEST"
  }
}
```

**The Cast Hub broadcasts this event to all participants in the session, synchronizing all viewers to the same study.**

**Participant 2 (Dr. Jones) makes a measurement:**
```json
{
  "eventType": "dicom:measurement-added",
  "timestamp": "2024-01-15T14:05:00Z",
  "source": "pacs-viewer-dr-jones",
  "sessionId": "tumor-review-2024-01-15",
  "userId": "dr-jones",
  "payload": {
    "studyInstanceUID": "1.2.840.113619.2.55.3.1234567890",
    "seriesInstanceUID": "1.2.840.113619.2.55.3.1234567890.1",
    "measurement": {
      "type": "tumor-size",
      "value": "2.5 cm",
      "coordinates": {"x": 150, "y": 200},
      "annotation": "Primary tumor"
    }
  }
}
```

**The Cast Hub broadcasts this measurement event to all participants, so all viewers display the same measurement simultaneously.**

**Participant 3 (Dr. Williams) navigates to a specific slice:**
```json
{
  "eventType": "dicom:slice-navigate",
  "timestamp": "2024-01-15T14:07:00Z",
  "source": "pacs-viewer-dr-williams",
  "sessionId": "tumor-review-2024-01-15",
  "userId": "dr-williams",
  "payload": {
    "studyInstanceUID": "1.2.840.113619.2.55.3.1234567890",
    "seriesInstanceUID": "1.2.840.113619.2.55.3.1234567890.1",
    "instanceNumber": 45,
    "windowCenter": 40,
    "windowWidth": 400
  }
}
```

**All participants' viewers automatically navigate to the same slice with the same window/level settings.**

This example demonstrates how Cast's hub-based architecture enables collaborative multi-user workflows, where the hub groups users together in a session and coordinates event distribution, ensuring all participants' applications remain synchronized in real-time.

---

## References

### Related Standards

- **FHIRcast**: [http://hl7.org/fhir/fhircast.html](http://hl7.org/fhir/fhircast.html) - The foundational standard upon which Cast is based. Note: FHIRcast focuses on FHIR context management, while Cast extends beyond context to support any type of event including user interactions and DICOM data exchange (DICOMCast).
- **HL7 FHIR**: [http://hl7.org/fhir/](http://hl7.org/fhir/) - Fast Healthcare Interoperability Resources
- **OAuth 2.0**: [RFC 6749](https://tools.ietf.org/html/rfc6749) - The OAuth 2.0 Authorization Framework
- **WebSocket**: [RFC 6455](https://tools.ietf.org/html/rfc6455) - The WebSocket Protocol
- **DICOM**: [https://www.dicomstandard.org/](https://www.dicomstandard.org/) - Digital Imaging and Communications in Medicine

### Additional Resources

- Cast Implementation Guide (to be published)
- Cast Conformance Profiles (to be published)
- Cast Test Suite (to be published)








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

