---
layout: pw45-project

permalink: /:path/

project_title: Improving QC protocols for AMP SCZ Clinical and MRI Data
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Sylvain Bouix
  affiliation: école de technologie supérieure
  country: Canada

- name: Owen Borders
  affiliation: Psychiatry Neuroimaging Lab
  country: U.S.

- name: Keerthana Srinivasan
  affiliation: Psychiatry Neuroimaging Lab
  country: U.S.

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We will be adding anomaly detection algorithms to clinical data and MRI data in the AMP SCZ project. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. We would like to achieve MRI QC reports that accurately correlate to human QC ratings, in addition to uncovering new QC rules for clinical forms using machine learning anomaly detection algorithms.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. For the clinical data, we will use DBSCAN to search for correlations between every variable and flag cases that deviate the most.
2. For the MRI data, we will artificially add artifacts to clean MRI scans and train a neural network to rank the severity.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Scanned the database for site distribution outliers, string anomalies, and time series anomalies that allowed several new quality control rules to be developed.
2. Created a web interface for MRI data that allowed various synthetic anatomical and scanner features to be visualized.
3. Used the synthetic anatomical and scanner augmentations to train a robust MRI QC model.
4. Next steps involve calculating the correlation between the automatic MRI QC and scores by human raters.




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img width="1276" height="614" alt="image" src="https://github.com/user-attachments/assets/ea7915eb-1a4a-4dd0-86b2-3be1369fda8c" />

_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

# Funding

This work is supported by NIH [U24MH137171](https://reporter.nih.gov/project-details/11118972).

