Back to [Projects List](../../README.md#ProjectsList)

# Migration of PILOT software for needle trajectory planning from MITK to 3DSlicer

## Key Investigators

- Caroline Essert (ICUBE / Université de Strasbourg)
- Jean-Christophe Fillon-Robin (Kitware Inc.)
- Nicole Aucoin (Harmonus Inc.)


# Project Description

## Objective

1. Make the MITK plugin PILOT for needle/electrode trajectory planning compatible with 3D Slicer


## Approach and Plan

1. Create a Slicer module and plug PILOT in it


## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

Progress:

1. Built Slicer on Mac OSX
2. Created a new extension with a loadable module in C++
3. Modified the UI to match the MITK PILOT plugin UI
4. Familiarized with the concepts of mrml scene, nodes, and connections in Slicer, thei link with vtk data structures, and made the link with MITK similar concepts
5. Started playing with the "manual" modification of nodes and vtkpolydatas
6. Started the process of building the core files of PILOT plugin along with Slicer (ongoing...)

Next steps:

1. Finish the build
2. Link UI widgets to functions in the PILOT code
3. Test !

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW27_2018_Boston/Projects/TrajectoryPlanning/Screen Shot 2018-01-12 at 13.21.22.png" width="600">

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

A short video of the MITK plugin in action: https://youtu.be/JG1hFJkmvtA

<!--- Source code: https://github.com/YourUser/YourRepository-->
<!--- Documentation: https://link.to.docs-->
<!--- Test data: https://link.to.test.data-->
