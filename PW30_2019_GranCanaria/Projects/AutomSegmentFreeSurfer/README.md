Back to [Projects List](../README.md#ProjectsList)

# Refining automatic segmentations from FreeSurfer in 3D Slicer


## Key Investigators

-	Nikos Makris (Brigham and Women’s Hospital and Harvard Medical School)
-	Juan Andrés Ramírez González (ULPGC – IUIBS)
- Yogesh Rathi (Laboratory for Mathematics in Imaging - Harvard Medical School)
-	Nayra Pumar Carreras (ULPGC – GTMA-IUIBS – MACbioIDi)
-	Juan Ruiz Alzola (ULPGC – GTMA-IUIBS – MACbioIDi)
- Zora Kikinis (Psychiatry Neuroimaging Laboratory, Harvard Medical School)


## Project Description

This project aims to improve the automatic segmentation results generated from the Freesurfer software, by loading these results in 3D Slicer and validating / editing these results in order to gain a better anatomical accuracy.


## Objectives

1.	To segment the brain using MRI images (images provided by Dr. Nikos Makris)
1.	To refine the generated automatic segmentations
1.	To identify the modules/tools in 3D Slicer used during the project


## Approach and Plan

1.	To import the labelmap and MRI files into Slicer
1.	To refine the existing segmentation following the guidance of an anatomist


## Progress and Next Steps

1. The image used on this project is the MIR of the brain labelled 103414.  
1. The two structures that have been segmented are:
* Subcallosal area SC (from slices A31.900mm to A15.116mm)
- Medial border: hemispheric margin
- Lateral border: grey-white matter border 
- Superior border: corpus callosum
- Inferior border: inferior hemispheric curvature (45º line)
- Anterior border:
- Posterior border: 
* Orbito Frontal Cortex OFC (from slices A55.800mm F3 to A8.200mm F5 on the right hemisphere, from slices A56.500mm to A7.500mm on the left hemisphere).
- Medial border: olfatory surcus
- Lateral border: orbital surcus
- Superior border: grey-white matter border
- Inferior border: hemispheric margin
- Anterior border:
- Posterior border: 
In the OFC segment the medial and two lateral segments have been merged into a single segment.
1. The segmentation has been done manually, tracing the countours of the desired segments between the defined anterior and posterior boundaries on the coronal view.
We have taken, for the OFC, the traditional approach, following the olfatory surcus


## Illustrations


## Background and References



