Back to [Projects List](../../README.md#ProjectsList)

# Working with the Slicer VMTK Extension

## Key Investigators

- Michael Schumaker (Sunnybrook Research Institute)
- Eman Arnout (LHSC)
- Olga Trichtchenko (Western)
- Jean-Christophe Fillion-Robin (Kitware)

# Project Description

Our interest is in using and enhancing Slicer's Vascular Modelling Toolkit (VMTK) extension. We plan to look at how to use VMTK capabilities, and whether they can be used more effectively in applications. We may see if there are capabilities of the VMTK package that can be added to the Slicer extension.

## Objective

1. Compile SlicerExtension-VMTK with VTK9 and Qt5. Fix problems compiling VMTK with the most recent VTK.
2. Use VMTK in Slicer effectively. Extract centerlines using start and end points, rather than using extractNetwork.
3. Explore other VMTK features, and whether they can be added as Slicer modules.
4. Use Slicer as preprocessing for further computations of fluid properties in blood vessels.

## Approach and Plan

1. Ask for help to compile VMTK with VTK9.
2. Try different approaches to using VMTK’s centreline computation features.
3. Look at VMTK tutorials, understand what else is available in the package, and try to use them from Slicer.
4. For computing fluid flow properties, the surface needs to be remeshed. This can be done in VMTK or in CFD software.

## Progress and Next Steps

1. Done! Thanks [@jcfr](https://github.com/jcfr). The initial fix was quick, but getting it to pass the integration checks took effort, and a bug fix to conda.
2. Made a testing module to try different centerline calculation options, though there's still a lot of things to try.
3. Found that VMTK centreline extraction does not automatically force starting and ending at the defined source and endpoints.  See tutorial at [http://www.vmtk.org/tutorials/Centerlines.html](http://www.vmtk.org/tutorials/Centerlines.html)
4. Found Slicer VMTK code from 2007-2010 project weeks, started looking at differences with current module.
5. Can use [TubeTK](https://github.com/KitwareMedical/ITKTubeTK) instead for extracting center lines [http://www.tubetk.org/](http://www.tubetk.org/).
6. One option for computing fluid flow, is to export an STL file in OpenFOAM. This can be done simply by using segmentation and creating the appropriate surface.
7. Second option for fluid flow is to use the meshing algorithm in VMTK [http://www.vmtk.org/tutorials/MeshGeneration.html](http://www.vmtk.org/tutorials/MeshGeneration.html) which has more specific features for blood vessels. This has not yet been implemented in Slicer. For obtaining a finer mesh, this algorithm relies on accurate computation of centerlines that include endpoints.

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

[Software for Navigating Vascular Centerlines](PADPlanner-Jul13-2018.png)

[Multi-branch with dropped trunk](dropped-trunk.png)

[Single vessel no centerline](single-vessel.png)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: [https://github.com/SunnybrookAngio/ProjectWeek2018.git](https://github.com/SunnybrookAngio/ProjectWeek2018.git)
