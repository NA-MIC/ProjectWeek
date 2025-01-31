---
layout: pw41-project

permalink: /:path/

project_title: 'CT image based prediction model in head and neck cancer: contribution to MHub'
category: DICOM
presenter_location: Online

key_investigators:

- name: Kate Akhmad
  affiliation: ???
  country: ???

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Head and neck cancers account for [nearly 4% of all cancers in the United States](https://www.cancer.gov/types/head-and-neck/head-neck-fact-sheet#how-can-people-who-have-had-head-and-neck-cancers-reduce-their-risk-of-developing-a-second-primary-new-cancer). Although there have been improvements in treatment and understanding of the disease, survival hasn't significantly improved in the last decades for the head neck cancer population in general. The CNN uses tumor delineations from the pre-treatment CT heard and neck scans to predict distant metastasis, loco-regional failure, and overall survival.

The model is peer-reviewed and was [open-sourced published](https://github.com/MaastrichtU-CDS/hn_cnn/tree/main?tab=readme-ov-file#description) . While the model is open-sourced, it still requires some additional settings for its implementation. To make it easily available, it's interesting to add this model to the standardized I\O framework as MHub platform.

Model characteristics:
- Model input: DICOM files of CT head and neck
- Preprocessing steps: slice selection and cropping around the tumour region, transformation in png format.
- Model output: prediction of loco-regional failure, overall survival and distant metastasis.
- Metrics Table [3](https://www.nature.com/articles/s41598-023-45486-5#Tab3):
The performance of our network varied for different outcomes:
-- the 2-year distant metastasis prediction had the highest AUC, around 0.90, across the training, validation, and testing sets;
-- 4-year overall survival AUC 0.78;
-- 2-year loco-regional failure prediction AUC.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Objective A. To make the model easy available through a standardized I/O framework in MHub.
Objective B. To estimate reproducibility and quality of the model on external datasets (if it applicable).
Objective C. To be acquainted with the contribution pipeline in MHub.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. To go through the contribution pipeline of MHub platform
2. To make it available through a standardized I/O framework.
3. To test the excitability of the model in the framework



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


- The model was developed by [CDS group at Maastricht University](https://github.com/MaastrichtU-CDS/hn_cnn/tree/main?tab=readme-ov-file#description )
- [Citation](https://doi.org/10.1038/s41598-023-45486-5)
- License:  MIT license
