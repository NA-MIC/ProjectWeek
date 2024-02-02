---
layout: pw40-project

permalink: /:path/

project_title: 'aeva: Annotation and Exchange of Virtual Anatomy'
category: Quantification and Computation
presenter_location: In-person

key_investigators:

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: David Thompson
  affiliation: Kitware
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Representation of anatomy in a virtual form is at the heart of clinical decision making, biomedical research, and medical training. Virtual anatomy is not limited to description of geometry but also requires appropriate and efficient labeling of regions - to define spatial relationships and interactions between anatomical objects; effective strategies for pointwise operations - to define local properties, biological or otherwise; and support for diverse data formats and standards - to facilitate exchange between clinicians, scientists, engineers, and the general public. Development of aeva, a free and open source software package (library, user interfaces, extensions) capable of automated and interactive operations for virtual anatomy annotation and exchange, is in response to these currently unmet requirements.

aeva (annotation and exhange of virtual anatomy) is a software suite designed to work with virtual anatomy in various forms. With aeva, one can navigate anatomical information that may be in the form of images (DICOM, NIfTI), surface meshes (stl, ply, vtk) and as volume meshes (vtk, med, exodus). aeva aims to provide import/export of anatomy in various formats and annotation by selecting regions and defining attributes. Templating of annotation can be achieved with simple schemas, e.g. one designed for the knee joint.

aeva software suite currently consists of:

**aevaSlicer** aevaSlicer will be familiar to users of Slicer. The interface is customized and new features have been added to accommodate a workflow amenable to generation of surface and volume meshes of anatomy from medical images.

**aevaCMB** aevaCMB will be familiar to users of ParaView and Computational Model Builder. The interface is customized and new features have been added to support operations for import and export of anatomical representations and for annotation (template based and freeform, including a powerful set of region selection).

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Demo the current version of the aeva suite.
2.  Collect feedback and ideas.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Breakout session scheduled during the week.
2. Demo the Slicer <-> CMB interop and the new graph based linkages between surfaces

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Demo and on Tuesday went well.
2.  THe team made good progress creating new demo videos 

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Selection demo:
<video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/25040869/60c8b158-65b2-40fe-9f3a-9245c6bd60a1"
   style="max-height:640px; min-height: 200px">
 </video>

Example tutorial:

 <iframe width="560" height="315" src="https://www.youtube.com/embed/cFiqL-oqM64?si=TDUtf99SpUEQcKO5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

*   [aeva page](https://simtk.org/projects/aeva-apps)
*   [aeva readthedocs](https://aeva.readthedocs.io/en/latest/)
