Back to [Projects List](../../README.md#ProjectsList)

# Automatic multi-anatomical skull structure segmentation of cone-beam computed tomography scans using 3D UNETR

![Segmentation](https://user-images.githubusercontent.com/46842010/172177602-8cbfc188-9715-488a-ad2e-abb8d219536d.png)

## Key Investigators

- Luc Anchling (UoM)
- Nathan Hutin (UoM)
- Maxime Gillot (UoM)
- Baptiste Baquero (UoM)
- Celia Le (UoM)
- Romain Deleat-Besson (UoM)
- Jonas Bianchi (UoM, UoP)
- Antonio Ruellas (UoM)
- Marcela Gurgel (UoM)
- Marilia Yatabe (UoM)
- Najla Al Turkestani (UoM)
- Kayvan Najarian (UoM)
- Reza Soroushmehr (UoM)
- Steve Pieper (ISOMICS)
- Ron Kikinis (Harvard Medical School)
- Beatriz Paniagua (Kitware)
- Jonathan Gryak (UoM)
- Marcos Ioshida (UoM)
- Camila Massaro (UoM)
- Liliane Gomes (UoM)
- Heesoo Oh (UoP)
- Karine Evangelista (UoM)
- Cauby Chaves Jr
- Daniela Garib
- F ́abio Costa (UoM)
- Erika Benavides (UoM)
- Fabiana Soki (UoM)
- Jean-Christophe Fillion-Robin (Kitware)
- Hina Joshi (UoNC)
- Lucia Cevidanes (UoM)
- Juan Prieto (UoNC)


# Project Description

The segmentation of medical and dental images is a fundamental step in automated clinical decision support systems.
It supports the entire clinical workflow from diagnosis, therapy planning, intervention, and follow-up.
In this paper, we propose a novel tool to accurately process a full-face segmentation in about 5 minutes that would otherwise require an average of 7h of manual work by experienced clinicians.
This work focuses on the integration of the state-of-the-art UNEt TRansformers (UNETR) of the Medical Open Network for Artificial Intelligence (MONAI) framework.
We trained and tested our models using 618 de-identified Cone-Beam Computed Tomography (CBCT) volumetric images of the head
acquired with several parameters from different centers for a generalized clinical application. Our results on a 5-fold cross-validation showed high accuracy and robustness with an Dice up to 0.962 pm 0.02.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Do some maintenance to the previously made code
1. Train new segmentations of stable regions of reference for image registration models (Cranial Base, Mandible, Maxilla)

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use the previously made code to train a model for the segmentation of the masks structures

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. New segmentation models have been trained and tested
1. An extension has been added to this module to take segmentation files as input to generate vtk files
1. Train models to detect bone defects and patients with alveolar and palatal cleft
1. Dicom File can be used as input

# Illustrations

## 1. Different process to perform a CBCT segmentation
- Contrast correction and rescaling to the trained model spacing
- Use the UNETR classifier network through the scan to perform a first raw segmentation
- Post process steps to clean and smooth the segmentation
- Upscale to the original images size

![prediction](https://user-images.githubusercontent.com/46842010/172177605-b2e5d91c-3e10-4608-9c2d-1e5f2dfcc261.png)

## 2. Screen of the slicer module during a segmentation
- Selection of the different parameters and which structure to segment
- Use of a dialog progress bar to show/cancel the progress of the segmentation in real time (top right end corner).
- One the 3D view, result of one of the segmentation with the generated VTK files

- A prediction takes from 120s to 300s for one patient depending on the local computer GPU capacity ( 15GB  down to 3GB)

![Screen slicer](https://user-images.githubusercontent.com/46842010/176789535-b7473878-fbeb-494d-988a-5ee1afa7d4fa.png)

## 3. Use of AMASSS to generate mask for a defacing tool
- The scan intensity in the pink region ( mainely nose, lips and eyes ) will be set to 0 to make it impossible to identify the patient
- The bones segmentations are used to make sure we dont remove important informations during the process

![mask for defaceing](https://user-images.githubusercontent.com/46842010/176813614-f9ec9123-4c34-4f8c-828f-ed4a84d30132.jpeg)


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
