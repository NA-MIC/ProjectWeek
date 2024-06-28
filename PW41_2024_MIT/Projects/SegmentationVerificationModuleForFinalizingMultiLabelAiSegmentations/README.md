---
layout: pw41-project

permalink: /:path/

project_title: Segmentation verification module for finalizing multi-label AI segmentations
category: Segmentation / Classification / Landmarking
presenter_location: Online

key_investigators:

- name: Csaba Pintér
  affiliation: EBATINCA
  country: Spain

- name: Andrey Fedorov
  affiliation: BWH
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Creating multi-label segmentation models is a challenge, because the deep learning model will try to segment all the structures that it was trained on, even if some are missing. This issue is present for vertebra segmentation, but most predominantly teeth segmentation. The Dent.AI 3D Guide dental implant planning software contains a tool for fixing the most typical errors in a user friendly way. It would be great if this tool was published as an open-source Slicer module.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Create an open-source Slicer extension from the Segmentation Verification widget from the Dent.AI 3D Guide custom app



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Discuss the current Segmentation Verification widget. Is the current design satisfactory for a more generic use? Is there any other issue that needs to be handled?
2. Take the existing Segmentation Verification widget from the custom app and create a Slicer module from it
3. Create an extension containing this module




## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Discussion with the people interested (Andrey)
2. Create extension [SegmentationVerification](https://github.com/cpinter/SlicerSegmentationVerification)
3. Implementation is done
4. Next steps
    - Integrate [Slicer PR](https://github.com/Slicer/Slicer/pull/7829), which is needed to use this new module


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![image](https://github.com/NA-MIC/ProjectWeek/assets/1325980/8637ee78-f228-4ba9-acc9-191d7709e3a1)

https://github.com/NA-MIC/ProjectWeek/assets/1325980/e452fb69-f95c-4e99-aab1-460949aa578c

![image](https://github.com/NA-MIC/ProjectWeek/assets/1325980/f341b4ab-08a2-4c9d-86b7-554ad7f85fd8)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


- [DeepEdit paper by Andrés](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=LbnADQ0AAAAJ&citation_for_view=LbnADQ0AAAAJ:ns9cj8rnVeAC)
- [Dent.AI 3D Guide software](https://www.youtube.com/watch?v=zs-0mZQLB48&ab_channel=DentAIMedicalImaging)

