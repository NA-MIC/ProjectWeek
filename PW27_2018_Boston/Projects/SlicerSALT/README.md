Back to [Projects List](../../README.md#ProjectsList)

# SlicerSALT

## Key Investigators

- Beatriz Paniagua (Kitware)
- Jean-Christophe Fillion-Robin (Kitware)
- Jared Vicory (Kitware)
- Laura Pascal (Kitware)
- Junpyo Hong (University of North Carolina)
- Chao Huang (University of North Carolina)
- Juan Carlos Prieto (University of North Carolina)
- Mahmoud Mostapha (University of North Carolina)
- Zhiyuan Liu (University of North Carolina)
- Loïc Michoud (University of Michigan)
- James Fishbaugh (NYU Tandon School of Engineering)

# Project Description

Slicer Shape AnaLysis Toolbox (SlicerSALT) is the dissemination vehicle of powerful shape analysis methodology based on 3D Slicer open-source software. SlicerSALT will enhance the intuitiveness and ease of use as well as allow researchers to find shape changes with higher statistical power. Altogether this constitutes a crucial resource for the imaging field that will enable many and important new findings in biomedical imaging studies.

SlicerSALT will be used to:
+ Compute Point Distributed Models (PDM) using Spherical Harmonic Representation on spherical topology objects (Extension alrealdy available in SlicerSALT: [SPHARM-PDM Extension](https://www.slicer.org/wiki/Documentation/4.8/Extensions/SpharmPdm))
+ Compute [estimating shape correspondence for population of objects with complex topology](https://github.com/laurapascal/slicerprojectweek2018/blob/master/Estimation_of_shape_correspondence_for_population_of_objects_with_complex_topology.pdf)
+ Run 4D regression in a collection of 3D PDMs associated to a linear variable (i.e. age) (Extension soon available in SlicerSALT: Shape Regression Extension)
+ Perform correspondence optimization using study-wise shape analysis
+ Fit skeletal representations (s-reps) to a collection of binary volumes
+ Compute image-based correspondence in binary volumes of different topologies


## Objective

1. Work on the new SlicerSALT release
1. Work on the methodology for the estimation of shape correspondence for population of objects with complex topology


## Approach and Plan

1. SlicerSALT's Project:
- Update of the Slicer version used by SlicerSALT to the new release
- Incorporation of Shape Regression Extension in the new SlicerSALT release
- Test of the new extensions
2. Project for the estimation of shape correspondence for population of objects with complex topology:
- Comparison of the three methods already existing
- Investigation in order to universalize the Deformetrica method (issue with the use of Cuda/GPU)
- Investigation in order to find a more efficient method (new tools, new algorithms, etc..)


## Progress and Next Steps

- Update of the Slicer version used by SlicerSALT to the new release
- Shape Regression Extension:
  - Fixing of some bugs on the shape regression computation
  - Adding of some tests
  - Test of the slicer extension package on Windows and Mac (Issue on Linux) -> Almost ready to be integrated in SlicerSALT
- Estimation of shape correspondence for population of objects with complex topology:
  - Comparison of the three methods already existing
  - Abandon of the ThinShellDemon method due to the generated results not enough accurate
  - Next Steps:
    - Improvement of the Deformetrica method in order to accelerate the computation
    - Tests on new data


# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->
Shape Regression Extension:

<img src="https://raw.githubusercontent.com/laurapascal/slicerprojectweek2018/master/ShapeRegressionExtension_UI.png" width="440" >

Estimation of shape correspondence for population of objects with complex topology:

<img src="https://raw.githubusercontent.com/laurapascal/slicerprojectweek2018/master/Example_of_corresponding_shape_estimation.png" width="500" >
<img src="https://raw.githubusercontent.com/laurapascal/slicerprojectweek2018/master/methods_estimation_of_shape_correspondence_for_population_of_objects_with_complex_topology.png" width="500" >


# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [SlicerSALT Source code](https://github.com/Kitware/SlicerSALT)
- [SlicerSALT Documentation](http://salt.slicer.org/)
- [SlicerSALT Presentation](https://github.com/laurapascal/slicerprojectweek2018/blob/master/SlicerSALT_presentation.pdf)
