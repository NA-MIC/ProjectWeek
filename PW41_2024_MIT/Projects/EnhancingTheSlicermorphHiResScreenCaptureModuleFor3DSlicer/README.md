---
layout: pw41-project

permalink: /:path/

project_title: Enhancing the SlicerMorph Hi-Res Screen Capture Module for 3D Slicer
category: Infrastructure
presenter_location: Online

key_investigators:

- name: Oshane Thomas
  affiliation: Seattle Children's Research Institute
  country: USA

- name: Murat Maga
  affiliation: Seattle Children's Research Institute
  country: USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


The HiRes Screen Capture module in the SlicerMorph extension for 3D Slicer is designed to capture high-resolution screenshots of 3D views. It allows users to specify filename, output folder, and resolution, capturing all visible objects in the selected render window. This functionality is crucial for producing detailed visual documentation of 3D renderings used in research and presentations.

The goal of this project is to prepare the HiRes Screen Capture module for the next update of 3D Slicer by addressing current limitations and enhancing its functionality. Specifically, the project aims to:

- Fix issues causing spontaneous crashes on macOS.
- Correct image resolution errors related to custom display scaling.
- Provide accurate estimates of the scaled output image based on user specifications.
- Ensure stable operation across all major operating systems (Windows, macOS, Linux).

High-resolution screenshots are essential for researchers and professionals who need to present detailed and accurate visual data. Enhancing this module will improve the reliability and usability of 3D Slicer, making it a more robust tool for the scientific community.



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


1. To enhance the HiRes Screen Capture module for 3D Slicer by fixing macOS crash issues, correcting image resolution with custom display scaling, providing accurate scaled output estimates, and ensuring stable operation across Windows, macOS, and Linux.



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Identify and Fix Crashes on macOS:
    1. Conduct thorough testing to reproduce and identify crash scenarios.
    1. Implement solutions to handle these issues and ensure stable performance on macOS.
2. Correct Image Resolution with Custom Display Scaling:
    1. Investigate how custom display scaling affects screenshot resolution.
    1. Adjust the module to correctly interpret and apply user-defined scaling settings.
3. Provide Accurate Scaled Output Estimates:
    1. Develop principled approach to accurately predict the output image size based on user specifications.
    1. Update the user interface to display these estimates before capturing the screenshot.
4. Ensure Cross-Platform Stability:
    1. Perform extensive testing on Windows, macOS, and Linux.
    1. Resolve any platform-specific issues to ensure consistent and reliable operation.



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


Thus far, the first version of the HiRes Screen Capture module has been integrated into the latest preview version of SlicerMorph. Issues with undisplayed markup and annotations have been resolved. The module is operational except for the aforementioned issues. Users can specify magnification and receive an estimated output resolution before exporting images, although this estimate may be inaccurate if custom display scaling is applied.



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


![image](https://github.com/NA-MIC/ProjectWeek/assets/18602669/1d4fc9b0-357e-4f42-a08b-2cbb1a7cb075)




# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


The current version of HiRes Screen Capture can be found at:

[https://github.com/SlicerMorph/SlicerMorph/tree/master/HiResScreenCapture](https://github.com/SlicerMorph/SlicerMorph/tree/master/HiResScreenCapture)
