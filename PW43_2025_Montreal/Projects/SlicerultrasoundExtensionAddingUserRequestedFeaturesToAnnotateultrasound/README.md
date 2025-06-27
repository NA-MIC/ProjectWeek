---
layout: pw43-project

permalink: /:path/

project_title: SlicerUltrasound Extension Development - New features
category: DICOM

key_investigators:

- name: Maha Kesibi
  affiliation: Queen's University
  country: Canada

- name: Tina Kapur
  affiliation: BWH
  country: USA

- name: Tamas Ungi
  affiliation: Queen's
  country: Canada

- name: Fahimeh Fooladgar
  affiliation: UBC
  country: Canada

- name: Shreyas Puducheri
  affiliation: BWH
  country: USA

- name: Matt Alves
  affiliation: BWH
  country: USA

- name: Caroline Schissel
  affiliation: Lahey
  country: USA

- name: David Dinh
  affiliation: SlicerUltrasound Team
  country: USA

- name: Atin Malaviya
  affiliation: SlicerUltrasound Team
  country: USA

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


**AnnotateUltrasound** is a 3D Slicer extension that enables structured sector annotation of lung ultrasound video clips, focusing on features such as pleura lines and B-lines. It provides an intuitive interface for frame-by-frame annotation, supports multiple raters, and saves annotation data for future research and machine learning.

We collaborate closely with several physicians who use AnnotateUltrasound in their clinical and research workflows. Their feedback directly shapes the module’s features and usability, ensuring a user-centered design. We regularly incorporate their suggestions for new features and improvements based on their real-world experiences.

This week, we focused on incorporating user-requested features to improve efficiency, usability, and comparative analysis of annotations.

More about the module: [https://github.com/SlicerUltrasound/SlicerUltrasound](https://github.com/SlicerUltrasound/SlicerUltrasound)


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->



1. **Frame-by-Frame Pleura Percentage Comparison**  
   - Display pleura percentage per frame.
   - Highlight the frame with the highest pleura coverage for each rater in the rater table.

2. **Annotation Time Tracking**  
   - Track and display time each rater spends annotating, to support workload analysis and training evaluation.

3. **Adjudication Mode**
   - Introduce an adjudicator workflow for validating or invalidating rater annotations and generating final consensus annotations.

4. **Label Annotation Comparison**  
   - Add label data to the rater table to allow comparison of both line and label annotations.

5. **Improved Line Endpoint Visualization**  
   - Refine endpoint markers to support more precise annotations.


## Approach and Plan


- Update the AnnotateUltrasound logic to compute and store pleura percentages per frame and clip.
- Extend UI tables to display these values, with live updates as annotations change.
- Integrate a timer using `QTimer` and idle detection (from the UserStatistics module) to track annotation time and store it in JSON.
- Modify endpoint visuals for clearer frame annotation.
- Add an adjudicator mode for validating annotations across raters, including new UI tools and changes to the annotation file structure to store validated results



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

**Completed**
- **Annotation Timer**  
  - Tracks time per rater, auto-pauses on inactivity  
  - Displays timer in MM:SS format  
  - Saves to annotation JSON

- **Pleura Percentage Display**  
  - Shows per-frame pleura percentages in annotation table  
  - Highlights max pleura frame in rater table with frame index  
  - Values stored in annotation JSON

- Added **Adjudicator Mode** for validating annotations across raters  
  - UI tools for validate/invalidate actions (+ keyboard shortcuts)  
  - Saves to `.adjudication.json` file with adjudicator metadata (status, timestamp)  
  - Updates schema to support final validated annotations  

**In Progress**
- Refine UI for adjudication visibility and toggles
- Add the Sandbox/UserStatistics module as a dependency
- Testing edge cases and fine-tuning timer and pleura calculations  
- Adding the label annotation to the UI in the rater table
- Get user feedback from clinicians for final usability tweaks
  
# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Pleura percentage saving per frame and populating rater table:
<video
   controls muted
   src="https://github.com/user-attachments/assets/b084e190-6eeb-4ec2-b0e9-2f07cf737c3a"
   style="max-height:640px; min-height: 200px">
 </video>

Timer demo:
<video
   controls muted
   src="https://github.com/user-attachments/assets/916eefb3-f4f7-489a-adae-0780b1454cc5"
   style="max-height:640px; min-height: 200px">
 </video>


Label annotation and populating rater tbale:

<img width="395" alt="labels" src="https://github.com/user-attachments/assets/82875613-02be-4548-b1d6-46c52103ed35" />
<img width="395" alt="labels in rater table" src="https://github.com/user-attachments/assets/496c3132-91d1-4512-849d-b49a0fdf05c3" />


Adjudication support:



https://github.com/user-attachments/assets/d3cb237e-92d7-4a67-87ff-18c41fe003cd



<img width="352" alt="adjudicator-tools" src="https://github.com/user-attachments/assets/c3d61cf3-a1bf-47ce-bbc7-f27af37c712f" />

<img width="1480" alt="validating-annotation-lines" src="https://github.com/user-attachments/assets/d8e455e8-6d5b-4867-8dc3-a5d5235c5d16" />




Current keyboard shortcuts:

![keyboardShortcuts](https://github.com/user-attachments/assets/a05b65e1-8bd4-40f5-8ccd-3abf3efc2589)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

- Source Code: [https://github.com/SlicerUltrasound/SlicerUltrasound](https://github.com/SlicerUltrasound/SlicerUltrasound)
- Related Extension: [Sandbox – UserStatistics module](https://github.com/Slicer/SlicerSandbox)

_No response_

