Back to [Projects List](../../README.md#ProjectsList)

# Streamlined Outlier Detection for Large Scale Mammogram Data

## Key Investigators

- Pablo Bendiksen (University of Massachusetts Boston)
- Neha Goyal (University of Massachusetts Boston)
- Ryan Zurrin (University of Massachusetts Boston)
- Kendrick Kheav (University of Masachusetts Boston)
- Daniel Haehn (University of Massachusetts Boston)

# Project Description


## Objective

1. Implementation of a flexible API for the quick access and viewing of any collection from our > 190,000 Dicom images 
1. Develop a good sense for what typical mammograms look like or, conversely, what atypical images look like.
1. Determine classifer and input type combination that yields sufficiently accurate outlier detection. 

## Approach and Plan

1. Develop a good sense for what typical mammograms look like or, conversely, what atypical images look like.
1. Prepare mammogram collection as input to unsupervised learning algorithm. Univariate versus Multivariate.
1. Determine classifer and input type combination that yields sufficiently accurate results. 

## Progress and Next Steps


1. It is known that the presence of views or frames are a telltale feature of an anomalous Dicom image but other features may be less easily identifiable.
1. Image samples have been normalized and converted to image histograms for simple automated univariate anomaly detection.
1. Using the easily-accessible pyOD toolbox library, batch testing for unsupervised learning has been employed.
1. Api for the fast access and easy viewing of any collection of our > 190,000 Dicom images or image histograms, sorted by corresponding trained outlier values, has been developed.

# Illustrations


# Background and References
See an explanatory article for the comprehensive and user-friendly PyOD outlier detection toolbox [here](https://www.jmlr.org/papers/volume20/19-011/19-011.pdf?ref=https://githubhelp.com))  
