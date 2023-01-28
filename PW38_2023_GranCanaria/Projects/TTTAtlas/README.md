Back to [Projects List](../../README.md#ProjectsList)

# Development of Anatomy Atlases and Training Tools with 3D Slicer and Open Source Software

## Key Investigators

- Juan Ruiz (ULPGC)
- Idafen Santana (ULPGC)
- Mario Monzón (ULPGC)
- Aday Melián (ULPGC)
- TBD

# Project Description

With the help of 3D Slicer and open source software, anatomy atlases and training tools are becoming more accessible than ever. These tools allow medical professionals to gain a better understanding of the human body, from its organs and muscles to its bones and tissues. They also provide an opportunity for medical students to practice their skills in a virtual environment without risking any harm to real patients.

This project aims to provide the tools and knowledge for generating a comprehensive set of atlasses. Additionally, it will enable the development of innovative tools such as augmented reality (AR) applications and virtual reality (VR) simulations to further enhance the learning experience.

## Objectives

1. Objective A: Create and define a straightforward pipeline to create atlases based in open source Web technologies from Slicer3D exported content.

2. Objective B: Select different open source atlas (OpenAnatomy and z-Anatomy as starting points) and define common needs to create an agnostic data importer.

3. Objective C: Application prototype development

## Approach and Plan

1. Choose the most appropiated current technologies to implement an scalable atlas based on 3D Content exported from Slicer3D. (Sample approach: Typescript + Three.JS)

2. Start from boilerplate or template project to create an appropiate dev environment.

3. Add 3D Rendering support and basic interactions of 3D engine.

4. Create data importer from different sources and load them into 3D engine.

5. Include a selector panel to choose between all available atlas in a local folder and load them individually and with customized content (For adaptation for different uses of the atlas)

6. Try out and test 3D Engine features (VR, AR, Multiuser...) over the imported models.

7. Publish conclusions and details of our work and publish our code as open source starting atlas project.

## Progress and Next Steps

- No previous work

# Illustrations

# Background and References
- Last two years we have been working with anatomic 3d models to create educative experiences like VRAINS (VR Anatomic atlas - ULPGC) and AVRIR (Collaborative VR dissection - ULPGC) using OpenAnatomy and z-Anatomy content imported into Unity3D.

- We have found several challenges with the adaptation of this kind of content for our objectives (Excess of polygons for target devices, too detailed anatomic distribution, language localization...).
