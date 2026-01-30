---
layout: pw44-project

permalink: /:path/

project_title: Long-COVID and the Brain White Matter
category: Segmentation / Classification / Landmarking
presenter_location: 

key_investigators:

- name: Zora Kikinis
  affiliation: Mass General Brigham
  country: Boston, USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


About 7% of COVID-19 survivors experience long-lasting symptoms known as long-COVID. There is no proven cure for long-COVID, nor do we know the pathology of the syndrome. Our research project aims to understand how changes in the brain, specifically the white matter, contribute to the symptoms of the neuropsychiatric subtype of long-COVID. 

The brain white matter fiber tract of interest to us is the dorsal vagal complex-corticolimbic fiber system (DVC-CLFS), which connects the brainstem and the frontal brain areas (Kikinis et al. 2024). 






## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Reconstruction of the DVC-CLFS fiber tract in study subjects with and without long-COVID.





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


I will use diffusion and structural MRI, specifically whole-brain tractography (UKF tractography) and FreeSurfer parcellations, to segment the DVC-CLFS fiber tract in its entirety, extending from the frontal lobe to the brainstem, using 3DSlicer tools.







## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. In the past project weeks, we established a standardized protocol for segmenting the anatomically accurate DVC-CLFS fiber tract from MRI images using 3D Slicer.
2. By the end of this week, I have segmented the fiber tract from 20 study subjects.
3. Next: Segmentation of the fiber tract in 100 more study subjects.
4. Next: To establish the relationship between this specific fiber tract and long-COVID symptoms, diffusion measures—fractional anisotropy (FA), radial diffusivity (RD), mean diffusivity (MD), and free water (FW) — will be extracted from the streamlines of the DVC-CLFS tract. These metrics will be used for statistical analyses and correlated with neuropsychiatric long-COVID symptom scores, including measures of cognition and fatigue.
  




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![](https://github.com/user-attachments/assets/12007fc5-7f9c-4ea1-8e71-21ae046ec721)

Segmentation of the DVC-CLFS fiber tract (white) from the UKF whole-brain tractography and FreeSurfer-generated parcellations using 3D Slicer tool and its extensions.


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Investigating the Structural Network Underlying Brain-Immune Interactions Using Combined Histopathology and Neuroimaging: A Critical Review for Its Relevance in Acute and Long COVID-19.
Kikinis et al. 2024,
https://pubmed.ncbi.nlm.nih.gov/38590789/
