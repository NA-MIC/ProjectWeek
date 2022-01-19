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

- Create a CLI tool for making new extensions/modes (similar to e.g. create-react-app), and automagically installing extensions/modes from npm and including them in the source.
  - Commands to include:
    - create-mode, create-extension : for generating template extension and mode
    - add-mode, add-extension : for adding mode/extensions to OHIF (either linking locally or installing published modes and extensions from npm)
    - remove-extension, remove-mode : same above but for removing
    - list : list all extensions and modes that are installed in OHIF
- Update OHIF to dynamically install extensions and modes from config files rather than having to hard code their inclusion.
  - For example one could install OHIF, then a set of modes/extensions, programmatically.
- Parse information from npm to populate the markdown of the OHIF page for installable modes and extensions.

Stretch Goals:

- Versioning errors + conflict resolution for mode dependencies.
- Installing a mode installs required extensions.
- Type the contract interfaces for extensions and modes in typescript.

Super stretch goal: type *all* the things

## Approach and Plan

Complete all of the primary objectives as fast as possible and then play with the stretch goals.

## Progress and Next Steps

### Primary Goals

Core:
- [x] Self registering extensions from configuration JSON (dynamically build JavaScript required in node and inject these files at build time ).
- [x] Basic CLI tool codebase.
- [x] Basic working create-mode command.
- [x] Basic working create-extension command.
- [x] Basic working add-mode, remove-mode commands.
- [x] Basic working add-extension, remove-extension commands.
- [x] Basic list command.
- [x] Test CLI tools with actual extensions.

Gallery
- [ ] WIP Example mode and extension + publish to NPM.
- [x] Create mode galery page which consumes markdown files to generate a page with a title, description, dependencies, images and copyable install commands.


### Stretch Goals

Stretch Goals

Core:
- [x] Installing a mode installs required extensions (not versioned).
- [ ] Augment mode schema to optionally specify semantic version for required ohif-extensions.
- [x] Automatically download extensions of correct version when installing modes.
- [ ] WIP Verify that npm packages fetched by CLI are _actually_ conforming to extensions/modes so we don't just cross our fingers.
- [ ] Error handling for extension conflicts.
- [ ] Error handling for missing extensions.
- [ ] Type mode and extension schema and make these types publically available somewhere.
- [ ] Add the type contracts to the templates produced by ohif-cli create-extension and ohif-cli create-mode.

Gallery:
- [x] Create "whitelist" for extensions.
- [x] Parse information from npm repo for whitelisted extensions to populate ohif-modes gallery page.


# Illustrations

We intend to showcase all modes (and hopefully extensions) that are developed for OHIF in the OHIF website.

![image](https://user-images.githubusercontent.com/7490180/149446827-ece3aa65-32a5-439d-803b-0492ad964a42.png)

Each mode will have a page explaining the usecase, and installation, along with screenshots of the mode.

![image](https://user-images.githubusercontent.com/7490180/149446888-7109ebec-a760-49dd-93cb-97073b53d9c0.png)

# Background and References
