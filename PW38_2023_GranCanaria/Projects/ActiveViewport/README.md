Back to [Projects List](../../README.md#ProjectsList)

# Active Viewport

## Key Investigators

- Davide Punzo (Freelancer, France) 
- Andras Lasso (Perk Labs, Canada)
- Anyone is welcome to join

# Project Description

Add the concept of active viewport in 3DSlicer

## Objective

1) Track the currently manipulated viewport by the user in a parameter in the Slicer logic

2) Add a colored border to the view (2D, 3D, Plot, Table, etc...)

## Approach and Plan

1) Design the solution: discuss the potential use cases (i.e. keyboard/mouse focus) and then use it for example in show/hide node in the selected view (similarly to Paraview).

2) Implement it: add implementation in CTK (e.q. QFrame around views with method to set color, thickness, style, etc... ), the uid parameter of the selected view (shall we save it in the scene? or just in the slicer logic?).

3) Get feedback

## Progress and Next Steps


# Illustrations


# Background and References

