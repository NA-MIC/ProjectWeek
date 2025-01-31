Back to [Projects List](../../README.md#ProjectsList)

# Collaborative VR breakout session

## Key Investigators

- Csaba Pinter (Ebatinca / Pixel Medical)
- Simon Drouin (ETS Montreal)

# Project Description

<!-- Add a short paragraph describing the project. -->
Virtual Reality (VR) has a great potential to facilitate communication between clinicians. For example, VR can be used to collaboratively plan a surgical case by manipulating 3D models derived from preoperative scans. Slicer already includes most of the components required to build prototypes for this kind of applications:
- The Virtual Reality module can display everything from Slicer's 3D in VR
- The VolumeRendering and PRISM Rendering modules enable advanced-programmable volume rendering
- The OpenIGTLinkIF module and OpenIGTLink protocol enables communication of medical and tracking data between different devices running Slicer
The Goal of this discussion is to coordinate future development of the above module to enable more natural collaborative interaction in VR.

## Objective

1. Review the current functionality of SlicerVR and PRISM Rendering
1. Discuss planned near future developments in those modules
1. Lay out a vision for the future of interactive VR in Slicer
1. Establish a protocol for Collaborative VR
1. Points for discussion:
   1. Future possibilities for interacting in VR: hand tracking, tool tracking
   1. Need to support different types of tracking in collaborative VR protocols
   1. Should SlicerVR have a fixed set of functionality and interaction paradigm or let users and/or developers choose.

## Progress and Next Steps

1. Potential application of SlicerVR: Learn dental anatomy (Sébastien Erckelbout)
1. Short term changes:
   1. Implement spatial references (e.g. a Floor)
   1. Improve object selection
1. Interaction
   1. Is it worth sharing a code base with Slicer Looking glass?
   1. For developers: need for more control over interaction: disable existing interaction and change behavior
   1. Long term: support for more complex VR controllers and hand tracking
   1. Have interaction settings for different scenarios (inside-out vs outside-in visualization)
1. Collaboration
   1. Currently, collaboration is setup using OpenIGTLinkIF and carefully setting up scenes on both ends. Transforms have to be setup for controllers and HMD
   1. We need to facilitate (automate) connection and scene setup for collaboration
   1. It might be necessary to use a server technology to hold common state (Mike Halle suggested [FireBase](https://firebase.google.com/) previously used)
   1. A matchmaking and communication solution to explore: [Photon](https://doc.photonengine.com/en-us/realtime/current/getting-started/realtime-intro)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

[SlicerVR](https://github.com/KitwareMedical/SlicerVirtualReality)

[PRISMRendering](https://github.com/ETS-vis-interactive/SlicerPRISMRendering)

[PRISMRendering doc](https://githubcomets-vis-interactiveslicerprismrendering.readthedocs.io/en/latest/)
