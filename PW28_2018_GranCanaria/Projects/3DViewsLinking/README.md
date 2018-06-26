Back to [Projects List](../../README.md#ProjectsList)

# Add 3D views linking capabilities

## Key Investigators

- [Davide Punzo](https://punzo.github.io/) (Kapteyn Astronomical Institue, Netherlands)
- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- [Steve Pieper](https://lmi.med.harvard.edu/people/steve-pieper) (Isomics Inc., USA)
- [Jean-Christophe Fillion-Robin](https://www.kitware.com/jean-christophe-fillion-robin/) (Kitware Inc., USA)
- [Csaba Pinter](http://perk.cs.queensu.ca/users/pinter) (Queen's University, Canada)
- [Simon Drouin](http://nist.mni.mcgill.ca/?page_id=369) (Montreal Neurological Institute, Canada)


# Project Description
Adding 3D views linking functionalities such as the 2D one.

## Objective
The 3D view controller widget should have GUI for synchronizing the following proprieties: 

* displayed content (what models, volumes, segmentations, etc. are visible in each view)
* view properties (show/hide ruler, orientation marker, background color, etc)
* camera (position, focal point, up vector, orthogonal/perspective, field of view, etc.)

## Approach and Plan

* Design the GUI
* Get feedback regarding the GUI
* Implement MRMLLogic

## Progress and Next Steps
Things to discuss to design the GUI:

do we what a popup menu for some buttons (either old or new ones)? or show all of them? or put part of them in the adavnced control in the View Controller module?

* 3Dview controllers buttons show/hide?
  * AxesWidget
  * CenterButton
  * OrthoButton
  * RulerButton
  * StereoButton
  * ZoomInButton
  * ZoomOutButton
  * SpinButton
  * RockButton
  * RulerButton
  * OrientationMarkerButton
  * VisibilityButton
  * StereoButton
  * deph peeling 
  * FPS
  
  let's leave as it is

* shall we add GUI for recent volume rendering varibales moved from the MRMLVolumeRendering to the MRMLView node (Csaba mod to volume rendering)? Probably adding also this will be confusing (i.e. duplication of GUI and sync with volume rendering GUI).
  * GPUMemorySize
  * VolumeRenderingQuality
  * RaycastTechnique
  * VolumeRenderingSurfaceSmoothing
  * VolumeRenderingOversamplingFactor
  
  not necessary!


* camera linking button (difference between "normal" and "hot"?)

no double mode, leave it very simple. Click linking and the cameras are all updated, GUI, etc..

Implementation as the MRMLSliceLogic one.

* angle differ? different camera motion, etc... 

specilized interface in the cameras module.

* Display content as in the 2D view? shall add models too? segmentation maust always be global (for 2d/3d etc...)??

add pick from 3d view when right click. It will show a menu with the edit action.



# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/3Dviewlinking.png)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

https://discourse.slicer.org/t/project-for-3dslicer-project-week/2558
