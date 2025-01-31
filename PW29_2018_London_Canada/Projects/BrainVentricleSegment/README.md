Back to [Projects List](../../README.md#ProjectsList)

## Segmentations of the sub-regions of the brain ventricles

## Hassan Haddad (Robarts)

# Project Description
* To divide the brain ventricles into a number of sub-reions and segment them by drawing a number of planes based on the known anatomical structures in the brain

## Objective
1. Segmentation of the brain lateral ventricles.
2. Segemenation of the sub-regions within laterla ventricles.

## Approach and Plan

1. Segmentation of the lateral ventricles of the brain using watershed module of the 3D Slicer.
2. Transferring the atlas and standard masks from the lobes to the subject space.
3. Finding the boundary voxels of the mask obtained from atlases and registration to the subject space, and match them with the partial voumes of the lateral ventricles that lie within the mask.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

[Segmentation of brain ventricle](Untitled.png)
[mask in the standard space](Untitled2.png)

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
