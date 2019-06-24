Back to [Projects List](../../README.md#ProjectsList)

# OHIF Viewer Plugin Architecture

## Key Investigators

- [Danny Brown][danny] ([Radical Imaging][radical])
- [James A Petts][james] ([Institute for Cancer Research, London][icr-london])
- [Erik Ziegler][erik] ([Radical Imaging][radical])
- [Steve Pieper][steve] ([Isomics][isomics])
- [Mete Akdogan][mete] ([Stanford University, Rubin Lab][rubin-lab])

## Description

The [OHIF Viewer][ohif-viewer] is a zero-footprint medical image viewer provided by the [Open Health Imaging Foundation][ohif] (OHIF). It is a configurable and extensible progressive web application with out-of-the-box support for image archives which support DICOMweb. We would like to make the OHIF Viewer easier to extend and customize in order to better support the workflow and feature needs of end users.

## Objective

Some amount of extensibility is available via OHIF [existing extensions][ohif-extensions]. Our objective is specific to our overarching goal of integrating [James A Petts][james] existing Segmentation tools and UI, currently maintained [here][james-magic]. For example, we would like it to be possible to add the following via plugins:

```bash
# INSERT COOL IMAGES OF JAMES'S STUFF HERE
```

1. Support for custom Commands, Hotkeys, and User Preferences
2. Support for custom Side Panels
3. Support for custom Toolbar Buttons
4. Create and publish `@ohif/extension-segmentation`

## Approach and Plan

The OHIF Viewer Platform is currently coupled to it's various components' dependencies and implementations. The goal is to refactor the Viewer to add it's features and functionality via it's own extension/module system. Then, migrate each of the existing components to do the same. Key concepts:

1. Create a unit tested `ExtensionManager` responsible for extension and module registration
    - Enforces consistent module types/interfaces
2. At the application level, indicate "active contexts" that modules can scope their behavior/availability to
    - Cornerstone Extension's command can only run if "ACTIVE_VIEWPORT::CORNERSTONE" is an active context
3. Command definitions are registered to a CommandsManager that other modules have access to
4. Modules have the ability to register custom React Components
5. Side Panels, Toolbar Buttons, and Hotkeys are primarily driven by configuration; but can specify already registered React Components for advanced customization.
6. Utilize Extension/Module system to convert each of Jame's segmentation features to the appropriate module.
    - Update implementation as necessary to accomodate his functionality's needs.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

![Example of seg/contour plugin in 1.0](https://github.com/NA-MIC/ProjectWeek/raw/master/PW31_2019_Boston/Projects/OHIFPluginArchitecture/Screen%20Shot%202019-06-03%20at%2016.17.19.png)

### Features Visible in Example Image:

- Four new toolbar buttons, capable of expanding to show additional options
- Two custom sidepanels that can be toggled using a segmented button group
    - Contours and Segments
- SidePanel form and table components that update tool options/configuration and display stored measurements
- Custom tools (Either Cornerstone "Core" tools, or 3rd party drop-ins)
- Addition of alternative display set thumbnail list (See XNAT Nav)

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

<!--
    Links
-->

[radical]: http://radicalimaging.com/
[icr-london]: https://www.icr.ac.uk/
[danny]: https://github.com/dannyrb
[isomics]: http://isomics.com/
[james]: https://github.com/jamesapetts
[erik]: https://github.com/swederik
[steve]: https://github.com/pieper
[ohif-viewer]: https://github.com/OHIF/Viewers
[ohif-extensions]: https://docs.ohif.org/advanced/extensions.html
[ohif]: http://ohif.org/
[james-magic]: https://github.com/JamesAPetts/OHIF-Viewer-XNAT/tree/xnatRoi-dev-vNext/Packages/icr-peppermint-tools
[mete]: https://github.com/muakdogan
[rubin-lab]: https://rubinlab.stanford.edu/
