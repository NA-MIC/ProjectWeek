---
layout: pw45-project

permalink: /:path/

project_title: That Rendering Thing
category: VR/AR and Rendering
presenter_location: 

key_investigators:

- name: Steve Pieper
  affiliation: Isomics
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


I've been experimenting with [wgpu-py](https://github.com/pygfx/wgpu-py), an implementation of WebGPU that you can pip_install directly into Slicer.

The work in progress in [SlicerWGPU](https://github.com/pieper/SlicerWGPU), which is now working pretty nicely in demo mode.

#### Key Features
* Easy to install, can work with any recent Slicer release.  Don't even need to restart Slicer.
* Can write shader code easily that works on Vulkan, DirectX, and Metal.
* It supports multi-volume rendering with full quality compositing
* It can directly render segmentations and provides instant updates in response to edits
* It supports interactive rendering of volumes under non-linear transforms
* Interactive elements like transform handles and markups are still handled by VTK and seamlessly composited

#### Current status
* Currently in demo mode.  Some things are integrated to work with the MRML scene while, others work alongside.
* The VTK OpenGL render window is tapped into so that most rendering works cleanly, but SlicerWGPU uses a different method to composite multiple translucent surfaces (A-Buffer compared to Depth Peeling) so those aren't currently combined.
* Performance seems about the same as VTK's GPU renderer, but no extensive testing has been done. 

#### How to try it
* Clone the [SlicerWGPU](https://github.com/pieper/SlicerWGPU) repository
* Drag and drop the folder onto a running Slicer (5.10.0 or really any version should work).
* Be sure to load the `Scene Rendering` module (you can ignore the others)
* Go to the `Scene Rendering` module and try the buttons.  The top block of buttons (the "VTK Injection" block) are the current demos and the "Dual View" bock are some older experiments.

<img width="539" height="308" alt="Image" src="https://github.com/user-attachments/assets/5c518029-b73d-4881-91d9-50b3eecf0ab9" />



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Give demos to anyone who might be interested and collect feedback
2. Collect use-cases where existing Slicer rendering doesn't fully meet requirements but the SlicerWGPU code could
3. Consider what would be needed for a more complete integration (i.e. possible custom display nodes and dedicated GUI).




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Experiment with an updated Volume Rendering module to take advantage of advanced features
2. Try implementing any new features or use cases people suggest
3. Think about how to render volumes that are too large for GPU memory (i.e. paging texture data)
4. Consider how to make this more easily available and useful



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


(TBD)



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


<img width="400" alt="Image" src="https://github.com/user-attachments/assets/2fc3ddb2-f485-40a6-b8e1-241e4fe4d155" />

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/6e41c142-0e47-427e-9bbd-e5efac80069e" />

<img width="400" alt="Image" src="https://github.com/user-attachments/assets/18f1e66d-4939-450b-9d88-bcd8de74c3da" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- SlicerCL: <https://github.com/pieper/SlicerCL> (<https://www.youtube.com/watch?v=hFxTyLPjQd0>)
- STEP: <https://github.com/pieper/step> (<https://www.youtube.com/watch?v=ML9_JWAz1kY>, <https://youtu.be/8dputUoKBTA> )
- Transfer function editor: <https://youtu.be/4Q9NfNmN-9w>

