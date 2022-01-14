Back to [Projects List](../../README.md#ProjectsList)

# OHIF-v3 Mode Gallery

## Key Investigators

- Alireza Sedghi (OHIF)
- James Petts (OHIF)
- Erik Ziegler (OHIF)


# Project Description

`OHIF-v3` architecture has been re-designed to enable building applications that are easily extensible to various use cases (Modes) that behind the scene would utilize desired functionalities (Extensions) to reach the goal of the use case. A mode can be thought of as a viewer app configured to perform a specific task, such as tracking measurements over time, 3D segmentation, a guided radiological workflow, etc. Addition of modes enables application with many applications as each mode become a mini app configuration behind the scene.

Currently OHIF developers have to copy paste the source code of a sample Mode/Extension and edit the source code to let OHIF know about the new Mode/Extension they are developing, which has its limitations. The purpose of this project is to overcome this by enabling self-registration of Modes and Extensions and provide a ohif-cli tool to automatically generate templates and link Mode/Extension(s) internally.

## Objectives

- Create a CLI tool (similar to create-react-app)

  - Commands to include:
    - create-mode, create-extension : for generating template extension and mode
    - install-mode, install-extensions : for installing mode/extensions to OHIF (either linking locally or installing published modes and extensions from npm)
    - uninstall-extension, uninstall-mode : same above but for uninstalling
    - list : list all extensions and modes that are installable in OHIF

- Update OHIF to dynamically install extensions and modes from config files rather than having to hard code their inclusion.
  - For example one could install OHIF, then a set of modes/extensions, programmatically.

Stretch Goals:
- Parse information from npm to populate the markdown of the OHIF page for installable modes and extensions.
- Versioning errors + conflict resolution for mode dependencies.
- Type the contract interfaces for extensions and modes in typescript.

Super stretch goal: type all the things

## Approach and Plan

## Progress and Next Steps

# Illustrations

We intend to showcase all modes (and hopefully extensions) that are developed for OHIF in the OHIF website.

![image](https://user-images.githubusercontent.com/7490180/149446827-ece3aa65-32a5-439d-803b-0492ad964a42.png)

Each mode will have a page explaining the usecase, and installation, along with screenshots of the mode.

![image](https://user-images.githubusercontent.com/7490180/149446888-7109ebec-a760-49dd-93cb-97073b53d9c0.png)

# Background and References
