---
layout: pw43-project

permalink: /:path/

project_title: Using IDC and AI for hypotheses exploration in the NLST cohort
category: Quantification and Computation

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Fadwa Elfeituri
  affiliation: Georgetown University
  country: USA

- name: Pari Shah
  affiliation: Georgetown University
  country: USA

- name: Vamsi Thiriveedhi
  affiliation: BWH
  country: USA

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Yuriy Gusev
  affiliation: Georgetown University
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


In 2024 [Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/explore) team processed CT images available in the National Lung Screening Trial (NLST) collection using TotalSegmentator and pyradiomics to segment anatomical organs and extract basic first order (e.g., mean intensity) and shape features (e.g., volume), and released all of the extracted quantitative features publicly in the IDC [`TotalSegmentator-CT-Segmentations` analysis results collection](https://portal.imaging.datacommons.cancer.gov/explore/filters/?analysis_results_id=TotalSegmentator-CT-Segmentations) [1,2]. A basic Looker dashboard for exploring this dataset is available [here](https://lookerstudio.google.com/reporting/c3e2965e-e615-4b4b-b523-1fc335dd9d43).

The motivation for that work was to utilize segmentation as a tool - as opposed as the objective of research endeavor - to enable downstream use of the data for exploration and hypothesis generation by the users who do not have expertise/time/resources to extract those quantitative features on their own.  

To date, one study was published utilizing liver mean attenuation measurements for this dataset to explore a novel biomarker of liver disease [3]. We also investigated detection of outliers/erroneous segmentation results in this dataset [4]. 

In this project we aim to improve materials/resources that accompany the dataset to make it more accessible to the community, and explore research directions where the extracted quantitative features can be useful. AI will facilitate and enable this project at multiple levels: for segmenting the regions of interest, extraction of radiomics features, analyzing relevant research literature for identifying hypotheses of interest, and facilitating exploration of those hypothesis on the real data.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Improve accessibility and usability of the dataset to simplify its use.
2. Demonstrate the utility of the dataset to inspire future users.
3. Prepare materials for a future publication to raise awareness of the dataset more broadly.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Develop tutorial notebooks explaining how to access and use the dataset.
2. Develop interactive dashboard(s) to simplify exploration of the dataset by non-technical users, collect feedback from potential/target users.
3. Identify and explore specific hypotheses that can be facilitated by the dataset, capture this exploration in notebooks.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Describe specific steps you **have actually done**.
  




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Example of segmentation](https://github.com/user-attachments/assets/869d4b98-f30f-46a5-b2b4-8654d243e931)
Individual images/segmentations can be loaded in Slicer using [SlicerIDCExplorer](https://github.com/imagingdatacommons/sliceridcbrowser) extension.

![T8 vertebra volume distribution](https://github.com/user-attachments/assets/0632004b-a481-427d-994b-6b110e396844)
A basic Looker dashboard for exploring this dataset is available [here](https://lookerstudio.google.com/reporting/c3e2965e-e615-4b4b-b523-1fc335dd9d43), screenshot above displays distribution of volume of the T8 vertebra.

![Vertebrae volume](https://github.com/user-attachments/assets/85b8fc85-3c7f-4738-9732-a8bf1867a20e)
Plot from the [Krishnaswamy et al. 2024](http://arxiv.org/abs/2406.14486) study summarizing concordance between the trends observed for the volume measurements of the total vertebrae volume derived using TotalSegmentator on a cohort of ~20,000 subjects vs a published study [Limthongkul et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20142072/) measuring vertebral body volume conducted on the data from 40 subjects.



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[1] Thiriveedhi, V. K., Krishnaswamy, D., Clunie, D., Pieper, S., Kikinis, R. & Fedorov, A. Cloud-based large-scale curation of medical imaging data using AI segmentation. Research Square (2024). https://doi.org/10.21203/rs.3.rs-4351526/v1
[2] Thiriveedhi, V. K., Krishnaswamy, D., Clunie, D. & Fedorov, A. TotalSegmentator segmentations and radiomics features for NCI Imaging Data Commons CT images. (2024). https://doi.org/10.5281/zenodo.8347012
[3] Weiss, J., Bernatz, S., Johnson, J., Thiriveedhi, V., Mak, R. H., Fedorov, A., Lu, M. T. & Aerts, H. J. W. Opportunistic assessment of steatotic liver disease in lung cancer screening eligible individuals. J. Intern. Med. (2025). https://doi.org/10.1111/joim.20053
[4] Krishnaswamy, D., Thiriveedhi, V. K., Ciausu, C., Clunie, D., Pieper, S., Kikinis, R. & Fedorov, A. Rule-based outlier detection of AI-generated anatomy segmentations. arXiv [eess.IV] (2024). at http://arxiv.org/abs/2406.14486

