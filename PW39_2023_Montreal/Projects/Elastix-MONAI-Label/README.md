Back to [Projects List](../../README.md#ProjectsList)

# Write full project title here
3D Medical Image Registration and Segmentation using Elastix and MONAI Label

## Key Investigators

- Investigator 1 Andres Diaz-Pinto (NVIDIA, UK)
- Investigator 2 Konstantinos Ntatsis (LUMC, Netherlands)
- Investigator 3 (Affiliation)

# Project Description

At the moment we have 5 project proposals as a starting point of discussion on the topic of combining registration using elastix with deep learning analysis using MONAI label. We are looking forward to the feedback of the NA-MIC project week community! Projects can be added and others can be removed.

**[Project 1]**

Train a single modality MONAI Label models on Elastix-aligned brain images (T1, T2, FLAIR, etc) using SynthSeg (https://github.com/BBillot/SynthSeg) as the source of annotated datasets - For Nomal brains

SynthSeg is a tensorflow-based deep learning segmentation tool for brain MRIs. It consists of a generative network that produces the synthetic images and a 3D U-Net trained to do the segmentation. The only input (training data) is the training labels so no real images are used.

We will use SynthSeg to produce annotations as “ground truth” on a publicly available dataset like BRATS (multimodal + non-healthy brains) or OASIS (temporal/monomodal + healthy brains). Elastix will be used for the co-registration of the different modalities or temporal images and achieve segmentation via registration.

**[Project 2]**

Train a MONAI Label model using the raw BRATS dataset (https://www.kaggle.com/competitions/rsna-miccai-brain-tumor-radiogenomic-classification/data). Elastix will be used to co-register the 4 modalities.

This is a classification task. Hypothesis: Registration with elastix might help the classification accuracy. So, we can compare the classification result with and without pre-alignment.

**[Project 3]**

Extend the whole brain segmentation model available in the Model Zoo (https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBrainSeg_Large_UNEST_segmentation)

The data used for the training were registered affinely in the MNI305 space. Hence, elastix can be used to also register any data used for inference in the same space. We could also store all the result transform parameters so that the users could just do the resampling directly without registering again (this holds true for the traning data - unseen data used for inference should still need to be registered).

**[Project 4]**

Compare registration performance between cross-modal registration (CT-MRI) versus intra-modal registration via synthesised MRI (MRI_syn - MRI). MONAI for the synthesis and elastix for the registration. What would a suitable dataset be?

**[Project 5]**

Train MONAI Label model for automatic landmark identification in e.g. lung images (dataset: https://med.emory.edu/departments/radiation-oncology/research-laboratories/deformable-image-registration/index.html) . Landmarks can be used either to assist registration with elastix OR elastix can be used to validate the landmark accuracy. 3D Slicer can be used to visualize the landmarks (ease the qualitative evaluation).


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Describe **what you plan to achieve** in 1-2 sentences.
1. Objective B. ...
1. Objective C. ...

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
1. ...
1. ...

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
