Back to [Projects List](../../README.md#ProjectsList)

# OpenIGTLinkIO Development

## Key Investigators

- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- [Kyle Sunderland](http://perk.cs.queensu.ca/users/sunderland) (Queen's University, Canada)
- Houssem Gueziri

# Project Description

## Objective

* [Plus Toolkit](http://www.plustoolkit.org) provides access to numerous hardware devices (imaging devices, tracking devices, navigations systems, sensors, etc.) and makes it available through [OpenIGTLink](http://www.openigtlink.org) protocol
* This group has created a common library, [OpenIGTLinkIO](http://igsio.github.io) that simplifies the integration of Plus (and OpenIGTLink-compatible devices or software) into different programs and :
  * Ensure software interoperability between [Slicer](https://www.slicer.org/), [MITK](http://mitk.org/), [CustusX](https://www.custusx.org/), [Ibis Neuronav](http://ibisneuronav.org/) and potentially other imaging platforms.
  * Share software maintenance workload
  * Make it easy to share new features
  * Add specific features for tracked ultrasound and and augmented reality in surgical navigation

## Approach and Plan

* Ensure that Plus, OpenIGTLinkIO, SlicerIGT features meet needs of groups participating at the project week
* Improve support for ultrasound image acquisition from BK ultrasound systems

## Progress and Next Steps

* Worked on the implementation of a Python based OpenIGTLink implementation for sending and receiving OpenIGTLink messages ([pyIGTLink](https://github.com/Sunderlandkyl/pyIGTLink/tree/pyIGTLink_client))
* Investigate issues with missing tool status metadata for transforms received from Plus
* Coordinated with other projects regarding the implementation and utilization of Plus and OpenIGTLink for image guided applications
  - [MRINeedleGuidance](https://github.com/NA-MIC/ProjectWeek/tree/master/PW30_2019_GranCanaria/Projects/MRINeedleGuidance)
  - [DataGlove](https://github.com/NA-MIC/ProjectWeek/tree/master/PW30_2019_GranCanaria/Projects/Data-glove_for_virtual_operations)


## Future work

* Improve robustness of pyIGTLink implementation and ensure support for both Python 2 and 3 
* Continue to maintain and develop Plus and OpenIGTLinkIO
* If you have any questions or issues, feel free to submit an issue on [GitHub](https://github.com/PlusToolkit/PlusLib/issues)

# Illustrations

Example image of CustusX using PLUS to receive ultrasound sector parameters as OpenIGTLink meta information from the BK interface in PLUS, by using OpenIGTLinkIO for the client in CustusX. The example is just streaming a random ultrasound image, so it don't match the ultrasound probe used in the example.
![CustusX](CustusX_screendump.png)

| Ultrasound systems supported by Plus toolkit | Live ultrasound image acquisition in 3D Slicer |
| --- | --- |
| ![](https://plustoolkit.github.io/assets/images/Ultrasound.png) | ![](https://plustoolkit.github.io/assets/images/PlusServer.png) |

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [Source code](https://github.com/IGSIO/OpenIGTLinkIO)
- [IGSIO web page](http://igsio.github.io/)
