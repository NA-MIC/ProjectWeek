---
layout: pw39-project

permalink: /:path/

project_title: Deep learning model for B-line detection in lung ultrasound videos using crowdsourced
  labels
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Mike Jin
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tamas Ungi
  affiliation: Queen's University
  country: Canada

- name: Colton Barr
  affiliation: Queen's University
  country: Canada / Brigham and Women's Hospital, USA

- name: Ameneh Asgari-Targhi
  affiliation: Brigham and Women's Hospital
  country: USA

- name: Tina Kapur
  affiliation: Brigham and Women's Hospital
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Automated B-line detection in lung ultrasound videos has been demonstrated before, most recently by [Lucassen 2023](https://pubmed.ncbi.nlm.nih.gov/37276107/).  However, acquiring the many labels necessary can be a resource-intensive process, limited by the availability of expert clinicians capable of producing high-quality labels.  Recently, gamified crowdsourcing with a new quality control mechanism and built-in learning for labelers has been demonstrated to be capable of producing annotations on lung ultrasound videos comparable in quality to expert clinicians (as well as analogous results for EEG and skin lesion classification tasks), which can greatly shorten the time required to acquire high-quality labels for model training.  Though these crowd labels have been shown to have expert-level quality, it has yet to be demonstrated whether crowd-produced labels are capable of training high-performance models.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Train a deep learning model to classify lung ultrasound videos as having B-lines or having no B-lines.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Create a data file associating all 3000+ clips with filepath, crowd label, and expert labels (for those that have expert labels).
2.  Adapt the model (ResNet(2+1)D-18 or similar pretrained model) and training procedure used in [Lucassen 2023](https://pubmed.ncbi.nlm.nih.gov/37276107/) to train a new model on a new crowd-labeled dataset of 3000+ lung ultrasound videos from 500 patients.
3.  Evaluate the model performance and compare to previously reported model performance for ultrasound video classification of B-line presence.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  De-identified and masked 3000+ lung ultrasound clips
2.  Uploaded 3000+ clips with standard filename format to a GPU cluster.
3.  Crowd-labeled all 3000+ lung ultrasound clips using 193 clips from \~70 patients for crowd training.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

<https://pubmed.ncbi.nlm.nih.gov/37276107/>
