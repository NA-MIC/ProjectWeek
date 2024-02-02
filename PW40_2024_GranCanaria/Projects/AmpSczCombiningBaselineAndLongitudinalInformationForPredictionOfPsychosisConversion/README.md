---
layout: pw40-project

permalink: /:path/

project_title: AMP SCZ Combining baseline and longitudinal information for prediction of psychosis
  conversion
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Pablo Polosecki
  affiliation: IBM Research
  country: USA

- name: Nora Penzel
  affiliation: MGH
  country: USA

- name: Ofer Pasternak
  affiliation: MGH
  country: USA
  
---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project is part of the [AMP SCZ program](https://www.ampscz.org/), an initiative for early detection of risk for schizophrenia.

A key goal in AMP SCZ is to predict which patients that present initially mild or sub-threshold symptoms will eventually develop psychosis. Most predictive models are based on data acquired on their first medical visit (the baseline visit). An important question is how much is gained by following patients over time (longitudinal data). Moreover, what is a principled way to combine baseline and longitudinal information?

In this project we will implement predictive models that make use of both baseline and longitudinal information for psychosis prediction. This project builds on a previous [one](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/LongitudinalModelOfPsychosisConversion/), in which we implemented an approach called "joint modeling", which had important limitations. For this project, we will implement one based on a combination of two approaches:

- Multiple kernel learning (MKL): a simple predictive model for the fusion of multiple modalities. MKL combines kernels (i.e. a similarity measure across samples) from different modalities. Some modalities could be baseline measures, while others could be longitudinal trajectories.
- Dynamic time warping (DTW): a way to estimate the dissimilarity or distance between trajectories, regardless of differences in the number of time points, sampling rate, or the existence of delays between them. It is simple to build kernels for MKL from DTW distances.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Implement a Python-based version of MKL-DTW longitudinal models adapted for common best practices in machine learning (separate train/test, scikit-learn compatible methods).
2.  Quantify the advantage of longitudinal models vs baseline predictors in a legacy dataset.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Write an estimator of kernel distances based on DTW in python.
2.  Write an extension of the MKL package MKLpy that can integrate DTW kernels for longitudinal modalities with traditional kernels for baseline modalities.
3.  Benchmark performance on a legacy dataset.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  We implemented a number of similarity measures for multivariate longitudinal sequences.
2.  We implemented the extension of multiple kernel learning to use these kernels in longitudinal datasets.
3.  We curated a dataset from a semi-public source (NIH) with cross-sectional and longitudinal information.
4.  We tried using the curared dataset to validate the new prediction method. We are currently finding some issues with the samples, which we are fixing.

### Next steps:
5.  Fix the issues with the proposed dataset.
6.  Find a new dataset to make longitudinal predictions in a clinically usefull scenario (e.g. few visits)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
