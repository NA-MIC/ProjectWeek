Back to [Projects List](../../README.md#ProjectsList)

# Integration of PyTorch and Slicer

## Key Investigators

- Fernando Pérez-García (University College London & King's College London)
- Andrés Díaz-Pinto (King's College London)
- Andras Lasso (PerkLab, Queen's University)

# Project Description

<!-- Add a short paragraph describing the project. -->

Investigate the potential issues faced by users who would like to use a trained
convolutional neural network (deep learning model) inside Slicer, using PyTorch.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Issues that will be addressed:

1. How to install PyTorch within Slicer. The main question is whether to install a version with GPU support and, if it does, which version of the CUDA toolkit to install.
1. How to handle the necessary conversion of Slicer nodes (e.g., `vtkMRMLScalarNode`) to PyTorch objects (e.g., `torch.Tensor`) and vice versa. Look into adding tools to `slicer.util`.
1. Write a tutorial with a toy example using a publicly available dataset.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Investigate issues related to [CUDA versions and GPU drivers](https://docs.nvidia.com/deploy/cuda-compatibility/index.html), and which installation method to use depending on the platform. Maybe, write a GUI to guide the user into choosing an appropriate installation type.
1. Once PyTorch has been installed, look into the best ways to prepare slicer nodes for inference and visualize the results in Slicer.
1. If necessary, write a tutorial (potentially a Jupyter Notebook using [SlicerJupyter](https://github.com/Slicer/SlicerJupyter))

<!-- ## Progress and Next Steps -->

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->



<!-- # Illustrations -->

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

The first discussion about this project appeared on the [Slicer forum (PW35) Projects List](https://discourse.slicer.org/t/pw35-projects-list/17905/4).
