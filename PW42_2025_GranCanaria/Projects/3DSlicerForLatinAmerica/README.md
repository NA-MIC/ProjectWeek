---
layout: pw42-project

permalink: /:path/

project_title: 3D Slicer for Latin America
category: Infrastructure

key_investigators:
- name: Sonia Pujol
  affiliation: Brigham and Women's Hospital, Harvard Medical School
  country: USA

- name: Luiz Murta
  affiliation: Universidade de São Paulo
  country: Brazil

- name: Douglas Samuel Gonçalves
  affiliation: Universidade de São Paulo
  country: Brazil

- name: Lucas Sanchez Silva
  affiliation: Universidade de São Paulo
  country: Brazil

- name: Paulo Eduardo de Barros Veiga
  affiliation: Universidade de São Paulo
  country: Brazil

- name: Paulo Guilherme Pinheiro Pereira
  affiliation: Universidade de São Paulo
  country: Brazil

- name: Mirela Teixeira Cazzolato
  affiliation: Universidade de São Paulo
  country: Brazil

- name: Adriana Herlinda Vilchis González
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Enrique Hernández Laredo
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Victor Manuel Montaño Serrano
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Monserrat Ríos-Hernández
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Valeria Gómez Valdes
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Juan Carlos Avila Vilchis
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Fatou Bintou Ndiaye
  affiliation: University Cheikh Anta Diop
  country: Senegal

- name: Mohamed Alalli Bilal
  affiliation: University Cheikh Anta Diop
  country: Senegal

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

The project aims to empower the biomedical research community in Latin America by localizing 3D Slicer to Spanish and Portuguese and improving tutorial localization infrastructure.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Solve the existing GitHub issues related to core functionalities of the extension Tutorial Maker. For example, not handling clicks or widget resizing during annotations blocks the user from finishing the tutorial.
2. Solve the existing GitHub issues raised during the African team tests. For example, buttons in the annotator that don't work properly, pdf exporter breaking the original format.
3. Fix problems in existing tutorials. For example, some missing slides in the PDF.
4. Improve the code's legibility and the extension's performance.
5. Collect more feedback from the users on the event.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. All the tasks (issues) are designated to pairs in the team, during the project week we will keep in continuous touch to solve each of these problems and any problem raised during feedback in the project week.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Fix core-related issues

| Old | New |
| --- | --- |
| ![image](https://github.com/user-attachments/assets/61f238dc-0352-403d-b909-ca03591524f0) | ![one](https://github.com/user-attachments/assets/d56da455-7fc8-46b5-afc5-7a591edd15d6) |
| ![image](https://github.com/user-attachments/assets/65cd72c9-ddc4-4511-9b05-8bd0e6e31a9f) | ![image](https://github.com/user-attachments/assets/9a2bf575-c500-42f2-92df-e42d658f60fa) |

2. Code improvement

- Creation of a GitHub Action to run the tests of the extension on pushing main or develop

| Old | New |
| --- | --- |
| ![image](https://github.com/user-attachments/assets/34c7d441-1039-4105-906f-5054b79bbdfd) | ![image](https://github.com/user-attachments/assets/bde1d39d-b2e5-47be-a137-66fc30e9f08c) |

- Review the approach FileMDHTML to export HTML and print PDF. [Commit](https://github.com/SlicerLatinAmerica/SlicerTutorialMaker/commit/4ae712601ffed42a7d39b96dc89f2212dd4caf22)
- Review the TutorialGUI approach to open Annotator and manipulate the events more reliably. Adding new features.
![ArrowShowcase](https://github.com/user-attachments/assets/aa88cd04-5584-4aa9-957c-92712fecab24)

![image](https://github.com/user-attachments/assets/81f8f7b9-77bc-426d-b564-7035c7449834) | ![image](https://github.com/user-attachments/assets/91e9c0dc-dd5b-4f59-ba4d-ddf9480ba6a7)

- Add new features like the ability to select and add screenshots more than one time
![image](https://github.com/user-attachments/assets/4181dbc5-cf40-4b28-8dc5-7b9a1360b51b)


3. Use case (WIP)

- BoneReconstructionPlannerTutorial - Mauro Dominguez [Repository](https://github.com/SlicerLatinAmerica/TestSlicerTutorials/blob/feature/add_bone_reconstruction_planner_tutorial/Tutorials/BoneReconstructionPlannerTutorial/BoneReconstructionPlannerTutorial.py)

![image](https://github.com/user-attachments/assets/54dd3cd7-6457-4dc7-a266-da222b813018)
![image](https://github.com/user-attachments/assets/f5bf233f-5b60-4c22-bef0-560afd150a9e)
![image](https://github.com/user-attachments/assets/8e073f1a-2d8c-4de5-9a63-1c05600610e9)

5. Tutorials manually translated

| Slicer Developer Tutorial: Programming in Slicer. S. Pujol, S. Pieper | Segmentation for 3D printing. A. Nagy, C. Pintér |
| --- | --- |
| [Portuguese](https://slicerlatinamerica.github.io/media/Tutorials/Slicer5_Programando%20no%20Slicer_SPujol-SPieper.pdf) |  [Portuguese](https://slicerlatinamerica.github.io/media/Tutorials/Segmentation3DPrinting-ANagy-CPinter_pt-BR.pdf) |
| [Spanish](https://slicerlatinamerica.github.io/media/Tutorials/Slicer5_ProgrammingTutorial_es-419.pdf) | [Spanish](https://slicerlatinamerica.github.io/media/Tutorials/SegmentationFor3DPrinting_es.pdf) |

# Nexts Steps

1. Merge all the work that was created during the PW
2. Discuss and define what will be generated to the repositories
3. Discuss and define how the other extensions will extends TutorialMaker to create tutorials

# Illustrations

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[TutorialMaker](https://github.com/SlicerLatinAmerica/SlicerTutorialMaker)
The repository with all the code related to the extension. Feel free to open an issue or contribute! You can also download using the Extension Manager in the preview version of 3D Slicer.
