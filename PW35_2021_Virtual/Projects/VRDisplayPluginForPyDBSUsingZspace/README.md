Back to [Projects List](../../README.md#ProjectsList)


# VR display plugin for PyDBS using a zSpace device 


## Key Investigators 

- Marine CAMBA (STIM team, CENIR - ICM, France) 

- Sara FERNANDEZ VIDAL (STIM team, CENIR - ICM, France) 

- Sinan HALIYO (Multi Scale Interaction team, ISIR, France) 

# Project Description


This project aims at developing a visualization tool that could help neurosurgeons who practice Deep Brain Stimulation. This tool will allow to navigate in the brain of patients (eg parkinsonian patients), in complex scenes that comprise MR images, anatomical atlases, stimulation electrodes, functional maps, etc… It will be used to plan trajectories for surgery, and to train future surgeons, as it is prefered to navigate in a 3D space in order to get a better understanding of the complexity of the human brain, and therefore be more precise in the OR.  
 
zSpace technology is at the interface of VR and 3D holographic-like environments. Thus, it can make navigating into Slicer's 3D scenes easier, and closer to reality. A module had already been made in Slicer 4.3. Unfortunately, after some changing in the zSpace's API, it was no longer running nor maintained. Earlier this year, Paraview, another VTK based software, launched a new plugin to allow a user to get access to the full potential of the zSpace device.   

Thanks to those achievements, we thought it would be interesting to create a new plugin for Slicer to work on this particular device, and help neurosurgical planification and postoperative navigation. The plugin would include head tracking and a stereoscopic view, to display in 3D, and a ray to interact with the objects using the given stylus. A good start was to try if Slicer could do QuadBuffer stereo by itself, prior to connected it to our zSpace, as QuadBuffer is the technology used by this device to display in 3D.  

We would use VTK 9 as Slicer is planning on using it for its future launches, and Slicer 4.13, the lastest version compatible with this VTK. Indeed, using Slicer actual VR extension is not feasible as the technologies are not close enough.  

 

## Objective 

 

<!-- Describe here WHAT you would like to achieve (what you will have as end result). --> 

 

1. Code a plugin to display PyDBS surgery planification module in QuadBuffer mode. 

2. Same but using zSpace API and stylus. 

 

## Approach and Plan 

 

<!-- Describe here HOW you would like to achieve the objectives stated above. --> 

 

1. Create a Qt/VTK based plugin to know how to render in Quadbuffer mode. 

2. Make it work on Slicer 4.13. 

3. Upgrating this plugin so it uses zSpace API rather than Qt/VTK functions (can then do head tracking...). 

4. Adding the stylus following Paraview example. 

5. See how PyDBS surgery plannification is working with it. 

 

## Progress and Next Steps 

 

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. --> 

 

1. A small VTK widget which display a sphere in QuadBuffer mode using Qt/VTK functions. 

2. 2 widgets one displayed in 3D QuadBuffer mode, the other in classic 2D, to see where I need to make the changes and how. 

3. Skeleton of this widget but with Slicer scenes. 

4. ... 

 

# Illustrations 

 

<!-- Add pictures and links to videos that demonstrate what has been accomplished. 

![Description of picture](Example2.jpg) 

![Some more images](Example2.jpg) 

--> 

 

# Background and References 

 

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. --> 

 
