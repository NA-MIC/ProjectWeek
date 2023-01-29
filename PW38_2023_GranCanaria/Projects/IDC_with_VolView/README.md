Back to [Projects List](../../README.md#ProjectsList)

# Using VolView with data in Google Storage buckets / IDC buckets

## Key Investigators

- Andrey Fedorov (Brigham and Women’s Hospital, USA)
- Forrest Li (Kitware, USA)
- Stephen Aylward (Kitware, USA)

# Project Description
<!-- Add a short paragraph describing the project. -->

[VolView](https://volview.kitware.com/) is an open source radiological viewer developed by Kitware that excels in 3D visualization. Currently, this viewer can be used to visualize files uploaded into the browser.

[NCI Imaging Data Commons](https://imaging.datacommons.cancer.gov/) is a cloud-based repository of cancer imaging data, which among other features provides free access to the DICOM files curated in Google Storage public buckets. 

While IDC integrates OHIF and Slim viewers, the instances of the viewers maintained by IDC can only be used to visualize data in IDC. Users that want to visualize analysis results they produce in OHIF or Slim need to deploy their own instances of the viewers. That process is documented, but involves many steps and can be too difficult for many users. Furthermore, OHIF Viewer v2 used in IDC does not have any functionality to support 3D visualization.

In this project we want to investigate the use of existing VolView instance maintained by Kitware at [https://volview.kitware.com/](https://volview.kitware.com/) to visualize data in public Google Storage buckets. This will allow:
1. 3D visualization of public data in IDC.
2. Not only "zero footprint", but more importantly "zero deployment" and "zero maintenance" viewer that can be used by IDC users to visualize analysis results.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Investigate ability of VolView to pull data from Google Storage public buckets - in IDC and/or from user projects.
2. Investigate representation of the manifest to be used to define VolView input.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Experiment with CORS settings on a public "test" bucket.
2. Define minimum necessary settings for CORS configuration.
3. Coordinate with GCP support and other GCP experts as needed.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Set up public bucket, so far changes to CORS do not seem to have effect, but maybe we did not wait long enough...
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

