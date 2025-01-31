Back to [Projects List](../../README.md#ProjectsList)

# DICOM for Quantitative Imaging

## Key Investigators

- Andrey Fedorov (BWH/HMS)
- Christian Herz (BWH/HMS)
- JC (Kitware)
- Curt Lisle (KnowledgeVis, LLC)
- Joost van Griethuysen (NKI)
- Csaba Pinter (Queen's)
- Christian Bauer (U.Iowa)

# Project Description

## Objective

1. Discuss with the interested attendees capabilities of the DICOM standard and available support in tools for standardized communication of data produced by image analysis.
2. Triage open issues for dcmqi, prioritize and fix at least some, revisit documentation and related open issues.
3. Work on converting an existing radiomics dataset into DICOM representation.

## Approach and Plan

Issues to fix:
* https://github.com/QIICR/QuantitativeReporting/issues/201
* https://github.com/QIICR/QuantitativeReporting/issues/209
* https://github.com/QIICR/QuantitativeReporting/issues/210

## Progress and Next Steps

* Fixed several dcmqi issues identified by the users during the project week
* Finished [scripts](https://github.com/fedorov/lidc-idri-conversion) for converting segmentations and corresponding radiomics features (extracted by pyradiomics) to DICOM  for TCIA LIDC IDRI dataset ([result of conversion for LIDC-IDRI-0011](https://www.dropbox.com/s/myirvs5y20rb64o/LIDC-IDRI-0011.zip?dl=0)); issues identified:
  * need to integrate pyradiomics features with IBSI-based ontology
  * improve presentation of large number of features in Quantitative Reporting

# Illustrations

<img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW27_2018_Boston/Projects/DICOMforQuantitativeImaging/radiomics_dcm.jpg" width="600">

<img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW27_2018_Boston/Projects/DICOMforQuantitativeImaging/dcmbrowser.jpg" width="600">

# Background and References

- [https://github.com/qiicr/dcmqi](https://github.com/qiicr/dcmqi)
- [https://qiicr.gitbooks.io/dicom4qi/content/](https://qiicr.gitbooks.io/dicom4qi/content/)
- Herz C, Fillion-Robin J-C, Onken M, Riesmeier J, Lasso A, Pinter C, Fichtinger G, Pieper S, Clunie D, Kikinis R, Fedorov A.  _dcmqi: An Open Source Library for Standardized Communication of Quantitative Image Analysis Results Using DICOM_. *Cancer Research*. 2017;77(21):e87–e90 [http://cancerres.aacrjournals.org/content/77/21/e87](http://cancerres.aacrjournals.org/content/77/21/e87).
- Fedorov A, Clunie D, Ulrich E, Bauer C, Wahle A, Brown B, Onken M, Riesmeier J, Pieper S, Kikinis R, Buatti J, Beichel RR. (2016) DICOM for quantitative imaging biomarker development: a standards based approach to sharing clinical data and structured PET/CT analysis results in head and neck cancer research. PeerJ 4:e2057 [https://doi.org/10.7717/peerj.2057](https://doi.org/10.7717/peerj.2057)

- [https://github.com/Radiomics/pyradiomics](https://github.com/Radiomics/pyradiomics)
- van Griethuysen, J. J. M., Fedorov, A., Parmar, C., Hosny, A., Aucoin, N., Narayan, V., Beets-Tan, R. G. H., Fillon-Robin, J. C., Pieper, S., Aerts, H. J. W. L. (2017). Computational Radiomics System to Decode the Radiographic Phenotype. Cancer Research, 77(21), e104–e107. [https://doi.org/10.1158/0008-5472.CAN-17-0339](https://doi.org/10.1158/0008-5472.CAN-17-0339)
