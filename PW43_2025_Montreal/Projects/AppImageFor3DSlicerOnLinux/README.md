---
layout: pw43-project

permalink: /:path/

project_title: AppImage, Flatpak, etc. for packaging 3D Slicer on Linux
category: Infrastructure

key_investigators:
- name: Benjamin Zwick
  affiliation: University of Western Australia
  country: Australia
---

# Project Description

<!-- Add a short paragraph describing the project. -->

This project aims to create a portable AppImage distribution of 3D Slicer for Linux systems. AppImage is a universal software package format that allows applications to run on various Linux distributions without installation, making 3D Slicer more accessible and easier to deploy across different Linux environments. The project will streamline the distribution process and reduce dependency conflicts that users often encounter when installing 3D Slicer on different Linux distributions.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. **Objective A. Create a functional 3D Slicer AppImage** that bundles all necessary dependencies and libraries to run 3D Slicer on major Linux distributions without requiring system-wide installation.
2. **Objective B. Establish an automated build pipeline** for generating AppImages from 3D Slicer releases, ensuring consistency and maintainability for future versions.
3. **Objective C. Validate cross-distribution compatibility** by testing the AppImage on multiple Linux distributions (Ubuntu, Fedora, openSUSE, Arch Linux, etc.) to ensure broad compatibility.
4. **Objective D. Document the build process and usage instructions** to enable community contributions and provide clear guidance for end users.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. **Analyze 3D Slicer's dependency requirements** and identify all libraries, Qt components, Python modules, and system dependencies needed for a standalone package.
2. **Set up AppImage build environment** using linuxdeploy tools and configure the build process to bundle 3D Slicer with all required dependencies.
3. **Create AppImage recipe and build scripts** that can automatically generate the AppImage from existing 3D Slicer builds, including proper library linking and Qt plugin configuration.
4. **Implement continuous integration pipeline** to automatically build AppImages for new 3D Slicer releases using GitHub Actions or similar CI/CD platforms.
5. **Test the generated AppImage** across different Linux distributions in virtual machines or containers to verify functionality and identify compatibility issues.
6. **Optimize AppImage size and performance** by removing unnecessary components and ensuring efficient library bundling without compromising functionality.
7. **Create comprehensive documentation** including build instructions, troubleshooting guide, and user installation/usage documentation.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Learnt that AppImage is not very suitable, and Flatpak is difficult to get working with e.g. the Extension Manager.
2. Decided to use existing `make package` for now.
3. Updated the [SlicerBuildEnvironment](https://github.com/Slicer/SlicerBuildEnvironment) instructions for building 3D Slicer, Slicer Custom Apps and Slicer extensions (See the [Slicer Build Instruction Updates project](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/SlicerBuildInstructionUpdates/) for more details).

TODO
<!-- 1. **Initial research and planning phase completed** - analyzed AppImage format requirements and 3D Slicer's current Linux build process. -->
<!-- 1. **Set up development environment** with necessary AppImage tools (linuxdeploy, appimagetool) and tested basic AppImage creation workflow. -->
<!-- 1. **Identified key technical challenges** including Qt plugin loading, Python environment isolation, and large file size optimization requirements. -->
<!-- 1. **Next: Begin creating initial AppImage prototype** focusing on core 3D Slicer functionality and basic dependency bundling. -->
<!-- 1. **Next: Establish testing framework** for validating AppImage functionality across target Linux distributions. -->

# Illustrations
<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

*Screenshots and demonstration videos will be added as the project progresses, showing the AppImage creation process and cross-platform testing results.*

# Background and References
<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

## Background

### Related Previous Projects

- [Slicer Flatpak - Project Week 39 (Montreal, June 2023)](https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/SlicerFlatpak/)
- [Systole OS: an operating system for development/deployment of medical devices - Project Week 38 (Gran Canaria, Jan 2023](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SystoleOS/)

### 3D Slicer Community Discourse

- [Appimage - for linux systems - Support / Feature requests - 3D Slicer Community](https://discourse.slicer.org/t/appimage-for-linux-systems/35594)
- [Interest to create Flatpak for 3D Slicer, have issue with GUISupportQtOpenGL not found - Support - 3D Slicer Community](https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532/34)

## References

3D Slicer:
- [3D Slicer Official Website](https://www.slicer.org/)
- [3D Slicer GitHub Repository](https://github.com/Slicer/Slicer)
- [GNU/Linux systems — 3D Slicer documentation](https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html)
- [SlicerBuildEnvironment](https://github.com/Slicer/SlicerBuildEnvironment)

AppImage:
- [AppImage - Linux apps that run anywhere](https://appimage.org/)
- [AppImage Best Practices](https://docs.appimage.org/packaging-guide/index.html)
- [linuxdeploy - AppImage creation tool](https://github.com/linuxdeploy/linuxdeploy)

Flatpak:
- [Flatpak—the future of application distribution](https://flatpak.org/)

Misc:
- [Qt 5 Application Deployment on Linux](https://doc.qt.io/qt-5/linux-deployment.html)
- [Qt for Linux/X11 - Deployment - Qt 6](https://doc.qt.io/qt-6/linux-deployment.html)
