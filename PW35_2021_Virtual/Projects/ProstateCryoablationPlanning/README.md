Back to [Projects List](../../README.md#ProjectsList)

# Slicer module for planning MR-guided focal cryoablation of prostate cancer

## Key Investigators

- Pedro Moreira (BWH)
- Nicholas Fordham (BWH)

# Project Description
Prostate cancer (PCa) recurrence after radiotherapy may affect 10 to 60% of patients within 5-10 years after treatment. 
Salvage prostatectomy of post-radiation recurrent PCa is challenging because of radiation-induced fibrosis and shrinkage of the prostate gland. 
Minimally invasive focal cryoablation has been selected as an alternative salvage treatment for PCa post-radiation recurrence. Safe and effective focal cryoablation requires the deployment of the cryo-needles at optimal locations so that the created lethal ablation zone fully encompasses the tumor while preserving surrounding healthy tissues. 
Currently, physicians rely on the pre and intraoperative images and their own experience to define the best cryo-needle locations and manually insert them using a grid template. However, predicting the final shape of the lethal ablation zone is challenging as it will depend on several patient-specific factors such as proximity to heat sources and thermal properties of the prostatic tissue. The primary objective of this project is to develop a planner to maximize the amount of the target volume encompassed by the defined isotherm while sparing critical structures. The planner will use a data-driven approach to estimate the visible iceball using a logistic regression model and consider a safety margin to define the best cry-needle placement. Our ultimate goal is to develop a 3D Slicer module for MR-guided focal cryoablation ready to be used in clinical procedures
## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Implement a planning algorithm in 3D Slicer
1. Objective B. Integrate the planning and the current Module used for MRI-guided cryoablation
1. Objective C. Deep learning for iceball segmentation

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Change the current module to work with Slcier 4.11
1. Implement optimization algorithm considering the constraints of the template approach
1. Test the algorithm with retrospective data

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. .
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
