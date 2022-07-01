# Write full project title here

## Key Investigators

Jax Luo (BWH & Harvard Medical School)

Loraine Franke (University of Massachusetts Boston)

Raymond Yang (University of Massachusetts Boston)

Daniel Haehn (University of Massachusetts Boston)

Steve Pieper (Isomics, Inc.)

Lipeng Ning (BWH & Harvard Medical School)


# Project Description

Transcranial magnetic stimulation (TMS) is a noninvase procedure used for treating depression. In the TMS treatment, a magnetic coil is placed on the subject's head to induce an electirc field (E-field) to stimulate targeted brain regions. 


Our project aims to predict the distribution of the E-field in real-time so that the clinicians can adjust the location of the coil and target the brain ROI with the maximal stimulation strength. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Predicting the distribution of the E-field based on the location of the coil



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Read a affine transform matrix from the updated (rotated) coil.
2. Perform an affine transformation to the Coil information and resample it to the subject head model space. 
3. Combine the Coil information and head model and to generate a new nifti file and pre-process it.
4. Predict the E-field using the generated nifti file and a pre-trained deep network.
5. Visualize the precition result (.nii)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Finished step 1-4. 
2. Working on intergrating the code to the visualization module. 

# Illustrations

Visualization of the predicted E-field using the developed interface.
![Visualization of the predicted E-field from another software](https://github.com/NA-MIC/ProjectWeek/blob/master/PW37_2022_Virtual/Projects/SlicerTMS/tmscoil_on_brain_surface.png)

-->

# Background and References
This is the sister project of [Slicer TMS Deep-Learning](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/SlicerTMS)
