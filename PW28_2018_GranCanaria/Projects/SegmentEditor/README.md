Back to [Projects List](../../README.md#ProjectsList)

# Segment Editor clinical workflows

## Key Investigators

- [Csaba Pinter](http://perk.cs.queensu.ca/users/pinter) (Queen's University, Canada)
- ~~Till Best~~
- [Nikos Makris](https://lmi.med.harvard.edu/people/nikos-makris) (Brigham and Women's Hospital and Harvard Medical School, USA)
- Filippo Cicali (Massachusetts General Hospital and Harvard Medical School, USA)
- Tina Kapur (Brigham and Women’s Hospital and Harvard Medical School, USA)

## Participating
- [Marco Nolden](https://www.dkfz.de/en/mic/team/people/Marco_Nolden.html) (DKFZ, Germany)
- [Attila Nagy](http://www.klinikaikozpont.u-szeged.hu/orl/index.php/hu/munkatarsak) (SZTE Medical School, Hungary)
- Sharon Peled (Brigham and Women's Hospital and Harvard Medical School, USA)

# Project Description

## Objective

* Segment Editor is the new manual and semi-automated image segmentation module in Slicer. It has powerful tools, but the learning curve can be steep for segmenting more complex cases.
* The objective is to help researchers aiming to use Segment Edtitor use it for their specific use cases, and augment the training material based on the results

## Approach and Plan

* Each participating researcher brings a dataset, for which we'll attempt to develop an effective segmentation workflow
* Add the developed workflows in the [Slicer Segmentation Recipes](https://github.com/lassoan/SlicerSegmentationRecipes) page
  * Publicly share dataset
  * Create a tutorial page for the segmentation case including screenshots

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

* Insula segmentation in MRI with Filippo Cicali and Nikos Makris
  * Possible solution: Use Grow from seeds iteratively, then use scissors and masked paint to cut
  * Consider speeding up segmentation by using a stylus instead of a mouse, and explore faster ways of slice navigation (3D mouse, webcam tracking, etc?)
* Brachytherapy needle segmentation in MRI for training deep learning models
  * Possible solution: Add "tube" mode from Markups to Models extension to Segment Editor, as an option to surface cut or a new effect in a new extension
  * Deep learning training support: need cohort segmentation slicelet that allows configuring segment editor before segmenting first patient for simpler, less distracting user interface for easier usage and smoother and more reliable segmentation workflow
* Minor help to multiple projects involving segmentation

# Illustrations
Whole heart segmentation:

![Whole heart segmentation](https://www.slicer.org/w/images/c/c1/20180612_SegmentEditor_WholeHeartScreenshot.PNG)

Spine phantom 3D printing:

![Spine phantom 3D printing](https://www.slicer.org/w/images/4/47/20180612_SegmentEditor_SpinePhantomMontage.png)

Segment Editor in presentation in Casa África:

![Segment Editor in presentation in Casa África](../../CasaAfrica_SegmentEditor_Panorama.jpg)

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [Segment Editor documentation](http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html)
- [Segmentation training material on Slicer wiki](https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation)
- [Slicer Segmentation Recipes](https://github.com/lassoan/SlicerSegmentationRecipes)
