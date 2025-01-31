---
layout: pw40-project

permalink: /:path/

project_title: 'Add a MONAI Auto3DSeg inference extension to 3DSlicer '
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Rudolf Bumm
  affiliation: Cantonal Hospital of Graubünden
  country: Switzerland

- name: Andras Lasso
  affiliation: Queens University
  country: Canada

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Andres Diaz-Pinto
  affiliation: Senior Deep Learning Engineer at NVIDIA
  country: UK

- name: Umang Pandey
  affiliation: Universidad Carlos III de Madrid
  country: Spain

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to implement MONAI Auto3DSeg in a 3DSlicer extension. This will enable fast inference with NVIDIA GPUs and CUDA and slower inference with CPU only.
Auto3DSeg is a relatively new technique in the MONAI project and our first experiments have been successful. inference is not as complicated as using the MONAOLabel inference function.\
A future aim is to integrate Auto3DSeg training into the MONAILabel extension.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Objective A. Implement Auto3DSeg into a new 3D Slicer extension.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

We have great starting code as well as 2 ready-to-use models from Andres Diaz-Pinto. We will build on that.
In addition, we will train a lung lobe and airway model which should be available at the PW.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Andras developed a new extension MONAI Auto3DSeg
2. It can be downloaded via the extension manager.
3. Andres created 3 Auto3DSeg models already to enable direct inference with CT datasets
   ![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/10bcc813-c4e6-4e6a-ae8e-0d3cf51b0ab3)

4. The best models get automatically downloaded for each process
5. They will be improved with further training
6. In future, we attempt to enable your own training of Auto3DSeg models in MONAILabel.

   ![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/ea045d96-ab84-4469-86e0-acbd7bec01ad)

2/24/2024

Andres and Andras achieved relevant progress working on the extension during the last weeks:

The extension
- is now much faster
- has a wider range of available models
- includes low res models which use less VRAM
- some models were split into smaller pieces to be able to run them on 8 GB VRAM or CPU
- The overall quality of the models was largely improved

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/8bfe7c55-045b-45f9-824f-513f4b9ea0fa)

(using NVIDIA RTX Geforce 3070 Ti)

We´ll continue to add relevant models.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Algorithm Generation:
![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/286ae610-4ab7-4352-ac80-ab4d2c4773c1)

Simulate a dataset and Auto3D datalist using MONAI functions:
![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/6208629d-5a2f-4c39-a98a-0b0a98367546)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

<https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg#performance-benchmarking>
