Back to [Projects List](../../README.md#ProjectsList)

# mpReview: Development of a streamlined Slicer module for (manual) image annotation

## Key Investigators

- Andrey Fedorov (BWH)
- Dora Szasz (U.Chicago)
- Masoom Haider (U.Toronto)
- Aytek Oto (U.Chicago)
- Andras Lasso (Queen's)
- Fiona Fennessy (BWH)
- Christian Herz (CHOP)
- Steve Pieper (Isomics)

## Project Description

**WE ARE HIRING - see [job opportunities here](https://spl.harvard.edu/join-us) if interested!**

In the past we have developed mpReview extension to streamline the manual annotation workflow of multiparametric MRI studies, designed specifically for prostate MRI annotation initially. The extension proved useful over time, and was utilized to support annotation of prostate MRI at BWH and U.Chicago. Over the recent years we were not able to maintain this extension to keep up to date with 3D Slicer upgrades. However, currently there is renewed interest in reviving and perhaps rewriting this extension, as it serves a need not addressed by any other capability in Slicer, or in commercial tools. The goal of this project is to evaluate the current status of the extension, collect the requirement and identify next steps for its development.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Document the current capabilities of the extension.
2. Document the annotation workflow requirements and the desired capabilities of the extension.
3. Identify relevant components of 3D Slicer that can be used to improve current implementation.
4. Define the next steps and the effort needed to implement them and interest from various groups of potential users to contribute to the development.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Evaluate current status of the module wrt the preview release of Slicer.
2. Document the workflow and desired features of the annotation module.
3. Identify next steps.
4. Revisit the [Slicer PI-RADS module](https://github.com/SlicerProstate/SlicerPIRADS) (WIP years ago)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
1. Revised documentation for the current version of the module: https://github.com/SlicerProstate/mpReview/wiki/Documentation
2. Updated test dataset
3. Discussed the current implementation, discussion notes [here](https://docs.google.com/document/d/1f6gXrl-u1mkMPVfLLT4oLHwPS8sZp48ent-qyWPzDMk/edit)
4. Tested with the current version of Slicer - some legacy Editor effects no longer work.
5. Based on feedback from Masoom, there is not much interest in patching existing mpReview, would need to rewrite it from scratch to work with the current Slicer infrastructure.
  * Instead of a custom module, maybe improve Slicer itself to improve effiency, like [this DICOM thumbnail experiemnt](https://github.com/commontk/CTK/pull/979)


## Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

![mpReview UI](mpReview_screenshot.jpg)

## Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
