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
The Automatic Quantification 3D Components(AQ3DC) was developed during Namic-project 37 is now available in Slicer Q3DC extension.

The Automatic Quantification 3D Components(AQ3DC) aims to provide a user-friendly automated tool that decrease user time for extraction of quantitative
image analysis features. 
AQ3DC is a Slicer extension to automatically compute lists of measurements seleted by users for a single case or a whole
study sample, at one or more time points. 
The current implementation is aimed at automatic computation of 3D components like distances (AP, RL and SI) 
between points, points to line, midpoint between two points or angles (Pitch, Roll and Yaw), interpretation of directionality,which can be further extended to any type of desired computation/quantitative image analysis. The design of the user interface is currently aimed at quantification of craniofacial dental,  skeletal and soft tissue structures. 

This project to to get input regarding : 
1. refactoring of the code to maintainable and more robust 
2. discuss updates that solve AQ3DC's issues
3. verify remaining duplicates and hard coded components
4. add tests to the module 
5. add user documentation.



- Project link : https://github.com/DCBIA-OrthoLab/Q3DCExtension
- Refactoring link : https://github.com/HUTIN1/Q3DCExtension 



## Objectives

- A. Receive guidance on whether the new types help encapsulate certain components in the code.
- B. Receive guidance on how to correct overload of the Python protocols for Group_landmark, MyList, and MyDict. 
- C. Receive input regarding how to improve other utilities like Line, Measure, Point, etc. 
- D.  Clarify new functionalites added to resolve issues or improve flexibility:
  - Added Midpoints meaning (interpretation of direction);
  - Added choice of complamteray angel  greater than 90 degress 
  - Added new functionality that allows users to upload landmark legends as excel files. This modifies the currently deployed AQ3DC code that displays only specific craniofacial dental,  skeletal and soft tissue structure landmarks that were hard coded, and any different landmarks would appear as "other" landmarks.
  - Added report error to detect where in the computation or lanmdmark list files an error  occured. This help users to identify if  for nay patient or landmark  their files have typos or missing data. 
- E. Update Readme in Github  DCBIA/Orhtolab
- F. Create documentation on SlicerCMF ( https://cmf.slicer.org/)

## Approach and Plan

1. Completed Users beta test of AQ3DC's refactoring 
2. Review code's robustness and clarity
3. Pull requests the code.
4. Update SlicerCMF workflow to document and integrate with AQ3DC.


## Progress and Next Steps

# Progress:
1. Refactoring codes
2. Resolved old issue
3. Weekly review of code clarity with David

# Next steps :

1. Add class test
1. Make the new types help encapsulate certain components in the code.
2. Correct overload of the Python protocols for Group_landmark, MyList, and MyDict. 
3. Improve other utilities like Line, Measure, Point, etc. Update SlicerCMF workflow to document and integrate with AQ3DC.
4. Verify remaining duplicates and hard coded components
5- Add tests to the module 
6- Add user documentation.
7. Update README
8- Pull request



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
