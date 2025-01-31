Back to [Projects List](../../README.md#ProjectsList)

# DeepHeart integration with MONAILabel

## Key Investigators (subject to change)

- Matthew Jolley, MD (Children's Hospital of Philadelphia, Philadelphia, PA, United States)
- Christian Herz, MS (Children's Hospital of Philadelphia, Philadelphia, PA, United States)
- Danielle F. Pace, PhD (Martinos Center for Biomedical Imaging, CSAIL, MIT, MGH, HMS, Boston, MA, United States)
- Andras Lasso, PhD (Laboratory for Percutaneous Surgery, Queen’s University, Canada)
- John Witt (Children's Hospital of Philadelphia, Philadelphia, PA, United States)
- Sachidanand Alle (NVIDIA)
- Prerna Dogra (NVIDIA)
- Andrés Díaz-Pinto (King's College London, UK)

# Project Description

Creation of a MONAILabel app for leaflet segmentation of heart valves in 3D echocardiographic (3DE) images. In particular, we have been developing AI models for segmentation of Tricuspid Valve leaflets in 3DE images of patients with Hypoplastic left heart syndrome (HLHS).

<!-- Add a short paragraph describing the project. -->

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Creation of a MONAILabel app
2. Bring own UI elements as FCN will need additional user input

### Slide 1
![image](https://user-images.githubusercontent.com/10195822/123651558-91ed2b00-d7f9-11eb-9016-41229ad7f416.png)

### Slide 2
![image](https://user-images.githubusercontent.com/10195822/123651594-9addfc80-d7f9-11eb-8f54-f15cba237a1f.png)

### Slide 3

![image](https://user-images.githubusercontent.com/10195822/123651723-b77a3480-d7f9-11eb-889d-f7232dbda0a8.png)


### Slide 4

![image](https://user-images.githubusercontent.com/10195822/123651929-dd073e00-d7f9-11eb-830b-2f5b940aa2cd.png)

### Slide 5

![image](https://user-images.githubusercontent.com/10195822/123651802-ca8d0480-d7f9-11eb-9b0b-ce38a728fac9.png)




### Slide 6

![image](https://user-images.githubusercontent.com/10195822/123651978-e5f80f80-d7f9-11eb-973b-b7e6a8f377d4.png)


## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Use MONAI framework for replacing most of our custom code to minimize overhead
2. Create MONAILabel app based on ported code
3. Create custom UI for additional user inputs

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. MONAILabel team created new sample app with support for multi-label segmentation (https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/segmentation_liver_and_tumor)
2. MONAILabel team added option to upload local image to the MONAILabel server
3. DeepHeart MONAILabel app created for the segmentation of tricuspid valve leaflets from 3DE images

![MONAILabel](https://user-images.githubusercontent.com/10195822/124171163-3380b080-da76-11eb-8ce7-4d38100227a0.gif)
