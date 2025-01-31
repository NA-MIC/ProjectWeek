Back to [Projects List](../../README.md#ProjectsList)

# Systole OS: an operating system for development/deployment of medical devices.

## Key Investigators

- Rafael Palomar (Oslo University Hospital and NTNU, Norway)
- Andras Lasso (Queen's University, Kingston, Canada)
- Steve Pieper (Isomics Inc., Cambridge, MA, USA)
- Jean-Christophe Fillion-Robin (Kitware Inc., Carrboro, NC, USA)
- Sam Horvath (Kitware Inc.)

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

## Objective

In PW37 we aim to take the first steps towards the creation of the Systole
overlay, which is a set of packages containing an installable version of
3D Slicer and its dependences.

## Approach and Plan

1. Project discussion
1. Review of dependencies and `-DSlicer_SUPERBUILD=OFF`
1. Development of the packages for the dependencies and 3D Slicer
1. Development of the packages for the 3D Slicer default modules

## Progress and Next Steps

First full installation of a minimal 3D Slicer!

[![asciicast](https://asciinema.org/a/505170.svg)](https://asciinema.org/a/505170)

- SystoleOS gentoo overlay has been made public at [https://github.com/SystoleOS/gentoo-overlay](https://github.com/SystoleOS/gentoo-overlay).

- Simple 3D Slicer installation with a `-DSlicer_SUPERBUILD=OFF` approach (-python). There are still some glitches and workarounds even for the simplest version, but this shows the feasibility of the project.

Systole OS, by nature, is a continuous project that needs to keep up with the developments of 3D Slicer and the developments of the underlying software packages itself. It is necessary to establish infrastructure for testing that can help us on the development process (next step). In addition we need to establish infrastructue to support a community documentation, containers, communication channels, etc (next step).

When it comes to the development of Systole OS itself, the first efforts will go on the direction of fixing bugs, enable new configurations of 3D Slicer (e.g, +python). To engage more users, it is important that Systole OS shows utility. We are planning to integrate a Slicer custom application (to be decided) as a deployment prototype.

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
