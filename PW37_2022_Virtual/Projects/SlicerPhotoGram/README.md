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


# Illustrations

Example point cloud exported from webODM and loaded in Slicer using [this code](https://gist.github.com/pieper/e4ca5e4c753c5ed6c61656d25b93402c).
![image](https://user-images.githubusercontent.com/126077/174670532-75d16428-15a5-4647-8b80-7820fe4dfde3.png)

![image](https://user-images.githubusercontent.com/126077/174670684-eae5cc87-b0da-41cb-9a79-6a903148168f.png)

# Background and References

1. The repository for SlicerPhotoGram: [https://github.com/SlicerMorph/PhotoGram](https://github.com/SlicerMorph/PhotoGram).
2. Currently, we have created a script [output_cropped_image.py](https://github.com/SlicerMorph/PhotoGram/blob/main/output_cropped_images.py) for loading digital image sequnece as a volume, crop each image using ROI tool for reducing background noise, and export each cropped slice as a tiff image. 
3. WebODM for photogrammetry that rely on OpenCV and OpenSFM: [https://www.opendronemap.org/docs/](https://www.opendronemap.org/docs/) and [https://github.com/OpenDroneMap/WebODM](https://github.com/OpenDroneMap/WebODM).
4. We have a script for loading WebODM point clouds in Slicer: [https://gist.github.com/pieper/e4ca5e4c753c5ed6c61656d25b93402c](https://gist.github.com/pieper/e4ca5e4c753c5ed6c61656d25b93402c)
