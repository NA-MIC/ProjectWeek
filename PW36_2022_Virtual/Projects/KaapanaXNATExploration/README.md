Back to [Projects List](../../README.md#ProjectsList)

# Investigation of Kaapana and XNAT as platforms for data management and collaborative research  

## Key Investigators

- Nadya Shusharina (BWH & MGH)
- Klaus Kades (DKFZ)
- Hanno Gao (DKFZ)
- Randy Gollub (MGH)
- Andrey Fedorov (BWH)


# Project Description

We have installed the platforms on the Googe Cloud Virtual Machines. To investigate the functionalities, we populated the platforms with publicly available datasets.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->
Ultimately, our goal is to have a platform that can be used to support data management needs for internal research activities.
1. Archival of DICOM images
2. Flexible and extensible interface to explore archived data
3. In-browser visualization of images and annotations
4. In-browser segmentation of images
5. Integration of analysis tools and their application to the data available in the platform

## Approach and Plan

1. Continue working on the evaluation of the platforms
2. Connect with any of the groups that worked on either Kaapana or XNAT to share experience
3. Meet with Kaapana maintainers to debug outstanding issues.
4. Work on resolving issues in the GCP installation.
5. Clarified status of XNAT OHIF plugin in the OHIF session (see [minutes](https://docs.google.com/document/d/1JYqLYsjaSJDLQPG0VPGKWMUjoDn8y8d1ySnafTmv8Bs/edit))

## Progress and Next Steps

Current unresolved issues

XNAT:
* not clear how to extend the search of DICOM metadata to include arbitrary attributes
* not clear if/how to integrate analysis tools
* workflow to access existing SEG/RTSTRUCT from XNAT-OHIF plugin is unclear (related post [here](https://groups.google.com/g/xnat_discussion/c/1Whl7kmjEh8))
* not clear if integration of desktop annotation tools like Slicer is possible

Kaapana:
* fixed MITK segmentation flow
* need to build platform from source - deployment from prebuilt solution has limitations
* need to work on integration of Slicer the same way as MITK - should be possible, can follow example, just need time
* overall, no blocking issues identified, just need time to debug/implement


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

* [Kaapana docs](https://kaapana.readthedocs.io/en/latest/)
* [XNAT](https://www.xnat.org/)

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
