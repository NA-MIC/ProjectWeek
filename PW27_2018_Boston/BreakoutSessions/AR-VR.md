Back to [Breakout Sessions List](../README.md#BreakoutSessions)

# Augmented/Virtual Reality

## Agenda
* AR/VR use cases
* VR demo stations
* Slicer VR interactions
* SlicerOpenVR software design discussion

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
- Moving in the world
  - If no object is grabbed, then the "world is moved" (i.e. the camera manipulated)  - "Swimming", pinch zoom: open/close arms with both controllers
  - Being able to fly anywhere is a distraction, causes losing orientation (the patient is the only focus)
    - Walk around (e.g. along surface of sphere) and zoom are the only modes of motion
	The clipped slice(s) will be the slice drawn on, the same way it is done now on the 2D slices
- Segmentation (show [DicomVR video](http://www.dicomvr.com/))
  - By simulating mouse interactions all the effects could be used
  - New effects
    - Surface deformation: Grow ROI on segment surface then push or pull with modification function (VR possibly makes it actually usable by allowing quick evaluation of the result while changing the input, and seeing all in real 3D with depth)

- **Discussion**
  - Sam Jang recommendations: Keep focus on the model, not fly around; rotate or walk around; keep actions very consistent.
  - If elbow and wrist rests on some gel pad then fine manipulation is feasible
  - Minimize virtual motion detached from physical motion to reduce motion thickness
  - Similarly to WebVR/AFrame (https://aframe.io/), WebAR is going to be available, too (for example, with Apple ARKit)
  - There are different use cases, which require different interaction models, such as room-centric and object-centric
    - Walking around the object is not always feasible (there is not always enough space)
    - "Turntable" mode could be good (keep a constant distance, view object from different side)
    - Games mostly "jump" to a new place, to reduce motion thickness
    - "Laser pointer" kind of interaction
  - Operations in VR must be faster, because arms get tired, time passes quicker
  - Segmentation: painting may betedious but cleaning up a model may be good
  - Warping of 3D surfaces (to match anatomy during segmentation) could be a good use case
  - Some things are possible in 3D that is almost impossible in 2D (such as drawing a knot or follow a complex 3D trajectory). Some other things, such as accurate drawing of contours may be easier using mouse&keyboard.
  - Orientation marker may help (small human figure)
  - From @curtislisle:
During the VR interaction session at the recent Project Week, we discussed interaction modes.  I was reminded of early research by some former colleagues at Univ. of Central Florida.  Here is a URL and Bibliography to some of the work that might be of interest:
https://www.mitpressjournals.org/doi/abs/10.1162/pres.1995.4.4.403
This is the work I described about selecting a nearby object to establish a coordinate system transformation and move the world with respect to the eyepoint instead of flying the eyepoint towards the target object.  The point was made about simulation sickness when moving the eyepoint, but our lab's work indicated this paradigm of direct manipulation of the virtual environment was effective.
Some literature search of the PRESENCE journal might help us take advantage of some of  the earlier work.    It is nice to see that rendering and VR technology is finally more widely accessible.


## VR software design

### Existing features
- Already available for SlicerOpenVR
  - Custom menu can be created in the VR view by VTK (useful for show/hide, change color, etc.)
  - 3D coordinate of widget - seed widget can now store floating point display coordinate instead of int (can be grabbed)
  - Same 3D displayable managers can be used
    - Updates automatically, so it may be slow. Could only be updated when control released
  - Clipping widget (plane) exist (developed at Kitware France) - [[videos](https://www.dropbox.com/sh/wbv5fc4yjazs84v/AADIHAdViDfoQze8TvBCkyvta?dl=0)], [[LucasGandelKitware/VR_VolumeRendering](https://gitlab.kitware.com/LucasGandelKitware/VR_VolumeRendering)]
  - Can show "floor" for easier orientation
  - Orientation marker

### Proposed changes

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
