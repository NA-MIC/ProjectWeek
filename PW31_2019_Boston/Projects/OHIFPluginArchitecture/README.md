Back to [Projects List](../../README.md#ProjectsList)

# OHIF Viewer Plugin Architecture

## Key Investigators

- [Danny Brown][danny] ([Radical Imaging][radical])
- [James A Petts][james] ([Institute for Cancer Research, London][icr-london])
- [Erik Ziegler][erik] ([Radical Imaging][radical])
- [Steve Pieper][steve] ([Isomics][isomics])
- [Mete Akdogan][mete] ([Stanford University, Rubin Lab][rubin-lab])
- [Zach Saltzaman][zach] ([Yale School of Medicine][yale])
- [Omar Toutounji][omar] ([Medical Informatics Lab][med-i-lab])

## Description

The [OHIF Viewer][ohif-viewer] is a zero-footprint medical image viewer provided by the [Open Health Imaging Foundation][ohif] (OHIF). It is a configurable and extensible progressive web application with out-of-the-box support for image archives which support DICOMweb. We would like to make the OHIF Viewer easier to extend and customize in order to better support the workflow and feature needs of end users.

## Objective

Some amount of extensibility is available via OHIF [existing extensions][ohif-extensions]. Our objective is specific to our overarching goal of integrating [James A Petts][james] existing Segmentation tools and UI, currently maintained [here][james-magic]. For example, we would like it to be possible to add the following via plugins:

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
    - Update implementation as necessary to accommodate his functionality's needs.

## Progress and Next Steps

### Before Project Week:

- An initial implementation of the Extension Manager
- Basic support for Commands
- Basic support for Toolbar Buttons
- Basic support for Hotkeys

### At Project Week:

1. The `ExtensionManager` was updated to support Panel Extensions
1. The `ExtensionManager` was updated to support a `preRegistration` hook
    - Also allows for configuration to be passed to extension at Application level
1. The `ToolbarDefinition` schema was updated to support nested menu items
1. Form components were added to `react-viewerbase` to assist Extension Authors
1. The existing `MeasurementsTable` was converted to a `PanelModule`
1. Authored Segmentation functionality as an `extension`


- [`react-viewerbase`](https://github.com/OHIF/react-viewerbase)
- [`ohif-segmentation-plugin`](https://github.com/JamesAPetts/ohif-segmentation-plugin)
- [`extensions-pr`](https://github.com/OHIF/Viewers/pull/593)


#### Next Steps

- Add unit tests for, and then simplify how ExtensionManager surfaces its registered modules
- Introduce new UI patterns to improve UX as the number of available tools/panels grows
- Iterate on styles of the Segmentation Extension's custom React Panels
- Add custom SVG Icon support for Toolbar Buttons
- Update `docs.ohif.org` with latest extension information


## Illustrations

![Example of seg/contour plugin in 1.0](https://github.com/NA-MIC/ProjectWeek/raw/master/PW31_2019_Boston/Projects/OHIFPluginArchitecture/Screen%20Shot%202019-06-03%20at%2016.17.19.png)

### Features Visible in Example Image:

- Four new toolbar buttons, capable of expanding to show additional options
- Two custom sidepanels that can be toggled using a segmented button group
    - Contours and Segments
- SidePanel form and table components that update tool options/configuration and display stored measurements
- Custom tools (Either Cornerstone "Core" tools, or 3rd party drop-ins)
- Addition of alternative display set thumbnail list (See XNAT Nav)

### Extension Schema

An OHIF extension is a POJO (plain old JavasSript object) that has properties and methods that provide information to OHIF's extension manager.

#### PreRegistration

```js
  preRegistration(configuration = {}) {
  },
```

#### Panel Module

```js
getPanelModule() {
    return {
      menuOptions: [
        {
          icon: 'th-list',
          label: 'Segments',
          target: 'segment-panel'
        },
        {
          icon: 'th',
          label: 'Contours',
          target: 'contour-panel'
        }
      ],
      components: [
        {
          id: 'segment-panel',
          from: 'right',
          width: '500px',
          component: SegmentationMenu // React Component
        },
        {
          id: 'contour-panel',
          from: 'right',
          width: '500px',
          component: RoiContourMenu // React Component
        }
      ],
      defaultContext: ['VIEWER']
    };
  }
```

#### Toolbar Module

```js
getToolbarModule() {
    return {
      definitions: [
        {
          id: 'freehandRoiTools',
          label: 'ROI',
          icon: 'level',
          buttons: [
            {
              id: 'FreehandRoi',
              label: 'Draw',
              icon: 'level',
              type: TOOLBAR_BUTTON_TYPES.SET_TOOL_ACTIVE,
              commandName: 'setToolActive',
              commandOptions: { toolName: TOOL_NAMES.FREEHAND_ROI_3D_TOOL }
            },
            {
              id: 'FreehandRoiSculptor',
              label: 'Sculpt',
              icon: 'level',
              type: TOOLBAR_BUTTON_TYPES.SET_TOOL_ACTIVE,
              commandName: 'setToolActive',
              commandOptions: { toolName: TOOL_NAMES.FREEHAND_ROI_3D_SCULPTOR_TOOL }
            }
          ]
        },
        ...
      ],
      defaultContext: 'ACTIVE_VIEWPORT::CORNERSTONE'
    };
  },
```

#### Commands Module

```js
/**
* Registers one or more named commands scoped to a context. Commands are
* the primary means for toolbar actions and actions that can be bound to hotkeys.
*/
getCommandsModule() {
  actions: {
    nextSegmentForActiveViewport: ({ viewports }) => {
      // Command implementation.
    },
    previousSegmentForActiveViewport: ({ viewports }) => {
      // Command implementations.
    },
    increaseBrushSize: () => {
      // Command implementations.
    },
    decreaseBrushSize: () => {
      // Command implementations.
    }
  }

  definitions: {
    nextSegmentForActiveViewport: {
      commandFn: actions.nextSegmentForActiveViewport,
      storeContexts: ['viewports']
    },
    previousSegmentForActiveViewport: {
      commandFn: actions.previousSegmentForActiveViewport,
      storeContexts: ['viewports']
    },
    increaseBrushSize: {
      commandFn: actions.increaseBrushSize
    },
    decreaseBrushSize: {
      commandFn: actions.decreaseBrushSize
    }
  }
  defaultContext: 'ACTIVE_VIEWPORT::CORNERSTONE'
};





```

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

<!--
    Links
-->

[radical]: http://radicalimaging.com/
[icr-london]: https://www.icr.ac.uk/
[rubin-lab]: https://rubinlab.stanford.edu/
[isomics]: http://isomics.com/
[med-i-lab]: http://medi.cs.queensu.ca/
[yale]: https://medicine.yale.edu/

[danny]: https://github.com/dannyrb
[james]: https://github.com/jamesapetts
[erik]: https://github.com/swederik
[steve]: https://github.com/pieper
[mete]: https://github.com/muakdogan
[zach]: https://github.com/zsaltzman
[omar]: https://github.com/omartoutounji

[ohif-viewer]: https://github.com/OHIF/Viewers
[ohif-extensions]: https://docs.ohif.org/advanced/extensions.html
[ohif]: http://ohif.org/
[james-magic]: https://github.com/JamesAPetts/OHIF-Viewer-XNAT/tree/xnatRoi-dev-vNext/Packages/icr-peppermint-tools
