Back to [Projects List](../../README.md#ProjectsList)

Automatic Quantification 3D Components

## Key Investigators
- Baptiste Baquero (University of Michigan)
- Maxime Gillot (University of Michigan)
- Lucia Cevidanes (University of Michigan)
- David Allemang (Kitware Inc)
- Jean-Christophe Fillion-Robin (Kitware Inc)

# Project Description
The Automatic Quantification 3D Components(AQ3DC) aims to provide a user-friendly tool that decrease user time for extraction of quantitative image analysis features. AQ3DC is a Slicer extension to automatically compute lists of measurements seleted by users for a single case or a whole study sample, at one or more time points. The current implementation is aimed at automatic computation of 3D components like distances (AP, RL and SI) between points, points to line, midpoint between two points or angles (Pitch, Roll and Yaw), which can be further extended to any type of desired computation/quantitative image analysis. The design of the user interface is currently aimed at quantification of craniofacial dental, skeletal and soft tissue structures.


## Objective

- A. Develop a Slicer extension that will automatically perform angular or linear measurements between landmarks in one or more time points for all patients in a study folder.
- B. Automatically generate the "clinical meaning" of the directionality for the numbers and signs obtained after the computation (skeletal directions: AP,SI,RL; dental directions: Mesio-Distal,Bucco-Lingual,Extrusion-Intrusion, 3D angles: Pitch, Roll and Yaw).
- C. Generate the mid point between two points.

## Approach and Plan

1. May 5,2022- Met with David Allemang and J-Christophe to plan design of AQ3DC and not replicate Markups or Q3DCfunctionalities.
2. May 12, 2022- David A. provide information regarding the markups module and its documentation about the markups module. After teh May 05th meeting, David sagreed that the markups module would not be suitable for this proposed work. as each type of markup must be contained in a different MRML node. For example, you can't have a plane and a line defined by the same markups node. This is the role that DependantMarkups fills.
3. Work on writing the code in the branch https://github.com/baptistebaquero/Q3DCExtension/tree/add-AQ3DC-module of Q3DC extension, focusing on the steps  described below and with feedback of project team members.
4. Pre-selection of the points needed.
5. Import/export excel file with all the measurement needed.
6. Creation of interactive table with the different measurement needed.
7. Computation of linear measurements for one time point and exporting of the data in an excel file.


## Progress and Next Steps

# Progress:
1. Computation of linear measurements for two time points and exporting of the data in an excel file
2. Computation of angles and distances with sign meaning depending on the type of points used
3. Met with David and J-Christophe to discuss overall infrastructure and discuss how to update the code to streamline future maintenance

# Next steps :
1. Computation of mid points.
2. Finalize branch https://github.com/baptistebaquero/Q3DCExtension.git and create a pull request.
3. Update SlicerCMF workflow to document and integrate with AQ3DC.


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
