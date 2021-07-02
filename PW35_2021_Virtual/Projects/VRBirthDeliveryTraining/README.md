Back to [Projects List](../../README.md#ProjectsList)

# VR for Birth Delivery Training

## Key Investigators

- Mónica García-Sevilla (Universidad Las Palmas de Gran Canaria, Las Palmas de Gran Canaria, Spain)
- Abián Hernández-Guedes (Universidad Las Palmas de Gran Canaria, Las Palmas de Gran Canaria, Spain)
- Nayra Pumar (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- David García-Mato (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)
- Juan Ruiz Alzola (Universidad Las Palmas de Gran Canaria, Las Palmas de Gran Canaria, Spain)
- Javier Pascau (Universidad Carlos III de Madrid, Madrid, Spain)
- Csaba Pinter (Ebatinca S.L., Las Palmas de Gran Canaria, Spain)

# Project Description

The World Health Organization recommends a rate of cesareans inferior than 15%. 
However, the actual rates in the US double this value, while the use of obstetrical instruments,
a recommended alternative to cesareans but which requires high skill and experience, has significantly decreased in the latest years. 
In this context there is a clear demand for simulators, with special interest in learning the correct use of Kielland’s forceps.

In 2018, we developed a training software in 3D Slicer for the correct use of forceps.
We used anatomical simulators of the mother and fetus, a forceps 3D printed in non-ferromagnetic material, and an electromagnetic tracking system to track the movements of the forceps relative to the simulators.
Further details can be found [here](https://link.springer.com/chapter/10.1007%2F978-3-030-01201-4_9).

The goal of this project is to translate this software into a Virtual Reality (VR) application using the SlicerVR extension. This way, only the VR device is required for training.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
1. Visualize the simulators and forceps models in the VR scene.
2. Interact with the models using the controllers.
3. Select the step of the procedure.
4. Check whether the maneuver for the step is correct or not.
5. Enable a collaborative mode.


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Visualize the simulators and forceps models in the VR scene. :heavy_check_mark:
2. Define a correct starting viewpoint. :heavy_check_mark:
3. Decide how to move the forceps with the VR controllers. :heavy_check_mark:
4. Learn how to access buttons from the controllers. (Already possible from python?) :question:
5. Define a way of selecting the step for the procedure (assembly, presentation, initial placement, final placement). A panel could be a good idea.
6. For each step, check whether the placement was correct or not. :heavy_check_mark: (2/6)
7. Connect to the same scene from other device.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. 3D models of the mother and baby are displayed in the VR glasses with an adequate size.
1. The 3D models are displayed in front of the user when starting the application. If the user changes position, the view can be reset to show the model in front of the user again.
2. Controller models are hidden and substituted by the forceps. The position of the forceps is configured as if the user was grabbing them.
3. The first two steps of the procedure (arrangement and presentation) have been added to the module. Forceps are displayed in green when correct and in red when incorrect.
4. The evaluation of each step is performed in real time. It has to be selected by the user in the module. Buttons for all the steps have been added.
5. When a step is selected, the name of the step is displayed on the scene. 3D models of the text have been created to show the message.

## To Do:
1. Access controller buttons so the user can change step without removing the headset. A panel widget could also be a good solution.
2. Add the remaining steps.
3. Add the collaborative option.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
## Previous setup (non-VR):
![module_scene_and_panel](https://user-images.githubusercontent.com/17642986/123103298-c34aad00-d42d-11eb-925a-15dd4b7bc4f0.png)
![experts_training](https://user-images.githubusercontent.com/17642986/123102863-6222d980-d42d-11eb-9292-e8731f1d4271.jpg)
![novices_training](https://user-images.githubusercontent.com/17642986/123102867-62bb7000-d42d-11eb-9f8b-f53d87b1000f.jpg)

## VR solution:
![setup](https://user-images.githubusercontent.com/17642986/124196551-9436da00-dac4-11eb-8441-e573675dc887.png)
![arrangement_correct](https://user-images.githubusercontent.com/17642986/124196569-99942480-dac4-11eb-9e99-405b15632ef8.png)
![arrangement_incorrect_1](https://user-images.githubusercontent.com/17642986/124196572-9a2cbb00-dac4-11eb-8b4a-189436c512fd.png)
![arrangement_incorrect_2](https://user-images.githubusercontent.com/17642986/124196573-9ac55180-dac4-11eb-9f56-a41ea9009ab2.png)
![presentation_correct](https://user-images.githubusercontent.com/17642986/124196576-9ac55180-dac4-11eb-9440-851377a34bd5.png)
![presentation_incorrect_1](https://user-images.githubusercontent.com/17642986/124196577-9b5de800-dac4-11eb-9893-86e1bb532e53.png)
![presentation_incorrect_2](https://user-images.githubusercontent.com/17642986/124196578-9b5de800-dac4-11eb-8777-86c7821229ac.png)

VR video: [https://youtu.be/Q8b7IehEQhE](https://youtu.be/Q8b7IehEQhE)


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
* [Publication of non-VR training system](https://link.springer.com/chapter/10.1007%2F978-3-030-01201-4_9)
* [Video of non-VR training system](https://www.youtube.com/watch?v=EEasWbH1jZI)

