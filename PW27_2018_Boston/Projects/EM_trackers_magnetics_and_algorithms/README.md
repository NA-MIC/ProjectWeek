Back to [Projects List](../../README.md#ProjectsList)

# EM Trackers Magnetics and Algorithms

## Key Investigators

- Peter Traneus Anderson (Retired)

# Project Description

Discuss the electromagnetics and algorithms of electromagnetic trackers, both at the workshop and as a starting point for later writeups. Math requirement: understand 3D rotation matrices.

## Objective

- Objective A. Find out level of interest.
- Objective B. Decide what to write-up at and after the workshop and where to put it.
- Objective C. Expand list of references.
- Objective D. Electromagnetic trackers have been used for over forty years in simple augmented-reality (AR) systems called Helmet-Mounted Sights. Pete wonders to what extent the ancient simple AR technology (whether EM or optical or other tracker is used) might be relevant to modern AR efforts.

## Approach and Plan

1. Those who are interested can find me at the workshop: look for a bearded old man in a longkilt.
2. Pete plans to attend the VR/AR breakout session to listen and learn.

## Progress and Next Steps
1. Level of interest is small to zero at the Project Week, though some use EM trackers in their work.
2. From discussions this year and years ago, an open-source research tracker should use off-the-shelf data-acquisition electronics, and concentrate specialized efforts on coils, cables, software and algorithms.
3. If an application can be tracked optically, that application should be tracked optically. Advances in cameras, computers, and algorithms have made optical trackers low-cost and accurate (no subtle field-distortion effects). Optical trackers tracking passive retroreflectors are also inherently wireless. Also, optical trackers are obvious in how they work, and obvious in when they don't work (when the cameras can't see the objects being tracked). Thus, there are few remaining applications for 6DOF EM trackers using tricoil receivers, but there are still some users.
4. 5DOF EM trackers using single-coil receivers are still useful for tracking catheters, as the body is opaque to light.
5. The Microsoft Hololens optically adds displayed data to the ambient direct-view image, so is an elaborated descendent of Polhemus's 1970s Helmet-Mounted Sight system. The Hololens passively optically tracks its environment to determine its position and orientation.
6. VR/AR might be replaced by sitting very close to a 4K monitor, so the monitor is larger than the user's field of view. The
user would put their hands (holding handheld controllers) behind the monitor to manipulate virtual objects. Track the user's head, so 3D depth perception occurs through different-depth objects changing perspective as the head is moved.
7. Pete thanks one of the presenters for showing the presenter's laptop computer running in nighttime mode with blue display turned off. Pete has successfully added this option in hardware (by opening VGA blue video signal) to his desktop computer.

## Pete thanks those with whom he shared conversations, listed here in random order:

1. Steve Pieper
2. Gregory Sharp
3. Tina Kapur
4. Sonia Pujol
5. Tamas Ungi
6. Simon Drouin
7. Nicole Wake
8. Mark Asselin
9. Longquan Chen
10. Jean-Christophe Fillion-Robin
11. Adam Rankin
12. Isaiah Norton
13. Andrey Feodorov
14. Gino Gulamhussene
15. Albian Hernandez-Guedes
16. Joost Van Griethuysen
17. Joseph Schornak

# Illustrations

No new ones; see Background and References for old ones.

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!--![Description of picture](Example2.jpg)-->

<!--![Some more images](Example2.jpg)-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [6DOF emtracker simulator and references](https://github.com/traneus/emtrackers)
- [Some documentation and references](https://na-mic.org/wiki/Open_Source_Electromagnetic_Trackers)
- [traneus's breadboard 6DOF EM tracker](https://web.archive.org/web/20151002101401/http://home.comcast.net/~traneus/dry_emtrackertricoil.htm)
- [traneus's PhD dissertation on an EM tracker](https://web.archive.org/web/20151002101400/http://home.comcast.net/~traneus/thesis.pdf)
- [four figures in traneus's dissertation](https://web.archive.org/web/20151002101400/http://home.comcast.net/~traneus/thesifig.pdf)
