Back to [Projects List](../../README.md#ProjectsList)

# Automatic Landmark Identification in IOS and Cranio Facial CBCT

## Key Investigators

- Maxime Gillot (UoM)
- Baptiste Baquero (UoM)
- Jonas Bianchi (UoM, UoP)
- Marcela Gurge (UoM)
- Najla Al Turkestani (UoM)
- Marilia Yatabe (UoM)
- Lucia Cevidanes (UoM)
- Juan Prieto (UoNC)


# Project Description

For CBCT :
We propose a novel approach that reformulates anatomical landmark detection as a classification problem through a virtual agent placed
inside a 3D Cone-Beam Computed Tomography (CBCT) scan. This agent is trained to
navigate in a multi-scale volumetric space to reach the estimated landmark position. The
agent movements decision relies on a combination of Densely Connected Convolutional
Networks (DCCN) and fully connected layers.

For IOS :


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Combine the old ALI CBCT of the first project week and the new ALI IOS in a new module
2. Add new landmarks in the available list
3. Deploy the tool in a Slicer module

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use the module we worked on during project week 36
1. Get new data to train on with more landmarks


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. We have models for landmark identification in CBCT and IOS
1. We have the begenning of an UI on slicer
1. The next steps are :
1. Link the UI with both ALI IOS and ALI CBCT algorithms
1. Train new models for more landmarks
1. Deploy the tool as a Slicer module in the sclicer CMF extention

# Illustrations
![Slicer screen](https://user-images.githubusercontent.com/46842010/174138265-66ab080e-e885-4f76-a150-7e4da3869aa0.png)

<img width="569" alt="results" src="https://user-images.githubusercontent.com/83285614/175572226-337d8a2e-dcf7-45d5-b7a4-35269e5d6f2b.png">



# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
