Back to [Projects List](../../README.md#ProjectsList)

# Insula segmentation with 3D Slicer

## Key Investigators

- Filippo Cicali (Mass General Hospital and Harvard Medical School - USA)
- Nikolaos Makris (Brigham and Women's Hospital and Harvard Medical School - USA)


# Project Description

To parcellate accurately the Insula into each principal anatomic units. Specifically the anterior (aINS) and the posterior (pINS) lobules.

## Objective

Using a T1 MRI dataset of the Human Connectome Project (HCP) we volumetrically measured the aINS and pINS.
This was achieved by defining the precise anatomy of the insula by identifying the morphology of the insular sulci which are visible using the T1 MRI and the Slicer 3D software.


1. To segment in each coronal slice the aINS and pINS ROIs in order to measure the number of voxels in each ROI per coronal slice.

1. Select a color for the aINS and for pINS to apply in each coronal slice.

1. 3D modelling.

1. Volume measures.


## Approach and Plan

Interact with developers to investigate the existence of appropriate tools and figure out how to implement them.

1. Document the procedure.

1. Disseminate the procedure to beta testers.


## Progress and Next Steps

Implement a method to accurately parcellate the anatomical structure Insula of Reil using 3D Slicer.

1. Improve the procedure with the new 3D Slicer Segment Editor.

Procedure:

	To achieve the goal of obtain the best balance between accuracy and time consume we studied in deep the possible combinations of the tools available in the Segment Editor, interacting with the developers.
After various trying with the Segment editor tools 'threshold painting', 'grow from seeds', 'watershed', 'fill between the slices', 'tracing level' the actual results are obtained with the following procedure:

1) On a T1 MRI image, using the Segment Editor module, add 3 segments (the first for the background, the second for the whole Insula, the third will be used for the separation, becoming pINS). 
In order to establish accurately the boarders we drawn the Circular sulcus and the Central sulcus of the Insula on sagittal images where this anatomical structure is well visually detectable.
Then on coronal view it will appear a series of dots, in correspondence of the sulci, that are the landmarks for the segmentation. The Central sulcus (cesi) signs the landmark for the separation of anterior and posterior Insula (coronal view).

2) Using "Tracing level" tool find the best separation boarder between white and grey matter in order to obtain the external part of the insular cortex ribbon. Important: the part segmented in this step, with the first segment selected, will be the background of the insular cortex, first delineated as a "negative" (unfilled area).

3) Using the "Paint" tool continue the draw of the outside part with respect of insular cortex, establishing the "negative" of our target structure.

4) Now select the second segment, "Paint" tool, masking editable area on "Outside all segments". Then draw inside the before obtained negative of the insular cortex, filling the area.
Repeat this on each coronal slice where Insula is visible (on average 85 slices with MRI slice thickness 0.7mm).

5) After manual completion visually check the 3D model.

(SEPARATION OF ANTERIOR, POSTERIOR INSULA AND VOLUMETRIC MEASURES)

6) Select the third segment added before.

5) On the 3D model of the parcellated Insula, in the 3D view, use 'Scissors' tool, drawing on the Central sulcus and comprehending the posterior lobule of the Insula. After this check the precision of the boarder of aINS and pINS with respect of the before drawn central sulcus.

6) In order to calculate the volume measures of the parcellated anatomical structure representations, in Segment Editor, 'Segmentations', export the segments converting them in labels 

7) Use 'Quantification' module, 'Label Statistics' to obtain volumetric measures of each label (aINS, pINS).


# Illustrations

Circular Sulcus (white) and Central Sulcus (yellow) in the parcellation method of anterior and posterior Insula

![Insula Circular Sulcus and Central Sulcus in the parcellation method of aINS and pINS](Insula_Project.png)

Parcellation of aINS and pINS - Volumetric measures

![Parcellation of anterior an posterior Insula and volumetric measures](https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/Insula_segmentation_with_3DSlicer/fullviews.png?raw=true)

<p align="center">
3D model of the "Insula of Reil"
</p>

<p align="center">
 <img src="https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/Insula_segmentation_with_3DSlicer/aINS_pINS_1.gif?raw=true"/>
 </p>

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
