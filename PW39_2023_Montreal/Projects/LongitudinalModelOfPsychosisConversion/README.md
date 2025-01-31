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
Our progress was somewhat less than it could have been otherwise since we could only stay for the first half of the week. Nevertheless we made significant progress on the aspects that benefited the most from in-person interaction: understanding the complex dataset we are working with.
1.  We first spent time understanding the coding of different events in the dataset, including a number of inconsistencies that were revealed as we dived into the data. We learned that psychosis conversion events are only recorded in special visits, and that their date does not coincide with the conversion date. The latter is coded in a separate field a followed a different date format.
2.  We followed an incremental strategy to decide if longitudinal information from a preselected set of clinical measures provided additional prognostic information relative to baseline alone.
    1.  We attempted the simplest models using linear classifiers based on baseline and follow-up clinical measures to get a rought estimate of predictive power with longitudinal data.
    2.  We built and tested baseline models using pre-selected baseline variables from the literature.
    3.  We combined the baseline models with the baselien and follow-up clinical measures to get a rough estimate of their combined predictive power.
3. We started implementing the "joint modelling" approach that combines standard survival analyses with linear mixed effects modeling.

We learned that a significant number of converters (close to 40%) do so before there is a chance for a follow-up visit. This complicates the comparison between baseline and follow-up predictions. We also saw little advantage of combining baseline and follow-up information. The mild benefits of follow-up information resided in the follow-up values alone and not their change relative to baseline.
Now that we have converged on an understanding of the dataset and the measures to be used for modeling, the next stepts involve estimations using "joint modeling". We hope to also create a python wrapper to these R packages that can be generally useful. A subsequent step would include multivariate modeling of trajectories.



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [Joint modeling in R](https://github.com/drizopoulos/JM)
*   [sci-kit survival](https://scikit-survival.readthedocs.io/en/stable/index.htmll)
*   [lifelines](https://lifelines.readthedocs.io/en/latest/index.html)
*   [rpy2](https://rpy2.github.io/doc/v3.5.x/html/index.html)
