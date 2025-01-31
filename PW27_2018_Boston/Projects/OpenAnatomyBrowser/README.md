Back to [Projects List](../../README.md#ProjectsList)

# Open Anatomy Browser
## Key Investigators

- Michael Halle (BWH)
- Ben Ball (BWH)
- Abián Hernández-Guedes (ULPGC - GTMA - MACbioIDi)
- María Dolores Afonso-Suárez (ULPGC - GTMA - MACbioIDi)
- Jose Carlos Ruiz-Luque (ULPGC - GTMA - MACbioIDi)
- Juan Ruiz-Alzola (ULPGC - GTMA - MACbioIDi)

# Project Description
The main objective of this project is to develop the open anatomy browser as a training platform for a wide audience, including developing countries. In the first place, we plan its adaptation to different languages and study its functionality to import/export data in order to facilitate the communication between both platforms (OpenAnatomy and Slicer). We also will develop new tools to view the atlas and add new annotations to its structures.

## Objective
1. To use the HAWG atlas format as a convenient container for storing information about structures
1. To bring more anatomic metadata into the SPL brain atlas
1. To define a strategy to follow in order to tackle i18n and L10n Oabrowser projects
1. To study how to import/export data from 3DSlicer to the HAWG atlas format
1. Create a prototype with both projects (i18n-L10n and import/export)

## Approach and Plan
1. Refine a HAWG parser
1. Study the framework and modules of oabrowser
1. Review other examples
1. Investigate additional features to validate the prototypes

## Progress and Next Steps

1. An export module that reads Slicer scene data and outputs a TSV file which can then be turned into a HAWG file has been implemented. It exports images, models, and colors. Work is ongoing to export label maps and lookup tables, tying together labels, models, and structure names.  We expect this next step will be done within a week or so.
1. We have explored several options for internationalization (both the application and the data). We are prototyping tools to help with structure translation. Prototyping the JavaScript-based apps is more complicated.
1. Medical student Ben Ball will be aligning the SPL brain atlas with TA98 vocabulary and filling in Wikipedia links.

# Illustrations

Open Anatomy and 3DSlicer update

<img src="https://raw.githubusercontent.com/MarilolaMACbioIDi/OpenAnatomyBrowser/master/OABrowser_update.png" width="440" ></img>

Open Anatomy Browser Screen

<img src="https://raw.githubusercontent.com/MarilolaMACbioIDi/OpenAnatomyBrowser/master/oabrowser.jpg" width="440"></img>

HAWG Inspector

<img src="https://raw.githubusercontent.com/mhalle/taviewer/master/screenshot/h-inspect1.png" width="450"></img></img>

TA98 Viewer

<img src="https://raw.githubusercontent.com/mhalle/taviewer/master/screenshot/taviewer1.png" width="450"></img>

Excel matching

<img src="https://raw.githubusercontent.com/mhalle/taviewer/master/screenshot/excel-ta.png" width="450"></img>



# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

+ [Open Anatomy Browser](https://www.frontiersin.org/articles/10.3389/fninf.2017.00022/full)
+ [Brief i18n Analysis](https://github.com/Mltechbox/MedTec_MACbioIDi_Internationalization/blob/master/Analysis_SystemRequirements.pdf)
