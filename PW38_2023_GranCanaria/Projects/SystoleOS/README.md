Back to [Projects List](../../README.md#ProjectsList)

# Systole OS: an operating system for development/deployment of medical devices.

## Key Investigators

- Rafael Palomar (Oslo University Hospital and NTNU, Norway)
- Steve Pieper (Isomics Inc., Cambridge, MA, USA)

# Project Description

<!-- Add a short paragraph describing the project. -->

For more than a decade, 3D Slicer has been enabling world-class biomedical
research. The great success of 3D Slicer is now pushing the boundaries of
research, making some research groups and companies regard 3D Slicer as a viable
software for building medical devices that not only could support regular
clinical workflows but also become commercial products. While the development of
3D Slicer has been tailored towards research, its modular architecture makes the 
development of industrial prototypes possible.

The vision of Systole OS is the integration of 3D Slicer and related software (e.g,
Plus Toolkit, MONAI Label and more!) in a free and open-source operating system
based on GNU/Linux, with the aim to support the development and deployment of
medical devices. 

![Systole](systole.png)

Here are some of the features that we would like to leverage in
Systole OS:

### Cutting-edge software
  
Systole OS is based on Gentoo Linux, which follows a rolling-release model
providing up-to-date support out of box.

### Installable Slicer...

Slicer, together with all the required dependencies will be installable with a simple
command (e.g., `emerge sci-medical/slicer`). No SuperBuild! No Slicer-Launcher!

### ...and Modular Slicer

The base installation of 3D Slicer will include only the components needed to
run the application (e.g., `emerge slicer-modules/models` can be done
separately).

### Source-based

Systole OS is a **source-based** distribution, which means that all packages
will be built from source. Having the flexibility to make decisions on
compile-time allows:

   - Tighter hardware integration
   - Highly configurable packages (e.g., `flaggie sci-medical/slicer -python +opencl; emerge sci-libs/slicer` will install Slicer without python support and with opencl support)
   - Portability to hardware architectures other than amd64 (e.g., arm, risc-v).

### Extensible

Systole OS works on the Gentoo overlay system which allows you to extend the
system with your own ovelay or override packages provided by Systole.

## Objectives

The main objective for PW38 is the consolidation of the development achieved in [PW37](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/SystoleOS) in Virtual Machines and Containers; this will enable researchers and developers to test the system and contribute to its development. This objective includes the generation of documentation to get started with the project.

As secondary objectives we aim to continue advancing on the integration of 3D Slicer:
 
 - Enabling Python support
 - Porting scripted modules
 
as well as the integration of allied technologies:

 - Plus Toolkit
 - MONAI Label
 - Total Segmentator

## Approach and Plan

1. Project discussion
2. Release of the SystoleOS development VMs and Containers
2. Documentation on how to get started with SystoleOS (gentoo-overlay, containers, VMs)

## Progress and Next Steps

# Background and References
1. [SystoleOS project in PW37](https://github.com/NA-MIC/ProjectWeek/tree/master/PW37_2022_Virtual/Projects/SystoleOS)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

