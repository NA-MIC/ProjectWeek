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
1. Here is an example file [https://drive.google.com/file/d/1ZxJcx2nM-fgywA8KMm6JO0t7QJIcQR7O/view?usp=sharing](https://drive.google.com/file/d/1ZxJcx2nM-fgywA8KMm6JO0t7QJIcQR7O/view?usp=sharing))

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. The goal is basically reached, thanks for the help from Steve Pieper. The script `OBJFile.py` is incorporated in the forked SlicerMorph repository: https://github.com/chz31/SlicerMorph. Git clone the repository and use the Extension Wizard to install the SlicerMorph extension.


2. After that, the `OBJ textured model` option would be registered in the data dialog. Drag the OBJ into Slicer and select the `OBJ textured model` option.

<p align="center">
<img src="https://user-images.githubusercontent.com/80793828/216435141-80300f14-aa08-4c51-9d05-85d3086f11c7.png", width = 700>
<p/>


3. The mtl file (in the same directory) will then be automatically parsed to retrieve the texture image name.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/80793828/216436895-09818bd2-05d7-4ad2-929f-bdce817708bf.png">


4. The `ImageStacks` functions from SlicerMorph will then be called to import texture as a vector volumetric node and map to the model using `SetTextureImageDataConnection`. The texture node will then be deleted.

<p align="left">
<img width="434" alt="image" src="https://user-images.githubusercontent.com/80793828/216438232-94eef208-71d2-4dee-9993-9eb7aa42db7b.png">
<img width="386" alt="image" src="https://user-images.githubusercontent.com/80793828/216438568-ff959b91-ced4-4b44-8af7-43869dc6c0fe.png">
<p/>
<p align="right">
<p/>

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->


# Background and References

Chi Zhang is working on a photogrammetry pipeline based on the open source package OpenDroneMap (ODM). Ultimately, the goal is being able to push and pull data between Slicer and ODM.

A sample obj file with associated texture can be downloaded here: https://drive.google.com/file/d/1ZxJcx2nM-fgywA8KMm6JO0t7QJIcQR7O/view?usp=sharing
