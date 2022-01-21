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
- [ ] WIP Documentation in the docs

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
- [x] Search NPM for ohif-extension and ohif-mode keywords within cli and show name and short description


# Illustrations

CLI illustrations

1) `create-mode` command to create a new template to write modes

  <img src="https://user-images.githubusercontent.com/7490180/150410383-ae7ee1f6-6c05-4789-ae1e-1d1b1370dcc7.png" alt="drawing" style="width:500px;"/>

It generates the template files for you to write your own mode

  ![image](https://user-images.githubusercontent.com/7490180/150410470-987847ce-0316-45d4-865d-27c03be3422f.png)

2) `create-extension` command to create a new template to write extensions.

  <img src="https://user-images.githubusercontent.com/7490180/150410874-f7e41153-4b4c-48ec-99e8-059d1c23ce8c.png" alt="drawing" style="width:500px;"/>

It also generates template for an extension

  ![image](https://user-images.githubusercontent.com/7490180/150410992-9738437d-1222-4b64-a33f-860a150cbec8.png)


3) `add-mode <mode-name>` will install any ohif-mode that has been published on npm registry and make it available on OHIF. 


  ![ezgif com-gif-maker (11)](https://user-images.githubusercontent.com/7490180/150447751-1428c1d0-26a4-4079-a99e-942ca7d11352.gif)


After installation the mode becomes avaiable. 

4) `remove-mode <mode-name>`

  ![ezgif com-gif-maker (12)](https://user-images.githubusercontent.com/7490180/150454474-1356a0d5-af35-41ec-b262-1100d077e86e.gif)

5) `search` will search in all npm packages for those who have `ohif-extension` or `ohif-mode` in their keywords and display their information

  <img src="https://user-images.githubusercontent.com/7490180/150463685-c22ace37-4daa-4489-9015-ea3d30a5812b.png" alt="drawing" style="width:600px;"/>

6) OHIF website update

Using Github GraphQL we showcase a list of modes that are published on the npm registry. 

![image](https://user-images.githubusercontent.com/7490180/149446827-ece3aa65-32a5-439d-803b-0492ad964a42.png)

The README file of each mode repository is fetched and shown in its detailed page

![image](https://user-images.githubusercontent.com/7490180/150454823-14fe56e5-0327-494a-ac36-e55f9ee88a87.png)


# Background and References
