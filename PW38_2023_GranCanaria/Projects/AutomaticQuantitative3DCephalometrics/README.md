Back to [Projects List](../../README.md#ProjectsList)

Automatic Quantification 3D Components

## Key Investigators
- Nathan Hutin (University of Michigan)
- Luc Anchling (University of Michigan)
- Baptiste Baquero (University of Michigan)
- Maxime Gillot (University of Michigan)
- Lucia Cevidanes (University of Michigan)
- David Allemang (Kitware Inc)
- Jean-Christophe Fillion-Robin (Kitware Inc)

# Project Description
The Automatic Quantification 3D Components(AQ3DC) aims to provide a user-friendly tool that decrease user time for extraction of quantitative
image analysis features. AQ3DC is a Slicer extension to automatically compute lists of measurements seleted by users for a single case or a whole
study sample, at one or more time points. The current implementation is aimed at automatic computation of 3D components like distances (AP, RL and SI) 
between points, points to line, midpoint between two points or angles (Pitch, Roll and Yaw), which can be further extended to any type of desired
computation/quantitative image analysis. The design of the user interface is currently aimed at quantification of craniofacial dental, 
skeletal and soft tissue structures. 

The Automatic Quantification 3D Components(AQ3DC) is already available on Slicer. The main goal now is to refactor the 
code can be maintainable, make AQ3DC more robust, solve AQ3DC's issues, and update documentation.


<ul>
<li>Project link : https://github.com/DCBIA-OrthoLab/Q3DCExtension</li>
<ul>


## Objective

- A. Refactoring the code to be maintainable.
- B. Resolve the old issues.
- C. Add a new tool that allows choosing display landmarks in the landmark tab.
- D. Make AQ3DC more robust.
- E. Update Readme and create documentation on SlicerCMF

## Approach and Plan

1. Users try AQ3DC's refactoring  to be sure there are fewer issues than before, for then pull requests the code.
2. Update SlicerCMF workflow to document and integrate with AQ3DC.


## Progress and Next Steps

# Progress:
1. Refactoring code
2. Resolve old issue


# Next steps :
1. Update SlicerCMF workflow to document and integrate with AQ3DC.
2. Update README
3. Update code Style


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
# 1. Slicer Interface
![Screenshot from 2022-06-30 18-31-37](https://user-images.githubusercontent.com/83285614/176789715-f90c3ea5-faf6-4e49-bdf3-2683b18ce375.png)

# 2. List of measurements exported.
![Screenshot from 2022-06-30 18-29-01](https://user-images.githubusercontent.com/83285614/176789814-29e76874-1060-4681-bbe3-a4853975f510.png)

# 3. Results of the computation for all the list of measurement for a sample of patient.
![Screenshot from 2022-06-30 19-01-23](https://user-images.githubusercontent.com/83285614/176792428-d5c3cb6f-4e56-45c0-95e2-fb24798453a8.png)

# 4. Skeletal measurements signs meaning.
![skeletal_measurement](https://user-images.githubusercontent.com/83285614/176794349-fa99dcc8-bdf7-4518-ba8e-01451ebf05d8.jpeg)

# 5. Linear measurements signs meaning.
![linear_measurement](https://user-images.githubusercontent.com/83285614/176794371-c87e7cba-8242-4149-bbda-5e67e28859cc.jpeg)

# 6. Angular measurements signs meaning.
![angular_measurement](https://user-images.githubusercontent.com/83285614/176794405-c1e283e6-bad2-4da5-b777-991e93c419ce.jpeg)


# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
