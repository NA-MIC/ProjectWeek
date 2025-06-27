---
layout: pw43-project

permalink: /:path/

project_title: Transition Slicer Default Build from Qt5 to Qt6
category: Infrastructure

key_investigators:

- name: Jean-Christophe Fillion-Robin
  affiliation: Kitware
  country: USA

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: James Butler
  affiliation: Revvity
  country: USA

- name: Hans Johnson
  affiliation: University of Iowa
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project focuses on updating Slicer's build system, dependencies, and related infrastructure to support building, packaging, and distributing Slicer with Qt6.

This effort lays the groundwork for supporting native builds on macOS ARM systems.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Ensure all Slicer dependencies can be built with Qt6.
2. Enable building Slicer itself against Qt6.
3. _Tentative_: Update infrastructure and build environments to support packaging and continuous integration with Qt6 builds.




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. **Identify Suitable Qt6 Version**: Evaluate supported Qt6 versions to determine the most compatible and stable version for Slicer (tentatively targeting Qt 6.9).

2. **Test Qt6 Compatibility of Dependencies**: Build Slicer’s external dependencies with Qt6, document any issues encountered, and work toward resolving them.

3. **Enable Qt6 Build of Slicer**: Support configuring Slicer with `Slicer_REQUIRED_QT_VERSION=6.9` (or selected version) to enable Qt6-based builds.

4. **Update Infrastructure and CI for Qt6** (_Tentative_)
   - Update packaging scripts and build environments (e.g., Docker images, GitHub Actions runners) to support Qt6-based builds.
   - Add CI jobs to test, build, and package Slicer against Qt6 on supported platforms (Linux, Windows, macOS ARM/x86_64).
   - Validate the creation of functioning Slicer packages built with Qt6.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

* Target Qt Version: Qt 6.9
* Initial focus is on enabling Slicer and its dependencies to build on macOS arm64 with Qt6. Work is ongoing across the main Slicer repository, key dependencies, and related infrastructure.

### Slicer Updates

* CMake and Build System
  * [PR-8501](https://github.com/Slicer/Slicer/pull/8501): ✅ Update minimum required CMake version from 3.16.3 to 3.20.6
  * [PR-8491](https://github.com/Slicer/Slicer/pull/8491): ⏳ Build cmake4 WORK IN PROGRESS WIP

* Dependency Updates
  * teem
    - [PR-8500](https://github.com/Slicer/Slicer/pull/8500): ✅ Update teem from r6245 to r7265
    - [PR-8503](https://github.com/Slicer/Slicer/pull/8503): ✅ Update teem to fix windows build
  * rapidjson
    - [PR-8502](https://github.com/Slicer/Slicer/pull/8502): ✅Update RapidJSON to latest revision
    - [PR-8508](https://github.com/Slicer/Slicer/pull/8508): ✅ Fix configuration on Windows by updating RapidJSON project installation
    - Pull requests contributed to upstream `Tencent/rapidjson`: ⏳ [PR-2343](https://github.com/Tencent/rapidjson/pull/2343), ⏳ [PR-2344](https://github.com/Tencent/rapidjson/pull/2344)
  * OpenSSL
    - [PR-8504](https://github.com/Slicer/Slicer/pull/8504): ✅ OpenSSL 1.1.1w is needed to fix missing include
    - [PR-8513](https://github.com/Slicer/Slicer/pull/8513): ✅ Fix OpenSSL 1.1.1w build on macOS with non-system zlib

* Compiler Warning Fixes
  * [PR-8509](https://github.com/Slicer/Slicer/pull/8509): ✅ Fix deprecated declarations related to vtkStdString
  * [PR-8510](https://github.com/Slicer/Slicer/pull/8510): ✅ Fix unused variable warning in qMRMLSortFilterColorProxyModel

* Identified issues
  * [PR-8515](https://github.com/Slicer/Slicer/pull/8515): ✅ Ensure deepcopy is propagated in vtkMRMLSequenceBrowserNode::CopyContent

### QtTesting Updates

* ⏳ Support for Qt6 being finalized

### PythonQt Updates

* ⏳ [commontk/PythonQt PR-90](https://github.com/commontk/PythonQt/pull/90), ⏳ [MeVisLab/pythonqt PR-269](https://github.com/MeVisLab/pythonqt/pull/269)
  - Qt6 Porting: Updated code to support Qt6, including replacing deprecated QVariant::Type with QMetaType and adding version checks for Qt5/Qt6 compatibility.
  - C++17/20 Modernization: Refactored code to use modern C++ features as required by newer Qt versions (e.g., constexpr, noexcept, alignas, etc.).
  - Compiler Detection Updates: Enhanced and updated compiler detection macros in qcompilerdetection.h for better support of recent compilers and platforms.
  - Warning and Attribute Macros: Improved handling of compiler warnings and attributes, including support for new C++ attributes like [[nodiscard]], [[maybe_unused]], and [[deprecated]].
  - Platform and Feature Checks: Added or updated macros for platform-specific and feature-specific checks, ensuring better cross-platform compatibility.
  - General Maintenance: Bug fixes, code cleanup, and improved documentation/comments throughout the codebase.

### simplecpp Updates (used by PythonQt wrapper generator)

* ⏳ [PR-448](https://github.com/danmar/simplecpp/pull/448): ENH: Add support to find Headers in Apple Frameworks


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


* [Slicer Issue](https://github.com/Slicer/Slicer/issues/6388)
* [Build Instructions PW43](https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/SlicerBuildInstructionUpdates/)

