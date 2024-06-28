---
layout: pw41-project

permalink: /:path/

project_title: NCI Imaging Data Commons - user support and platform development
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

- name: Deepa Krishnaswamy
  affiliation: BWH
  country: USA

- name: Vamsi Thiriveedhi
  affiliation: BWH
  country: USA

- name: Cosmin Ciausu
  affiliation: BWH
  country: USA

- name: Leonard Nuerenberg
  affiliation: AIM Lab
  country: USA

- name: Suraj Pai
  affiliation: AIM Lab
  country: USA

- name: Steve Pieper
  affiliation: Isomics Inc
  country: USA

- name: Ron Kikinis
  affiliation: BWH
  country: USA

- name: Michael Onken
  affiliation: OpenConnections GmbH
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


[NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/explore/) is a cloud-based environment containing publicly available cancer imaging data co-located with analysis and exploration tools and resources.

IDC provides a growing amount of publicly available cancer imaging data (>65TB at the moment, radiology and digital pathology, including images, annotations, analysis results and clinical data) curated in the cloud to support highly efficient access and to simplify analysis.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Raise awareness about IDC, help users, collect feedback to help prioritize future development.
2. Identify robust AI models that can be applied to IDC data to enrich IDC with annotations.
3. Work on various issues related to the development of IDC platform and related software tools.
   
## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Interact with current and prospective users to answer questions and collect feedback.
2. Support any project that has a need for public datasets available for testing, cloud-based notebook implementations of the analysis, scaling up analysis to large cohorts within IDC.
3. Work on priority aspects of the project: maintenance and improvement of SlicerIDCBrowser and idc-index, improvements of the documentation and other learning materials
4. Improve/simplify access to the [NLST/TotalSegmentator analysis results](https://discourse.canceridc.dev/t/new-in-idc-v18-totalsegmentator-segmentations-and-radiomics-features-for-nlst-cts/582).
5. Work on maintenance of dcmqi priority issues: https://github.com/QIICR/dcmqi/issues/489, python wrapper API
6. MRTotalsegmenator SCT codes - Andras
7. DCMTK upgrade in Slicer - JC


## Progress and Next Steps

1. Prepared initial version of the query to extract processing steps for slide microscopy (SM) images using DICOM metadata ([https://github.com/ImagingDataCommons/idc-index-data/pull/30](https://github.com/ImagingDataCommons/idc-index-data/pull/30)). When completed, this will allow selecting SM images by embedding method, staining (H&E), and fixative without using BigQuery, and with queries of significantly lower complexity as compared to querying full index.
2. Implemented new feature in the dcmqi converter that allows including into DICOM SEG references to the segmented images when geometry of the segmentation is different from the image (e.g., when segmentation was done on the slices orthogonal to the segmented image) ([https://github.com/QIICR/dcmqi/issues/489](https://github.com/QIICR/dcmqi/issues/489)). Lacking this feature, ReMIND collection encoded images that are disconnected from the segmented MR images.
3. Mapped model-specific segmentation labels for [OMAS](https://docs.google.com/spreadsheets/d/1pBicNskjMDJBnD3w4yAQroj8SGSAhDfA_TUK24dLEyc/edit?gid=1390863317#gid=1390863317) and [TotalSegmentator](https://docs.google.com/spreadsheets/d/1oEzXCmraoLgbbb5lNxWiHuYDza86aXxKqSUmUetwI7M/edit?gid=780795691#gid=780795691) to SNOMED-CT (related PRs [https://github.com/wasserth/TotalSegmentator/pull/324](https://github.com/wasserth/TotalSegmentator/pull/324) and [https://github.com/wasserth/TotalSegmentator/pull/325](https://github.com/wasserth/TotalSegmentator/pull/325)).
4. Presented IDC updates at the Thu breakout session (see notes and references in [this document](https://docs.google.com/document/d/11IG53uKYePUlQFCUX6nFw4HqQDyt2jcLkvqjnHGNPCI/edit)).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Summary of IDC content as of data release v18](https://learn.canceridc.dev/~gitbook/image?url=https%3A%2F%2F1103581492-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MCTG4fXybYgGMalZnmf-2668963341%252Fuploads%252FBPUPVLBlGOSoK0iQxXbl%252Fidc_v18_summary.jpg%3Falt%3Dmedia%26token%3D332a4ac5-5850-4e23-9340-d50607ec3dfd&width=768&dpr=2&quality=100&sign=a98506d4008137a946a692376342be1a161a5301dca7439f7ee2d94db9fa95f1)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* Fedorov, A., Longabaugh, W. J. R., Pot, D., Clunie, D. A., Pieper, S. D., Gibbs, D. L., Bridge, C., Herrmann, M. D., Homeyer, A., Lewis, R., Aerts, H. J. W., Krishnaswamy, D., Thiriveedhi, V. K., Ciausu, C., Schacherer, D. P., Bontempi, D., Pihl, T., Wagner, U., Farahani, K., Kim, E. & Kikinis, R. National Cancer Institute Imaging Data Commons: Toward Transparency, Reproducibility, and Scalability in Imaging Artificial Intelligence. RadioGraphics (2023). [https://doi.org/10.1148/rg.230180](https://doi.org/10.1148/rg.230180)
* Thiriveedhi, V. K., Krishnaswamy, D., Clunie, D., Pieper, S., Kikinis, R. & Fedorov, A. Cloud-based large-scale curation of medical imaging data using AI segmentation. Research Square (2024). [https://doi.org/10.21203/rs.3.rs-4351526/v1](https://doi.org/10.21203/rs.3.rs-4351526/v1)

