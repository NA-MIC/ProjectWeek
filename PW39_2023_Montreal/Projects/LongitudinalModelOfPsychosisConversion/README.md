---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/LongitudinalModelOfPsychosisConversion/README.html

project_title: AMP SCZ Longitudinal model of psychosis conversion
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
  affiliation: BWH
  country: USA

- name: Guillermo Cecchi
  affiliation: IBM Research
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project is part of the AMP SCZ program, an initiative for early detection of risk for schizophrenia(<https://www.ampscz.org>).

A key goal in AMPSCZ is to predict which patients that present initially mild or sub-threshold symptoms will eventually develop psychosis. Most predictive models are based on data acquired on their first medical visit (the baseline visit). An important question is how much is gained by following patients over time (longitudinal data). In this project we will implement predictive models that make use of this longitudinal information for psychosis prediction. We will focus on implementing a type of models called "joint models", which incorporate time-varying predictors into well known survival analyses.

https://www.ampscz.org/

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A. Implement a Python-based version of longitudinal models adapted for common best practices in machine learning (separate train/test, scikit-learn compatible methods).
2.  Objective B Quantify the advantage of longitudinal models vs baseline predictors in a legacy dataset.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Write a python wrapper, using rpy2, for the R library JM that implements longitudinal analysis.
2.  Use synthetic and legacy datasets to test the predictions.
3.  Use python libraries such as lifelines or scikit-survival to implement survival analysis with baseline predictions only.
4.  Implement permutation tests in time to asses the significance of prediction improvements due to longitudinal change.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Describe specific steps you **have actually done**.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [Joint modeling in R](https://github.com/drizopoulos/JM)
*   [sci-kit survival](https://scikit-survival.readthedocs.io/en/stable/index.htmll)
*   [lifelines](https://lifelines.readthedocs.io/en/latest/index.html)
*   [rpy2](https://rpy2.github.io/doc/v3.5.x/html/index.html)
