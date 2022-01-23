Back to [Projects List](../../README.md#ProjectsList)

# Real-time visualization for transcranial magnetic stimulation (TMS)

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

Real-time visualization of an electric field (E-field) for transcranial magnetic stimulation (TMS) on the brain surface, possible visualization through an AR app (over browser).

## Approach and Plan
- TMS module mapping NifTi file onto brain mesh
- OpenIGTLinkIF used to transfer data into 3D Slicer
- Next steps include connecting 3DSlicer to the web browser (via WebSocket) and
- Using a mobile device via WebXR to view/control 3D Slicer and later the TMS module

## Progress and Next Steps

1. Connecting Slicer with a mobile phone via SlicerWeb (https://github.com/pieper/SlicerWeb)
2. Explore WebXR: WebXR needs https, so either generate local certificate (https://blog.anvileight.com/posts/simple-python-http-server/) and make modifications in the SlicerWeb WebServer.py file. OR alternatively run with USB cable connected to computer (USB debugging in developer tools for Android. iPhone requires an Apple Developer Account for this)
3. Evaluating different approaches for AR with WebXR by testing different libraries: ThreeJS, A-Frame or React. 
4. Visualizing our created 'butterfly' TMS coil in WebXR: A-Frame only allows obj and gltf file formats as models, Threejs also more like stl files. A-Frame allowed only image-, location- and marker-based AR tracking. Recently, AR.js enables markerless AR. Using WebXR without a marker is still in early stages of development.
5. Moving the TMS coil and scene by tapping on it on the mobile device.

Next steps:
- More precise interaction with objects in AR on the phone: scaling and rotating of the coil via mobile screen gestures (Current WebXR approaches only allow static interaction without handling user's finger gestures on screen.)
- Retrieving user's and coil position coordinates.
- Send the current coil position coordinates into Slicer via SlicerWeb connection.

## Illustrations

- TMS coil model visualized in AR with A-Frame:

![Moving TMS coil in AR](./render_coil_A-frame.gif)


- Current TMS module inside Slicer:

![Slicer Module](./TMSModule_normedcoil_fmricolor.png)


-Visualization goal in Slicer from another software:

![Brain surface and DT](./tmsonbrain.png)


# Background and References

## Infos for running WebXR:

Phones need a Depth sensorto run AR/VR. A list of supported devices can be found here: https://developers.google.com/ar/devices

On an Android Phone via USB: 
- PlayStore: Download Google VR Services and Google AR Services App
- Update Chrome/Camera apps etc.
- On the phone: Enable Developer tools (https://developer.android.com/studio/debug/dev-options) and USB debugging (description here: https://developer.chrome.com/docs/devtools/remote-debugging/)
- Run chrome://inspect#devices in the browser on your computer and it should detect USB connected devices

For iPhone: 
- Mozilla offers a WebXR Emulator that can be downloaded from the Apple Store for any iPhone and iPad: https://labs.mozilla.org/projects/webxr-viewer/

## For Slicer TMS Module (see previous project week ![PW 35](https://github.com/NA-MIC/ProjectWeek/tree/master/PW35_2021_Virtual/Projects/TMS_Slicer_Module)):

vtkProbeFilter: https://vtk.org/doc/nightly/html/classvtkProbeFilter.html
Moving fiducials with CPYY: https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5

Measure rendering time in 3D Slicer:
1. Getting renderer: https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-views-renderers-and-cameras
2. Then applying renderer.GetLastRenderTimeInSeconds()
