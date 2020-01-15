# Slicer VR

This breakout aims to identify the current state of VR capabilities in Slicer, identify areas of most need for improvement, and brainstorm about future potential applications of VR in Slicer.

## Attendees
1. Adam Rankin (Robarts Research Institute)

## Current State
VR is currently available in Slicer out-of-the-box via the [SlicerVirtualReality](https://github.com/KitwareMedical/SlicerVirtualReality) extension. This extension uses the VTK OpenVR interface that provides input, tracking, and visualization capabilities. To use this, [Steam](https://store.steampowered.com/) and [SteamVR](https://store.steampowered.com/app/250820/SteamVR/) must be installed and running (SteamVR installed from within Steam).

Preliminary work for AR support in Slicer is functional at [SlicerAugmentedReality](https://github.com/VASST/SlicerAugmentedReality) but needs improvements. Video passthrough infrastructure is available in VTK (last tested 8.2).

Tested OpenVR headsets include:
* HTC Vive
* HTC Vive Pro
* Samsung WMR Headset

### Extensions
* [SlicerVirtualReality](https://github.com/KitwareMedical/SlicerVirtualReality) - stable
* [SlicerAugmentedReality](https://github.com/VASST/SlicerAugmentedReality) - preview
* [SlicerLeapMotion](https://github.com/VASST/SlicerLeapMotion) - preview
* [SlicerLeapMotionControl](https://github.com/lassoan/SlicerLeapMotionControl) - unknown
* [SlicerVideoCameras](https://github.com/VASST/SlicerVideoCameras) - stable

### Interaction
Tracking data is available for all OpenVR devices including headset, controllers, and generic trackers. Input from the controllers is available and the default interactor provides navigation, zoom, and selection capabilities.

### Visualization


The Leap Motion hand tracking device can be streamed into Slicer and visualized using the SlicerLeapMotion extension.

### Hardware

### Infrastructure/Algorithms

## Areas of Improvement

### Interaction

### Visualization

### Hardware
* Input devices
* Headsets
  * Oculus support

### Infrastructure/Algorithms
