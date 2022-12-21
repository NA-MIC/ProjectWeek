Back to [Projects List](../../README.md#ProjectsList)

# Automated Standardized Orientation for Cone-Beam Computed Tomography (CBCT)

<!--![Segmentation](https://user-images.githubusercontent.com/46842010/172177602-8cbfc188-9715-488a-ad2e-abb8d219536d.png)-->


## Key Investigators

- Luc Anchling (UoM)
- Nathan Hutin (UoM)
- Maxime Gillot (UoM)
- Baptiste Baquero (UoM)
- Jonas Bianchi (UoM, UoP)
- Antonio Ruellas (UoM)
- Felicia Miranda (UoM)
- Selene Barone (UoM)
- Marcela Gurgel (UoM)
- Marilia Yatabe (UoM)
- Najla Al Turkestani (UoM)
- Hina Joshi (UoNC)
- Lucia Cevidanes (UoM)
- Juan Prieto (UoNC)


# Project Description

<!-- Add a short paragraph describing the project. -->
To develop a standardized head orientation approach for medical and dental images is crucial to improve the reliability of automated image analysis towards clinical decision-making. Manual and user-dependent head orientation is time-consuming and prone to errors. For this reason, this study aims to automatically obtain the desired standardized orientation of Cone Beam Computed Tomography scans, regardless of the patient's positioning during the scan or any CT scanner initialization changes.

The Automated Standardized Orientation (ASO) tool presented in this work automatically identifies landmarks on 3D volumes regardless of orientation, using a deep learning landmark identification algorithm that handles images with random orientation ([ALI_CBCT](../ALI_CBCT/README.md)). ASO uses a landmark-based registration approach to automatically orient a 3D volume to a common space. The method aligns the identified landmarks to a set of reference ones. The method starts by aligning 3 randomly chosen landmarks and refines their position using an Iterative Closest Point (ICP) transform. The tool also allows user-selected landmarks for precision purposes. All the transforms computed during this process are concatenated and the final transform is applied to the CBCT volume.

To make ASO more robust, a pre-orientation algorithm has been developed. This part uses a deep learning algorithm to identify the head orientation and then rotates the volume to the desired orientation. This algorithm is currently being tested and will be implemented in the ASO module. The training has been realized with random rotations.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Create a Slicer Module to use this algorithm with CBCT files
1. Make the algorithm more robust to different head orientations
1. Do some maintenance to the previously developed ASO module

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Develop in collaboration with Nathan Hutin ([ASO_IOS](../AutomaticStandardizeOrientation_IOS/README.md
)) a Slicer Module to make ASO work for both IOS and CBCT files
1. Implement the pre-orientation algorithm to this module

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Slicer Module has been developed:
    - In a first step, only a SEMI-Automated version has been implemented (with scan and landmark files as inputs)
    - In a second step, a fully automated version has been developed (with ONLY scan files as inputs and ALI module running in the background)
1. Pre-orientation algorithm will be implemented in the ASO module

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
## Oriented Output Example
![ASO](https://user-images.githubusercontent.com/72148963/209001336-95ad3818-f1fd-4ab6-8537-c3f79515167e.png)

## User Interface
![ASOUI](https://user-images.githubusercontent.com/72148963/209001568-ccffbb51-3318-447e-987e-db432dd16380.png)



# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
