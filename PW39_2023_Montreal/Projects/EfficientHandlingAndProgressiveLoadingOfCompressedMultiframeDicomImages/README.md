---
layout: pw39-project

permalink: /:path/

project_title: Efficient Handling and Progressive Loading of Compressed Multiframe DICOM Images
category: Cloud / Web
presenter_location: Online

key_investigators:

- name: Ozge Yurtsever
  affiliation: Stanford
  country: USA

- name: Emel Alkim
  affiliation: Stanford
  country: USA

- name: Steve Pieper
  affiliation: Isomics, Inc.
  country: USA
  
- name: Alireza Sedghi
  affiliation: Accolade Imaging, Inc.
  country: Canada
---

# Project Description

<!-- Add a short paragraph describing the project. -->

Loading compressed multiframe DICOM images as a whole causes frequent browser crashes, particularly on Microsoft machines. This issue arises due to the large file size of the DICOM images, exceeding the browser's memory capacity.

The browser's rendering engine attempts to load the entire file into memory, due to the significant size of these images, the browser can quickly exhaust its allocated memory, leading to crashes or unresponsive behavior.

This issue affects both ePAD and OHIF with the latest WADO-loader version.  Note that the crash can be reproduced in the current OHIF v3 version, so it has impact on projects including IDC.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

Initiate a discourse about the methodologies for saving, storing, and reading DICOM data, and explore strategies for optimizing the handling of compressed multiframe images to achieve enhanced efficiency and avoid browser crashing.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
* Confirm that the DICOM data is valid.  Issues from dciodvfy seem unrelated:
```
Warning - Missing attribute or value that would be needed to build DICOMDIR - Study ID
USMultiFrameImage
Warning - Unrecognized defined term <SECTRA> for value 1 of attribute <Coding Scheme Designator>
Error - Missing attribute Type 2C Conditional Element=<Laterality> Module=<GeneralSeries>
Warning - Unrecognized defined term <L> for value 1 of attribute <Coding Scheme Designator>
```
* Create a deidentified dataset to reproduce the data.  Original US data has burned in patient info, so blank pixel data will be substituted.
*  Done: https://github.com/emelalkim/sampledata/releases/tag/large_multiframe
* Explore changing the code so that instead of loading the entire DICOM file at once, the image loading process can be modified to load the image in smaller chunks or frames progressively. This approach may allow the browser to handle smaller portions of the image, reducing the memory burden and enhancing overall stability.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

After conducting further tests, we discovered an additional observation regarding the uncompressed images. It became evident that even when working with uncompressed images, if the image size exceeds a certain threshold (500 MB), OHIF crashes almost instantly, within a matter of seconds.

This finding underscores the importance of addressing the performance and stability concerns, not only for handling compressed images but also for handling larger uncompressed images. It emphasizes the need to optimize the OHIF viewer and its underlying components like cornerstoneWADOImageLoader and dicomParser to ensure robust performance across a wide range of image sizes.

We have made significant progress in addressing various issues related to the OHIF viewer and its underlying components: 

* _OHIF Build with Proposed PR for Uncompressed Images:_ We successfully created an OHIF build incorporating the proposed pull request (PR) for uncompressed images. Previously, the demo ultrasound series would cause immediate failure and crash the browser. However, the proposed fix effectively resolved this issue, allowing smooth loading and scrolling through a multiframe image of approximately 600 MB without any problems.

PR link: <https://github.com/cornerstonejs/cornerstoneWADOImageLoader/pull/454#issue-1287614710>
       
* _Handling Compressed Images:_
    * To address the issue with compressed images, we adapted a solution approach inspired by the provided PR link. While the original solution focused on uncompressed images, we applied a similar method within the dicomParser library to handle compressed images. Initially, the attempted solution did not yield the desired outcome. However, after further work and refinement, we were able to fix the issue and submit a PR to dicomParser.
    * _Successful Testing of Proposed PR with Compressed Images:_ We have successfully built and tested the proposed PR in ePAD using compressed images. This implementation resolved the crashing issue associated with compressed images, ensuring stable functionality.
    * _Deidentify Sample Dataset:_ Although we made efforts to create a deidentified sample dataset, we encountered challenges in blacking out the pixels. We are actively working on finding a solution to overcome this obstacle.
    * Configuration of dicomparser's sharedCopy Method: Alireza suggested making the dicomParser's sharedCopy method configurable with a useCopy option. This enhancement would provide other applications and users utilizing dicomparser with the flexibility to choose whether they want to use a copy or not. We will diligently work on implementing this suggestion and update the PR accordingly.

Ticket link: <https://github.com/cornerstonejs/dicomParser/issues/248> 

PR Link: <https://github.com/cornerstonejs/dicomParser/pull/251>

* _Stress Testing OHIF Viewer and cornerstoneWADOLoader:_ As part of our testing, we performed a stress test to evaluate the limits of the OHIF viewer and the cornerstoneWADOLoader. Despite the implementation of the proposed changes that significantly improved performance, we encountered an ongoing challenge with the OHIF Viewer crashing when loading large datasets. It is important to note that this issue does not appear to be specific to either compressed or uncompressed data, as it is reproducible with both types. Upon further investigation, we identified the following key issues:

  * _Crashing when trying to load large data folder:_ Attempting to load a folder larger than 3GB resulted in the viewer failing to load and crashing immediately. It is important to note that the crash occurs while trying to index the folder, and it is likely due to the cache size limitation, which is currently set to 2GB.
  * _Crashing when trying to load a large multiframe after loading a couple of series: After a certain number of multiframe images have been opened, the browser crashes during the image loading process. To reproduce this issue, please follow the steps outlined below:
    1. Open the local OHIF page
    2. Load the sample deidentified multiframe
    3. Open the page again in the same browser tab
    4. Load the sample deidentified multiframe
    5. Repeat steps _c_ and _d_ seven or eight times
    6. After a certain number of iterations, the browser will crash during the image loading phase.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Crash screenshot ![crash-image](https://github.com/NA-MIC/ProjectWeek/assets/9955081/9f80cbd7-cfa7-4c54-934c-9d165fe38e1a)
Sample multiframe loaded successfully with suggested improvements 

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
     
Uncompressed ultrasound image <https://github.com/emelalkim/sampledata/releases/tag/large_multiframe>

Unfortunately we couldn't deidentify the compressed ultrasound images.

Related libraries:
<https://github.com/cornerstonejs/cornerstoneWADOImageLoader>
<https://github.com/cornerstonejs/dicomParser>

