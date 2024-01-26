---
layout: pw40-project

permalink: /:path/

project_title: Implement OpenUSD output into the OpenAnatomy Export extension
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Rudolf Bumm
  affiliation: KSGR Switzerland)
  country: Steve Pieper (Isomics, Inc., USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to implement the export of OpenUSD files in the OpenAnatomyExport 3DSlicer extension.
OpenUSD files can be imported into NVIDIA Omniverse.

OpenUSD, or Universal Scene Description, is an advanced framework for representing and handling 3D scenes and animations. Developed initially by Pixar, OpenUSD addresses the complexities involved in creating computer graphics for films, games, industrial engineering, and scientific experimentation, which often require managing large amounts of 3D data.

NVIDIA Omniverse is a platform designed for real-time collaboration and physically accurate simulation in 3D workflows. Essentially, it's a tool for creating and operating virtual worlds, offering a shared space for creators, designers, and engineers. Here are some key aspects of NVIDIA Omniverse:

**Real-Time Collaboration**: One of the main features of Omniverse is its ability to enable multiple users to collaborate in real-time on the same project. This is especially useful in fields like game development, architectural visualization, industrial design, and more.

**Physically Accurate Simulation**: The platform provides tools for accurate physical simulation of materials, lighting, and environments. This allows for incredibly realistic rendering and animation, useful in fields that require high-fidelity visualizations.

**Compatibility and Interoperability**: Omniverse is designed to be compatible with a wide range of software tools commonly used in 3D design and development. It supports a variety of file formats and has integrations with popular design software like Autodesk Maya, Adobe Photoshop, and others.

**AI Integration:** NVIDIA has integrated various AI capabilities into Omniverse, which can assist in tasks like object recognition, scene understanding, and even automated 3D asset generation.

**Ray Tracing and Advanced Rendering**: Powered by NVIDIA's RTX technology, Omniverse offers advanced ray tracing capabilities, resulting in highly realistic lighting and reflections.

**Use Cases and Applications**: The platform is aimed at a range of industries, including animation and film, architecture, engineering, game development, and more. It can be used for creating virtual prototypes, digital twins, animated content, and interactive experiences.

**Extension and Customization**: Developers can extend the capabilities of Omniverse through custom plugins and extensions, allowing for tailored solutions for specific industry needs.

**Cloud and Edge Computing**: Omniverse can leverage cloud and edge computing, enabling large-scale simulations and collaboration across different geographical locations.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Implement OpenUSD export in 3D Slicer

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

We want to discuss, improve and then merge the pull request for OpenAnatomy.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

Rudolf implemented the necessary code, changed the UI and created a Pull request

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

OpenAnatomy extension with new feature

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/61b24da4-0513-4e29-a499-a75c76542f5a)

NVIDIA Omniverse

![image](https://github.com/NA-MIC/ProjectWeek/assets/18140094/e86951da-fdca-486e-b204-468d2a51c223)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[Universal Scene Description documentation](https://openusd.org/release/index.html)

[Omniverse Platform](https://www.nvidia.com/en-us/omniverse/)

[Pull request](https://github.com/PerkLab/SlicerOpenAnatomy/pull/19)
