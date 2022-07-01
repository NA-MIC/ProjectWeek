Back to [Projects List](../../README.md#ProjectsList)

# Write full project title here

## Key Investigators

- Xiang Chen (Memorial University of Newfoundland)
- Oscar Meruvia-Pastor (Memorial University of Newfoundland)
- Touati Benoukraf (Memorial University of Newfoundland)

# Project Description

This is an extension for computing the percentage of colocalization(Spatial overlap between different channels) of Z-stack TIFF images, which developed for category 'Quantification'.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. As of now, the computation of my module is a bit slow(when the threshold range for each selected channel is very large), so I'm hoping to get help from slicer experts to make it faster.

## Approach and Plan

1. Collaborate with Slicer community members during this Project Week.

## Updates and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Currently my extension has already implemented the calculation functionality and the current goal is to increase the calculation speed.
2. As shown below, The calculation time has been greatly reduced after removing all unnecessary code related to creating the closed surface representations for all segments.

**Before:**
<div align=center><img src="https://user-images.githubusercontent.com/27936765/176801278-a7f6814e-4a82-4ca1-b44e-9f9348692145.png"/></div>

**Now (The calculation time has been shortened to less than 30s):**
<div align=center><img src="https://user-images.githubusercontent.com/27936765/176802296-cc2bda9e-9c7e-42c2-beba-e98e95a5d835.png"/></div>

When the threshold range is set not that so large, the calculation time will be shorter:
<div align=center><img src="https://user-images.githubusercontent.com/27936765/176802305-dbd17585-b8e0-4f13-a71b-f4193e1d6d11.png"/></div>

**Next Steps:**
1. Convert the volume corresponding to each channel in the ROI to a numpy array.
2. Apply thresholding to all numpy array of the volumes within the ROI.
3. Detect all intersections among all channels using numpy indexing.
4. Count the number of voxels resulting from step 3 and multiply by the volume of one voxel.

# Illustrations

Users can threshold the volume rendering of the input Z-stack image in the 3D view window, select the region of interest(ROI) by the bounding box, and get a Venn diagram that shows the critical metric of colocalization's percentage.
[Extension ScreenShots](https://github.com/ChenXiang96/SlicerColoc-Z-Stats/blob/main/Images/Screenshots.png)


# Background and References
[The link to the source code repository](https://github.com/ChenXiang96/SlicerColoc-Z-Stats)

[Download links to sample image](https://drive.google.com/file/d/1IYlggsikgtQR7jXE83sSS2ZtMCuswsA0/view)
