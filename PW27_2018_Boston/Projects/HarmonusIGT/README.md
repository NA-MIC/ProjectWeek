Back to [Projects List](../../README.md#ProjectsList)

# Harmonus IGT

## Key Investigators

- Nicole Aucoin (Harmonus Inc.)

# Project Description

Harmonus has developed Slicer extensions for MR guided prostate biopsy, supporting listening for incoming DICOMs, calibration of hardware to patient space, lesion targeting, and needle position confirmation. The project is a mixture of closed and open source modules and we wish to communicate with other open source Slicer modules in order to interoperate. This will be done via data transfer using OpenIGTLink.

## Objective

1. Define data of interest for sharing between modules.
2. Add support to Harmonus modules to connect with other modules.
3. Add support to Harmonus modules to send data of interest to other modules.

## Approach and Plan

1. Consult with developers of other IGT enabled modules to define data sharing opportunities, especially SliceTracker.
2. Extend the current IGT support in the Harmonus software to also communicate with external modules.
3. Encapsulate data for sharing via OpenIGTLink.
4. Implement a helper function to listen for changes in data structures of interest and send them.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

* Data available for sharing:
    * registration transform node
    * hardware relative positions transform nodes
    * target fiducials list
    * needle artefact location fiducials list
* Discussed data sharing with Andrey with respect to the Slice Tracker extension
    * swapping between programs requires a new calibration scan
    * swapping hardware will result in patient motion, hence lesion target fiducials being invalid
    * different hardware will require different calibration transformations
    * no data needs to be shared between the two extensions

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!-- ![Description of picture](Example2.jpg)

![Some more images](Example2.jpg)
-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: [Development branch of HMS_SlicerModule](https://github.com/nicoleaucoin/HMS_SlicerModule/tree/290-Support-communication-with-external-Slicer-extensions "Support communication with external Slicer extensions")

- Documentation:
    - http://openigtlink.org/developers/

- Test data:

<!--Link for editing page when displayed in GitHub pages-->
<a href="{{site.github.repository_url}}/edit/master/{{page.path}}">Edit this page on GitHub</a>
