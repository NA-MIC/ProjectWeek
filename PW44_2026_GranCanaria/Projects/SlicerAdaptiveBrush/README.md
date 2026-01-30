---
layout: pw44-project

permalink: /:path/

project_title: SlicerAdaptiveBrush - Adaptive Brush Segment Editor Effect
category: Segmentation / Classification / Landmarking
presenter_location: In-person

key_investigators:

- name: Ben Zwick
  affiliation: The University of Western Australia and Talk2View
  country: Australia

- name: Andy Huynh
  affiliation: Talk2View
  country: Australia

---

# Project Description

<!-- Add a short paragraph describing the project. -->

SlicerAdaptiveBrush is a segment editor effect extension for 3D Slicer that provides an adaptive brush tool for semi-automatic segmentation. The brush automatically segments regions based on image intensity similarity within the brush area, adapting to image features (edges, boundaries) rather than using a fixed geometric shape.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Submit to Extension Index
2. Improve documentation and tutorials
3. Optimize performance for real-time interaction
4. Add GPU acceleration for Level Set algorithm

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

### 1. Submit to Extension Index

- Complete submission requirements
- Test on all platforms (Linux, macOS, Windows)
- Create extension icon and screenshots

### 2. Improve documentation

- Write user tutorial with example workflows
- Document algorithm selection guide
- Add parameter tuning recommendations

### 3. Optimize performance

- Profile and optimize critical paths
- Implement ROI result caching for nearby brush positions
- Add slice-by-slice preview mode

### 4. GPU acceleration

- Implement OpenCL/CUDA backend for Level Set
- Benchmark CPU vs GPU performance

## Progress and Next Steps

### Completed

1. **Extension Index Submission (In Progress)**
   - CI/CD pipeline with GitHub Actions for automated builds
   - Extension not yet in the Slicer Extension Index

2. **Documentation**
   - Full documentation site live at [benzwick.github.io/SlicerAdaptiveBrush](https://benzwick.github.io/SlicerAdaptiveBrush/)
   - [Getting Started Tutorial](https://benzwick.github.io/SlicerAdaptiveBrush/user_guide/getting_started.html) with 10-step workflow
   - [Algorithms Guide](https://benzwick.github.io/SlicerAdaptiveBrush/user_guide/algorithms.html) covering all 7 algorithms
   - [Parameter Wizard Guide](https://benzwick.github.io/SlicerAdaptiveBrush/user_guide/parameter_wizard.html) for interactive setup
   - Developer documentation for optimization, testing, and recipes
   - Auto-generated screenshots from test suite

3. **Performance Optimization**
   - Implemented PerformanceCache with gradient and threshold caching
   - Undo/redo integration with single save per stroke
   - Cache statistics and hit rate logging

4. **GPU Acceleration**
   - Backend selector UI prepared (Auto/CPU/GPU)
   - GPU implementation deferred to v2.0+

### Next Steps

- Complete Extension Index submission
- Parameter optimization and testing for different image modalities (CT, MRI T1/T2, PET) and tissue types (tumor, bone, vessels, brain tissue)
- Testing with [Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/) data using Claude skills:
  - [ImagingDataCommons/idc-claude-skill](https://github.com/ImagingDataCommons/idc-claude-skill)
  - [mhalle/idc-skill](https://github.com/mhalle/idc-skill)
  - [benzwick/imaging-data-commons-skill](https://github.com/benzwick/imaging-data-commons-skill)
  - See also: [claude-scientific-skill for Imaging Data Commons](../ClaudeScientificSkillForImagingDataCommons/) project
- Mouse shortcuts can be configured using [SlicerMouseMaster](../SlicerMouseMaster/) for workflow optimization

# Illustrations

![Selecting Adaptive Brush effect](https://benzwick.github.io/SlicerAdaptiveBrush/_images/getting_started_005_select_adaptive_brush.png)

*Selecting the Adaptive Brush effect in Segment Editor*

![Painting with Adaptive Brush](https://benzwick.github.io/SlicerAdaptiveBrush/_images/getting_started_008_paint.png)

*Painting a brain tumor segmentation - the brush adapts to image boundaries*

![3D visualization of segmentation](https://benzwick.github.io/SlicerAdaptiveBrush/_images/getting_started_010_view_in_3d.png)

*3D surface rendering of the segmented tumor*

# Background and References

Code repository: <https://github.com/benzwick/SlicerAdaptiveBrush>

Documentation: <https://benzwick.github.io/SlicerAdaptiveBrush/>

- [Getting Started Tutorial](https://benzwick.github.io/SlicerAdaptiveBrush/user_guide/getting_started.html)
- [Algorithms Guide](https://benzwick.github.io/SlicerAdaptiveBrush/user_guide/algorithms.html)
- [Parameter Wizard](https://benzwick.github.io/SlicerAdaptiveBrush/user_guide/parameter_wizard.html)

## Features

- **Multiple algorithm choices** - Geodesic Distance, Watershed, Random Walker, Level Set, Connected Threshold, Region Growing, Threshold Brush
- **Auto-threshold methods** - Otsu, Huang, Triangle, Maximum Entropy, IsoData, Li
- **Automatic intensity analysis** - GMM-based threshold estimation adapts to image content
- **Edge-aware boundaries** - Respects anatomical boundaries automatically
- **2D and 3D modes** - Works on single slices or volumetrically (sphere mode)

## References

- [ITK-SNAP Adaptive Brush](https://www.itksnap.org/) - Original inspiration
- [3D Slicer Segment Editor](https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html)
- [SlicerSegmentEditorExtraEffects](https://github.com/lassoan/SlicerSegmentEditorExtraEffects)
