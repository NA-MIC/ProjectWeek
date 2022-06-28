Back to [Projects List](../../README.md#ProjectsList)

# Automatic multi-anatomical skull structure segmentation of cone-beam computed tomography scans using 3D UNETR
![Segmentation](https://user-images.githubusercontent.com/46842010/172177602-8cbfc188-9715-488a-ad2e-abb8d219536d.png)

## Key Investigators


- Maxime Gillot (UoM)
- Baptiste Baquero (UoM)
- Celia Le (UoM)
- Romain Deleat-Besson (UoM)
- Jonas Bianchi (UoM, UoP)
- Antonio Ruellas (UoM)
- Marcela Gurge (UoM)
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
In this paper, we propose a novel tool to accurately process a full-face segmentation in about 5 minutes 
that would otherwise require an average of 7h of manual work by experienced clinicians. 
This work focuses on the integration of the state-of-the-art UNEt TRansformers (UNETR)
of the Medical Open Network for Artificial Intelligence (MONAI) framework. 
We trained and tested our models using 618 de-identified Cone-Beam Computed Tomography (CBCT) volumetric images of the head 
acquired with several parameters from different centers for a generalized clinical application. Our results on a 5-fold cross-validation 
showed high accuracy and robustness with an Dice up to 0.962 pm 0.02.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Create only one model for multiple structures.
2. Create a slicer module for the algorithm
4. Add new structure to segment
5. Deploy the AMASSS tool with the updated trained models

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Get the data merged by the clinicians for the skull.
1. Use the begening of a slicer module to create a new one for AMASSS. 
1. Use new dataset to train new HD models.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. A model has already been trained on a full face segmentation with 5 strucures in the large field of view
1. An other model has been trained to segment high definition, small field of view CBCT
1. We also have a model for root canal
1. The begenning of a slicer module has been made, the next steps are:
1. Finish the module to link the UI with the algorithms and models
1. Deploy the module on slicer CMF extention

# Illustrations


![prediction](https://user-images.githubusercontent.com/46842010/172177605-b2e5d91c-3e10-4608-9c2d-1e5f2dfcc261.png)



# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
