Back to [Projects List](../../README.md#ProjectsList)

# Conversion of MONAI Label trained network into a MONAI bundle

## Key Investigators

- Deepa Krishnaswamy (Brigham and Women's Hospital, USA)
- Cosmin Ciausu (Brigham and Women's Hospital, USA)
- Nazim Haouchine (Brigham and Women's Hospital, USA)
- Andres Diaz-Pinto (NVIDIA, USA)
- Jesse Tetreault (NVIDIA, USA)
- Roya Hajavi (Brigham and Women's Hospital, USA)
- Stephen Aylward (Kitware, USA)
- Steve Pieper (Isomics Inc, USA)
- Andrey Fedorov (Brigham and Women's Hospital, USA)

# Project Description

MONAI Label has become a very popular tool in the NA-MIC community for developing new trained models and incorporating expert feedback into the training process.

Unfortunately, it is currently not straightforward to take the models trained using MONAI Label and apply them in batch mode.

MONAI supports bundles, which are designed for batch mode processing, but the process of converting MONAI Label trained networks into MONAI bundle representation is not well understood and (per MONAI experts) currently requires support from MONAI developers.

In this project we want to explore the process of converting MONAI Label trained networks into MONAI bundle format, and demonstrate how the resulting bundles can be applied to datasets in [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Develop a complete example transforming MONAI Label network to MONAI bundle.
1. Improve existing documentation.
1. Demonstrate how MONAI Label trained network converted to bundle can be applied to a representative sample of data from IDC.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use MONAI Label trained model for [segmentation of vertebrae in CT](https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L174) as the use case. 
2. Identify MONAI documentation for transforming MONAI Label trained network into MONAI bundle format.
3. Develop MONAI bundle from the network in 1.
4. Select applicable representative subset of data from IDC and apply resulting bundle to a produce segmentations, save segmentations as DICOM SEG, confirm visualization with OHIF.
5. Document the process and any refinements to the existing instructions.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Identified MONAI Label network location; discussed the project with Stephen, identified relevant expertise on MONAI side; planning to have coordination meeting with Roya.
1. Identified from Andres an example of a [MONAI Label app](https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py) and the corresponding [MONAI bundle](https://github.com/Project-MONAI/model-zoo/tree/dev/models/spleen_deepedit_annotation/configs). 
1. Identified another possible example of a [MONAI Label app](https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation_spleen.py) and the corresponding [MONAI bundle](https://github.com/Project-MONAI/model-zoo/tree/dev/models/spleen_ct_segmentation/configs). 
1. In progress [colab notebook](https://github.com/ImagingDataCommons/idc-vertebrae-ct-segmentation/blob/main/MONAI_spine_localization_task.ipynb) for the conversion of spine localization task
1. Discussion with Jesse, Andres, Stephen, Steve: 
  - Look into creating a bundle vs MONAI deploy app SDK. 
  - We started a public discussion of MONAI label app to bundle creation [here](https://github.com/Project-MONAI/MONAI/discussions/5894#discussioncomment-4769712)
1. Yesterday during the MONAILabel AWS workshop, we tried out the localization_spine step. It seemed to work on the dataset, but we noticed that the model was both named differently and in a different app folder. We wanted to make sure that we could also perform the localization_spine successfully either in Slicer or in a script. We started with the scripted version [here](https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py), on a nifti file from VERSE, which was also used for training. We expected this to produce a somewhat reasonable segmentation of the spine, but it produced an empty segment. We tried the second stage of localization_vertebra model, and this produced a partial segmentation of one vertebra. 
1. We then explored into setting up MONAILabel locally. We managed to install everything and start the server on Windows (Mac is a WIP), and ran inference using the localization_spine model through Slicer on a nifti file from the training data in VERSE. This again yielded empty segments...
1. We found a post in the [Slicer discourse forum](https://discourse.slicer.org/t/monailabel-vertebrae-segmentation-sample-app-doesnt-work-for-sample-data/27243). However, this doesn't completely address our problem as this one uses a network trained on TotalSegmentator data to perform segmentation of organs+vertebrae. Though the segmentations might be acceptable, this might not work for all as there is no preservation of the ordering of the vertebrae, which might be better addressed by the 3 stage vertebra_pipeline (localization_spine, localization_vertebra, vertebra_segmentation). 
1. We will talk to Nazim tomorrow to see if he has encountered issues using the localization_spine step on data that it was trained on. In the meantime, we will try out the updated model provided by Andres for vertebra segmentation [here] (https://drive.google.com/drive/folders/17eJan-8_oNCnZyJk8B9zLQpwaOjtDuKi?usp=share_link) to make sure we can at least get results with this in Slicer. Perhaps we can convert this to a bundle first?

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

- [NCI Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/)
- [MONAI bundle docs](https://github.com/Project-MONAI/tutorials/blob/main/bundle/get_started.md)
- [MONAI Label app for vertebrae segmentation](https://github.com/Project-MONAI/MONAILabel/blob/fullCTSegmentation/sample-apps/radiology/lib/configs/segmentation_full_CT.py)
- [MONAI Label app for whole body segmentation](https://github.com/Project-MONAI/MONAILabel/blob/fullCTSegmentation/sample-apps/radiology/lib/configs/segmentation_full_CT.py)
- [MONAI bundle specification](https://docs.monai.io/en/stable/mb_specification.html)
- Script from Steve to run MONAILabel model in batch from Slicer: [https://github.com/LymphNodeQuantification/Monailabel-LNQ/blob/main/Experiments/reviewer.py](https://github.com/LymphNodeQuantification/Monailabel-LNQ/blob/main/Experiments/reviewer.py)
