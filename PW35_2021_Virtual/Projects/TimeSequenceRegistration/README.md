Back to [Projects List](../../README.md#ProjectsList)

# Time Sequence Registration for Deep Learning

## Key Investigators

- Curtis Lisle, Ph.D. (KnowledgeVis,LLC)
- Neha Goyal, (U Mass, Boston)
- Greg Sharp, Ph.D. (MGH)

## Project Description

We plan to prepare a Lung RadioTherapy patient cohort for deep learning segmentation and annotation.  We will first use Slicer and other NA-MIC 
tools to register patients' follow-up scans to their original planning CT scans as a preparatory step for deep learning. if time allows, we will train a deep neural network to predict patient outcomes from the time series data.   

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Align follow-up scans to planning CTs using 3D Slicer, Plastimatch, or other algorithms.
2. Objective B. Gain insight on traditional registration methods vs. emerging deep learning methods
3. Objective C. Develop scripts to run on multiple patients and inspect the results using 3D Slicer. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Select candidate patient scans and registration tools in Slicer
2. Compare registration results from a few algorithms in Slicer (Elastix, Plastimatch, etc.)
4. Investigate Deep Learning based methods for image registration (e.g. VoxelMorph, DeepReg)
6. Determine which approaches are suitable for automated use on a large cohort

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Acquired anonymous patient dataset with preplanning CT&PET,Planning CT, follow-up CT and PET
1. We solicit recommendations: Elastix and Plastimatch both offer command line and Slicer integration
1. **Plastimatch:** An interactive session with Greg showed us how to register scans (see below example)
1. **MONAI:** - Neha adapted a MONAI / DeepReg example to train a DNN for registration between patient CTs.  This is still a work-in-progress, but shows promise. 
2. Automation - Curt started developing scripts for automating registration between the planning CT and the follow-ups
3. **Next Steps:** - Tweak registration parameters to improve results; Run on 100 patient cohort 

## Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![Planning CT has excellent structure segmentation](https://data.kitware.com/api/v1/item/60d92be32fa25629b980f149/download?contentDisposition=inline)

![No registration between successive scans](https://data.kitware.com/api/v1/item/60d92be52fa25629b980f151/download?contentDisposition=inline)

![Images after a preliminary registration](https://data.kitware.com/api/v1/item/60de5f252fa25629b9c6ee2e/download?contentDisposition=inline)


## Background and References

The **Image Data Commons** has datasets with annotations across multiple time points, so this is an available dataset to practice with: https://imaging.datacommons.cancer.gov/explore/?filters_for_load=%5B%7B%22filters%22:%5B%7B%22id%22:%22120%22,%22values%22:%5B%22qin_prostate_repeatability%22%5D%7D%5D%7D%5D

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. 
-->
Registration tools added to Project-MONAI: 

https://github.com/Project-MONAI/tutorials/blob/master/3d_registration/paired_lung_ct.ipynb
