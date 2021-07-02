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

3. Creating a scripted module that displays a 3D view outside the Slicer layout, it displays the scene in stereo (red/blue etc) but not in quadbuffer mode for now.

4. Next step : change the default type widget of Slicer 4.13 so I can have my module working in quadbuffer mode. 

 

# Illustrations 

Already existing QuadBuffer stereo mode in 3DSlicer 4.8, photo taken by phone so quadbuffered image can be seen as it is supposed to without glasses:  
<img width="373" alt="IMG_20210628_112539" src="https://user-images.githubusercontent.com/76939787/123618437-7dfcf580-d808-11eb-8a39-c66edc125a32.jpg">


Module created and tested before implemeting it to Slicer 4.13 using VTK 9 and QT 4.15, still taken by phone:  
<img width="373" alt="IMG_20210628_112539" src="https://user-images.githubusercontent.com/76939787/123618384-70477000-d808-11eb-8b43-004ecffbfa42.jpg">


zSpace device:  
<img width="373" alt="Automotive_Student" src="https://user-images.githubusercontent.com/76939787/124276865-a6f0f380-db44-11eb-99c7-5f97080a26e2.gif">


Pre-op module for trajectory planning, using PyDBS:  
<img width="373" alt="image" src="https://user-images.githubusercontent.com/76939787/123618539-9836d380-d808-11eb-9009-bfe73d0657a4.jpeg">


Scripted module to display a new 3D view outside the actual layout [1] and in different stereo modes [2]. For now even if the button is named QuadBuffer this mode is not working:   

[1]  <img width="373" alt="Capture d%u2019écran du 2021-06-30 15-41-07" src="https://user-images.githubusercontent.com/76939787/124274204-43b19200-db41-11eb-8eed-07c43e0eedd0.png">
[2]  <img width="373" alt="Capture d%u2019écran du 2021-06-30 16-01-33" src="https://user-images.githubusercontent.com/76939787/124274266-56c46200-db41-11eb-9277-058ea6d17315.png">



 

# Background and References 

 

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. --> 
* [Paraview support for ZSpace](https://blog.kitware.com/zspace-device-support-coming-to-paraview/)
* [Paraview plugin's repository](https://gitlab.kitware.com/paraview/paraview/-/tree/master/Plugins/ZSpace)
* [Slicer/zSpace implementation 2013](https://fr.slideshare.net/zSpace/pieper-slicer-clinicalzspace20131021) 

 
