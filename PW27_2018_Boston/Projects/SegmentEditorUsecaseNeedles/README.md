Back to [Projects List](../../README.md#ProjectsList)

# Using SegmentEditor for Deep Learning Data Annotation

## Key Investigators
- Guillaume Pernelle (@gpernelle), Roya Khajavi (@royak), Steve Pieper (@pieper), Csaba Pinter (@cpinter), Andras Lasso (@lassoan), Tina Kapur (@tkapur)

# Project Description

The superior ability of MR to visualize soft tissue has led to an increase in its use  in guiding percutaneous needle-based interventions such as brachytherapy and biopsy, especially in the human pelvis. A technical challenge associated with the use of MRI imaging in such cases, in contrast to say, CT imaging, is the clear visualization of needles that are inserted into cancerous tissue to either deliver radiation or extract a sample. We have developed algorithms for catheter segmentation and visualization through numerous project weeks [1-3]. In each case, we relied on a custom (editing) tool for creating gold standard segmentations of the needles.  We would like to explore the use of SegmentEditor for this task.

## Objective

1. Objective. Explore SegmentEditor as an alternative to current manual segmentation of needles in MRI.

## Approach and Plan

1. Learn how to apply SegmentEditor to  needles in MRI from experts
1. Optimize the workflow. Document it.
1. Use it to segment 500 needles in one day!

## Progress and Next Steps

1. We learned how to apply SegmentEditor and explored the extra effects of the SegmentEditorExtraEffects module
1. We considered adapting the SurfaceCut extra effect in order to draw multiple Bezier splines, but it would require substantial work to modify the UI of SegmentEditor to allow for segmentation and modification of several needles for a single case.
1. We decided instead to improve NeedleFinder, that has been developed for the specific case of multi needle segmentation.
1. The next steps are the make the NeedleFinder UI more user friendly and ask users for their feedback how to make the workflow easier/faster.

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [NeedleFinder](http://needlefinder.org)
- [SegmentEditor](https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html)
- [SurfaceCut](https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699)
- [Recent Publication](http://www.medicalimageanalysisjournal.com/article/S1361-8415(17)30098-1/abstract)
- Source code: [https://github.com/needlefinder/NeedleFinder](https://github.com/needlefinder/NeedleFinder)
