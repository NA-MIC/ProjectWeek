Back to [Projects List](../../README.md#ProjectsList)

# Real-time visualization in transcranial magnetic stimulation (TMS)

## Key Investigators

- Loraine Franke (University of Massachusetts Boston)
- Lipeng Ning (BWH & Harvard Medical School)
- Yogesh Rathi (BWH & Harvard Medical School)
- Steve Pieper (Isomics, Inc.)
- Daniel Haehn (University of Massachusetts Boston)

# Project Description

Transcranial magnetic stimulation is a nonivasive procedure used for treating depression with magnetic and electric fields to stimulate nerve cells. 
A TMS coil is slowly moved over the subject's head suface to target certain areas in the brain. 
Our project aims to develop a deep-learning powered software for real-time E-Field prediction and a visualization of TMS within 3D Slicer.

## Objective

Real-time visualization of an electric field (E-field) for transcranial magnetic stimulation (TMS) on the brain surface as well as visualizing the E-field along fiber bundles (DTI), and later the possibility to optimize the exact coil position or to target certain fibers.

## Approach and Plan

Integrate the visualization process as a new module within the MRML scene architecture:

- Evaluate different methods to visualize the E-field on the surface mesh (find fastest method which is appropriate for a real-time visualization)
- Rendering of a virtual TMS coil in the 3D Slicer module
- Develop an approach to move/rotate the coil model over the brain surface in 3D Slicer (similar to markups/fiducials)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->
1. Visualize Efield (volume) on brain surface (polydata/mesh) by adjusting the models orientation and applying the vtkProbeFilter within a new Slicer Module.
2. Tested the rendering time of our visualization approach with renderer.GetLastRenderTimeInSeconds() resulted in around 0.0005 seconds.
3. Added a functionality to create fiducials and to move it along the brain model's surface.

Next steps: 
- Replace the fiducial with a TMS coil model.
- Apply visualization on DTI data / pick fibers (similar to [DBS Navigation](../DBSNavigation/README.md) )

## Illustrations

Fiducial (yellow sphere) moving along the brain surface:
![Fiducial (Sphere) moving along brain surface](./fiducial_on_brain_surface.png)
Fiducial will later be replaced by a TMS coil model.

![Vector Field volume and brain surface](./map_evec_on_brain_surface.mov)

Visualization goal in slicer:
![Brain surface and DT](./tmsonbrain.png)

Visualization process:
![Visualization Process](./visualization_process.png)

# Background and References

https://vtk.org/doc/nightly/html/classvtkProbeFilter.html

