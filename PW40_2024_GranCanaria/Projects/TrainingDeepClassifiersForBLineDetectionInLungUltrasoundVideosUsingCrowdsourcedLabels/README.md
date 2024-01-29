---
layout: pw40-project

permalink: /:path/

project_title: Training deep learning models for B-line detection and localization in lung ultrasound videos using crowdsourced labels
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Mike Jin
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tamas Ungi
  affiliation: Queen's University
  country: Canada

- name: Ameneh Asgari-Targhi
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Crowdsourced labels on medical imaging data can bridge the gap in labeled data required for training AI models for clinical applications.  Using crowdsourced labels on lung ultrasound videos that have been shown [(Duggan 2023)](https://arxiv.org/pdf/2306.06773.pdf) to have comparable accuracy to medical experts, we will train a deep learning model using an approach [(Lucassen 2023)](https://ieeexplore.ieee.org/document/10143623) shown to work with expert-created labels and use the previous model performance to compare the new model's performance.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Using crowdsourced labels, train a deep learning model to classify lung ultrasound videos as having B-lines or having no B-lines.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Run model training and evaluation code from [(Lucassen 2023)](https://ieeexplore.ieee.org/document/10143623) on crowdsourced labels
2.  Compare model performance to same model [(Lucassen 2023)](https://ieeexplore.ieee.org/document/10143623) trained on expert-created labels.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

What are B-lines in lung ultrasound? Here is a picture. The white beams are B-lines, the dark sectors are shadows from ribs.

<img width="1032" alt="Screenshot 2024-01-29 at 1 14 33 PM" src="https://github.com/NA-MIC/ProjectWeek/assets/1342279/d57a43da-34cd-4cd9-aa84-e0ee0cc31b28">

For crowdsourcing, we collect opinions from 5 experts and combine their opinions, like so.  Yellow is the expert consensus:

<img width="809" alt="Screenshot 2024-01-29 at 1 16 56 PM" src="https://github.com/NA-MIC/ProjectWeek/assets/1342279/fc2560c2-f143-437b-aa4a-81b75818609b">

Then, we collect opinions from crowd using a gamified system very similar to Google's RECAPTCHA.  We take the most reliable opinions and combine them to get a high-quality consensus.  Here are the crowd opinions for the same image frame, with the expert consensus in yellow:

<img width="757" alt="Screenshot 2024-01-29 at 1 19 19 PM" src="https://github.com/NA-MIC/ProjectWeek/assets/1342279/faaa837b-f071-4c26-b6a9-e49f9f3c41cf">

For this image, here are the crowd consensus and expert consensus both overlaid:

<img width="797" alt="Screenshot 2024-01-29 at 1 21 08 PM" src="https://github.com/NA-MIC/ProjectWeek/assets/1342279/da6a827e-4c1d-4deb-a704-1785afb43ac9">

We will be continuing to crowdsource B-line segmentations throughout Project Week!  Here is the visualization of the progress so far (mid-day 2024-01-29):

<img width="813" alt="Screenshot 2024-01-29 at 1 22 02 PM" src="https://github.com/NA-MIC/ProjectWeek/assets/1342279/78b897d0-3df4-44b8-ae9d-b0a2a23f0d1a">

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Lucassen 2023: https://ieeexplore.ieee.org/document/10143623 (Github code: https://github.com/RTLucassen/B-line_detection)
Duggan 2023: https://arxiv.org/abs/2306.06773
Jin 2023: https://arxiv.org/abs/2312.10198
