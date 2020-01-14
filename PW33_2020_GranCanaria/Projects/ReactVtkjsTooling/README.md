Back to [Projects List](../../README.md#ProjectsList)

# Tool Framework for [react-vtkjs-viewport](https://github.com/OHIF/react-vtkjs-viewport).

## Key Investigators

- [James A Petts][james] ([Radical Imaging][radical], [Ovela Solutions][OvelaSolutions])
- [Danny Brown][danny] ([Radical Imaging][radical])
- [Erik Ziegler][erik] ([Radical Imaging][radical])

## Description

The `react-vtkjs-viewport` library is a wrapper around `vtk.js` with the idea that it should become a really simple way to get quickly get past the boilerplate required to use vtk-js in a react application.
There have been improvements to loading, rendering and segmentation display, but an extensible tool framework in the vein of cornerstoneTools is severly lacking.

## Objective

Clear objectives:
- Refactor the current `interactorStyle`s to a set of manipulators and a single configurable `interactorStyle`, where "tool load-outs" can be set via configuration in the constructor (See this)[https://kitware.github.io/vtk-js/examples/InteractorStyleManipulator.html].
- Refactor the crosshairs to be less of "annotation" and more of reference line tool that is calculated every render based on a single world position as its centre.

Open questions:
- How do we deal with 2D annotations?
  a) Can we shoehorn the `cornerstoneTools` canvas over the `vtk.js` viewport and rewrite the rendering routine.
    - Annotations would be 2D, project them onto the screen?
    - When do we render them?
  b) Annotations exist as 3D objects in `vtk.js`, and we write a render hook to re-render all of these as SVG projected onto the display coordinates of the device, with a similar "invalidated" pattern to `cornerstoneTools`.
- Should "`vtkjs-tools`" be its own repo? Are we shovelling too much into react-vtkjs-viewport that could be used elsewhere? Is this important enough to be formalized in vtk.js itself?

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Discuss the above open questions.
2. Work on the clear objectives.
3. Work on any objectives derived from (1.).

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

# Illustrations


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

* New free tutorials for VTK.js and OHIF: https://discourse.vtk.org/t/new-free-video-tutorials-vtk-js-and-ohif-web-apps/2164
* https://vtk.org/Wiki/VTK/ProgrammableMultiVolumeRendering
* https://github.com/Kitware/vtk-js
* https://github.com/OHIF/react-vtkjs-viewport

<!--
    Links
-->

[radical]: http://radicalimaging.com/
[danny]: https://github.com/dannyrb
[isomics]: http://isomics.com/
[james]: https://github.com/jamesapetts
[erik]: https://github.com/swederik
[steve]: https://github.com/pieper
[OvelaSolutions]: https://www.ovelasolutions.com
[ohif-viewer]: https://github.com/OHIF/Viewers
[ohif-extensions]: https://docs.ohif.org/advanced/extensions.html
[ohif]: http://ohif.org/
