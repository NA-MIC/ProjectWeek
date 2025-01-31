---
layout: pw42-project
permalink: /:path/
project_title: Builds of Slicer for ARM-based systems Mac and Linux
category: Infrastructure

key_investigators:
- name: Andres Diaz-Pinto
  affiliation: NVIDIA
  country: UK
- name: Steve Pieper
  affiliation: Isomics
  country: USA
- name: Rafael Palomar
  affiliation: OUH
  country: Norway
- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA
- name: Andras Lasso
  affiliation: Queen's University
  country: CA
- name: Mauro I. Dominguez
  affiliation: Independent
  country: Argentina  
- name: Robin Peretzke
  affiliation: German Cancer Research Center
  country: Germany  
---

# Project Description

Investigate, document, and fix any issues related to building Slicer from source on ARM-based systems (e.g. Apple silicon or Nvidia linux systems).

During the Slicer Week, we plan to have a working 3D Slicer version on ARM architecture. This version will facilitate the use of Slicer for volume rendering and access to other modules with segmentation AI models for interaction with radiology copilots. We'll have virtual (ssh) access to an IGX box for testing this and finding the gaps for a complete solution to ARM version of 3DSlicer.

## Objective

1. Achieve a functional 3D Slicer build on ARM architecture, specifically targeting Apple silicon and Nvidia linux systems.
2. Identify and resolve issues related to volume rendering, segmentation AI models, and radiology copilot interactions on ARM-based systems.

## Approach and Plan

1. Set up virtual (ssh) access to an NVIDIA IGX box for testing and development.
2. Compile and build 3D Slicer from source on the ARM-based system.
3. Test volume rendering capabilities and identify any performance issues or incompatibilities.
4. Integrate and test segmentation AI models on the ARM version of 3D Slicer.
5. Evaluate the interaction between 3D Slicer and radiology copilots on the ARM architecture.
6. Document all encountered issues, workarounds, and solutions.
7. Collaborate with the Slicer community to implement necessary fixes and optimizations.

## Progress and Next Steps

1. Initiated project planning and team coordination.
2. Secured access to NVIDIA IGX box for development and testing purposes.
3. Began preliminary research on existing ARM-related issues in the Slicer GitHub repository.
4. Environment setup on the NVIDIA IGX box.
5. Build scripts published at https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e
6. Slicer built on Ubuntu 22.04 (aarch64) ✨✅

```
$ uname -a
Linux demos-NVIDIA-IGX-Orin-Development-Kit 5.15.0-1012-nvidia-tegra-igx #12-Ubuntu SMP Wed Apr 24 15:57:28 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux
```

```
$ cd ~/Projects
$ ./build-CTKAppLauncher.sh
[...]
[100%] Built target CTKAppLauncher
Install the project...
-- Install configuration: "Release"
-- Up-to-date: /home/demos/Projects/CTKAppLauncher-install/bin/CTKAppLauncher
-- Up-to-date: /home/demos/Projects/CTKAppLauncher-install/CMake/ctkAppLauncher.cmake
-- Up-to-date: /home/demos/Projects/CTKAppLauncher-install/CMake/ctkAppLauncher-configure.cmake
-- Up-to-date: /home/demos/Projects/CTKAppLauncher-install/bin/CTKAppLauncherSettings.ini.in
-- Up-to-date: /home/demos/Projects/CTKAppLauncher-install/./CTKAppLauncherConfig.cmake

$ ./build-tbb.sh
[...]
[100%] Built target tbb
Install the project...
-- Install configuration: "Release"
-- Up-to-date: /home/demos/Projects/tbb-install/lib/libtbb.so.12.15
-- Up-to-date: /home/demos/Projects/tbb-install/lib/libtbb.so.12
-- Up-to-date: /home/demos/Projects/tbb-install/lib/libtbb.so
[...]

$ ./build-Slicer.sh
[...]
[ 99%] No install step for 'Slicer'
[ 99%] Forcing configure step for 'Slicer'
[100%] Completed 'Slicer'
[100%] Built target Slicer
```

