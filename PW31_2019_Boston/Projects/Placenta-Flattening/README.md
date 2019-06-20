Back to [Projects List](../../README.md#ProjectsList)

# Placenta Flattening and Visualization in Slicer

## Key Investigators

- Mazdak Abulnaga (MIT)
- Steve Pieper (Isomics)
- Polina Golland (MIT)

# Project Description

The project aims to develop a module in Slicer to visualize placenta shapes embedded in MR images. We will use the transformations described in
["Placental Flattening via Volumetric Parameterization" by Abulnaga et al.](https://arxiv.org/pdf/1903.05044.pdf) to map placentae shapes embedded in in-utero MRI to
a flattened canonical template. The goal is to use the transformation tensor to be able to easily map between the original image space and the canonical space.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Develop a module to load the transformation field, the original MRI image, and the flattened image. Given the three inputs, allow the user to "click" a location in the flattened image then have Slicer automatically map to the corresponding location in the original image space.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Export transformation field tensor to Slicer.


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. 


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->


# Background and References

[Source code](https://github.com/mabulnaga/placenta-flattening)
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
