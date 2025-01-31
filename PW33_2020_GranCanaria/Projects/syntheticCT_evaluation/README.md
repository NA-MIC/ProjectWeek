Back to [Projects List](../../README.md#ProjectsList)

# Synthetic CT evaluation

## Key Investigators

- Paolo Zaffino (Magna Graecia University of Catanzaro, Italy)
- Maria Francesca Spadea (Magna Graecia University of Catanzaro, Italy)
- Everyone else wants to join

# Project Description

Several algorithms for MRI to synthetic CT have been proposed.
Each group quantifies conversion accuracy in different ways, making difficult to compare algorithms.
We want to create a Slicer module for stardazied conversion accuracy assessment.

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Implement in 3D Slicer the validation workflow proposed in Spadea, M.F., Pileggi, G., Zaffino, P., Salome, P., Catana, C., Izquierdo-Garcia, D., Amato, F. and Seco, J., 2019. Deep Convolution Neural Network (DCNN) Multiplane Approach to Synthetic CT Generation From MR images—Application in Brain Proton Therapy. International Journal of Radiation Oncology* Biology* Physics, 105(3), pp.495-503.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Write an extension that will quantify conversion accuracy. The code will be written in python.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. The extension "ImageCompare" was created. For the moment is contains just a module for synthetic CT evaluation.
   More modules could be add later.

2. The extension in already available in the nigthly build (thanks JC and Andras!)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
![](https://raw.githubusercontent.com/pzaffino/SlicerImageCompare/master/ImageCompare_screenshot.png)

# Background and References

1. Spadea, M.F., Pileggi, G., Zaffino, P., Salome, P., Catana, C., Izquierdo-Garcia, D., Amato, F. and Seco, J., 2019. Deep Convolution Neural Network (DCNN) Multiplane Approach to Synthetic CT Generation From MR images—Application in Brain Proton Therapy. International Journal of Radiation Oncology* Biology* Physics, 105(3), pp.495-503.

2. https://github.com/pzaffino/SlicerImageCompare

3. https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ImageCompare

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
