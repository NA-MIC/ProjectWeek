---
layout: pw39-project

permalink: /:path/
redirect_from:
- /PW39_2023_Montreal/Projects/MobileAugmentedRealityInteractiveNeuronavigator/README.html

project_title: 'MARIN: Mobile Augmented Reality Interactive Neuronavigator (in Slicer)'
category: IGT and Training
presenter_location: In-person

key_investigators:
- name: Mehrdad Asadi
  affiliation: Concordia University
  country: Canada
  
- name: Étienne Léger
  affiliation: Montreal Neurological Institute
  country: Canada
  
- name: Bahar Jahani
  affiliation: Concordia University
  country: Canada

- name: Zahra Asadi
  affiliation: Concordia University
  country: Canada
---

# Project Description

<!-- Add a short paragraph describing the project. -->
[MARIN](https://github.com/AppliedPerceptionLab/MARIN) is an application that can be used in conjunction with a neuronavigation platform to enable in situ AR guidance on a mobile device. It currently supports iOS and works in conjunction with [Ibis](https://github.com/IbisNeuronav/Ibis) (with the additional [MARIN plugins](https://github.com/AppliedPerceptionLab/IbisPluginsExtraMARIN)). The goal of this project is to implement the same support in Slicer.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Add Slicer support for MARIN (provide the same functionalities that Ibis currently does)

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

MARIN is a mobile application that can overlay virtual structures over the live camera feed from a device, enabling *in situ* augmented reality navigation for surgical applications (see image below). The MARIN application itself can interface with any platform, provided that the platform supports real-time communication, can handle tracking and generate 3D renderings. Slicer has all of these capabilities. Communication between Slicer and MARIN can be set-up through the OpenIGTLinkIF module. The main components that will have to be implemented are Slicer modules to handle device configuration and rendering of tracked virtual objects.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

Because MARIN and the OpenIGTLinkIF don't currently support the same video codecs (H264 only for MARIN vs VP9 only for OpenIGTLinkIF), most of this week's effort was focused on extending MARIN to support more codecs as well as support sending unencoded images. Further work could then be done on the Slicer side to enable more codecs as well. This would allow more flexibility and support for more devices. Unencoded frames will be limited in terms of resolution by the available bandwidth.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

MARIN demo, with Ibis:

![teaser_looped_small](https://github.com/NA-MIC/ProjectWeek/assets/17100565/07faf583-2238-4760-8a54-896b75c2f300)

# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->
Article: Léger, É., Reyes, J., Drouin, S., Popa, T., Hall, J. A., Collins, D. L., Kersten-Oertel, M., "MARIN: an Open Source Mobile Augmented Reality Interactive Neuronavigation System", International Journal of Computer Assisted Radiology and Surgery (2020). 
https://doi.org/10.1007/s11548-020-02155-6

Source code repository: [MARIN](https://github.com/AppliedPerceptionLab/MARIN/tree/master)
