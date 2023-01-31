Back to [Projects List](../../README.md#ProjectsList)

# Automated map texture when importing the OBJ file into Slicer

## Key Investigators

- Chi Zhang (Seattle Children's Research Institute)
- Steve Pieper (Isomics, Inc.)
- A. Murat Maga (Seattle Children's Research Institute)
- Andras Lasso (The Perk Lab, Queen’s University)
- Sara Rolfe (Seattle Children's Research Institute)

# Project Description

<!-- Add a short paragraph describing the project. -->
Automatedly map the associated texture image to the obj file when importing it into Slicer without a creating a volume node for the texture image. This can facilitate importing textured model acquired by photogrammetry into Slicer. The ultimate goal is to be able to access OpenDronMap(ODM) photogrammetric package via Slicer to facilitate the use of photogrammetry.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

When the obj file is imported into Slicer, Slicer will automatically call the Texture Model module from SlicerIGT to map the texture on the obj file without the need to import the texture image as a volumetric node and manually map it to the model using this module. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Register a hook for the obj file type in the data import dialog (a similar approch suggested by Steve Pieper for loading nii file as either volume or segmentation (NIFTI file reader from SlicerDMRI extension: ([https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py](https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py))
1. When the 'obj' option is selected in the data importing dialog, the 'Texture Model' functions will be called to automatically map texture to the model (The TextureModel module of SlicerIGT: [https://github.com/SlicerIGT/SlicerIGT/tree/master/TextureModel](https://github.com/SlicerIGT/SlicerIGT/tree/master/TextureModel)
1. Here is an example file ([https://github.com/chz31/PhotoGram/blob/main/textureImport_test.py](https://drive.google.com/file/d/1ZxJcx2nM-fgywA8KMm6JO0t7QJIcQR7O/view?usp=sharing))

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![Screenshot 2023-01-29 at 9 50 01 PM](https://user-images.githubusercontent.com/80793828/215397544-df4f7af9-ec31-4699-9def-2676f3f713f5.png)


# Background and References

Chi Zhang is working on a photogrammetry pipeline based on the open source package OpenDroneMap (ODM). Ultimately, the goal is being able to push and pull data between Slicer and ODM.

A sample obj file with associated texture can be downloaded here: https://drive.google.com/file/d/1ZxJcx2nM-fgywA8KMm6JO0t7QJIcQR7O/view?usp=sharing
