Back to [Projects List](../../README.md#ProjectsList)

# OHIF Viewer Plugin Architecture

## Key Investigators

- [Danny Brown][danny] ([Radical Imaging][radical])
- [James A Petts][james] ([Institute for Cancer Research, London][icr-london])
- [Erik Ziegler][erik] ([Radical Imaging][radical])

## Description

The [OHIF Viewer][ohif-viewer] is a zero-footprint medical image viewer provided by the [Open Health Imaging Foundation][ohif] (OHIF). It is a configurable and extensible progressive web application with out-of-the-box support for image archives which support DICOMweb. We would like to make the OHIF Viewer easier to extend and customize in order to better support the workflow and feature needs of end users.

## Objective

Some amount of extensibility is available via OHIF [existing extensions][ohif-extensions]. Our objective is specific to our overarching goal of integrating [James A Petts][james] existing Segmentation tools and UI, currently maintained [here][james-magic]. For example, we would like it to be possible to add the following via plugins:

```
INSERT COOL IMAGES OF JAMES'S STUFF HERE
```

1. Support for custom Commands, Hotkeys, and User Preferences
2. Support for custom Side Panels
3. Support for custom Toolbar Buttons
4. Create and publish `@ohif/extension-segmentation`

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Describe specific steps of **what you plan to do** to achieve the above described objectives.
1. ...
1. ...

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

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
[james]: https://github.com/jamesapetts
[erik]: https://github.com/swederik
[ohif-viewer]: https://github.com/OHIF/Viewers
[ohif-extensions]: https://docs.ohif.org/advanced/extensions.html
[ohif]: http://ohif.org/
[james-magic]: https://github.com/JamesAPetts/OHIF-Viewer-XNAT/tree/xnatRoi-dev-vNext/Packages/icr-peppermint-tools
