# MRI Scanner Remote Control

# Key Investigators
- Ahmed Mahran (Brigham and Women's Hospital)
- Franklin King (Brigham and Women's Hospital) 
- Nobuhiko Hata  (Brigham and Women's Hospital) 



# Project Description
Establish network communication between SRC and 3D Slicer to control MR's scan plane, and reterieve real-time images from the scanner remotely over the local area network.
Python script running a JSON-based proprietary is used to communicate between the MR scanner and 3Dslicer.

## Objective
1. Establish Communication between MRI simulator and 3Dslicer 
2. Use volume reslice driver to Set a new scan position and orientation
3. Reterieve DICOM images from simulator to 3Dslicer

## Approach and Plan

1. Define coordinate sytem of scanner
2. Apply transform to convert from RAS To Scanner Coordinates (LPS)
3. create needle model and use Volume Reslice Driver module to define a new orientation. Send coordinates to simulator

## Progress and Next Steps



# Illustrations

https://github.com/mahrana/ProjectWeek/blob/master/Screenshot%20(6).png

https://github.com/mahrana/ProjectWeek/blob/master/Screenshot%20(7).png

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
