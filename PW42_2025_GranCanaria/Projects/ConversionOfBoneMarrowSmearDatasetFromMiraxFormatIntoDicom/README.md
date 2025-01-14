---
layout: pw42-project

permalink: /:path/

project_title: Conversion of bone marrow smear dataset from MIRAX format into DICOM
category: DICOM

key_investigators:

- name: Daniela Schacherer
  affiliation: Fraunhofer MEVIS

- name: David Clunie
  affiliation: PixelMed
  country: USA

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


As the DICOM standard is increasingly used in digital pathology imaging, conversion of available datasets from proprietary formats into DICOM format can make the data more FAIR and improve transparency and reproducibility of research conducted with these data. For this reason, the NCI Imaging Data Commons (IDC) hosts all its data in DICOM format. 

A set of bone marrow smear WSI available in MIRAX (.mrxs) format are to be ingested into the IDC. For that purpose they need to be converted into DICOM (.dcm) along with all available image and clinical metadata. 
In addition, this dataset contains extensive deep-learning generated nuclei annotations (bounding boxes) that should also be converted in DICOM in a suitable way. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


 1. **Objective A**: Have a working script for the conversion of the complete set of bone marrow smear WSI into DICOM format based on [wsidicomizer](https://github.com/imi-bigpicture/wsidicomizer).
 2. **Objective B**: Include clinical metadata in an IDC-conformant way.
 3. **Objective C (optional)**: Have a script that converts the nuclei annotations into DICOM. 




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

**Objective A**
1. Implement and verify code for conversion of the .mrxs files as is into .dcm. 
2. Add code for ingestion of metadata that are not obtained from the .mrxs files / correct potential falsely estimated metadata.
3. Have a few successfully converted samples and be ready to run code on complete collection. 

**Objective B**
1. Prepare additional clinical and lab data as table such that they can be ingested into IDC as BigQuery table. 



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


Background reading: 
- Herrmann, M. D., Clunie, D. A., Fedorov, A., Doyle, S. W., Pieper, S., Klepeis, V., Le, L. P., Mutter, G. L., Milstone, D. S., Schultz, T. J., Kikinis, R., Kotecha, G. K., Hwang, D. H., Andriole, K. P., John Lafrate, A., Brink, J. A., Boland, G. W., Dreyer, K. J., Michalski, M., Golden, J. A., Louis, D. N. & Lennerz, J. K. Implementing the DICOM standard for digital pathology. J. Pathol. Inform. 9, 37 (2018). [http://dx.doi.org/10.4103/jpi.jpi_42_18]( http://dx.doi.org/10.4103/jpi.jpi_42_18)
- Clunie, D. A. DICOM format and protocol standardization-A core requirement for digital pathology success. Toxicol. Pathol. 49, 738–749 (2021). [http://dx.doi.org/10.1177/0192623320965893](http://dx.doi.org/10.1177/0192623320965893)

Further resources:
- [IDC Portal](https://portal.imaging.datacommons.cancer.gov/)
- Conversion tool: [wsidicomizer](https://github.com/imi-bigpicture/wsidicomizer)
- Related project from this project week: [Evaluation of imi-bigpicture/wsidicomizer as a tool for conversion into DICOM whole slide imaging format](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/EvaluationOfImiBigpictureWsidicomizerAsAToolForConversionIntoDicomWholeSlideImagingFormat/)
- Related earlier project from PW40: [WSI-DICOM Improvement - From Viewer to Analysis](https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/WsiDicomImprovementFromViewerToAnalysis/)

