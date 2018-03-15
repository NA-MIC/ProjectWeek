Back to [Projects List](../../README.md#ProjectsList)

# SlicerAR Development

## Key Investigators

- Adam Rankin (Robarts Research Institute)
- Ken Martin (Kitware, Inc.)

# Project Description

## Objective

1. Enable video passthrough augmented reality via stereo camera capture

## Approach and Plan

- [x] Capture images from stereo camera via Plus
- [x] Send images to Slicer via OpenIGTLink
- [ ] Display images as left and right eye renderer backgrounds in SlicerVR

## Progress and Next Steps

- [x] Stereo camera operational
- [x] SlicerVR operational
- [ ] Background display operational
  - Initial work completed by Isabella Morgan (UWaterloo & NDI) [github.com](https://github.com/imorgan1618/VTK/commit/0f9bf00fc6ca953007ca644057e6c8acd8194faf)
  - VTK [pull request](https://gitlab.kitware.com/vtk/vtk/merge_requests/3902) submitted for base class vtkRenderWindow
  - Work on vtkOpenVRRenderWindow for on-GPU texture passing on-going

# Background and References
+ Stereo camera resources
  + [ATTACHING A RASPBERRY PI CAMERA MODULE TO THE COMPUTE MODULE IO BOARD](https://www.raspberrypi.org/documentation/hardware/computemodule/cmio-camera.md)
  + [Stereo Vision Using Compute Module: Syncing Pi Cameras](https://www.raspberrypi.org/forums/viewtopic.php?f=98&t=154314&sid=732f6438b6d83c6dc3c5525e62e81a54)
  + [UV4L Stereoscopic vision](https://www.linux-projects.org/uv4l/tutorials/stereoscopic-vision/)
  + [UV4L Raspicam](https://www.linux-projects.org/documentation/uv4l-raspicam/)
  + [Protect your Raspberry PI SD card, use Read-Only filesystem](http://hallard.me/raspberry-pi-read-only/)
