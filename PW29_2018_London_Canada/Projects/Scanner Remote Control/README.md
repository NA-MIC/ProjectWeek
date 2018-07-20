# MRI Scanner Remote Control

# Key Investigators
- Ahmed Mahran (Brigham and Women's Hospital)
- Junichi Tokuda (Brigham and Women's Hospital)
- Nobuhiko Hata  (Brigham and Women's Hospital) 
- Franklin King (Brigham and Women's Hospital)
- Jean-Christophe Fillion-Robin (Kitware Inc.)


# Project Description
Establish network communication between SRC and 3D Slicer to control MR's scan plane, and reterieve real-time images from the scanner remotely over the local area network.
Python script running a JSON-based proprietary is used to communicate between the MR scanner and 3Dslicer.

<!--
## Objective
1. Objective A. Describe it in 1-2 sentences. 
1. Objective B. Describe it in 1-2 sentences. 
1. Objective C. Describe it in 1-2 sentences. 

## Approach and Plan

1. Describe planned approach to reach objectives.
1. ...
1. ...

-->

## Progress and Next Steps

* Improved associated python package (may be release publicly in the future)
  * change name to `scanner_remove_control`
  * update infrastructure to
    * compute coverage
    * execute test using pytest, start/stop scanner simulator automatically
    
* Discussed approach to integrate the package with Slicer. Few options:
  * Switch the implementation to use [websocket-client](https://github.com/websocket-client/websocket-client) instead of [websockets](https://pypi.org/project/websockets/) so that it works with Python 2
  * Leverage OpenIGTLink to send data to Slicer

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- Source code: https://github.com/YourUser/YourRepository
- Documentation: https://link.to.docs
- Test data: https://link.to.test.data
