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


## Progress and Next Steps


# Illustrations


# Background and References

1. The repository for SlicerPhotoGram:https://github.com/SlicerMorph/PhotoGram.
2. Currently, we have created a script [output_cropped_image.py](https://github.com/SlicerMorph/PhotoGram/blob/main/output_cropped_images.py) for loading digital image sequnece as a volume, crop each image using ROI tool for reducing background noise, and export each cropped slice as a tiff image. 
3. WebODM for photogrammetry that rely on OpenCV and OpenSFM: https://www.opendronemap.org/docs/ and https://github.com/OpenDroneMap/WebODM.
