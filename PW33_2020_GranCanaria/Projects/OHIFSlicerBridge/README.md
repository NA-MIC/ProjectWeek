Back to [Projects List](../../README.md#ProjectsList)

# OHIF Slicer Bridge

## Key Investigators

- Steve Pieper (Isomics)
- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- James Petts
- Mark Asselin
- Kyle Sunderland
- Csaba Pinter

## Project Description

Brainstorm and prototype synergies between the projects.

Possible scenarios:
* "Segmentation overdrive"
  * view studies with OHIF accessing dicomweb
  * perform annotation with OHIF
  * launch Slicer instance with same study loaded (transfer segmentation work-in-progress)
  * continue segmentation with Slicer Segment Editor
  * transfer results back to dicomweb server and continue review in OHIF
* Other use cases?

## Objectives

Define use cases and explore implementation options.

Possible implementation plan:
* use OHIF authenticated to google dicomweb
* add "overdrive" button
  * launches [containerized](https://github.com/pieper/SlicerDockers) slicer compute instance
  * passes in path to study, slocer downloads and loads the data ready to segment
  * opens new tab to slicer vnc
  * user can push segmentation results back to same study via dicomweb

List other requirements:
* reasonable performance launching and using cloud slicer for segmentation
* secured connection to Slicer
* lossless data transfer (especially about segmentation semantics)

## Approach and Plan

1. Discuss and document use cases (e.g. exposing Slicer modules as services instead of vnc)
1. Evaluate alternative implementations and requirements (running local, using aws, etc)
1. See what projects might take advantage of this capability

## Progress and Next Steps

1. Significant discussion to build on [previous project week work](https://projectweek.na-mic.org/PW31_2019_Boston/Projects/OHIFPluginArchitecture/) with additional use cases:
    1. Generalized from OHIF to other launch options (see Kheops, Mevis, and ePad projects).
    1. Generalized to running local Slicer in addition to option of launching cloud instances
    1. Performed testing with dicomweb-server DICOMweb interfaces

2. Implemented downloading of DICOM data to local Slicer from browser using dicomweb from a url: ```slicer://viewer/?studyUID=%202.16.840.1.113669.632.20.121711.10000158860&access_token=token_here&dicomweb_endpoint=http%3A%2F%2Fdemo.kheops.online%2Fapi&dicomweb_uri_endpoint=%20http%3A%2F%2Fdemo.kheops.online%2Fapi%2Fwado```
<details>
 <summary>Registry key to associate Slicer application with "slicer://" custom URL</summary>

 ```
 Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Slicer]
@="URL:Slicer Slicer Protocol"
"URL Protocol"=""

[HKEY_CLASSES_ROOT\Slicer\DefaultIcon]
@="Slicer.exe,1"

[HKEY_CLASSES_ROOT\Slicer\shell]
[HKEY_CLASSES_ROOT\Slicer\shell\open]
[HKEY_CLASSES_ROOT\Slicer\shell\open\command]
@="\"C:\\D\\S\\SNW\\Slicer-build\\Slicer.exe\" \"%1\""

```
 </details>

[![https://youtu.be/FMIdAzQlKw8](SlicerDICOMURLYoutube.png "3D Slicer: Downloading DICOM datasets from browser")](https://youtu.be/FMIdAzQlKw8)

3. Implemented OHIF extension to start google VM running Slicer container ([WIP implementation](https://gist.github.com/pieper/658731a7ef77231711c651ec622a6432)) for presentation at [NAC meeting](http://nac.spl.harvard.edu)
![SlicerInOHIF](Untitled.png)

## Background and References
