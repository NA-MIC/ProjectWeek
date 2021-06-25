Back to [Projects List](../../Readme.md#ProjectsList)

# Development of Deep Learning Segmentation for Spines with Metastatic Disease 

## Key Investigators

- Ron Alkalay (Beth Israel Deaconess Medical Center)
- Curtis Lisle  (KnowledgeVis,LLC)
- Andres Diaz-Pinto (Kings College Longon) 

## Project Description

We have 50 labeled CT data sets for lumbar and/or thoracic as well as full spine columns for 
patients at baseline. For a good # of patients, we also have 3 and 6m follow-up CT, but these are 
not yet labeled.  It would be great to get some help/advice regarding how to 
speed up the segmentation for the labeling and extraction of volume information from the masks.
The segmented volumes are needed for the analytical and computational modeling pipeline 
as part of a collaboration with MIT. Lytic spines present a special segmentation challenge because the interior of
vertibrae have degraded and appear like surrounding tissue in CT scans.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Setup MONAI-based neural network training on the labeled scans. 
1. Objective B. Investigate using MONAILabel as a possibly better way to annotate new scans. 
1. Objective C. Train a DNN on the labeled data.  Can this model be used in MONAILabel? 
1. Objective D. Find a path forward to better annotation using DL-assisted segmentation.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Start with publically available VerSe spine dataset.
1. Evaluate MONAILabel from Andres using model trained on VerSe as a segmentation tool for these lytic spines.  How good is segmentation? 
1. Consider fine-tuning model in MONAILabel with lytic spines from our dataset
1. Train model on only our lytic spines for comparison
1. Install MONAILabel on GPU hardware at BI to setup for better annotation after project week

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Acquired anonymous patient dataset. Have requested permission to share for the project week
1. Acquired GPU hardware.  Currently running Windows.  Evaluated installing Linux, WSL, and Conda-on-windows.  None working yet.
1. ...

## Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
[Sample lytic vertebrae](lytic-vertebrae-example.png)
[Segmentation in Slicer](lytic-vertebrae-in-slicer.png)

## Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

[VerSe: A Vertebra Labelling and Segmentation Benchmark](https://www.researchgate.net/publication/338853005_VerSe_A_Vertebrae_Labelling_and_Segmentation_Benchmark).

