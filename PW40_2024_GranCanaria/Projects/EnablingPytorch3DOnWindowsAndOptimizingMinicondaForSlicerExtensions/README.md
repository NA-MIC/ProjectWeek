---
layout: pw40-project

permalink: /:path/

project_title: Enabling PyTorch3D on Windows and Optimizing Miniconda for Slicer Extensions
category: Infrastructure
presenter_location: Online

key_investigators:

- name: Leroux Gaelle
  affiliation: University of Michigan
  country: USA

- name: Claret Jeanne
  affiliation: University of Michigan
  country: USA

- name: Cevidanes Lucia
  affiliation: University of Michigan
  country: USA

- name: Hutin Nathan
  affiliation: CPE Lyon
  country: France

- name: Allemand David
  affiliation: Kitware
  country: USA

- name: Prieto Juan Carlos
  affiliation: University of North Carolina
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project focuses on enhancing compatibility and usability in two key areas. Firstly, we aim to enable the use of PyTorch3D on the Windows platform. By leveraging the Windows Subsystem for Linux (WSL2) and a virtual Miniconda environment, we intend to bypass the traditional limitations and provide Windows users with full access to PyTorch3D's capabilities. Secondly, the project seeks to improve the integration of Miniconda with Slicer extensions. Our goal is to simplify the process of creating and managing virtual environments for Slicer extensions, thereby making the procedure more intuitive. This will not only ease the use of various analytical tools and libraries but also streamline the setup process within WSL, especially for tools incompatible with Windows. This approach aims to bridge the gap in functionality and user experience across different platforms.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Our project aims to achieve two primary objectives:

Operationalizing PyTorch3D on Windows: The first goal is to make PyTorch3D, typically unsupported on the Windows platform, fully functional. We plan to employ the Windows Subsystem for Linux (WSL2) combined with a virtual Miniconda environment to overcome this limitation. This strategy is designed to provide Windows users with complete access to the extensive functionalities of PyTorch3D.

Improving Miniconda Integration for Slicer Extensions: Our second objective is to enhance the use of Miniconda as a virtual environment manager specifically for Slicer extensions. We aim to streamline the process of creating and managing new virtual environments that are utilized by Slicer extensions, making the procedure more intuitive and user-friendly. This advancement will facilitate the use of specialized libraries required for a variety of analytical tools, which are currently not integrable directly into Slicer. Additionally, this approach will assist in the setup of Miniconda3 and the creation of new environments within WSL, particularly for tools that are not available on Windows.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

*   Investigate PyTorch3D and Windows compatibility, pinpointing causes of incompatibility.
*   Catalog PyTorch3D dependencies for WSL2 and outline requisite system configurations.
*   Operationalize PyTorch3D on Windows using WSL2 and Miniconda.
*   Develop an Automated Installer for WSL2 Setup on Windows.
*   Create a Module to Streamline Miniconda for Slicer Extensions

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

*   Completed Initial Research on PyTorch3D and WSL2 Compatibility
*   Successfully ran PyTorch3D on WSL2
*   Created an installer for WSL2
    Next Step :
*   Development of a new Slicer module for managing Miniconda

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

*No response*

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*No response*
