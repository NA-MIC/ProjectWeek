Back to [Projects List](../../README.md#ProjectsList)

# Lumbar Spine Segmentation using MONAI Label

## Key Investigators

- Nayra Pumar (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- María Rosa Rodriguez (Universidad de Las Palmas de Gran Canaria (ULPGC), Spain)
- David García Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)

# Project Description

Our goal is to have a trained model in MONAI that is able to segment five lumbar vertebrae and four intervertebral discs, working with the 3D volumes of a public dataset.

## Objective

Train and deploy neural network to segment lumbar verteral bodies and intervertebral discs from MRI 3D volumes of the lumbar region.

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Prepare the public dataset of choice, using the T2.
1. Objective B. Train MONAI to segment the 5 vertebrae (from L1 to L5) and the 4 intervertebral corresponding discs.
1. Objective C. Deploy the trained model to another computer and be able to run it to perform segmentations without being connected to a server.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Choose a public dataset
1. Get the files ready for MONAI.
1. Install the MONAI server locally
1. Train the model

## Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. The chosen dataset is [Multi-scanner and multi-modal lumbar vertebral body and intervertebral disc segmentation database](https://www.nature.com/articles/s41597-022-01222-8): consisting of 39 patients. From all the images provided, we selected 51 of them, the ones with a T2 volume.
5. Change the file format to .nii for the selected t2 images.
6. Unify the 9 segments into a single file (5 segments for vertebrae and 4 for discs)

# Past issues

* MONAI not being able to read the .nii images when they been resized with nibabel.
The command we used for resize was:
`result1 = skTrans.resize(im, (newSize,newSize,numSlices), order=0, preserve_range=True)`
* Resized masks no longer in B/W, but having some grayscale pixels: solved with conditional value replacing using numpy (replacing values <0.5 to 0 and the remaining ones to 1)
* Missing segmentations in the dataset

# Illustrations
T2 volume with the mask file, showing the 9 segments:

<img src="https://user-images.githubusercontent.com/10054456/175941015-bf185cc4-26a3-4a4f-be3b-27df8afb8459.png" width="550">

The segmentation, with the corresponding labels, as seen in 3DSlicer

<img src="https://user-images.githubusercontent.com/10054456/175942464-395eb6f4-ec12-4aa4-b7ce-84d018b71d0a.png" width="550">

# Progress
Using the public dataset, once all segments had been placed in the same .nii file, and with the right segment IDs: 1 to 5 for the vertebrae (named from top to bottom) and 6 to 9 for the discs (named from top to bottom as well), we trained the model using different setups.

The tags were configured like this in the segmentation.py file:

<img src="https://user-images.githubusercontent.com/10054456/176892498-4861de87-7a71-4211-9a76-0eb7a4a39043.png" width="550">

These were commented or left as this, depending on the number of tags to use on each training attempt.
One issue we found is that tags should be always be numbered starting at 1; if we tried to run the model using tags from 6 to 9 we would get an error and the model wouldn't train. This issue will be solved soon in the code.

## Al Khalil dataset

### 2000 epochs and 9 tags

<img src="https://user-images.githubusercontent.com/10054456/176892815-5271846d-851e-4514-8b4b-b10477245f51.png" width="550">

The accuracy was too low (23%), and the results weren't good.
Note also that we had only 32 images for training and 8 for validation. So we went for less tags.

### 2000 epochs and 5 tags

This time we are only segmentating bone: tags 1 to 5 corresponding to the vertebrae.

<img src="https://user-images.githubusercontent.com/10054456/176893062-551f3554-0034-4dbf-95cc-6cc4e9ace786.png" width="550">

Visual results are better, but the accuracy is still too low (51%).

### 2000 epochs and 2 tags

Trying to determine if the poor results were caused by the lack of an appropriate nuber of images, the model was trained for only two tags: vertebrae L1 and L2.

<img src="https://user-images.githubusercontent.com/10054456/176893289-1b939a24-148e-404d-adb5-8a77ce7c5074.png" width="550">

Accuracy 52%, almost the same than when aiming for 5 tags.

A possible approach then would be to train five different networks, each for two elements. Then use it to segment volumes from another dataset, put all of these segmentations into a single file (like what we did when we prepared the Al Khalil dataset) and have a larger segmented dataset with the 9 tags. This idea was put on hold, to go for further training with different approaches.

## CHU dataset

We tried with another public dataset, called CHU for short, [Annotated T2-weighted MR images of the Lower Spine](https://zenodo.org/record/22304#.Yr7nSXZ_paY). This one only has bone, and all seven vertebrae (the 2 last thoractic and 5 lumbar) are all in the same tag.

The dataset comprises 23 images, and we hand processed them, separating the 7 vertebrae into 7 segments (numbered from top to bottom).

### 2000 epochs and 5 tags

<img src="https://user-images.githubusercontent.com/10054456/176894231-347433ef-7f32-4305-b8f7-f5d9fb1824fe.png" width="550">

Good accuracy (92%), acceptable visual results, but there is an evident confusion in one of the vertebrae, where tags are mixed.

We tried one of the images from the Al Khalil database with this model and got this result, because of the different ways the x,y,z coordinates are oriented on each dataset:

<img src="https://user-images.githubusercontent.com/10054456/176894487-0f7004e8-7092-4426-900f-99e9733ba67d.png" width="550">

### 2000 epochs and 1 tags

This is using a single tag with all the vertebrae together. (The image shows only the last segment, but it segmented the 7 vertebrae)

<img src="https://user-images.githubusercontent.com/10054456/176894556-7abd7914-a819-4d46-8f1a-235d85f73842.png" width="550">

Accuracy 94%.

## DeepEdit

Andres Diaz Pinto suggested to train using the deep edit module, instead of the segmentation we had been using until the moment.

The computer we have been using for this has a RTX 3070, and we tailored the memory usage for a 128x128x128 train image size:

<img src="https://user-images.githubusercontent.com/10054456/176895054-9c704015-7430-4712-aaf1-dade605f515a.png" width="550">

### 200 epochs and 9 tags

It took 22 hours to train. Again, we had 32+8 images and 9 tags.

<img src="https://user-images.githubusercontent.com/10054456/176895201-30ee5d15-dec5-42cf-b72a-beef0a546efd.png" width="550">

Taking into account the low number of images used for training, the results are good. But not good enough to start segmentating other images. Accuracy is 80%.

# Work in progress

* Separate the Al Khalil dataset into two different ones: vertebrae (5 tags, 1 to 5) and discs (4 tags, 1 to 4) and train separatedly
* Put the CHU dataset in the same coordinate system than Al Khalil and use the L1 to L5 segments to increase the number of images available for training the vertebrae segmentation: 32 from Al Khalil + 23 from CHU = 55 volumes.
* Train the model for the vertebrae with the 55 images for 5 tags, using the segmentation and deep edit and compare results.
* Train the model for the discs with the 32 images for 4 tags, using the segmentation and deep edit and compare results.

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
* Al Khalil dataset: [Multi-scanner and multi-modal lumbar vertebral body and intervertebral disc segmentation database](https://www.nature.com/articles/s41597-022-01222-8)
* CHU dataset: [Annotated T2-weighted MR images of the Lower Spine](https://zenodo.org/record/22304#.Yr7nSXZ_paY)

# Acknowledgments

Many thanks to all those who stopped by the Discord channel to contribute their knowledge. And especially thanks to Andrés Diaz-Pinto for his availability and patience in helping us to configure the models.
