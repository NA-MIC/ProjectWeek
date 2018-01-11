Back to [Breakout Sessions List](../README.md#BreakoutSessions)

# Augmented/Virtual Reality

## Agenda
* AR/VR use cases
* VR demo stations
* Slicer VR interactions
* SlicerOpenVR sofware design discussion

## Presenters
- Sam Jang (Medical Augmented Intelligence): Clinical use cases
- Steve Pieper (Isomics): VR web integration
- Andras Lasso (Queen's University): Augmented reality use cases
- Adam Rankin (Western University): AR development
- Csaba Pinter (Queen's University): Slicer VR interactions

## Interactions design
- After grabbing an object (volume, model, etc), moving it should work by manipulating a transform
  - Constraints can be set to the objects, restricting the DOFs
    - There is an "interaction" transform that will contain the constrained interaction
    - This interaction transform can be used to determine the actual transform of an object if needed by observing it and updating another (for example for the imaging panels in Room's Eye View)
  - Auto-add transform for "movable" objects when grabbed and moved
    - These default transforms are simple: parent is world, no constraints
    - Moving group of objects or moving with constraints can be set up explicitly
- Moving in the workd
  - If no object is grabbed, then the "world is moved" (i.e. the camera manipulated)
  - "Swimming", pinch zoom: open/close arms with both controllers
  - Being able to fly anywhere is a distraction, causes losing orientation (the patient is the only focus)
    - Walk around (e.g. along surface of sphere) and zoom are the only modes of motion
	The clipped slice(s) will be the slice drawn on, the same way it is done now on the 2D slices
- Segmentation (show [DicomVR video](http://www.dicomvr.com/))
  - By simulating mouse interactions all the effects could be used
  - New effects
    - Surface deformation: Grow ROI on segment surface then push or pull with modification function (VR possibly makes it actually usable by allowing quick evaluation of the result while changing the input, and seeing all in real 3D with depth)
- **Discussion**

## VR software design
- Already available for SlicerOpenVR
  - Custom menu can be created in the VR view by VTK (useful for show/hide, change color, etc.)
  - Fiducials can have a floating point 3D coordinate in the view (can be grabbed)
  - Same 3D displayable managers can be used
    - Updates automatically, so it may be slow. Could only be updated when control released
  - Clipping widget (plane) exist (developed at Kitware France) - [[videos](https://www.dropbox.com/sh/wbv5fc4yjazs84v/AADIHAdViDfoQze8TvBCkyvta?dl=0)], [[LucasGandelKitware/VR_VolumeRendering](https://gitlab.kitware.com/LucasGandelKitware/VR_VolumeRendering)]
  - Can show "floor" for easier orientation
  - Orientation marker
- Excluding VR view from main layout management: Node reference parentLayoutNodeID in view nodes
  - None by default, meaning main layout. Set to node (e.g. itself) to indicate it's standalone and should not be managed
  - Abstract layout node class
    - Current layout node and the new VR layout node will be its child classes
    - VR "layout" may contain HUD-like objects such as slice views or charts that are positioned and kept stationary in the VR view by the layout
- **Discussion**

## Background and References

- [SlicerOpenVR](https://github.com/KitwareMedical/SlicerOpenVR)
- [Medical Augmented Intelligence](http://mai.ai)
- [DICOM VR](http://www.dicomvr.com/)
- [SliVR Tractography](http://pieper.github.io/sites/slivr)
- [A-Frame](http://iframe.io)
- [SlicerWeb](http://github.com/pieper/SlicerWeb)

- ...
