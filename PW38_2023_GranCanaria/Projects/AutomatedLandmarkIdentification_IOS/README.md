Back to [Projects List](../../README.md#ProjectsList)

# Automated Landmark Identification on IOS

## Key Investigators

- Nathan Hutin (University of Michigan)
- Luc Anchling (UoM)
- Maxime Gillot (UoM)
- Baptiste Baquero (UoM)
- Jonas Bianchi (UoM, UoP)
- Marcela Gurge (UoM)
- Najla Al Turkestani (UoM)
- Marilia Yatabe (UoM)
- Lucia Cevidanes (UoM)
- Juan Prieto (UoNC)

# Project Description

We develop a method that identifies landmarks on dental crowns. The method must be robust and handle models with different orientation. Existing methods perform poorly if the surface models are not correctly oriented. The method proposed here is rotation invariant and handles 3D surface models with a wide variety of dental crown shapes.


Data come from clinician. All data are segmented manually or by SlicerDentalModelSeg (Slicer extension). Dataset create surface according to teeth’s number. Each surface is center on one tooth and scale according to the size of tooth. The dataset make a texture with normal of surface. The dataset make a texture where we can see a projection of landmark on the surface. For each batch the dataloader give two surface, one with normal texture and second one with landmark texture. We place cameras around the tooth in center on the 3D space. Each camera take a picture. We give images of surface with normal texture to the model. The lost function compare output of the model and images of surface with landmark texture. After we backward the model to improve him.

Github repository : https://github.com/HUTIN1/ALIDDM/tree/refactoring 

## Objective

1. Refactoring the code 
2. Found good parameter to get better prediction
3. Train model for different landmark



## Progress and Next Steps

### Progress

1. Refactoring the code

### Next Step
1. Found good parameter to get better prediction
2. Train model for different landmark


# Illustrations
### User Interface
![ali_user_interface](https://user-images.githubusercontent.com/72212416/215179106-15994380-29d5-49b0-825e-be910dcb9b6c.png)

### Landmark Output Example
![ali_output](https://user-images.githubusercontent.com/72212416/215205073-dec0a8d1-72b1-4584-a12e-42b4e10e838e.png)


