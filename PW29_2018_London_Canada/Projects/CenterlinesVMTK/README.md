Back to [Projects List](../../README.md#ProjectsList)

# Navigating Vascular Centerlines

## Key Investigators

- Michael Schumaker (Sunnybrook Research Institute)
<!--- Investigator 2 (Affiliation)-->

# Project Description

I'm developing a Slicer application that uses the Slicer VMTK extension to find the centerlines of segmented arteries, and uses these centerlines to reformat medical images. This allows a user to navigate through an artery to find regions of stenosis and occlusions.

## Objective

1. Compile SlicerExtension-VMTK with VTK9 and Qt5. Fix problems compiling VMTK with the most recent VTK.
2. Create a glyph or marker to follow the 2D slice position on a straightened artery view.
3. Using SlicerExtension-VMTK effectively. Extract centerlines using ComputeCenterlines module, rather than ExtractNetwork.
4. Create a loadable module to work with the VTK remote module "Spline Driven Image Slicer", with additional features. 

## Approach and Plan

1. With experts, examine changes that caused VMTK to stop compiling.
2. Understand options to add glyphs to slice views, try them out.
3. Understand use of ComputeCenterlines, and see if new tools would be useful.
4. Create a loadable module from the template, and set it up to compile with Spline Driven Image Slicer.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

[Navigating Vascular Centerlines](PADPlanner-Jul13-2018.png)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/mschumak

