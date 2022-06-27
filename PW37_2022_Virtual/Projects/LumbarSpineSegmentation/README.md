Back to [Projects List](../../README.md#ProjectsList)

# Lumbar Spine Segmentation using MONAI Label

## Key Investigators

- Nayra Pumar (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- María Rosa Rodriguez (Universidad de Las Palmas de Gran Canaria (ULPGC), Spain)
- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)

# Project Description

<!-- Add a short paragraph describing the project. -->

## Objective

Train and deploy neural network to segment lumbar verteral bodies and intervertebral discs from MRI 3D volumes of the lumbar region.

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Prepare the public dataset of choice, using the T2.
1. Objective B. Train MONAI to segment the 5 vertebrae (from L1 to L5) and the 4 intervertebral corresponding discs.
1. Objective C. Test the trained model with different public datasets, or try it with T1 images

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Choose a public dataset
1. Get the files ready for MONAI.
1. Install the MONAI server locally
1. Train the model

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. The chosen dataset is [Multi-scanner and multi-modal lumbar vertebral body and intervertebral disc segmentation database]([https://www.google.com](https://www.nature.com/articles/s41597-022-01222-8 "Multi-scanner and multi-modal lumbar vertebral body and intervertebral disc segmentation database"): consisting of 39 patients. From all the images provided, we selected 51 of them, the ones with a T2 volume.
1. Change the file format to .nii for the selected t2 images.
1. Unify the 9 segments into a single file (5 segments for vertebrae and 4 for discs)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
