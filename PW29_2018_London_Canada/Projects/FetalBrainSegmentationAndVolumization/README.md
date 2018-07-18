Back to [Projects List](../../README.md#ProjectsList)

## Fetal Brain Segmentation and Volumization    

## Key Investigators
- Estee Goldberg (Biomedical Engineering, Western University)
- Denis Kikinov (Software Engineering, Western University) 
- Wenyao Xia (Robarts Research Institute) 


# Project Description
<!-- Add a short paragraph describing the project. --> 
This will be a tool to segment the fetal brain from the a fetal MRI. Afterwards the fetal brain will be compiled into a brain volume for later comparisons


## Objective
1. Take any fetal MRI image
1. Semiautomatically segment the fetal brain
1. Semiautomatically produce a brain volume for the segmented brain 

## Approach and Plan

1. Look for modules and extensions that already exist.
1. If none exist, figure out to the steps of segmentation and attempt to semiautonomize it.
1. Write code the allows segmentation then output the result in Slicer.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
### Progress
After some search we found no automatic modules or extensions that work for fetal MRIs. As such we have experimented with ways to manually segment and get a volume. We have tried using Slicer Segment Editor, however the resulting segmentation is not exact due to the quality of images (segmentation has to be done manually as well). We were able to write Matlab code that was able to segment using a Slicer volume label mask, and the resulting segmentation is cleaner than that done manually in Slicer and has a very similar volume.

### Next Steps
Either get the Matlab code working in Slicer using the Matlab bridge, or replicate the same steps as a Slicer extension. 

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
