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


1. Icon swap approach: External resource binaries
    - Refactor out current resources into an external resource file
    - [Dynamically Loaded Resources](https://doc.qt.io/qt-6/qresource.html#dynamic-resource-loading)
    - Load dark vs. light resources at startup
    - Pros
        - Minimal changes to the Slicer core code (still using the resource system)
    - Cons
        - Icons can only be refreshed with a restart
        - Build system will need to generate the rcc file instead of compiling in the resources
        - Will need to add calls to register custom resources for modules and main application
2. Icon swap progress
    - Created standalone example in [test extension](https://github.com/sjh26/SlicerIconSwitch)
    - Created [branch](https://github.com/Slicer/Slicer/tree/icon-switching) for Slicer with WIP implementations for bundling external resources
    - Setup external resources for loadable modules and libraries
  
3. Next steps
    - Work on swapping bundled resources for Python (or an icon picker approach in code)
    - Work on bugs with existing implementation (timing of loading resources for loadable modules, using SVGs as mouse cursors, Transform icon is being stubborn)
    - Review approach with Slicer dev team, mainly  when / where the external resources are loaded at runtime, and where they are stored on disk

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
## Example of New icons
![image](https://raw.githubusercontent.com/Slicer/slicer-media-assets/main/SlicerIcons/SlicerSVG/SeparateStyles/LightThemeIcons/SpatialProbes/SlicerSlicePlanesOptions.svg)
![image](https://raw.githubusercontent.com/Slicer/slicer-media-assets/main/SlicerIcons/SlicerSVG/SeparateStyles/LightThemeIcons/Modules/SegmentEditorModule.svg)
![image](https://raw.githubusercontent.com/Slicer/slicer-media-assets/main/SlicerIcons/SlicerSVG/SeparateStyles/LightThemeIcons/Modules/WelcomeModule.svg)

## Switching with external resources in test extension

### Slicer Dark:
![SlicerDarkUpdated](https://github.com/NA-MIC/ProjectWeek/assets/25040869/12767317-b88c-4340-8652-4b919d2da814)

![DarkToolBar](https://github.com/NA-MIC/ProjectWeek/assets/25040869/ea3b494a-d07e-40ca-a47c-ad4139380551)


### Slicer Light: 
![SlicerLightUpdated](https://github.com/NA-MIC/ProjectWeek/assets/25040869/a13bea8b-5e7a-4da0-af67-02849cbe810e)

![LightToolBar](https://github.com/NA-MIC/ProjectWeek/assets/25040869/fe36d249-a489-4a45-bfbf-5bd21c1183c2)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
- [Icon design document](https://docs.google.com/document/d/1OYhRzBFjwT6dUOIDVL_II8ZQ8QUwDl68wbtt3eIV1ao/edit?usp=sharing)
- [Asset repo](https://github.com/Slicer/slicer-media-assets)
- [Testing extension](https://github.com/sjh26/SlicerIconSwitch)
- [WIP Slicer branch](https://github.com/Slicer/Slicer/tree/icon-switching)

