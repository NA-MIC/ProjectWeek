---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/SlicerFlatpak/README.html

project_title: 'Slicer Flatpak '
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Rafael Palomar
  affiliation: Oslo University Hospital
  country: Norway

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware, Inc.
  country: USA

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

- name: Sam Horvath
  affiliation: Kitware, Inc.
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Slicer Flatpak is a project focused on packaging the 3D Slicer software as a Flatpak. This initiative aims to offer an easy and universal way to install and run the 3D Slicer on any Linux distribution that supports Flatpak. By doing this, it seeks to reduce installation complexities and improve compatibility across different systems. The distribution of 3D Slicer as a Flatpak has potential benefits:

The convenience of having a 3D Slicer Flatpak has been long discussed in the 3D Slicer Discourse platform (<https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532>). Soon after PW38, we started a renewed discussion on the topic and a new initiative to make 3D Slicer Flatpak happen. Right now, our efforts have been focused on getting a first feasible 3D Slicer Flapak (<https://github.com/RafaelPalomar/Slicer-Flatpak/tree/feature/slicer-flatpak-generatorand> <https://github.com/RafaelPalomar/org.slicer.Slicer/tree/development>). With this project we want to consolidate this effort and discuss about the potential distribution of the 3D Slicer Flatpak.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Consolidation of 3D Slicer Flapak build infrastructure.
2.  Add support for deployment of SimpleITK along with 3D Slicer Flatpak.
3.  Testing and verification of 3D Slicer extensions.
4.  Discussion about the release model (flathub, own repository, etc.).

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Continue the current development and obtain a first version (even if with limited functionality) of the 3D Slicer Flatpak
2.  Fix a dependencies issue with SimpleITK
3.  Enable the use of the Slicer Extension manager and discuss on possibilities to deploy extensions (sandboxes vs. local)
4.  Strategy to build/deploy 3D Slicer Flatpak.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Fixed issue [Slicer-Flatpak#5](https://github.com/RafaelPalomar/Slicer-Flatpak/issues/5)  through [Slicer#7019](https://github.com/Slicer/Slicer/pull/7019) updating ITK to fix Flatpack dependency analysis.
2.  Additional analysis causing the Slicer-Flatpak python dependencies download to fail. See [Slicer-Flatpak/4#issuecomment-1588628987](https://github.com/RafaelPalomar/Slicer-Flatpak/issues/4#issuecomment-1588628987)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
