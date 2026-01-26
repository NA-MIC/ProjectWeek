---
layout: pw44-project

permalink: /:path/

project_title: SlicerMouseMaster - Advanced Mouse Customization for 3D Slicer
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Ben Zwick
  affiliation: The University of Western Australia and Talk2View
  country: Australia

- name: Andy Huynh
  affiliation: Talk2View
  country: Australia

---

# Project Description

<!-- Add a short paragraph describing the project. -->

SlicerMouseMaster is a 3D Slicer extension for advanced mouse customization, button remapping, and workflow optimization. It allows users to assign custom actions to extra mouse buttons (back, forward, thumb buttons), create workflow-specific presets, and use context-sensitive bindings that change based on the active Slicer module.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Submit to Extension Index
2. Add support for additional mouse models
3. Create workflow presets for common tasks
4. Improve cross-platform compatibility

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

### 1. Submit to Extension Index

- Complete submission requirements
- Test on all platforms (Linux, macOS, Windows)
- Create extension icon and screenshots

### 2. Add mouse model support

- Test with various mice from different manufacturers
- Improve button detection wizard
- Create community mouse profile database

### 3. Create workflow presets

- Segment Editor optimized preset
- Markups workflow preset
- Volume rendering preset

### 4. Cross-platform compatibility

- Test button codes across operating systems
- Document platform-specific differences
- Implement platform-specific fallbacks

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Code repository:

- <https://github.com/benzwick/SlicerMouseMaster>

## Features

- **Button Remapping**: Assign custom actions to mouse buttons (back, forward, thumb, etc.)
- **Mouse Profiles**: Built-in support for popular mice with auto-detection
- **Workflow Presets**: Save and share button configurations for different tasks
- **Context-Sensitive Bindings**: Different mappings per Slicer module
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Supported Mice

- Logitech MX Master 3S/4 (fully supported)
- Generic 3-button and 5-button mice (basic support)
- Custom profiles via button detection wizard
