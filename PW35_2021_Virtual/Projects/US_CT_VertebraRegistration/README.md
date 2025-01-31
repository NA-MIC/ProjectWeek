Back to [Projects List](../../README.md#ProjectsList)

# US-CT Vertebra Registration

## Key Investigators

- Houssem Gueziri (Montreal Neurological Institute, Montreal, Canada)
- Tamas Ungi (Queen's University, Kingston, Canada)

# Project Description

This project aims at evaluating the feasibility of percutaneous US to CT image registration, on a porcine dataset, for minimally invasive spine surgery.
The goal is to combine the registration method for _open_ surgery implemented in IBIS with the segmentation/bone enhancement method in AIGT.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Read/Write US data acquired with IBIS into Slicer.
3. Segment the vertebral surface of US data obtained from porcine cadavers
4. Register segmented images with CT images

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Convert the data from IBIS acquisitions to ultrasound sequences
2. Generate ground truth segmentation from CT images
3. Use AIGT to train model for axial image segmentation - [Video tutorial](https://youtu.be/l0BcW8c9CnI)
4. Use segmented data with IBIS registration and evaluate registration

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

- Align US images with CT using ground truth transform and export data as Sequences readable in Slicer :heavy_check_mark:
- Segment data using pre-trained model:heavy_check_mark:
- Generate ground truth segmentation and train model [TODO]
- Segment data with fine-tuned model [TODO]

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

**Data processing workflow:**

![Workflow](workflow.png)

**Generate aligned CT-US data:**

![US-CT Data](https://github.com/NA-MIC/ProjectWeek/releases/download/project-week-resources/PW35__US_CT_VertebraRegistration__US-CTAlignment.gif)



**Segmentation with pre-trained model:**

![Segmentation](Segmentation.png)







# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
