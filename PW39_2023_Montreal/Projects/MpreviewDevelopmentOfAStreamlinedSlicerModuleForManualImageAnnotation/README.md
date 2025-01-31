---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/MpreviewDevelopmentOfAStreamlinedSlicerModuleForManualImageAnnotation/README.html

project_title: mpReview Development of a streamlined Slicer module for manual image annotation
category: Cloud / Web
presenter_location: In-person

key_investigators:

- name: Deepa Krishnaswamy
  affiliation: BWH

- name: Nadya Shusharina
  affiliation: MGH

- name: Andrey Fedorov
  affiliation: BWH

- name: Andras Lasso
  affiliation: Queen's University

---

# Project Description

<!-- Add a short paragraph describing the project. -->

Currently, there does not exist a simple, streamlined way to annotate many DICOM series and save Segmentation objects. Users have to manually load data into Slicer, set up the layouts themselves (in the case of multi-parametric data), name the files, etc. -- this is difficult to do for a large dataset!

There are extensions that already exist, for instance [CaseIterator](https://github.com/JoostJM/SlicerCaseIterator), [FlywheelCaseIterator](https://github.com/Slicer/ExtensionsIndex/pull/1942) and [SegmentationReview](https://github.com/zapaishchykova/SegmentationReview). Unfortunately, some do not take DICOM files as input, and so far cannot handle cases where a clinician needs to view multiple series at the same time.

The 3DSlicer module mpReview (part of the SlicerProstate extension) was previously developed to handle these cases, specifically for assisting with manual annotation of the prostate and other related anatomical regions. In previous project weeks, we have streamlined the extension [here](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/mpReview/) and updated the module to use the latest SegmentEditor, and incorporated the use of Google Cloud Platform [here](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/mpReview/).

However, there are improvements that can be made in terms of functionality. For instance, we would like to allow the user to access multiple types of servers, and perform annotation of body parts other than the prostate.

In this project week we'd like to focus on getting user feedback on the current state of the extension, and ideas for improvements and features to add. We will try out extensions mentioned above to get ideas of how ours could be more streamlined.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Get feedback from the current [multiple_server_feature](https://github.com/deepakri201/mpReview/tree/multiple_server_feature) branch of the module.
2.  Try out [CaseIterator](https://github.com/JoostJM/SlicerCaseIterator), [FlywheelCaseIterator](https://github.com/Slicer/ExtensionsIndex/pull/1942), and [SegmentationReview](https://github.com/zapaishchykova/SegmentationReview)
3.  Brainstorm ideas for improvements and features to include.
4.  Define the steps that are needed to accomplish the changes.
5.  Release the module as a new Slicer extension

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  We will provide instructions below how to setup the module, and download sample data, etc. --> see below "Installation Instructions for Users"
2.  We will ask users to experiment with the module and provide us feedback.
3.  We will make some changes to the module based on user feedback and from our experimentation with the other extensions
4.  At the same time we'll test out other approaches

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  I made some UI changes to the module from feedback from Nadya and Andrey
2.  I tested out two Slicer extensions that are also used for annotations -- [CaseIterator](https://github.com/JoostJM/SlicerCaseIterator) and [SegmentationReview](https://github.com/zapaishchykova/SegmentationReview). Still waiting for Flywheel instance to test FlywheelCaseIterator
3.  I was able to get multiple users to try the module, and fixed some of the errors they found
4.  I also demo'd the module and received very useful feedback [here](https://docs.google.com/document/d/1_Ou1Uns0LrzQ_w-As-1u1PSnLxyqXgUuNgVtkm2Eebc/edit?usp=sharing)
5.  Next week I will make a PR so the latest version of mpReview can be used. After that I will submit it as a separate extension with some additional features

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

Demo of the module

<!-- ![image](https://user-images.githubusercontent.com/59979551/173397664-c3a7f567-d5f2-4214-a366-7cef1344860c.png) -->

 <video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/59979551/b09afbb7-1c31-4fab-b273-7f5b16088922"
   style="max-height:640px; min-height: 200px">
 </video>

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

We have worked on this during multiple project weeks, [PW35](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/mpReview/) and [PW37](https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/mpReview/). The code from PW37 is available [here](https://github.com/deepakri201/mpReview/tree/multiple_server).

# Installation Instructions for Users

1. Clone the mpReview [multiple_server_feature branch](https://github.com/deepakri201/mpReview/tree/multiple_server_feature)
2. Add the following extensions: SlicerDICOMWeb, DCMQI, QuantitativeReporting, SlicerDevelopmentToolbox
3. Enable the developer mode in the Application settings and add the path from #1 to the module list
4. If you want to use the local Slicer DICOM database to experiment with the module, download some sample data from this dropbox link [here](https://www.dropbox.com/scl/fo/br63z27pfjm421vbn9m96/h?dl=0&rlkey=unxlhva3ifkden5usxfn6b78d). We've provided data from a typical prostate MR imaging scan (collection QIN-Prostate-Repeatability) and a typical CT scan (from NLST).
5. Or, if you want to be adventurous and try out using the Google Cloud Platform server, you will first need to have a google account and a project. You will have a 90 day free trial with credits, or go [here](https://learn.canceridc.dev/getting-started-with-idc) to request $300 credits from Imaging Data Commons. Then follow [this Google Colab notebook](https://colab.research.google.com/drive/1nDsnERKpWWr32xK_M7_pA1GjHPbghwjK#scrollTo=FaapolCoufCX) to set up your very own DICOM datastore which will hold the same data from above. You will also need to install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) on your machine (for Mac/Linux make sure you install it in your home directory and add to PATH). In windows it should be added to the path automatically.
6. Install the mpReview module by going to Applications and adding the path.
7. If you have time, it would be great to get your feedback on this [google form](https://docs.google.com/forms/d/e/1FAIpQLSe2fGjdiWVfPSh3gDOoZ5fm0IaUHdB4lultvjwRqVskodN2sw/viewform?usp=sf_link) :)
