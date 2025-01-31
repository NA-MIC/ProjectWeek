# Slicer module for 3D stereophotogrammetry

## Key Investigators

- Chi Zhang (Seattle Children's Research Institute)
- A. Murat Maga (University of Washington and Seattle Children's Research Institute)
- Steve Pieper (Isomics, Inc)

# Project Description

3D stereophotogrammetry has becoming increasingly common in biomedical and clinical fields as an economic, fast, flexible and safe (non-invasive, no radiation) way to achieve accurate 3D surface models. In particular, photogrammetry can acquire realistic surface texture that allows researchers and clinicians to accurately assess traits and placing landmarks.

To further reduce the cost and faciliate the use of photogrammetry, we want to build an open-source pipeline for photogrammetry in 3D Slicer for from digital image post-processing to photogrammetric 3d mesh reconstruction and texturing that incorporate open-source software and packages. Eventually, we will also create guidelines for clinicians and researchers, espically using mobile devices (e.g., smart phone), for Slicer-based photogrammetry.


## Objective

1. Build open-source software and packages asscoiated with photogrammetry (e.g., WebODM, ExifTool, OpenCV, OpenSFM) into Slicer. Create GUI for adjusting parameters.
2. Loading multi-png textured model into Slicer
3. 3D model and texture building from point clouds created from photogrammetry software.
4. Import partial textured models into Slicer, clean them up, align and fuse.

## Approach and Plan
1. Figure out what our issues and priorities are:
   * how imporant is visual fidelity vs convenience (point clouds are more conveneient but lower image quality compared to textured models)
   * how much do we imaging users interactively fixing geometry at various levels of detail
   * how much do we need to rely on third party code and what maintenance or licencing considerations come with it
3. Determine what parts of the process Slicer can be particularly useful for (i.e. should we bring in the raw images and estimate the camera parameters or assume that other software has already done that).
4. Work to define and describe the ideal interactive workflow leveraging existing Slicer functionality like markups and segmentations.

## Progress and Next Steps
1. Adapt an online example to render an obj file with multiple resources through `vtkRenderer`. First build a `vtkOpenGLPolyDataMapper` to link to the mesh and store each texture image according to material names, and then add a `vtkOpenGLActor` to refer to the content of the mapper. Finally, passing the actor to the rendere. However, for our dataset, `vtkRenderer` crashed whenever I rendered the model with more than 14 texture images (on Windows), while w111 accompanied texture images. Steve confirmed the same issue on Mac. Below an example of rendering with 10 texture images.

<p align="left">
<img src="https://user-images.githubusercontent.com/80793828/176799669-20fa6858-f508-4533-ae34-0e9985736b11.PNG" width = 400>
<p/>

2. Andras suggested spliting the mesh according to texture images and each part being mapped with a few texture images. However, the texture appears to have one dominant image, the rest just cover isolated areas. This may make mesh splitting complicated. Below are the model matched with the 1st & 10th texture image.

<p align="left">
<img src="https://user-images.githubusercontent.com/80793828/176800048-607ecd77-e1a7-4f67-924b-b9d66a6ca935.PNG" width = 300>
<img src="https://user-images.githubusercontent.com/80793828/176800046-01881345-0583-4cc2-a329-a38bffe5c448.PNG" width = 300>
<p/>

3. I then followed Steve and Andras' suggestions to try using Blender to merge texture images. I merged the first 25 texture images into one using Blender and map to the model using the Texture Modeler in Slicer. Slicer successufully rendered the model with the texture. The result is showing below.

<p align="left">
<img src="https://user-images.githubusercontent.com/80793828/176800803-2349d6b7-6852-447a-af6b-869e90ce7d1e.PNG" width = 600>
<p/>

* The resolution is pretty low. This is probably because the scaling for each texture image after merging into one texture image. Below shows the 1st texture image (the dominant one) (left) and the merged one (right). In the merged one, the texture of the specimen basically concentrate at the lower left corner.

<p align="left">
<img src="https://user-images.githubusercontent.com/80793828/176801710-98d1d20b-a86b-4b53-899c-60485102695f.png" width = 400>
<img src="https://user-images.githubusercontent.com/80793828/176801723-1ed94d94-0330-4199-8448-e9b4fa8a94cc.png" width = 400>
<p/>

4. Future directions:
* Merge texture images properly:
  * I did not merge all 111 texture images because Blender requires me to add the same texture mapping node for every image. It appears that we can do python scripting in Blender. Thus, it might be useful to explore looping through every image using python and later connect to Slicer.
   * Find a proper way to merge texture to retain the resolution. I'm also checking with the ODM people to see if they can do it.
* Follwing Andras' suggestion, directly access vtkRenderer() in Slicer scene to have stable rendering.
* Steve suggested geometry accuracy is more important than visual fidelity at this moment and we can archiving images for adding more algorithms in the future, such as machine learning. For the near future, we can focus on first getting a pipeline based on ODM. In the long run, we should definitely consider adding machine/deep learning algorithms, for example, to image registration, which is the foundation of geometric & texture accuracy in structure-from-motion photogrammetry. This can also greatly improve the efficieny of photo taking. Currently, we have to take a lot photos carefully to ensure proper registration but it is still tricky. We will have more discussions with Murat.
* We will also discuss how much we can rely on Slicer & how much we have to use 3rd party software & packages.


# Illustrations
Example

Example textured model (.obj) exported from WebODM viewed in MeshLab

<img src="https://user-images.githubusercontent.com/80793828/175820570-1dd33815-a151-4469-9f30-42470906fc0a.png" width = 400>

Example camera positions reconstructed by WebODM, viewed in WebODM

<img src="https://user-images.githubusercontent.com/80793828/175820800-78f81f9c-6d44-42a1-b8e2-c201abd04fc3.png" width = 400>

Example point cloud exported from webODM and loaded in Slicer using [this code](https://gist.github.com/pieper/e4ca5e4c753c5ed6c61656d25b93402c).

<img src="https://user-images.githubusercontent.com/126077/174670532-75d16428-15a5-4647-8b80-7820fe4dfde3.png" width = 400>

<img src="https://user-images.githubusercontent.com/126077/174670684-eae5cc87-b0da-41cb-9a79-6a903148168f.png" width = 400>



# Background and References

1. The repository for SlicerPhotoGram: [https://github.com/SlicerMorph/PhotoGram](https://github.com/SlicerMorph/PhotoGram).

2. Currently, we have created a script [output_cropped_image.py](https://github.com/SlicerMorph/PhotoGram/blob/main/output_cropped_images.py) for loading digital image sequnece as a volume, crop each image using ROI tool for reducing background noise, and export each cropped slice as a tiff image.

3. WebODM for photogrammetry that rely on OpenCV and OpenSFM: [https://www.opendronemap.org/docs/](https://www.opendronemap.org/docs/) and [https://github.com/OpenDroneMap/WebODM](https://github.com/OpenDroneMap/WebODM).

4. We have a script for loading WebODM point clouds in Slicer: [https://gist.github.com/pieper/e4ca5e4c753c5ed6c61656d25b93402c](https://gist.github.com/pieper/e4ca5e4c753c5ed6c61656d25b93402c)
