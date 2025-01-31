Back to [Projects List](../../README.md#ProjectsList)

# Decision Support for End-Stage Liver Disease Transplants

## Key Investigators

- Mike Halle (BWH)
- Jennifer Nitsch (University of Bremen, Fraunhofer MEVIS)
- Hans Meine (University of Bremen, Fraunhofer MEVIS)
- Ben Ball (BWH)
- April Wall (BWH)
- Anna Rutherford (BWH)
- Michael Schwier (BWH)
- Ron Kikinis (BWH)

# Project Description

The waiting list for liver transplants is ordered according to a score
based on multiple criteria.  However, qualitative parts describing the
quality of life (encephalopathy, coma, ascities, GI or variceal bleeds) have been excluded from the score because they were
subjective too easy to "game" to move closer to transplant.  These scores are important, though, so we would
like to introduce a quantitative, image-based scoring in order to

* better reflect the true urgency of transplant for liver disease patients by looking for patterns of disease throughout the abdomen,
* provide physicians with information that might allow them to defer transplants for people who are already too sick.
* Look at established clinical practice, including MELD scores, physical assessment of liver disease, and other existing assessment methods.

We are using Partner's image database for a corpus of imaging data (liver disease patients and controls with the same scan protocol but no liver disease).

## Objective

1. Understand standard/established clinical scores and effects/representation in medical imaging.
1. Familiarize with the data from this study.
1. Review and discuss current literature/ feature extraction approaches.
1. This is kind of a Project Kick-Off: Create a work plan how to approach this problem also beyond the scope of the project week.

## Approach and Plan

1. Discuss features and feature extraction.
1. Radiomics is mostly done on CT, not so much on MR. Applicability of pyradiomics features?

## Progress

1. We had a first team meeting to bring together computer scientists and clinicians.
1. Dr. Wall reviewed her progress in selecting a small set of optimal diseased and control patients. This process has been challenging because many people with liver disease have had surgery or tumor ablation that changes the liver morphology. It is also not possible to select only patients on 3T scanner before BWH began using EPIC (2015).
1. Alireza Ziaei,  Raul San Jose, and Randy Gollub are assisting with RPDR querying and image retrieval.
1. Jennifer worked on CITI training for IRB clearance to access the data. And talked with experts using PyRadiomics on MRI Data and their approaches on evaluating features (Michael Schwier and Joost van Griethuysen).

## Next Steps

1. Lock down the image queying and retrieval pipeline.
1. Get deidentified data to University of Bremen team.
1. Think hard about segmentation, machine learning, and analysis techniques for the data.

# Background and References
