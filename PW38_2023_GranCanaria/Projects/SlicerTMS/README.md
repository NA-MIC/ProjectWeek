Back to [Projects List](../../README.md#ProjectsList)

# Real-time visualization for transcranial magnetic stimulation (TMS)

## Key Investigators

- Loraine Franke (University of Massachusetts Boston)
- Jax Luo (BWH & Harvard Medical School)
- Yogesh Rathi (BWH & Harvard Medical School)
- Lipeng Ning (BWH & Harvard Medical School)
- Steve Pieper (Isomics, Inc.)
- Daniel Haehn (University of Massachusetts Boston)

# Project Description

Transcranial magnetic stimulation is a nonivasive procedure used for treating depression with magnetic and electric fields to stimulate nerve cells. 
A TMS coil is slowly moved over the subject's head suface to target certain areas in the brain. 
Our project aims to develop a deep-learning powered software for real-time E-Field prediction and a visualization of TMS within 3D Slicer.

## Objective

Real-time visualization of an electric field (E-field) for transcranial magnetic stimulation (TMS) on the brain surface, visualization through an AR app (over browser).

## Approach and Plan
What is done so far: 
1. We created a TMS module in Slicer mapping NifTi file onto brain mesh with 3D TMS coil that can be moved by the user.
2. OpenIGTLinkIF is used to transfer data (E-Field from TMS) into 3D Slicer
3. Connected 3DSlicer to the web browser using our newly implemented secure WebSocket from https://github.com/liampaulhus/slicerWebWSS-WIP
4. Mobile device via WebXR connected and we can control the coil inside 3DSlicer.
5. We have integrated a deep learning model (CNN) inside our SlicerTMS module. We receive real time updates of newly generated Nifti files via the OpenIGTlink Plugin. The current deep learning model predicts the TMS E-field. We visualized this field with the magnetic field of the coil in the correct position on the brain mesh.
6. Beside the brain surface, we can visualize the E-Field on tractography fiber bundles. We have integrated the Fiber Bundle selection with an ROI attached to the TMS coil with the SlicerDMRI module.

## Progress and Next Steps

1. We improved the performance of the Fiber ROI selection by downsampling the fibers (see demo below).
2. Fixed CUDA bug of the neural network model that generates the Nifti files to be visualized.


## Illustrations


####  Current Visualization of the TMS Module in 3DSlicer with Coil and....
#### Mapping of E-field on tractography with ROI selection:

<img src="https://user-images.githubusercontent.com/38534852/216506888-347b3a78-21d9-47c2-a32e-26088b7dc08d.gif" width="600" alt="SlicerTMS Module with Efield mapped on fiber tracts">

#### Mapping of E-field on brain surface:

<img src="https://user-images.githubusercontent.com/38534852/204691744-c2ee8451-7f4c-40c3-83a5-c2fd0103f0a7.gif" width="600" alt="SlicerTMS Module with Efield mapped on brain">


# Background and References

<!-- This project is related to: ../SlicerTMS_E-field -->

## Infos for running WebXR:

Phones need a Depth sensor to run AR/VR. A list of supported devices can be found here: https://developers.google.com/ar/devices

On an Android Phone via USB: 
- PlayStore: Download Google VR Services and Google AR Services App
- Update Chrome/Camera apps etc.
- On the phone: Enable Developer tools (https://developer.android.com/studio/debug/dev-options) and USB debugging (description here: https://developer.chrome.com/docs/devtools/remote-debugging/)
- Run chrome://inspect#devices in the browser on your computer and it should detect USB connected devices

For iPhone: 
- Mozilla offers a WebXR Emulator that can be downloaded from the Apple Store for any iPhone and iPad: https://labs.mozilla.org/projects/webxr-viewer/

## For the full SlicerTMS Module and instructions see our [repository](https://github.com/lorifranke/SlicerTMS)

## Also see previous project week [PW 37](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/SlicerTMS)

<!-- vtkProbeFilter: https://vtk.org/doc/nightly/html/classvtkProbeFilter.html
Moving fiducials with CPYY: https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5

Measure rendering time in 3D Slicer:
1. Getting renderer: https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-views-renderers-and-cameras
2. Then applying renderer.GetLastRenderTimeInSeconds()
