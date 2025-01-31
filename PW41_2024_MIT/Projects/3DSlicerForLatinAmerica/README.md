---
layout: pw41-project

permalink: /:path/

project_title: 3DSlicerForLatinAmerica
category: Infrastructure
presenter_location: Online

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

- name: Juan Carlos Avila Vilchis
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Vianney Muñoz Jiménez
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Mariana Alvarez-Carvajal
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Valeria Gómez Valdes
  affiliation: Universida Autónoma del Estado de México
  country: Mexico

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Steve Pieper
  affiliation: Isomics Inc.
  country: USA

---

# Project Description

The goal of this project is to empower the biomedical research community in Latin America by localizing 3D Slicer to Spanish and Portuguese and improving tutorial localization infrastructure.


## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Internationalize the Tutorial Maker module
2. Translate the step-by-step Tutorial Maker guide to Portuguese and Spanish.
3. Upgrade the Slicer tutorials in Portuguese with the Portuguese version of Slicer.
4. Solve functional issues in the Tutorial Maker repository, such as changing the infrastructure to a more human-readable one.
5. Translate MonaiLabel extension to Portuguese and Spanish.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Verify if the Qt widgets are all marked as translatable and enclose the strings with the tr class. Also, verify the necessary configuration to add these strings in Weblate.
2. The Slicer for Latin America translation team will work on translating the user manual and tutorials to guarantee that the Tutorial Maker module can be used by English, Portuguese, and Spanish users.
3. The Slicer for Latin America engineering team will work with the Slicer developer community to solve the issues opened in the repository.
4. The Slicer for Latin America translation team will work on translating the MonaiLabel extension to Spanish and Portuguese using Slicer Weblate

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. An incomplete ts file is committed to the SlicerLanguageTranslations repository—[Link to the Pull Request](https://github.com/Slicer/SlicerLanguageTranslations/pull/543/commits). Still need to mark some errors as translatable.
2. Slicer for Latin America session

   <img width="666" alt="SlicerLA_PW41" src="https://github.com/NA-MIC/ProjectWeek/assets/1847492/56024eb3-7e6d-43f5-b11b-5e65a2711602">
3. Tutorial Maker Demo
<img width="1065" alt="Screenshot 2024-06-27 at 11 41 50 PM" src="https://github.com/NA-MIC/ProjectWeek/assets/1847492/f25354ef-fe4f-47b1-8979-134d738df279">

Progress in resolving functional issues in the Tutorial Maker repository, such as changing the infrastructure to a more human-readable one: During the sessions a Demo of the Tutorial Maker module was shown, in which a stable version of the module was shown, where problems were solved, such as larger quantities in the drawing directions, elimination of undesirable effects of flashing on the screen when generating images, and the incorporation of the function of generating the tutorial in PDF format, previously limited to HTML and Md.

4. This week has started the translation of the step-by-step Tutorial Maker guide into Spanish for Latin America. The goal is that this new module allows the creation of Tutorials for every user of the software. The progress of this translation until now is 80%.

5. Tutorial Maker creates three files with the same information (images, annotations, descriptions): markdown, html and pdf

    <img width="150" alt="SlicerLA_PW41" src="https://github.com/NA-MIC/ProjectWeek/assets/111019594/9567deee-80c9-41c4-a345-49c2013c87bf">

PDF example:

<img width="449" alt="pdf" src="https://github.com/NA-MIC/ProjectWeek/assets/111019594/392f4029-fc58-4e9c-93de-e7073fe14360">

6. Translation of the tutorials to Portuguese with the interface in Portuguese.
![image](https://github.com/NA-MIC/ProjectWeek/assets/28208639/1158351c-46b0-48a9-9728-755e47cab2ee)

7.

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
### GitHub Repository

[TutorialMaker](https://github.com/SlicerLatinAmerica/TutorialMaker)
