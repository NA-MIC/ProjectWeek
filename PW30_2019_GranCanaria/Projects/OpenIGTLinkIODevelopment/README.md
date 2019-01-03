Back to [Projects List](../../README.md#ProjectsList)

# OpenIGTLinkIO Development

## Key Investigators

- [Simon Drouin](http://nist.mni.mcgill.ca/?page_id=369) (Montreal Neurological Institute, Canada)
- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- [Kyle Sunderland](http://perk.cs.queensu.ca/users/sunderland) (Queen's University, Canada)

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
<!--Describe progress and next steps in a few bullet points as you are making progress.-->

* To be completed

## Future work

* To be completed 

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
