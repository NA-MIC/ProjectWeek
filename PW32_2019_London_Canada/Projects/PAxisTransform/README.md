Back to [Projects List](../../README.md#ProjectsList)

## Principal Axis Transform

## Key Investigators
- Tina Wu (Sunnybrook Health Science Centre)

# Project Description
<!-- Add a short paragraph describing the project. --> 
Current slicer modules for general registration (BRAINs or Elastix) are unable to handle large initial mismatch between the two objects of interest. The purpose of this project is to create a slicer module that would allow registering two volumes with large initial mismatches (>15-20 degs) based on their principal axes. The module would also come with the capability for allowing users to visualize the volumes (as a model) and the direction of the principal vectors.

## Objective
1. Implement algorithm for performing principal axis transformation. 
1. Implement visualization tools. 

## Approach and Plan

1. Load the CT scans
2. Threshold the scans
3. Find the inertial matrices associated with the two volumes
4. Obtain the eigen vectors associated with the inertial matrices
5. Calculate the transformation matrix
6. Create models from the the initial scans
7. Transform the center of the model to the world origin
8. Apply the transform obtained from #5
9. Create ruler annotations for visualizing the vectors and applying appropriate transformations (from #7 then #5)

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
The approach listed above was implemented but there are a few bugs, potentially due to the coordinate system mismatch between slicer/numpy/vtk. The goal during this week is to fix these and optimize the module.

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![In this picture, the color green is associated with the fixed volume and yellow is associated with the moving volume. The goal is to match the position and orientation of the moving to the fixed volume. The green lines represent the principal directions of the volume and as you can see, they don't look like they are pointing in the right directions.](slicer-descript.png)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->
paper: http://jnm.snmjournals.org/content/31/10/1717.full.pdf


- Source code: https://bitbucket.org/blackfish03/paxistransform/src
- Test data: https://drive.google.com/open?id=1KaZk2cU_w5bR5BxWTUorOXIp1BnFHKfB
