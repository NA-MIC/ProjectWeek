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

## Progress and Next Steps

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
![itksnap](https://user-images.githubusercontent.com/10054456/175941015-bf185cc4-26a3-4a4f-be3b-27df8afb8459.png)

The segmentation, with the corresponding labels, as seen in 3DSlicer
![enslicer](https://user-images.githubusercontent.com/10054456/175942464-395eb6f4-ec12-4aa4-b7ce-84d018b71d0a.png)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
