Back to [Projects List](../../README.md#ProjectsList)

# Annotation of Neurosurgical MR and Ultrasound Images with Corresponding Landmarks

## Key Investigators

- Fryderyk Kögl (BWH, TUM)
- Harneet Cheema (BWH, UOttawa)
- Tina Kapur (BWH)
- Simon Drouin (ETS)
- Andrey Titov (ETS)
- Steve Pieper (Isomics)
- Tamas Ungi (Queen's University)
- Sandy Wells (BWH)

# Project Description

<!-- Add a short paragraph describing the project. -->
Corresponding landmarks between MR and ultrasound images acquired during neurosurgery are valuable for **(a)**
validation of registration algorithms and **(b)** training supervised registration algorithms **(c)** initializing a
registration. In this project we aim to create a tool that makes the process of finding those landmarks easier.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Create a UI that provides new functionality and gathers existing functionality in one place to
facilitate landmarking
2. Objective B. Investigate the rendering infrastructure that would facilitate the adjustment of landmark position in
the 3D view of Slicer

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. We use an iterative process for creating the UI - the user(s) give feedback to the developer(s) who then continuously
update(s) the UI


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps
that you could not complete then you can describe them here, too. -->

**Progress**
1. The extension is ready. It can be found
[here](https://github.com/koegl/mthesis-slicerLandmarkingView) on the main branch. A screenshot can be seen
below in **Illustrations**. For more details refer to the
[readme](https://github.com/koegl/mthesis-slicerLandmarkingView#readme).
2. A lot of bug fixes
3. More intuitive control of active views
4. More fine-grained control of viewing options
5. Automatically join corresponding landmarks with curves to visualise brain shift (also sanity check - the curves should be more or less smooth)

**Next Steps**
1. Fulfill all formal requirements for a pull request
2. Search for bugs/corner cases
3. Push to the ExtensionIndex

**Next Steps (outside the scope of this project week)**
1. Add volume rendering
2. Automatically detect landmarks (e.g. 3D-SIFT features) and manually choose the best ones

# Illustrations
<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Some more images](Example2.jpg)
-->
**Current state of the extension**
![Screenshot of the current state of the extension](https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/GUIpreview.png)

**Landmark flow**

<img src="https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/fiducial_flow.png" alt="Landmark flow" width="200"/>

**Example landmarks**

<img src="https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/1_Landmark%201%20MRI%20Pre-Op.png" alt="L1-MR1" width="200"/>
<br />
<img src="https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/2_Landmark%201%20US1.png" alt="L2-US1" width="200"/>
<br />
<img src="https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/3_Landmark%201%20US2.png" alt="L3-US2" width="200"/>
<br />
<img src="https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/4_Landmark%201%20US3.png" alt="L4-US3" width="200"/>
<br />
<img src="https://github.com/koegl/SlicerMRUSLandmarking/raw/main/misc/5_Landmark%201%20Intra-Op.png" alt="L5-MR2" width="200"/>



# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample
data, and to any relevant publications. -->

1. [Current version of the extension](https://github.com/koeglfryderyk/mthesis-slicerLandmarkingView)
2. [Mini dataset based on RESECT[1] to use for testing the extension](https://www.dropbox.com/sh/gabm0rqdh8kttj6/AADJfwfJnduJG4GJ92tygPufa?dl=0)

[1] Xiao, Yiming, et al. "RE troSpective Evaluation of Cerebral Tumors (RESECT): A clinical database of pre‐operative
MRI and intra‐operative ultrasound in low‐grade glioma surgeries." Medical physics 44.7 (2017): 3875-3882.
