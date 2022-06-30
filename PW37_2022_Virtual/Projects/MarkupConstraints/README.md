Back to [Projects List](../../README.md#ProjectsList)

# MarkupConstraints Slicer Module

## Key Investigators

- David Allemang (Kitware Inc.)
- Jean-Christophe Fillion-Robin (Kitware Inc.)
- Lucia Cevidanes (University of Michigan)
- Maxime Gillot (University of Michigan)
- Baptiste Baquero (University of Michigan)

## Acknowledgements

- Kyle Sunderland (PerkLab)

# Project Description

MarkupConstraints is a Slicer module intended for Slicer extension developers to constrain
and synchronize markups and control points of different nodes.

The module has been developed to support Q3DCExtension, however I intend to expand it 
further for reuse in other interactive tools.

## Objective

1. Robust constraints between control points in different vtkMRMLMarkupNode instances
   * Support for constraining points between for example a line and fiducial markup is 
     very limited
2. Detect dependency cycles and provide meaningful error messages
   * Slicer freezes indefinitely when updating constraints with cycles
3. Robust constraints from control points to other node types
   * Project a point to the surface of a model
4. Support saving/loading a markup node or MRML scene while preserving constraints
5. Determine the best mode of distribution and publish
   * Likely will be published on the Extension Index in "Developer Tools"
6. Create a simple interactive UI for debugging/testing purposes
   * Should allow viewing or editing existing constraints in the scene

## Progress

* Created a Slicer module and logic with appropriate observers for applying constraints
* Began refining API to support arbitrary constraints and dependencies (as means to 
  resolve #1)
* Fully resolved #1 with a robust API to define arbitrary constraints.
* Created [architecture documentation][arch] and [API documentation][api] for build constraint functions.
* Created unittest suite for primary features.

[arch]: https://github.com/KitwareMedical/SlicerMarkupConstraints/blob/main/Docs/Architecture.md
[api]: https://github.com/KitwareMedical/SlicerMarkupConstraints/blob/main/Docs/API.md

Thanks to Kyle Sunderland (PerkLab) for his advice and inspiration!

## Next Steps

* Implement more adaptors to enable constraints against arbitrary node types, not just control points.
* Use adaptors and node parameters/references to enable serialization with scene.
* Implement graph analysis to detect cycles and deadlocks.
* Expand constraint interface using abstract class for more extensibility.

# Illustrations

![Projection and Distance constraints](./length-chain.gif)
![Chain of distance constraints](./project-anchor.gif)
![Constraint Demo](./project-axis.gif)

# Background and References

Source code is hosted in [SlicerMarkupConstraints][repo]. 

[repo]: https://github.com/KitwareMedical/SlicerMarkupConstraints
