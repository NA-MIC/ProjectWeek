Back to [Projects List](../../README.md#ProjectsList)

# SlicerHeart Polar Map Module

## Key Investigators

- Connor Haberl (University of Ottawa Heart Institute)
- Investigator 2 (Affiliation)
- Investigator 3 (Affiliation)

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to add polar map funcitonality to SlicerHeart. Polar maps provide a standardized 2D representation of the 3D LV myocardium for consistent comparisons across different patients or over time, and allow the entire LV to be viewed at once in a single 2D image. 
Polar maps are commonly used in:
-nuclear imaging (PET, SPECT) to show perfusion or other radiotracer uptake
-scar imaging (LGE MRI or LIE CT) to show contrast washout to identify regions of scar
-anatomical imaging (CT, MRI or Echo) to show myocardial wall motion or thickening, typically to identify regions or scar or hypomobility
This project looks to create a module within SlicerHeart to enable the creation of polar maps for each of these use-cases.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Create LV polar maps from surfaces (e.g. a 3D polydata surface representing scalar values at either the endo- or epi- cardial surface)
1. Objective B. Create LV polar maps from nuclear imaging volumes (e.g. perfusion mapping from PET scan)
1. Objective C. Create LV polar maps from CT/MR volumes showing washout (e.g. Late Gadolineum uptake in LGE MRI to identify regions of scar)
1. Objective C. Create LV polar maps from 4D CT/MR/Echo volumes showing wall motion & thickening (e.g. )
1. Objective E. Allow user to interact (e.g. draw a segmentation) on the polar map, and transfer to 3D scene.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Create method for automatic LV long-axis detection (or require user to define using markers at apex and center of LV)
1. Create method for interactive plot of polar coordinates in Slicer (similar to matplotlib 'polar' plot type https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)
1. Create method for apical sampling (or, eventually, allow user to select one of 3 common methods of apical sampling for polar maps)
1. Implement some level of semi-automatic LV myocardial segmentation (for CT, MR, PET, SPECT)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. In MATLAB, implemented 3D surface to polar plot method
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
1. What is a polar map?
Polar maps enable properties of the left ventricle, a 3D object, to be viewed entirely in 2D. Apical segments of the LV are shown in the center of the polar map, and basal segments are shown near the perimeter.
Polar maps are viewed as if looking at the myocardium from the apex with the anterior LV wall at the top and the septal wall to the left.
Polar maps are commonly used 

1. What is the 17-segment heart model?
