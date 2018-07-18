Back to [Projects List](../../README.md#ProjectsList)

## Fetal Brain Segmentation and Volumization    

## Key Investigators
- Estee Goldberg (Biomedical Engineering, Western University)
- Denis Kikinov (Software Engineering, Western University) 
- Wenyao Xia (Medical Biophysics, Robarts Research Institute) 


# Project Description
<!-- Add a short paragraph describing the project. --> 
This will be a tool to segment the fetal brain from the a fetal MRI. Afterwards the fetal brain will be compiled into a brain volume for later comparisons


## Objective

1. Take any fetal MRI image
1. Semiautomatically segment the fetal brain
1. Semiautomatically produce a brain volume for the segmented brain 

## Approach and Plan
Due to the nature of our MRI data, each subject was scanned from Axial,Sagittal, and Coronal views separetely resulting in three separate volumes. These scans are at different coordinates preventing a simple merge of the volumes.

1. The first step is to find similarities between the volumes, and to transform them into the same coordinate system.
1. Once the volumes are in the same system, they are registered together by registering two together, and then registering the third on top. This should result in a clear and accurately fused fetal brain.
1. Interpolate a 3D volume from the registration. *
1. With a full 3D volume, a mask of the brain will be manually created in Slicer.
1. The mask will be applied to the volume, extracting the fetal brain. Skull stripping will be applied if needed.
1. With the extracted fetal brain, the volume will be computed in centimetres cubed. 

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
### Progress
As of now, we were able to fuse two of the images together.

After some search we found no automatic modules or extensions that work for fetal MRIs. As such we have experimented with ways to manually segment and get a volume. We have tried using Slicer Segment Editor, however the resulting segmentation is not exact due to the quality of images (segmentation has to be done manually as well). We were able to write Matlab code that was able to segment using a Slicer volume label mask, and the resulting segmentation is cleaner than that done manually in Slicer and has a very similar volume.



### Next Steps
Fuse in the last image, and segment the brain from the fused 3D volume.

Either get the Matlab code working in Slicer using the Matlab bridge, or replicate the same steps as a Slicer extension. 

# Illustrations

<!--Due to the secrecy of the fetal MRI images, the following artistic representations have been created.-->
<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->
<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

<!-- - Source code: https://github.com/YourUser/YourRepository-->
<!-- - Documentation: https://link.to.docs
- Test data: https://link.to.test.data
-->
