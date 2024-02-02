---
layout: pw40-project

permalink: /:path/

project_title: SlicerArduino
category: Infrastructure
presenter_location: In-person

key_investigators:

- name: Paolo Zaffino
  affiliation: Magna Graecia University of Catanzaro
  country: Italy

- name: Maria Francesca Spadea
  affiliation: Karlsruhe Institute of Technology
  country: Germany

---

# Project Description

<!-- Add a short paragraph describing the project. -->

[SlicerArduino](https://www.mdpi.com/2306-5354/7/3/109) is a Slicer extension that allows to stream data from/to [Arduino](https://www.arduino.cc/) (and Arduino-like) board.
The extension is already deployed but several improvements can be made.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1.  Add Bluetooth support
2.  Manage connection drop
3.  Think about switching from pyserial to qt serial module

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1.  Edit SlicerArduino code having Arduino board with Bluetooth module on the side
2.  Discuss with people about switching from pyserial to qt serial module
3.  Manage connection drop

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Bluetooth connection was investigated. Preliminary tests were done just by interfacing Arduino board with the computer, without including Slicer in the loop (for the moment).
2.  Connection drop management is now implemented and working. Right now it is in a separate git branch, some code cleanup is required.
    When the connection drops a vtkErrorEvent is invoked on the arduinoNode and a popup appears to the user.
4.  QSerialPort is not included by default in the current Slicer build but it can be done.
    Performance/feasibility tests have to be carried on to understand if migration is worth it.
5.  We had a (very nice and useful) meeting to discuss SlicerArduino both from a developer and user point of view.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->

![image](https://github.com/NA-MIC/ProjectWeek/assets/4259198/28afb312-9ae4-4db7-a54a-09a2fc0a9585)

![97f6abbf-30c6-4562-a96a-f2c6a6bfe922](https://github.com/NA-MIC/ProjectWeek/assets/4259198/e523bf25-cf5c-46e7-85f0-0fb0f3b03fc8)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->

[SlicerArduino paper](https://www.mdpi.com/2306-5354/7/3/109)
[SlicerArduino GitHub page](https://github.com/pzaffino/SlicerArduinoController)
[SlicerArduino website](https://pzaffino.github.io/SlicerArduinoController/)
