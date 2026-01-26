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

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

Code repository:

- <https://github.com/benzwick/SlicerAdaptiveBrush>

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
