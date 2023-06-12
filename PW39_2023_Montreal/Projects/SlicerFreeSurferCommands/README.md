---
layout: pw39-project

permalink: /:path/

project_title: Slicer FreeSurfer Commands
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:
- name: Ben Zwick
  affiliation: The University of Western Australia
  country: Australia

- name: Andy Huynh
  affiliation: The University of Western Australia
  country: Australia
 
- name: Steve Pieper
  affiliation: Isomics
  country: USA
---

# Project Description

<!-- Add a short paragraph describing the project. -->

Run [FreeSurfer](https://freesurfer.net) commands using [3D Slicer](https://www.slicer.org)'s graphical user interface.

For example:
- [mri_watershed - strip skull and other outer non-brain tissue](https://surfer.nmr.mgh.harvard.edu/fswiki/mri_watershed)
  ```
  mri_watershed -brainsurf surface.vtk mri-t1.mgz stripped.mgz
  ```
  Note that FreeSurfer uses mgz file format.

- [SynthStrip: Skull-Stripping for Any Brain Image](https://surfer.nmr.mgh.harvard.edu/docs/synthstrip/)
  ```
  mri_synthstrip -i input -o stripped -m mask --no-csf
  ```

- [SynthSeg: Segmentation of brain MRI scans](https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSeg)
  ```
  mri_synthseg --i <input> --o <output> [--parc --robust --fast --vol <vol> --qc <qc> --post <post> --resample <resample> --crop <crop> --threads <threads> --cpu --v1 --ct]
  ```
  Note that SynthSeg is a [Python package](https://github.com/BBillot/SynthSeg) that can be installed without FreeSurfer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Complete the development of existing modules based on Slicer user and developer feedback.
2. Develop additional modules for other commands (e.g. SynthSeg).
3. Package modules as an installable 3D Slicer extension.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Demonstrate and get feedback on the use and implementation of the existing modules from Slicer users and developers.
2. Discuss the implementation of the modules with Slicer developers (in particular the use of CLI vs scripted Python modules for this application).
3. Modify modules based on feedback from Slicer developers.
4. Complete the [New extension checklist](https://github.com/SlicerCBM/SlicerFreeSurferCommands/issues/1).

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Developed Python scripted and CLI modules for FreeSurfer's SynthStrip command for skull stripping.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

FreeSurfer SynthStrip Skull Strip
![FreeSurfer SynthStrip Skull Strip](https://raw.githubusercontent.com/SlicerCBM/SlicerFreeSurferCommands/147729c2976d3a4ab6ed95c908b4973bcf330aee/Screenshot01.png)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Software repository: <https://github.com/SlicerCBM/SlicerFreeSurferCommands>

FreeSurfer website: <https://freesurfer.net/>

Similar extensions for 3D Slicer:
- [SlicerFreeSurfer](https://github.com/PerkLab/SlicerFreeSurfer)
- [SlicerNeuroSegmentation](https://github.com/HOA-2/SlicerNeuroSegmentation)
