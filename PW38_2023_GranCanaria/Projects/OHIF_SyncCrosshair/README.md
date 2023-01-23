Back to [Projects List](../../README.md#ProjectsList)

# Cross study sychronizer for OHIF Crosshair

## Key Investigators

- Salim Kanoun MD (Pixilib, Toulouse, France)
- Alireza Sedghi (Radical Imaging)
- Celian Abadie (Pixilib)
- Sofien Sellamo (Pixilib)

# Project Description

Create a tool to synchronise two volume viewport comming for 2 different study to help physicians to track lesions of follow up scans

## Objective

In follow up studies, physicians needs to compares two studies (ex baseline vs end of treatement). 
It would be nice to sync the display between viewport to help them comparing tumor evolution.

## Approach and Plan

As Spatial coordinate change between study, we will use the crosshair to the user to set in a same anatomical region (ex : pubis). 
At sync we either : 
- track crosshair distance for each crosshair update and apply to the other crosshair
- Calculate an offset to apply to convert crosshair A to B coordinate

Would be nice if can sync rotation as well.

## Progress and Next Steps

We made an implementation of the sync that works well for syncrhonizing crosshair but do not handle rotation. Would need to extend rotation.
Crosshair implementation might need some refactoring.
Once done tools is meant to be integrated as an OHIF tool (as an improvement of the stack sync tool)

# Illustrations

None

# Background and References

None
