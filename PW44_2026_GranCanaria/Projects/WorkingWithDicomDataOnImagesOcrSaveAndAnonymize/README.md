---
layout: pw44-project

permalink: /:path/

project_title: 'Working with DICOM data on images: OCR, save, and anonymize'
category: DICOM
presenter_location: 

key_investigators:

- name: Attila Nagy
  affiliation: University of Szeged
  country: Hungary

- name: Gábor Fichtinger
  affiliation: Queen's University
  country: Kingston, ON, Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Sometimes CT or MR scans arrive as plain images (JPEG, PNG...), and the data is overlaid on them.
The task is two-fold: 
- get the data, because it may store spatial, series and patient information. This is an OCR task.
- get rid of the data, so it can be anonymized




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Our goal was to create an extension prototype that can achieve the above goals, using pure Slicer and python infrastructure.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


Work on prototype data, test various OCR solutions (Tesseract, EasyOCR), and implement the module with a GUI.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Module done.
It is able to OCR text in selected ROIs, and then blank out those regions in all of the sliced (technically images).
The modules support reviewing the OCR'ed data, saving it as JSON (and also save it in the scene MRML), and load it back.
The regions can be blanked both with pure black (0,0,0) and pure white (255,255,255) RGB values. The DICOM functionality is not yet extensively tested, and there is also a placeholder where with the use of some regex DICOM data can automatically be imported into the series.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Here is a short video demonstrating the current functionality:
<iframe width="420" height="315" src="https://www.youtube.com/embed/Ao9UofN0RsY">
 </iframe>



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

