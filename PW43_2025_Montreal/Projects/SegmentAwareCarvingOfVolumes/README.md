---
layout: pw43-project

permalink: /:path/

project_title: Segment-aware carving of volumes
category: VR/AR and Rendering

key_investigators:

- name: Andrey Titov
  affiliation: ÉTS
  country: Canada

- name: Simon Drouin
  affiliation: ÉTS
  country: Canada
  
- name: Liam O'Connor
  affiliation: Concordia University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The goal of this project is to implement segment-aware carving mechanism, that will make it possible to clip specific user-defined segments when rendering a medical volume. This will allow users to create very customized visualizations tailored for specific needs, like anatomy learning or preoperative planning. Eventually, the goal is to add a VR interactions, as demonstrated in this video:


<iframe width="420" height="315" src="https://www.youtube.com/embed/YFl7LF5hWxI">
</iframe>



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement a segment-aware clipping occlusion management technique, which may be useful for anatomy learning or preoperative planning.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Create a a basic architecture using the currently existing OpenGL that allows chaining multiple compute shaders and then to visualize the computed image
2. Implement segment-awake clipping visualization using the computer shader chaining pipeline




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. This project has already been implemented in Unity, and the goal of this project is to port it to 3D Slicer. However, the Unity implementation relies a lot on compute shaders.
2. An approach to fill a volume in an OpenGL a compute shader has been tested, and this result can then be displayed by writing the output to an existing multi-component volume. However, to access the texture ID of this multi-component volume, a loadable C++ is required, which has already been made.
3. The different segements from the volume are rendering using volume rendering and the texels take in the proper color based on the segments' labels.
4. The editor makes it possible to add a 'clipping sphere' to the scene. This clipping sphere is created using a point markup and a radius value can be set in the editor. The clipping sphere is then used in a compute shader to clip into the different segments within the volume. If the sphere clips into a voxel it sets the intensity value of said voxel to 0.
5. The clipping sphere uses a 'mask' to only clip certain segements in the volume. Whether the the segment will be clipped depends on the segment visibility value in the Segment Editor, which can be changed in real time.
6. The module was published online and is accessible in the Extension Manager:
   - https://github.com/andrey-titov/SlicerAnatomyCarve

Future work:
1. The rendering needs to be polished to reduce the antialiasing on the segments and make it look better.
2. Multiple clipping spheres should be possible to be created. This would then enable the ability to have each sphere clip different segments within the volume. 



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![Screenshot 2025-06-26 153232](https://github.com/user-attachments/assets/d24714da-98f3-4215-a942-40092ff9d8e7)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Article describing the occlusion management technique was submitted to the ISMAR 2025 conference.

Relevant technique for unsegmented data: A. Joshi, D. Scheinost, K. Vives, D. Spencer, L. Staib, and X. Papademetris, “Novel interaction techniques for neurosurgical planning and stereotactic navigation,” IEEE Trans. Vis. Comput. Graph., vol. 14, no. 6, pp. 1587–1594, Nov. 2008, doi: 10.1109/TVCG.2008.150.

