Back to [Projects List](../../README.md#ProjectsList)

# Deep Learning for Subcortical Brain Segmentation

## Key Investigators

- Jarrett Rushmore (BU/BWH/MGH)
- Elizabeth Kenneally (Tufts/BWH)
- Sylvain Bouix (BWH)
- Nikos Makris (MGH/BWH/BU)
- Kyle Sunderland (Queens)

# Project Description

The goal of the project is to evaluate and implement deep learning approaches to the segmentation of brain structures on MRIs, particularly those with complex shapes and borders.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Investigate and evaluate the utility of MONAI and/or 3D Slicer AIAA to accomplish our goal.
1. Objective B. Set up hardware and software.
1. Objective C. Generate training datasets based on 50 manually segmented ventricles.
1. Objective D. Produce segmentation from deep learning and evaluate results.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Speak to experts for MONAI and AIAA.
2. Start process of setting up server and testing out software
3. Produce and distribute lateral ventricles
4. Evaluate segmentation results

## Progress

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Learned from and consulted with experts.
2. Identified a server and began setting it up to run MONAI label
3. Benefited from the benificence of the NAMIC community to get input on segmentation results from high-resolution lateral ventricle segmentation and whole brain segmentation.
4. Were very impressed with the power, timeliness, potential and results of the segmentation results (DICE of 0.88 after only 15 training sets!; good whole brain parcellation after less than one minute).


## Next Steps
1. Complete server set-up.
2. Build training sets and networks for subcortical structures; test integration of DL-based results with current segmentation workflow.
3. Investigate training whole brain parcellation with 0.7mm voxel size.


# Illustrations



![Namic_1](https://user-images.githubusercontent.com/51300488/124282278-a7739500-db18-11eb-8d9d-94352fd832ac.png)
Results of MONAI on Left Lateral ventricle segmentation

![Namic_2](https://user-images.githubusercontent.com/51300488/124282344-b8bca180-db18-11eb-80da-196b6a80e4e7.png)
Results of Whole Brain Segmentation (HighResNet; https://github.com/fepegar/highresnet)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, a![Uploading Namic_1.png…]()
nd to any relevant publications. -->
