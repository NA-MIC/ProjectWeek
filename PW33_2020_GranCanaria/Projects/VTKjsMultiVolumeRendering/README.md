Back to [Projects List](../../README.md#ProjectsList)

# VTK.js Multi-volume Volume Rendering

## Key Investigators

- Someone from Kitware? JC? Ken? Forrest?
- [Steve Pieper][steve] ([Isomics][isomics])
- [James A Petts][james] ([Radical Imaging][radical], [Ovela Solutions][OvelaSolutions])
- [Danny Brown][danny] ([Radical Imaging][radical])
- [Erik Ziegler][erik] ([Radical Imaging][radical])

## Description

The Open Health Imaging Foundation (OHIF) Viewer uses [VTK.js](https://github.com/Kitware/vtk-js) for multi-planar reformatting (MPR). We use thin-slice volume rendering to implement MPR in the OHIF Viewer. In order to support PET/CT image fusion with overlaid segmentation label maps, we need to implement multi-volume rendering in VTK.js. At present, multi-volume rendering sort of works but only for two volumes.

## Objective

Our goal is to add proper support for multi-volume volume rendering to VTK.js.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Evaluate how VTK C++ implements multi-volume rendering
2. Make similar changes to the VTK.js JavaScript / WebGL implementation
3. Clean up [terminology in VTK.js' RenderWindow](https://github.com/Kitware/vtk-js/pull/1264#issuecomment-561653542)

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

* Held a preparation tcon with the Kitware team to review status and goals.

# Illustrations


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

* New free tutorials for VTK.js and OHIF: https://discourse.vtk.org/t/new-free-video-tutorials-vtk-js-and-ohif-web-apps/2164
* https://vtk.org/Wiki/VTK/ProgrammableMultiVolumeRendering
* https://github.com/Kitware/vtk-js
* https://github.com/Kitware/vtk-js/pull/1264

<!--
    Links
-->

[radical]: http://radicalimaging.com/
[danny]: https://github.com/dannyrb
[isomics]: http://isomics.com/
[james]: https://github.com/jamesapetts
[OvelaSolutions]: https://www.ovelasolutions.com
[erik]: https://github.com/swederik
[steve]: https://github.com/pieper
[ohif-viewer]: https://github.com/OHIF/Viewers
[ohif-extensions]: https://docs.ohif.org/advanced/extensions.html
[ohif]: http://ohif.org/
