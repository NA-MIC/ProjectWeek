Back to [Projects List](../../README.md#ProjectsList)

# Streamlined Outlier Detection for Large Scale Mammogram Data

## Key Investigators

- Pablo Bendiksen (University of Massachusetts Boston)
- Neha Goyal (University of Massachusetts Boston)
- Ryan Zurrin (University of Massachusetts Boston)
- Kendrick Kheav (University of Masachusetts Boston)
- Daniel Haehn (University of Massachusetts Boston)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Implementation of a flexible API for the quick access and viewing of any collection from our > 190,000 Dicom images 
1. Develop a good sense for what typical mammograms look like or, conversely, what atypical images look like.
1. Determine classifer and input type combination that yields sufficiently accurate outlier detection. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Develop a good sense for what typical mammograms look like or, conversely, what atypical images look like.
1. Prepare mammogram collection as input to unsupervised learning algorithm. Univariate versus Multivariate.
1. Determine classifer and input type combination that yields sufficiently accurate results. 

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. It is known that the presence of views or frames are a telltale feature of an anomalous Dicom image but other features may be less easily identifiable.
1. Image samples have been normalized and converted to image histograms for simple automated univariate anomaly detection.
1. Using the easily-accessible pyOD toolbox library, batch testing for unsupervised learning has been employed.
1. Api for the fast access and easy viewing of any collection of our > 190,000 Dicom images or image histograms, sorted by corresponding trained outlier values, has been developed.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
