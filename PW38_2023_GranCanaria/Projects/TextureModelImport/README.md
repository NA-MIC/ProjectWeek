Back to [Projects List](../../README.md#ProjectsList)

# Automated map texture when importing the OBJ file into Slicer

## Key Investigators

- Chi Zhang (Seattle Children's Research Institute)
- Steve Pieper (Isomics, Inc.)
- Andras Lasso (The Perk Lab, Queen’s University)

# Project Description

<!-- Add a short paragraph describing the project. -->
Automatedly map associated texture image to the obj file when importing it into Slicer. This can facilitate importing textured model acquired by photogrammetry into Slicer. The ultimate goal is to be able to access OpenDronMap(ODM) photogrammetric package via Slicer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

When the obj file is imported into Slicer, Slicer will automatically call the Texture Model module from SlicerIGT to map the texture on the obj file without the need to manually map texture using this module.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Add an 'obj' option in the data importing dialog
1. Create a hook for the functions from the 'Texture Model' module
1. When the 'obj' option is selected in the data importing dialog, the 'Texture Model' functions will be called to automatically map texture to the model.

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

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
