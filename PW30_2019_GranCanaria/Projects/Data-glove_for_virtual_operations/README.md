Back to [Projects List](../../README.md#ProjectsList)

# Data-glove for virtual operations

## Key Investigators

- Endre Vecsernyés (University of Szeged)
- Attila Nagy (University of Szeged)
- Kitti Farkas (University of Szeged)
- Bence Horvath (University of Szeged)
- Kyle Sunderland (Queen's University)
- Eleni Siampli (Children's National)
- Andras Lasso (Queen's University)

# Project Description

We built a data-glove that tracks hand movements. Our goal is to connect it to Slicer with OpenIGTLink or with the Plus toolkit. The glove has a simple IMU (with 3-axis gyroscope and 3-axis accelerometer /MPU9250/) and a processing unit (Arduino Uno).


## Objective

1. Stable connections between the glove and the Slicer

## Approach and Plan

1. Making connection between the glove and Slicer with Plus toolkit
1. Plans for the future

## Progress and Next Steps

1. The glove can be used as an orientation sensor.
1. For virtual operations we need a different approach and decvice. (For example Leap Motion)


<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

![The glove](glove.jpg)

![Arduino and the IMU](hardware1.jpg)

![The IMU's other side](hardware2.jpg)

Result:

![Result](20190201_095221.gif)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->
- Previous work in Slicer using PhidgetSpatial 3/3/3 sensor: http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Kotwicz2014.pdf
- MPU9250 Datasheet: https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/MPU9250REV1.0.pdf
- Arduino Uno website: https://store.arduino.cc/arduino-uno-rev3
- MPU9250-Arduino library: https://github.com/bolderflight/MPU9250
- Code for the orientation sensor: https://github.com/riduid/MPU9250-with-Arduino
- Leap Motion website: https://www.leapmotion.com/


<!--- Source code: https://github.com/YourUser/YourRepository  -->
<!--- Documentation: https://link.to.docs  -->
<!--- Test data: https://link.to.test.data  -->

