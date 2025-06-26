---
layout: pw43-project

permalink: /:path/

project_title: Add ClaroNav MicronTracker 4 Support to Plus
category: IGT and Training

key_investigators:

- name: Tamas Ungi
  affiliation: ClaroNav Kolahi Inc
  country: Canada

- name: Sean Chen
  affiliation: ClaroNav Kolahi Inc
  country: Canada

- name: Kyle Sunderland
  affiliation: Queen's University
  country: Canada

- name: Andras Lasso
  affiliation: Queen's University
  country: Canada

---

# Project Description

<!-- Add a short paragraph describing the project. -->


MicronTracker 4 is the latest optical tracker from [ClaroNav](https://claronav.com/oem/microntracker-4/). Currently Plus supports only MicronTracker 3.6 and 3.7.

During this project week we will work on integrating support for the ClaroNav Micron Tracker 4 into Plus.  There is a pending [pull request](https://github.com/PlusToolkit/PlusLib/pull/1236) that we will compile, test and integrate to add support for this device.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Add support for the ClaroNav MicronTracker 4 to Plus.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Compile Plus using the changes added in this [PR](https://github.com/PlusToolkit/PlusLib/pull/1236)
2. Test the the connection between Plus and MicronTracker 4.
3. Make necessary changes and integrate the PR.
4. Add options to support compiling, and automatically finding the SDK using PlusBuild.




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Generated Plus MicronTracker 4.1 package: [https://github.com/PlusToolkit/PlusLib/actions/runs/15842387536/artifacts/3389393270](https://github.com/PlusToolkit/PlusLib/actions/runs/15842387536/artifacts/3389393270)




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

<img src="https://github.com/user-attachments/assets/a0e80c73-11a9-4d74-9d9d-5443cf3dc2d1" alt="MicronTracker 4" width="500"/>

![20250625_133833](https://github.com/user-attachments/assets/72251628-4b85-4e02-b519-9d33e5e475cc)


# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [https://claronav.com/oem/microntracker-4/](https://claronav.com/oem/microntracker-4/)
- [https://github.com/PlusToolkit/PlusLib/pull/1236](https://github.com/PlusToolkit/PlusLib/pull/1236)

