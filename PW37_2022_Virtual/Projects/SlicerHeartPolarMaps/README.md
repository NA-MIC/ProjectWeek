Back to [Projects List](../../README.md#ProjectsList)

# SlicerHeart Polar Map Module

## Key Investigators

- Connor Haberl (University of Ottawa Heart Institute)
- Investigator 2 (Affiliation)
- Investigator 3 (Affiliation)

# Project Description

<!-- Add a short paragraph describing the project. -->

<a href="url"><img src="https://user-images.githubusercontent.com/3187316/175366354-3aa45998-4a91-4d05-a3e4-f30ad784140f.png" align="left" width="150" ></a>

This project aims to add polar map funcitonality to SlicerHeart. Polar maps provide a standardized 2D representation of the 3D LV myocardium for consistent comparisons across different patients or over time, and allow the entire LV to be viewed at once in a single 2D image.
Polar maps are commonly used in:
-nuclear imaging (PET, SPECT) to show perfusion or other radiotracer uptake
-scar imaging (LGE MRI or LIE CT) to show contrast washout to identify regions of scar
-anatomical imaging (CT, MRI or Echo) to show myocardial wall motion or thickening, typically to identify regions or scar or hypomobility
This project looks to create a module within SlicerHeart to enable the creation of polar maps for each of these use-cases.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
(Within Project Week)
1. Objective A. Create LV polar maps from surfaces (e.g. a 3D polydata surface representing scalar values at either the endo- or epi- cardial surface)
2. Objective B. Create LV polar maps from nuclear imaging volumes (e.g. perfusion mapping from PET scan)
3. Objective C. Allow user to interact (e.g. draw a segmentation) on the polar map, and translate those segmentations to the 3D scene.

(Beyond Project Week)
4. Objective D. Create LV polar maps from CT/MR volumes showing washout (e.g. Late Gadolineum uptake in LGE MRI to identify regions of scar)
5. Objective E. Create LV polar maps from 4D CT/MR/Echo volumes showing wall motion & thickening


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Create method for automatic LV long-axis detection (or require user to define using markers at apex and center of LV)
1. Create method for interactive plot of polar coordinates in Slicer (similar to matplotlib 'polar' plot type https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)
1. Create method for apical sampling (or, eventually, allow user to select one of 3 common methods of apical sampling for polar maps)
1. Implement some level of semi-automatic LV myocardial segmentation (anything existing to leverage?)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. (Complete) Create initial extension with basic polar plot capabilities for surface data
1. (To Do) Try to solve objective C - interactive plots with connection to 3D
1. (To Do) Work with sample data to develop sampling method for nuclear imaging data to create polar map.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
An example of 17 segment display of LV wall thickening:

<a href="url"><img src="https://user-images.githubusercontent.com/3187316/175652378-0aaf14a1-e5b1-43d9-9d30-903a6cfcc0f7.gif" width="175" ></a>


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
1. Sample Data

We have some PET and SPECT images to use for nuclear imaging polar map development. We also have 3D Electroanatomic Voltage Maps for converting a 3D surface into polar map. These will be linked prior to project week.
TBD - we have not yet found any LGE MRI or LIE CT images to use for testing yet, so we wll probably start by working on the pathways for which we have data to analyze.

2. What is a polar map?

Polar maps enable properties of the left ventricle, a 3D object, to be viewed entirely in 2D. Apical segments of the LV are shown in the center of the polar map, and basal segments are shown near the perimeter.
Polar maps are viewed as if looking at the myocardium from the apex with the anterior LV wall at the top and the septal wall to the left. They are commonly used to show perfusion or tissue health.

3. What is the 17-segment heart model?

<a href="url"><img src="https://user-images.githubusercontent.com/3187316/175365939-23ce1a55-1090-4d2e-af80-8185df7b62cc.png" align="left" width="350" ></a>
The 17 segment model is a standardized myocardial segmentation nomenclature used to discretize segments of the left ventricular myocardium. The model describes the left ventricle as 17 distinct segments - 6 basal segments, 6 mid-ventricular segments, and 5 apical segments.
Physicians may be familiar with looking at the heart in transaxial slices on CT, in cardiac planes, or literally through the chest wall (e.g. surgeon). The 17-segment model is very commonly used and can act as a common-ground for physicians with different backgrounds.
Assigning characteristics to each of these 17-segments is commonly used in cardiology, be it to describe the health of the tissue for the corresponding region, or to draw attention to an anatomical anomaly in a certain region. It is particularly helpful in considering bloodflow because each of the 3 main cardiac arteries source distinct segments of the 17-segment model.
More on the definition of the 17-segment model can be found in [this American Heart Association paper] (https://www.ahajournals.org/doi/pdf/10.1161/hc0402.102975)

4. Apical Sampling Methods

<a href="url"><img src="https://user-images.githubusercontent.com/3187316/175435343-31295965-07f2-411d-ac08-f2302581ab9b.PNG" align="left" width="200" ></a>

All polar maps sample the basal and mid segments the same, but there are 3 different convensions to how to sample the apex. These are described in more detail in
  Lin, G. Sharat et al. “Automated Quantification of Myocardial Ischemia and Wall Motion Defects by Use of Cardiac SPECT Polar Mapping and 4-Dimensional Surface Rendering.” Journal of nuclear medicine technology 34.1 (2006): 3–17. Print.
