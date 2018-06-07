Back to [Projects List](../../README.md#ProjectsList)

# OpenIGTLinkIO Development

## Key Investigators

- [Simon Drouin](http://nist.mni.mcgill.ca/?page_id=369) (Montreal Neurological Institute, Canada)
- [Andras Lasso](http://perk.cs.queensu.ca/users/lasso) (Queen's University, Canada)
- [Csaba Pinter](http://perk.cs.queensu.ca/users/pinter) (Queen's University, Canada)
- [Ole Vegard Solberg](https://www.sintef.no/alle-ansatte/ansatt/?empId=541) (SINTEF, Trondheim, Norway)
- [Geir Arne Tangen](https://www.sintef.no/alle-ansatte/ansatt/?empId=1605) (SINTEF, Trondheim, Norway)

## Participating remotely

- [Adam Rankin](http://www.imaging.robarts.ca/petergrp/node/113) (Robarts Research Institute, Canada)
- [Kyle Sunderland](http://perk.cs.queensu.ca/users/sunderland) (Queen's University, Canada)
- [Mark Asselin](http://perk.cs.queensu.ca/users/asselin) (Queen's University, Canada)
- [Étienne Léger](http://www.ap-lab.ca/people/etienneleger/) (Concordia University)
- [Longquan Chen](https://www.linkedin.com/in/longquan-chen-68672340/) (Brigham and Women's Hospital)
- [Tamas Ungi](http://perk.cs.queensu.ca/users/ungi) (Perk Lab)

# Project Description

## Objective

* [Plus Toolkit](http://www.plustoolkit.org) provides access to numerous hardware devices (imaging devices, tracking devices, navigations systems, sensors, etc.) and makes it available through [OpenIGTLink](http://www.openigtlink.org) protocol
* This group has created a common library, [OpenIGTLinkIO](http://igsio.github.io) that simplifies the integration of Plus (and OpenIGTLink-compatible devices or software) into different programs and :
  * Ensure software interoperability between [Slicer](https://www.slicer.org/), [MITK](http://mitk.org/), [CustusX](https://www.custusx.org/), [Ibis Neuronav](http://ibisneuronav.org/) and potentially other imaging platforms.
  * Share software maintenance workload
  * Make it easy to share new features
  * Add specific features for tracked ultrasound and and augmented reality in surgical navigation

## Approach and Plan

* Complete and improve refactoring of command messages.
* Embed information about images in the image message itself (currently sent as string messages in CustusX) 
* Fix limited length device names (potential solution: troncate long names and put complete name in meta-data)
* Add possibility to use external video compression codecs in OpenIGTLinkIO even if they are not supported by OpenIGTLink (Longquan)
* Create a command-line example in OpenIGTLinkIO that implements a simple but complete tracked US session:
  * launch a PlusServer with a config that simulates US and includes tracking data
  * Connect to the server
  * Capture a few frames and prints the metadata
  * Changes US acquisition parameters
  * Capture more data
  * Export acquired images before shutting down
* Improve Plus server launcher

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [Source code](https://github.com/IGSIO/OpenIGTLinkIO)
- [IGSIO web page](http://igsio.github.io/)
