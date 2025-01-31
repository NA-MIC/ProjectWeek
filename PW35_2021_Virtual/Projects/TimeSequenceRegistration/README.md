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
1. We solicited recommendations: Elastix and Plastimatch both offer a command line option as well as Slicer integration
1. **Plastimatch:** An interactive session with Greg showed us how to register scans (see below example)
1. **MONAI:** - Thanks to Neha for adapting a MONAI / DeepReg example and training a DNN for registration between patient CTs.  This is still a work-in-progress, but it shows promise. Curently, this approach requires more computation time during training than traditional registration methods.  However, in certain cases, inferencing on a pretrained registration network is reported to be faster than traditional methods, such as B-spline deformable registration. We didn't test the claim this week.
1. Automation: Curt began developing scripts for automatic registration between the planning CT and the follow-ups for each patient in a cohort
1. We didn't get to training a network on the registered cohort this week, but we have tested all the steps individually.
4. **Next Steps:** - Tweak registration parameters to improve results; Run on 100+ patient cohort; train deep learning network; celebrate with clinicians.

## Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
The Planning CTs have excellent annotations:

![Planning CT has excellent structure segmentation](https://data.kitware.com/api/v1/item/60d92be32fa25629b980f149/download?contentDisposition=inline)

But since follow-up scans are different times, there is no registration between them.  The CTs are "miles apart".  Shown below is the annotations from the planning CT superimposed over a follow-up CT, showing the shift between the different patient scans:

![No registration between successive scans](https://data.kitware.com/api/v1/item/60d92be52fa25629b980f151/download?contentDisposition=inline)

After a prelimary registration in Plastimatch, the anatomy annotations are much closer, as shown below. The image shows the original segmentation objects superimposed over a registered follow up scan taken 3 months later.  Because of the time between scans, there was actual morphology changes to the anatomy as well.  This result was encouraging after trying only a few parameter exploration attempts.  Since Plastimatch operations can be scripted, this approach can automate registration for multiple patient scans in a  cohort:

![Images after a preliminary registration](https://data.kitware.com/api/v1/item/60df063c2fa25629b9d1ae28/download?contentDisposition=inline)

Below is a snapshot of how the segmentation mask for the moving image is growing to match the anatomy and mask in the fixed image.  Our deep learning registration results this week don't match as well as using traditional methods, but this is an emerging application area for deep learning that will continue to improve.  Thanks, Neha!

![deep learning registration changes](https://data.kitware.com/api/v1/item/60df14472fa25629b9d34d65/download?contentDisposition=inline)

We also learned that giving a registration system incorrect parameters can warp an moving image too much.  After generating a strangely warped image by mistake, we just gave it some coloring to create art.  Here are our project team's two submissions to the "Project Week 35 3D-Slicer Art Competition".  Vote for your favorite. Vote by editing this page or vote on Curt's facebook page...

![slicer art](https://data.kitware.com/api/v1/item/60df033a2fa25629b9d17345/download?contentDisposition=inline)

Votes for #1: 0

Votes for #2: 0

## Background and References

The **Image Data Commons** has datasets with annotations across multiple time points, so this is an available dataset to practice registration techniques.  Free Google Cloud credentials are available for experimenting without having to download data for processing.  Simply select the cohort through IDC for analysis:
https://imaging.datacommons.cancer.gov/explore/?filters_for_load=%5B%7B%22filters%22:%5B%7B%22id%22:%22120%22,%22values%22:%5B%22qin_prostate_repeatability%22%5D%7D%5D%7D%5D

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications.
-->
Registration tools have been added to Project-MONAI in the 0.5 release.  The MONAI tutorials include a registration example now, which we used as a basis for our experimentation:

https://github.com/Project-MONAI/tutorials/blob/master/3d_registration/paired_lung_ct.ipynb
