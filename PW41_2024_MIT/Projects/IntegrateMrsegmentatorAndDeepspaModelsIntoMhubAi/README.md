---
layout: pw41-project

permalink: /:path/

project_title: Integrate MRSegmentator and DeepSpA models into mhub.ai
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Felix Dorfner
  affiliation: Charité Universitätsmedizin Berlin
  country: Germany

- name: Hartmut Häntze
  affiliation: Charité Universitätsmedizin Berlin
  country: Germany

- name: Keno Bressem
  affiliation: Technical University of Munich
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->


This project will aim to integrate two models into mhub.ai.

**1. MRSegmentator:**
- Is a segmentation model that can accurately segment 40 organs and structures in human MRI scans of the abdominal, pelvic and thorax regions. The model works on different sequence types, including T1- and T2-weighted, Dixon sequences and even CT images.
- Paper: [https://arxiv.org/abs/2405.06463](https://arxiv.org/abs/2405.06463)

**2. DeepSpA:**
- Is classification model that incorporates anatomical awareness to detect radiographic sacroiliitis. Detecting radiographic sacroiliitis plays an essential role in diagnosing and classifying axial Spondyloarthritis (axSpA).
- Paper: [https://arxiv.org/abs/2405.07369](https://arxiv.org/abs/2405.07369)





## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. Objective: Working implementation of MRSegmentator into the mhub.ai platform.
2. Objective: Working implementation of DeepSpA into the mhub.ai platform





## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->





## Progress and Next Steps

### During Project Week
- MRSegmentator is wrapped in the MhubAI framework and ready to be tested
  - Segmentations are registered as DICOM-SEG and can easily compared to other segmentation models

- DeepSpA is wrapped in the MhubAI framework and ready to be tested
  - Model produces both visual and classification outputs, both are organized and saved by mhub


### After Project Week
- Complete the testing process and publish both models on MHub.ai




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->
 <video
   controls muted
   src="https://github.com/NA-MIC/ProjectWeek/assets/122161540/d6d749b3-3916-4bf5-8312-5cf21fdbb60b"
   style="max-height:640px; min-height: 200px">
 </video>




Illustrations of both models can be seen on their respective GitHub pages, linked below:



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


**MRSegmentator:**
- Code: [https://github.com/hhaentze/MRSegmentator](https://github.com/hhaentze/MRSegmentator)
- Paper: [https://arxiv.org/abs/2405.06463](https://arxiv.org/abs/2405.06463)

**DeepSpA:**
- Code: [https://github.com/FJDorfner/Anatomy-Aware-Classification-axSpA](https://github.com/FJDorfner/Anatomy-Aware-Classification-axSpA)
- Paper: [https://arxiv.org/abs/2405.07369](https://arxiv.org/abs/2405.07369)
