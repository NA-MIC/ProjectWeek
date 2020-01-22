# Slicer VR

This breakout aims to identify the current state of VR capabilities in Slicer, identify areas of most need for improvement, and brainstorm about future potential applications of VR in Slicer.

## Attendees
1. Adam Rankin (Robarts Research Institute)

## Current State
VR is currently available in Slicer out-of-the-box via the [SlicerVirtualReality](https://github.com/KitwareMedical/SlicerVirtualReality) extension. This extension uses the VTK OpenVR interface that provides input, tracking, and visualization capabilities. To use this, [Steam](https://store.steampowered.com/) and [SteamVR](https://store.steampowered.com/app/250820/SteamVR/) must be installed and running (SteamVR installed from within Steam).

Preliminary work for AR support in Slicer is functional at [SlicerAugmentedReality](https://github.com/VASST/SlicerAugmentedReality) but needs improvements. Video passthrough infrastructure is available in VTK (last tested 8.2).

### Extensions
* [SlicerVirtualReality](https://github.com/KitwareMedical/SlicerVirtualReality) - stable
* [SlicerAugmentedReality](https://github.com/VASST/SlicerAugmentedReality) - preview
* [SlicerLeapMotion](https://github.com/VASST/SlicerLeapMotion) - preview
* [SlicerLeapMotionControl](https://github.com/lassoan/SlicerLeapMotionControl) - unknown
* [SlicerVideoCameras](https://github.com/VASST/SlicerVideoCameras) - stable

### Interaction
Tracking data is available for all OpenVR devices including headset, controllers, and generic trackers. Input from the controllers is available and the default interactor provides navigation, zoom, and selection capabilities.

### Visualization
The 3D view in Slicer can be rendered in compatible OpenVR headsets. Other views including 2D Slice, Chart, etc... view are not currently rendered to the headset.

The Leap Motion hand tracking device can be streamed into Slicer and visualized using the SlicerLeapMotion extension.

### Hardware

Tested OpenVR headsets include:
* HTC Vive
* HTC Vive Pro
* Samsung WMR Headset

### Infrastructure/Algorithms
The SlicerVideoCameras extension provides a wrapper to OpenCV's camera calibration techniques.

## Areas of Improvement
We have identified the following major categories as areas that need improvement in the current Slicer ecosystem.

### Interaction
It is still unclear which input methods will provide the easiest navigation and action capabilities in VR, but is most likely a combination of input methods.

* Controllers provide a high accuracy method for localization/selection, but are potentially bulky
* Voice provides a contact-free method for input, but can be a potentially complicated implementation
* Hands provide an intuitive input method, but depending on the implementation can suffer from accuracy and field-of-view limitations
  * Gesture recognition complexity is highly dependent on the implementation
* Eye tracking offers an intuitive input method, but interaction guidelines are not yet commonly defined (gaze linger, gaze select, etc...?)
  * Hardware availability is still limited or expensive

Even once input methods have been decided, interaction guidelines for input are still a shifting target in VR. Using controllers, for example, does one use the point of the device as a selection point, or use the direction of the controller as a laser pointer? There are many such questions/decisions to be settled.

### Visualization
* UI library
  * Collection of VR widgets to provide input events (buttons, sliders, etc...)
* Other views necessary/wanted?

### Hardware
* Input devices
* Visualization devices
  * MagicLeap - LuminOS, Nvidia Tegra SoC
  * Phone/tablet - Android, arm

### Infrastructure/Algorithms
* ?

## Minutes
