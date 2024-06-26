---
layout: pw41-project

permalink: /:path/

project_title: Updated Icons and Theme switching
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Sam Horvath
  affiliation: Kitware
  country: USA

- name: Wendy Plesniak
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We will be working on integrating new icons, QSS support, and better dynamic theme switching



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Get a working light /dark theme switch for icon sets
2. Use the newly developed icon set in Slicer
3. Mov towards using QSS for styling




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Investigate current methods for swapping out light and dark themes for icons.
2. Work on putting together a QSS style implementation for the current Slicer Light / Dark themes
3. Investigate methods of orverrding the existing icon set
4. Consolidate and icons and remove non-existent icons




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. External resource binaries
    - Refactor out current resources into an external resource file
    - [Dynamically Loaded Resources](https://doc.qt.io/qt-6/qresource.html#dynamic-resource-loading)
    - Load dark vs. light resources at startup
    - Pros
        - Minimal changes to the Slicer core code (still using the resource system)
    - Cons
        - Icons can only be refreshed with a restart
        - Build system will need to generate the rcc file instead of compiling in the resources
        - Will need to add calls to register custom resources for modules and main application




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
## Example of New icons
![image](https://raw.githubusercontent.com/Slicer/slicer-media-assets/main/SlicerIcons/SlicerSVG/SeparateStyles/LightThemeIcons/SpatialProbes/SlicerSlicePlanesOptions.svg)
![image](https://raw.githubusercontent.com/Slicer/slicer-media-assets/main/SlicerIcons/SlicerSVG/SeparateStyles/LightThemeIcons/Modules/SegmentEditorModule.svg)
![image](https://raw.githubusercontent.com/Slicer/slicer-media-assets/main/SlicerIcons/SlicerSVG/SeparateStyles/LightThemeIcons/Modules/WelcomeModule.svg)

## Switching with external resources in test extension

### Slicer Dark:
![SlicerDark](https://github.com/NA-MIC/ProjectWeek/assets/25040869/fbb2c794-a1d6-4bf4-b490-0c3fa7ddd341)


### Slicer Light: 
![SlicerLight](https://github.com/NA-MIC/ProjectWeek/assets/25040869/bdaa9be2-2b56-4357-bc36-ea95927a2d2b)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
- [Icon design document](https://docs.google.com/document/d/1OYhRzBFjwT6dUOIDVL_II8ZQ8QUwDl68wbtt3eIV1ao/edit?usp=sharing)
- [Asset repo](https://github.com/Slicer/slicer-media-assets)
- [Testing extension](https://github.com/sjh26/SlicerIconSwitch)

