Back to [Projects List](../../Readme.md#ProjectsList)

# NCI Imaging Data Commons

## Key Investigators (subject to change)

- Andrey Fedorov (Brigham and Women's Hospital, Boston)
- Markus Herrmann (Mass General Hospital, Boston)
- Theodore Aptekarev ()
- Steve Pieper (Isomics Inc)
- Ron Kikinis (Brigham and Women's Hospital, Boston)

# Project Description

**National Cancer Institute (NCI) Imaging Data Commons.**


NCI IDC is a new component of the Cancer Research Data Commons (CRDC). The goal of IDC is to enable a broad spectrum of cancer researchers, with and without imaging expertise, to easily access and explore the value of de-identified imaging data and to support integrated analyses with non-imaging data. IDC maintains cancer imaging data collections in Google Cloud Platform, and is developing tools and examples to support cloud-based analysis of imaging data.

Some examples of what you can do with IDC:
* quickly explore the available public cancer imaging datasets using rich metadata, visualize images and annotations, build cohorts of relevant subsets of the data
* retrieve DICOM files corresponding to the selected cohort to a cloud-based Virtual Machine (VM)

In this project we would like to interact with the project week participants to answer their questions about IDC and understand their needs, collect feedback and suggestions for the functionality users would like to see in IDC, and help users get started with the platform.

Free cloud credits are available to support the use of IDC for cancer imaging research.

**GBM series tagging Project Week experiment.**

Broad motivation for the experiment is to enrich IDC data offering by improving the richness of metadata accompanying IDC content.

An experiment that can be completed within the Project Week can implement tool for tagging of the individual series within an MRI exam with the series type. The experiment will follow the catigorization of individual series that was proposed in [Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features](https://www.nature.com/articles/sdata2017117).
It is a valuable capability currently missing to allow for automatic tagging of individual series within a DICOM study, which is important for feeding data into the subsequent analysis steps.
The idea for the experiment is to develop a tool allowing to tag individual series, using, as needed, DICOM metadata and content of the image, utilizing the metadata table of the mentioned paper as a source of inspiration if not training/testing.
<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

**NCI IDC.**

1. Provide attendees with the opportunity to interact with the platform developers to answer questions.
2. Collect use cases and suggestions

**GBM series tagging experiment.**

1. Create a cloud native workflow for training ML models on IDC data
2. Produce a trained model for tagging of the individual series within an MRI exam with the series type.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

**GBM series tagging experiment.**

1. Explore the data overlap between the TCIA-GBM data used in the paper and the data in IDC
2. Produce a training dataset to be used with a 2d classifier
3. Try out MONAI to train a 2d classifier

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
