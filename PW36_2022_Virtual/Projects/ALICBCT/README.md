Back to [Projects List](../../README.md#ProjectsList)

# Automatic Landmark Identification in 3D Cone-Beam Computed Tomography scans

## Key Investigators

- Maxime Gillot
- Baptiste Baquero
- Juan Carlos Prieto
- Hina Shah

# Project Description

We propose a novel approach that reformulates anatomical landmark detection as a classification problem through a virtual agent placed
inside a 3D Cone-Beam Computed Tomography (CBCT) scan. This agent is trained to
navigate in a multi-scale volumetric space to reach the estimated landmark position. The
agent movements decision relies on a combination of Densely Connected Convolutional
Networks (DCCN) and fully connected layers. Our method achieved high accuracy with an average of
less than a 1.3mm error on the landmarks position without failures.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The goal is to have a model that automatically finds accurate landmarks in CBCT scans.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
A virtual agent is placed inside a 3D CBCT scan. This agent is trained to
navigate in a multi-scale volumetric space to reach the estimated landmark position. The decision making is processed through a deep neural network.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

Done :
1. Prepare the data to be used for training and prediction
2. Train the model with a set of 6 landmarks and 60 CBCTs
3. Test the accuracy of the prediction on new scans

Next:
1. Train the model on new landmarks and new CBCTs set
2. Create a slicer module that can be used to predict the landmark on various types of file
3. Optimize the training method to make it accessible for clinicians to train on their own dataset

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

Selection of 6 landmark to test the method
![LM_SELECTION](https://user-images.githubusercontent.com/46842010/148439491-f2dd1d7c-65f3-44dc-9590-8c12a143b3ad.png)

Environment to search the agent
![Environment used for the landmark search](https://user-images.githubusercontent.com/46842010/148282250-a2be2edf-e8b8-4d4e-bc16-c71fd0ea9d38.png)

Architecture of the agent
![Agent used to find the landmark](https://user-images.githubusercontent.com/46842010/148282323-a423f5a3-1ecf-4cff-b824-e6073c835163.png)

The 3 steps to search the landmark
![Search_3Steps_labeled](https://user-images.githubusercontent.com/46842010/148439759-e7db327a-f9a4-4d45-93b9-c566f19137ba.png)


# Project week results 

I managed to learn the basics on ho to develop a slicer module.
I spent this week on creating a first sketch of a future module that will be used to launch the landmark prediction.
For now, it allows the user to browse folders where the AI models are and create a menu wher the clinician can choose wich landmark to predict :
<img width="1331" alt="Screen Shot 2022-01-20 at 11 47 24 PM" src="https://user-images.githubusercontent.com/46842010/150468043-db9f0b87-a724-4a53-b91d-dd318a8c7b4f.png">

<img width="522" alt="Screen Shot 2022-01-20 at 11 47 50 PM" src="https://user-images.githubusercontent.com/46842010/150468053-89c5b68d-83d2-4725-b8cd-d62891b9a0b9.png">


<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
