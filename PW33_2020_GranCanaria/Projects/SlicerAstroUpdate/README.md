Back to [Projects List](../../README.md#ProjectsList)

# [SlicerAstro](https://github.com/Punzo/SlicerAstro) Update
<img src="https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/SlicerAstroIcon.png" width="150" height="150">

## Key Investigators
<img src="https://www.davidepunzo.com/assets/images/DPLogo.png" width="150" height="150">
- [Davide Punzo][punzo] ([Freelancer][punzodavide])


## Description

A list of bugs to fix (and enhancement to do) to update SlicerAstro
to the current version of 3DSlicer is reported in SlicerAstro issue [106][slicerastroissue].

## Objective

Address SlicerAstro issue [106][slicerastroissue]

## Approach and Plan
Prioritize items in the to do list and implement them.

## Progress and Next Steps
High priority:
* [x]  (1) Fix packing of astropy and scipy
* [x]  (2) Fix Contours (in binary segmentation) in the modules AstroVolume, AstroSmoothing and AstroModeling.
* [x]  (3) AstroModeling linking between plots and points annotations is broken.
* [x]  (4) AstroMasking crash when doing a Crop operation on a Region of Interest.
* [x]  (5) AstroStatistics crash when calculating the median.
* [x]  (6) Replace old wigets with new annotation widgets: Ruler with the new line widget in the AstroPVSlice module.

Low priority:
* [x]  (7) Consider updating cfitio from 3.450 to 3.470.
* [x]  (8) Consider updating wcslib from 5.18 to 7.1.
* [ ]  (9) Fix compilation of wcslib for windows for having SlicerAstro binaries for windows too.
* [ ]  (10) Consider updating BBarolo from 1.4 to 1.5.

Last two points will be addressed later on (tickets: [107][slicerastroissue107] and [108][slicerastroissue108]).

**All the 13 SlicerAstro modules are updated and properly working with current Slicer master branch (23/01/2020)!**

# Illustrations
[![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/Screenshot-SlicerAstro-ProjectWeek2020.png)](https://www.youtube.com/watch?v=D-4G9lKVjaY "Wein069")
[![](https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/Screenshot-PVSLICE.png)](https://www.youtube.com/watch?v=D-4G9lKVjaY "Wein069")

# Background and References
SlicerAstro extends 3DSlicer to provide a 2D/3D interactive viewer for astronomical datasets with 3D interaction features,
based on traditional 2D input/output hardware, and visual analytics capabilities.


For more information refer to this [link](https://github.com/Punzo/SlicerAstro/wiki).


[punzo]: https://github.com/Punzo
[punzodavide]: https://www.davidepunzo.com/
[slicerastroissue]: https://github.com/Punzo/SlicerAstro/issues/106
[slicerastroissue107]: https://github.com/Punzo/SlicerAstro/issues/107
[slicerastroissue108]: https://github.com/Punzo/SlicerAstro/issues/108
