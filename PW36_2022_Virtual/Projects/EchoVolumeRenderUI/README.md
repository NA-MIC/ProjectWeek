Back to [Projects List](../../README.md#ProjectsList)

# Update the Echo Volume Render interface

## Key Investigators

- Samuelle St-Onge (ÉTS, Montreal)
- Simon Drouin (ÉTS, Montreal)
- Andrey Titov (ÉTS, Montreal)

# Project Description

<!-- Add a short paragraph describing the project. -->

In this project, we aim to rework the interface of the Echo Volume Render module in order to make it more intuitive and better adapted to clinical users' needs. 

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Update and polish the module's interface to improve its usability for clinical users. 

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Have a good understanding of the Echo Volume Render's parameters
1. Get input from users on what could be improved (Children's Hospital of Philadelphia (CHOP)
1. Compare the module with commercial platforms to see which 3DE parameters are familiar to clinicians
1. Determine the modifications to be made to improve the interface 
1. Implement these modifications in the UI
1. Send the updated interface to collaborators from CHOP to get feedback

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Discussion on previous versions of the module to understand the changes that have been made in the last 2 years
1. Discussion with a collaborator from CHOP on aspects to be improved in the module
1. Determined modifications that could potentially improve visualization of volume rendered 3DE : 
    - Try to implement a [Phase Symmetry filter](https://pypi.org/project/itk-phasesymmetry/) to reduce noise in images while preserving anatomical detail prior to volume rendering
    - Implement Gaussian filtering in the GPU

# Illustrations
![Echo Volume Render UI](https://user-images.githubusercontent.com/57685132/149667633-524c8285-3f81-4c91-92c8-87b22a3d29c1.jpg)

## Long-term Objectives

1. Implement new features similar to [TrueView and Glass from Philips](https://www.usa.philips.com/healthcare/resources/landing/epiq/cardiology)
1. Implement Color Doppler

# Background and References
<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
