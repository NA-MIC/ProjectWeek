Back to [Projects List](../../README.md#ProjectsList)

# Visualization of catheter path based on an electromagnetic tracking with TMR sensors

## Key Investigators
- Wenran Cai (University of Tokyo)
- Kazuaki Hara (University of Tokyo)
- Rina Nagano (University of Tokyo)
- Junichi Tokuda (Brigham and Women's Hospital

# Project Description
Intra-arterial chemotherapy requires knowing the position of the catheter tip in the body in order to insert the catheter accurately. 
Currently, the position of the catheter is confirmed by acquiring an X-ray image. However, repeated acquisition of X-ray images increases
radiation exposure to the patient and healthcare personnel who are involved in the procedure. 

We have been developing a new catheter trakcing system using electromagnetic tracking system with a TMR (Tunnel Magnetoresistance) sensor,
which provides real-time travel distance of the catheter tip. By combining the anatomical map created from the preoperative CT image and
the distance information, one can potentially track the tip in the 3D space intraoperatively without repeated X-ray acquisition. 

## Objective
We will incorporate the new catheter tracking system into 3D Slicer for the reconstruction and visualization of the catheter shape. 

## Approach and Plan

A vessel model will be reconstructed from a preoperative 3D CT.
During the operation, real-time data from the sensor is imported into 3D Slicer via OpenIGTLink.
The imported data will be used for 1) displaying the distance information on the 3D Slicer window, and 2) reconstruct the shape of the catheter using the anatomical map and the distance.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
