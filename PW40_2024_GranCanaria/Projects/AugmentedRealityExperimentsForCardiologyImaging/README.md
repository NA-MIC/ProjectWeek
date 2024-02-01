---
layout: pw40-project

permalink: /:path/

project_title: Augmented reality experiments for cardiology imaging
category: VR/AR and Rendering
presenter_location: In-person

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: Inc., USA

- name: Vitaliy Petrov
  affiliation: Lviv Regional Clinical Hospital
  country: Ukraine

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Explore tools for clinician review and patient education using smartphone browser-based augmented reality.
There are two possible scenarios we could support:

* Using existing SlicerHeart and SlicerVirtualReality extensions to support smartphone tracking
* Exporting Slicer scene data to a web page for rendering locally in smartphone browser

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Determine how much work would be required to make a system that could be tested in clinical scenarios
2. See what other people's experience has been in the feasibility and/or utility of such systems

A few of the features we'd like to explore:
* Using the a smartphone as a controller in SlicerVirtualReality
* Communicating events from smartphone to Slicer to control rendering
* Sending rendered images to phone vs. rendering in phone locally
* Exporting data to a stand-alone scene that could be viewed on a smartphone (e.g. by emailing a link or generating a QR code)
  
## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Review existing technologies for applicability for this use case
2.  Talk with Project Week attendees about similar needs and experiences
3.  If time, do some prototyping

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Resurrected WebServer tracker experiment
2. Updated https support with custom certificate that can be uploaded to android phone
3. Tried demo controlling volume rendering with phone
4. Showed demo to other prooject week attendees using another another android phone

WIP in this YouTube shorts link: [https://youtube.com/shorts/JeNtDT1LF6k?feature=share](https://youtube.com/shorts/JeNtDT1LF6k?feature=share)

# Illustrations

 <iframe src="[https://www.youtube.com/embed/ZWxE5QcGvE8](https://youtu.be/Dwza9Bbg4J4)">
 </iframe>


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   Phone based tracking communicating with Slicer from earlier Project Week: <https://www.youtube.com/watch?v=kQKskHYlpQE>
*   Use of Slicer's WebServer to host tracker data: <https://github.com/pieper/SlicerWeb/blob/master/WebServer/docroot/WebXR-controller/index.html>
*   vtk.js based volume rendering demo compatible with Android smartphone AR tracking: <https://kitware.github.io/vtk-js/examples/WebXRVolume/WebXRVolume.html?xrSessionType=1&fileURL=https://data.kitware.com/api/v1/file/63fe3f237b0dfcc98f66a857/download&colorPreset=CT-AAA&rotateX=90&rotateY=180>
