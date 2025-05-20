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

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The goal of this project is to implement segment-aware carving mechanism, that will make it possible to clip specific user-defined segments when rendering a medical volume. This will allow users to create very customized visualizations tailored for specific needs, like anatomy learning or preoperative planning. Eventually, the goal is to add a VR interactions, as demonstrated in this video:

https://www.youtube.com/watch?v=YFl7LF5hWxI



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Implement a segment-aware clipping occlusion management technique, which may be useful for anatomy learning or preoperative planning.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Decide upon the best architecture (OpenGL or WebGPU) to achieve the task
2. Implement segment-awake clipping
3. Add VR interactions 




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. This project has already been implemented in Unity, and the goal of this project is to port it to 3D Slicer. However, the Unity implementation relies a lot on compute shader
2. An approach to fill a volume shader and then pass to to the fragment shader has been tested, however, 




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![Image](https://github.com/user-attachments/assets/e2d313f4-ea24-4636-8af8-4f04d3598e6e)



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


Article describing the occlusion management technique was submitted to the ISMAR 2025 conference.

Relevant technique for unsegmented data: A. Joshi, D. Scheinost, K. Vives, D. Spencer, L. Staib, and X. Papademetris, “Novel interaction techniques for neurosurgical planning and stereotactic navigation,” IEEE Trans. Vis. Comput. Graph., vol. 14, no. 6, pp. 1587–1594, Nov. 2008, doi: 10.1109/TVCG.2008.150.

