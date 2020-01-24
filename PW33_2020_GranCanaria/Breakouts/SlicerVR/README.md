- [Slicer VR](#slicer-vr)
  * [Attendees](#attendees)
  * [Current State](#current-state)
    + [Extensions](#extensions)
    + [Interaction](#interaction)
    + [Visualization](#visualization)
    + [Hardware](#hardware)
    + [Infrastructure/Algorithms](#infrastructure-algorithms)
  * [Areas of Improvement](#areas-of-improvement)
    + [Interaction](#interaction-1)
    + [Visualization](#visualization-1)
    + [Hardware](#hardware-1)
    + [Infrastructure/Algorithms](#infrastructure-algorithms-1)
  * [Minutes](#minutes)
  * [Other References](#other-references)

# Slicer VR

This breakout aims to identify the current state of VR capabilities in Slicer, identify areas of most need for improvement, and brainstorm about future potential applications of VR in Slicer.

## Attendees
1. Adam Rankin (Robarts Research Institute)
1. Andras Lasso (Queen's University)
1. Sam Horvath (Kitware, Inc.)
1. JCFR (Kitware, Inc.)
1. Csaba Pinter (Ebatin S.L.)
1. Steve Pieper (Isomics Inc.)
1. Thomas Muender (University of Bremen)
1. Verena Reinschluessel (University of Bremen)
1. Thomas Mildner (University of Bremen)

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
* Introduction and meeting motivation - Adam Rankin
* Adam initiates a discussion on the current state of VR in Slicer
  * Csaba Pinter discussing his latest work in VR UI
    * Implementation able to render Qt widgets directly in VR
      * Custom patches required to update VTK version used by Slicer
      * Branch available at https://github.com/cpinter/SlicerVirtualReality/tree/virtual-widget/VirtualReality
  * Steve inquires as to the state of text renderering in VR
    * Ensuing discussion regarding different approaches of rendering text
    * Slicer currently using 2D actor for fiducial markup label
  * Adam inquires Csaba as to progress regarding input into VR rendered QWidget - see work by Ken Martin (Kitware Inc.)
* Adam initiates discussion regarding development of VR widget library
  * Csaba explains the state of his SlicerVR widgets
  * Control panel type widget, with a few different views
    * Home view
    * Subject hierarchy view
    * App view
* Steve inquires to UBremen attendees as to the state of their [Slicer<->Unity VR](https://github.com/NA-MIC/ProjectWeek/blob/master/PW33_2020_GranCanaria/Projects/SlicerToUnity/README.md) project
  * Demonstration and discussion follow
  * HTC Vive, Steam Index HMD used by UBremen group
* Adam initiates discussion on input methods
  * Gaze tracking - generally agreed to be a good direction to pursue - An example by David Garcia - https://github.com/PerkLab/EyeTracking
  * Voice input - Andras explains their poor success in OR environment, multiple people comment on detection accuracy with accents, Andras comments that an XBox controller in a sterile bag was much more effective than both voice and gesture input
  * Hand gestures - Andras explains that gesture input is also not intuitive, hard to remember/learn for participating clinicians
* Adam puts out a call for recommended development directions
  * Generally agreed that a library of widgets in VR is most needed
  * Andras thinks that AR is promising, but more accurate object tracking needed (possibly develop a new image analysis method of depth cameras)
  * Hand tracking of value, but high accuracy finger tracking required
  * Eye tracking - good for multi-user interaction and realistic collaboration environments

## Other References
  * https://gitlab.kitware.com/vtk/vtk/merge_requests/6326#note_671975
