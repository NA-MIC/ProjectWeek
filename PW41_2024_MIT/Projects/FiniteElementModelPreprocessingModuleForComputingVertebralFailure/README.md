---
layout: pw41-project

permalink: /:path/

project_title: Finite element model preprocessing module for computing vertebral failure
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Ron Alkalay
  affiliation: Beth Israel Deaconess Medical Center
  country: US

- name: Zahra Soltani
  affiliation: Beth Israel Deaconess Medical Center
  country: US

- name: Steve Pieper
  affiliation: Isomics
  country: US

- name: Csaba Pinter
  affiliation: Ebatinka
  country: Spain

- name: Gnaneswar Chundi,
  affiliation: Rutgers University
  country: US

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Finite element simulations of the spine allow insight into the effect of bone metastatic lesions, affecting up to 70% of cancer patients at advanced stages of the disease, on the mechanism of pathologic vertebral fractures that cannot be measured in human subjects noninvasively. However, establishing personalized FE models from clinical imaging is complex and time-consuming, historically requiring manual vertebrae segmentation, creation and optimization of the model's mesh parameters,  interrogation of the image data for the application of material models, and applying these material models at the element level. These operations often require expensive commercial applications with little control over the method used and, critically, the ability to extend their capabilities or incorporate new capabilities without significant financial expense.

In collaboration with MIT, our group established a damage-based FE framework to investigate the effect of bone metastatic lesions on the failure and, more recently, the post-failure mechanical response of the human spines in cancer patients. Based on our ongoing collaboration with members of the 3D Slicer community, our group has developed DL models for segmenting human thoracic and lumbar vertebrae in cancer patients and developed scripts for meshing and applying bone modules based on the CT data. We propose to integrate our DL segmentation models, the Gmsh open-source meshing application, work on optimizing our material allocation algorithm, and create a parser for input file for the FE simulations (ABAQUS, MIT-Summit) within an extension framework to enable the complete pipeline (CT-data- FE input model).

Having such an open-source model in 3d Slicer will significantly contribute to the scientific and clinical community for cancer patient research and to studying the effect of vertebral fractures on morbidity not only in cancer patients but also in the elderly populations and surgical outcomes.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1.	Create an open-source Slicer extension to integrate DL spine segmentation, Gmsh, and our material allocation scripts, allowing the preparation of an input file for FE simulations.
2.	Discuss the possible integration of tools for the DL segmentation of the intervertebral disc and the derivation of disc tissue material models from MR data (DTI) and, finally, assembly of vertebrae-disc models (boundary conditions from our muscle models and joint interactions). Simulations within 3Dslicer😊



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1.	Discuss the current analysis and management scripts pipeline. Integration of the DL-based masks for generating data for the pipeline. Visualization and optimization options of mesh quality and applied bone modulus.
a.	The key gap is how best to optimize the mesh-based material allocation, which requires the computation of bone properties at the location of each mesh element.
2.	What issues must be solved for this integration within the extension mechanism? Build an integration plan emphasizing a framework for modularity and code expansion.
3.	Discuss methods of results presentation.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


We follow the following steps:
1. The element size on the boundary is set manually: in 3DSlicer we use "Surface Toolbox" under "Surface Models" to increase the size of boundary elements in the .vtk file (change the Number of points in Uniform remesh) and save the .vtk file.
2. We create and save a basic geo file to generate volume out of the .vtk file as below:
```
Merge "Model.vtk";
//+
Surface Loop(1) = {1};
//+
Volume(1) = {1};
```
3. We generate optimized 3D mesh using Gmsh by running the following command
`gmsh $geo_file -3 -optimize -format msh2`
4. For calculating average BMD, we use the concept of shape functions to find which voxels belong to an element, and then we average among the values greater than 0. To do this, first, in 3D Slicer, we find the coordinates of voxels and the HU values. Then, for each element, a voxel will belong to the element if the summation of 4 shape functions at the voxel's location equals 1. For linear tetrahedrons, the shape function of each vortex is the volume of the tetrahedron made with three other vertices and the point. The below figure, for example, shows these volumes for an arbitrary point inside the element.

    ![Picture1](https://github.com/NA-MIC/ProjectWeek/assets/49168951/47d36e51-a130-4d2a-b25c-3283d44979da)
    - We are eager to use any other approach for better numerical efficiency.
    - In this approach, each voxel is assessed based on the coordinates of its center. Is there any possibility that one can calculate partial inclusions of voxels in the element? This approach will give us the capability of going to the smaller resolutions.






# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->



![Graphical abstract](https://github.com/NA-MIC/ProjectWeek/assets/49168951/e841d76c-012c-4c38-b3fa-cd3cbc4421c2)

Figure 2: Graphical summary of the intended pipeline..



# Background and References
- [CT-based finite element simulating spatial bone damage accumulation predicts metastatic human vertebrae strength and stiffness](https://www.frontiersin.org/articles/10.3389/fbioe.2024.1424553/abstract)

# Results

**Extension Creation**
<img width="1680" alt="Screenshot 2024-06-28 at 9 39 14 AM" src="https://github.com/NA-MIC/ProjectWeek/assets/56100029/864cbd08-0693-4aa5-867b-2ae1a775fcb3">

**GMSH integration**
<img width="992" alt="Screenshot 2024-06-28 at 10 11 55 AM" src="https://github.com/NA-MIC/ProjectWeek/assets/56100029/028217e3-907d-4ff1-ad90-d8b43b3360b0">

**Visualization of Mesh in Slicer**
<img width="1680" alt="Screenshot 2024-06-28 at 10 12 45 AM" src="https://github.com/NA-MIC/ProjectWeek/assets/56100029/225b9681-838c-408b-bb3f-09d5379d4c50">

**Future Steps**
- Add more advanced GMSH options for user
  - Size fields (finer control over mesh size)
  - Sampling Rate
  - Rate of change
  - etc.
- Add functionality to interrogate CT volume for HU data to assign modulus values to each element.
- Add QA functionality to evaluate and visualize mesh quality and fix bad elements.
- Add implementation into existing SegmentMesher

<img width="675" alt="Screenshot 2024-06-28 at 10 13 54 AM" src="https://github.com/NA-MIC/ProjectWeek/assets/56100029/ea976b9a-f866-4f9e-b8c5-9f6b06aa08de">




<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
