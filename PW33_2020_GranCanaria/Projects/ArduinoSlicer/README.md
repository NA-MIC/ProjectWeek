Back to [Projects List](../../README.md#ProjectsList)

# Arduino Slicer

## Key Investigators

- Paolo Zaffino (Magna Graecia University of Catanzaro, Italy)
- Andras Lasso (Queen's, Canada)
- Mike Halle (Brigham and Women’s Hospital and Harvard Medical School, USA)
- Steve Pieper (Isomics, USA)
- Attila Nagy (University of Szeged, Szeged, Hungary)
- Badiaa Ait Ahmed (University Abdelmalek Essaâdi, Morocco)
- Nayra Pumar Carreras (University of Las Palmas de Gran Canaria, Spain)
- Mark Asselin (ACMIT Gmbh / Queen’s University, Canada)
- Everyone else is interested in

# Project Description

<!-- Add a short paragraph describing the project. -->
Arduino is a well know and widely used open source microcontroller. Is is extremely cheap (10-20 €/$) and a plenty of sensors and actuators have been desined for this platform.
The idea is to implement a link between 3D Slicer and Arudino.
Slicer IGT offers an outstanding solution for connecting hardware, but for some entry-level users/students can be difficult to use. We want to develop a thin layer of code to connect cheap hardware (Arduino and its sensor/actuators). In this way the user will have a simple way for linking hardaware, being aware that is a solution that does not offer the full options available in SlicerIGT.
It can be useful for students and for not complex data/instruction stream.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. The main aim right now is to colled ideas/comments/suggestions from experts.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Discuss with people that are already using/developing Arduino stuff.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Interesting a breakout session, discussing with experts and people interested in
2. We decided to not use SlicerIGT to keep it as simple as possible
3. We decided to create an extension with multiple modules inside
4. The first layer of code was written (thanks to Andras!)

   https://github.com/pzaffino/SlicerArduinoController

5. The next step will be to refine the link module and to start writing more modules (one for each possible application).

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
