---
layout: pw42-project

permalink: /:path/

project_title: Integration of Jülich Brain Atlas to 3D Slicer EpiSTIM project
category: Segmentation / Classification / Landmarking

key_investigators:

- name: Sara Fernandez Vidal
  affiliation: Paris Brain Institute
  country: France

- name: Valerio Frazzini
  affiliation: Paris Brain Institute - APHP
  country: France

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We intend to integrate the Julich Brain Atlas into our 3D Slicer Extension dedicaated to SEEG proceuder, called EpiSTIM.

SEEG, or Stereo-Electroencephalography, is a medical procedure used to study epilepsy. It involves placing electrodes inside the brain to record its electrical activity. Neurologists use SEEG to find the exact areas of the brain causing seizures. It helps to decide the best treatment, like resection surgery or other therapies.

EpiSTIM is a software project developed to assist neurosurgeons, neurologists and researchers in image processing tasks related to SEEG surgical procedures, from surgical stereotaxic planning to postoperative studies.


The Julich-Brain Atlas (Amunts et al. Science 2020) contains cytoarchitectonic maps of more than 200 areas of the human brain including cortical areas and subcortical nuclei. This atlas is widely used in the epileptology community both in SEEG planning and postoperatively to localize intracranial activity recorded during clinical cognitive tasks or other types of tasks.

The Julich-Brain is the foundation of the [Multilevel Human Brain Atlas](https://atlases.ebrains.eu/viewer/#/a:juelich:iav:atlas:v1.0.0:1/t:minds:core:referencespace:v1.0.0:dafcffc5-4826-4bf1-8ff6-46b8a31ff8e2/p:minds:core:parcellationatlas:v1.0.0:94c1125b-b87e-45e4-901c-00daee7f2579-290/@:0.0.0.-W000.._eCwg.2-FUe3._-s_W.2_evlu..7LIx..0.0.0..1LSm), which integrates neuroanatomical features with complementary maps of the molecular architecture, function and connectivity across multiple scales and is openly available to the research community via the Human Brain Project’s research infrastructure EBRAINS.




## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective A. Describe **what you plan to achieve** in 1-2 sentences.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Download the two versions of Julich Brain Atlas (on fsaverage and MNI templates) and visualize in 3D Slicer atlas.
2. Add Julich atlas terminology to the slicer
3. Add Julich data and terminology in EpiSTIM resources.
4. Map the Julich on Subject natif  space for the planning module of the SEEG procedure
5. Add the Julich maps on the MNI visualisation of the postoperative reconstruction of the SEEG procedure


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->




I  spent the most time exploring the latest Julich dataset published on EBRAIN and adapting the formats of certain annotations, colormaps and ontologies (thanks to Murat Maga) to 3D Slicer. In the first figure you can see one of the labelsmap in the MNI template.
And in the second one the Julich anotations in the Freesurfer Fsaverage template in the pial and inflate surfaces.

#### Next Steps

I think I will prepare a 3D Slicer module to easily visualize and navigate all components, especially probability maps.

And integrate the Julich in our SEEG toolbox.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


#### Postoperative SEEG reconstruction EpiSTIM module


<img width="641" alt="Image" src="https://github.com/user-attachments/assets/92c02f99-4d94-42db-986d-2a0e7de3e2af" />

#### Jülich Brain Atlas

![Image](https://github.com/user-attachments/assets/aa403d4b-34ce-4207-863b-be3847cdb9b6)

![Image](https://github.com/user-attachments/assets/a66cfb45-207a-455e-bdc5-23a22634a3a4)


#### Jülich Brain Atlas in 3D Slicer

<img width="1658" alt="Capture d’écran 2025-01-31 à 10 17 35" src="https://github.com/user-attachments/assets/61bf5308-c105-4187-9fb1-9fc070b2c274" />


<img width="1247" alt="Capture d’écran 2025-01-31 à 10 49 16" src="https://github.com/user-attachments/assets/7baba491-e787-44e4-917d-b4a7acbf8521" />

<img width="823" alt="Capture d’écran 2025-01-31 à 10 50 37" src="https://github.com/user-attachments/assets/e2b0fcf4-260c-4782-ac5e-41f576757d1c" />


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->



[Jülich Atlas 👍](https://www.fz-juelich.de/de/inm/inm-1/aktuelles/meldungen/complete-data-package-of-julich-brain-atlas-released)


_No response_
