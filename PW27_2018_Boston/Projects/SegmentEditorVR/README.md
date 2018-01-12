Back to [Projects List](../../README.md#ProjectsList)

# Segment Editor VR

## Key Investigators

- Csaba Pinter (PerkLab)
- Andras Lasso (PerkLab)

# Project Description

Contouring with Segment Editor in VR view!

## Objective

Make basic decisions about usage of Segment Editor in VR and possibly prove the concepts by simple prototypes.

## Approach and Plan

1. Usage of current Segment Editor features in VR
2. Decide which effects will be most useful and how they will be fully supported
3. Come up with new effects that become viable via VR

## Progress and Next Steps

In a nutshell:
1. Try everything and see what is best
2. Go the usual Slicer way and offer multiple features and make them selectable as options

Details:
* Usage of current Segment Editor features in VR
    * The clipped slice(s) will be the slice drawn on, the same way it is done now on the 2D slices
      * By simulating mouse interactions all the effects could be used
    * Also offer free-hand painting for annotations, illustrations. Some people may prefer this for their use cases
* There are different use cases, which require different interaction models, such as room-centric and object-centric
  * Walking around the object is not always feasible (there is not always enough space)
  * "Turntable" mode could be good (keep a constant distance, view object from different side)
  * Games mostly "jump" to a new place, to reduce motion thickness
  * "Laser pointer" kind of interaction
* Operations in VR must be faster, because arms get tired, time passes quicker
  * If elbow and wrist rests on some gel pad then fine manipulation is feasible without quick tiring
* Painting may betedious but cleaning up a model may be good
* Orientation marker (small human figure) prevents getting lost
* New effects enabled by VR (things can be possible in 3D that are almost impossible in 2D)
  * Examples: drawing a knot or follow a complex 3D trajectory
  * Surface deformation tool: grow ROI on segment surface then push or pull with function (VR possibly makes it actually usable by allowing quick evaluation of the result while changing the input)
* Some other things, such as accurate drawing of contours may be easier using mouse&keyboard

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

![DICOM VR](http://www.dicomvr.com/)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Breakout session: https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/BreakoutSessions/AR-VR.html