Next steps:
- Begin testing basic functionality and identify initial challenges.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

# Main Challenges

Building and running 3D Slicer on the NVIDIA IGX box (ARM architecture) involves several significant challenges:

1. **Qt Dependency**: There are no official Qt binary packages for arm64, requiring developers to build Qt from source. This process can trigger dependency errors and may force disabling of components such as QtWebEngine and QtPDF.

2. **VTK Compilation**: VTK needs to be built with Qt and Python support on ARM, adding extra complexity to the build process.

3. **CUDA Library Compatibility**: Some Holoscan applications that rely on CUDA have shown instability due to library differences, leading to crashes when deallocating memory.

4. **Long-term Maintenance**: Maintaining these custom builds for ARM devices can pose a significant long-term effort unless a broader community helps to support and test the codebase.

5. **Dependency Management**: Building Qt with necessary plugins like xcb for X11 support requires installing additional dependencies that are not always well-documented.

6. **Component Disabling**: Some Qt components may need to be disabled due to build errors, potentially limiting functionality.

**Note:** 3D Slicer works on Mac with ARM architecture (Apple Silicon) primarily due to Apple's Rosetta 2 translation layer, which allows x86_64 applications to run on ARM-based Macs36. This translation layer is not available on other ARM-based architectures like the NVIDIA IGX. While 3D Slicer is not yet natively compiled for ARM on Mac, the Rosetta 2 emulation is efficient enough to provide good performance6. In contrast, other ARM-based systems like the IGX would require a native ARM build of 3D Slicer, which is not yet available.

## Building Slicer in [Ubuntu 22.04 (x86)](https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-22-04-jammy-jellyfish):

This section provides instructions for building Slicer on x86 systems:

0. Install the development tools and the support libraries:

```console
sudo apt update && sudo apt install git build-essential \
  cmake cmake-curses-gui cmake-qt-gui \
  libqt5x11extras5-dev qtmultimedia5-dev libqt5svg5-dev qtwebengine5-dev libqt5xmlpatterns5-dev qttools5-dev qtbase5-private-dev \
  libxt-dev libssl-dev
```
![running_x86_commands](https://github.com/user-attachments/assets/ecc6630f-5c72-432a-bdd2-02d66d151b73)



1. Create a folder called Slicers where you will clone the Slicer repository and create the build directory:
 
```console
mkdir ~/Slicers
cd ~/Slicers
```

2. Clone the Slicer repository:

```console
git clone https://github.com/Slicer/Slicer.git
```
3. Locate the Qt installation. It is typically found in /opt/qt/. For example: /opt/qt/5.15.2/gcc_64/lib/cmake/Qt5

4. Run the following bash commands to set up the environment and build Slicer:

```console
# Set variables
export Slicer_RELEASE_TYPE=Stable
export SLICER_CODE_PATH=/home/$USER/Slicers/Slicer
export SLICER_SUPERBUILD_PATH=/home/$USER/Slicers/SlicerR
export SLICER_BUILD_PATH=$SLICER_SUPERBUILD_PATH/Slicer-build
export NUMBER_OF_SLICER_COMPILATION_JOBS=2

# Create build directory
mkdir -p $SLICER_SUPERBUILD_PATH
cd $SLICER_SUPERBUILD_PATH

# Configure Slicer build
cmake -DCMAKE_BUILD_TYPE:STRING=Release -DQt5_DIR:PATH=/opt/qt/5.15.2/gcc_64/lib/cmake/Qt5 $SLICER_CODE_PATH

# Build Slicer
time make -j$NUMBER_OF_SLICER_COMPILATION_JOBS
```

# Background and References

The effort to build 3D Slicer on ARM architecture is part of a broader initiative to expand the platform's compatibility and leverage the capabilities of modern ARM-based systems. This project aligns with the growing trend of ARM adoption in various computing environments, from mobile devices to high-performance computing.

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- [Slicer ARM-related Issues](https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+arm)
- [NVIDIA IGX Platform](https://www.nvidia.com/en-gb/edge-computing/products/igx/)
