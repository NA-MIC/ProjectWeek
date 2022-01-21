Back to [Projects List](../../README.md#ProjectsList)

# El Cheapo Tracking

## Key Investigators

- Steve Pieper (Isomics)
- Gabor Fichtinger (Queens)
- YOU

# Project Description

Investigate less expensive but still good tracking for IGT.  Modern AR/VR devices use inside-out tracking with IMUs, cameras, lidar, and other sensors (e.g. in phones and glasses).
These are small enough and becoming (maybe?) good enough to consider for IGT.
Would these be options for NousNav or the SlicerTMS projects?

## Objective

1. Make a plan for determining accuracy and utility of options
2. Plan any implementation efforts or further experiments
3. Consider issues like form-factor, sterilization, re-usability, etc.


## Approach and Plan

1. Survey developments in the field pushed by AR/VR devices
2. Look at any prototypes, e.g. [Steve's WebXR](https://github.com/pieper/SlicerWeb/blob/master/WebServer/docroot/WebXR-controller/index.html) experiment
3. Determine next steps

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

### Progress
1. Improved demo to work with https using letsencript on Google Cloud virtual machine running Slicer
2. Added touch screen events to control attributes of Slicer model (brighter yellow when touching the screen).
3. Gave demos to colleagues at the [Wednesday IGT breakout](https://docs.google.com/document/d/1mwTbzy_ulATfrU97cFfQM_ikhz1CUr1xaocj6lp6c8w/edit#heading=h.296xjyux0jir) and discussed the tradeoffs of intrinsict tracking vs EM and extrinsic optical tracking

### Next steps
1. Explore the use of phone-based tracking for SlicerTMS research
2. Experiment with local rendering and touch interactions on phone mixed with remote rendering and computation on CPU/GPU with Slicer
3. Consider developing native phone app to avoid https performance overhead vs upgrading Slicer's web server to support web sockets for faster performance
4. Brainstorm about other applications of this technology
5. Monitor developments of intrinsic tracking systems in non-phone form factors for use in other tracking scenarios (e.g. in IGT)

# Illustrations


[![Phone controller demo (click to see video)](https://user-images.githubusercontent.com/126077/150543016-34926be4-7eca-4c47-87c0-95f0fdb29230.png)](https://youtu.be/kQKskHYlpQE "Phone Controller Demo (click to view on youtube")


* Demo uses moto g100 Android phone that includes Qualcom chips for tracking.

# Background and References

* https://github.com/pieper/SlicerWeb/blob/master/WebServer/docroot/WebXR-controller/index.html
* https://immersive-web.github.io/webxr-samples/
* https://www.qualcomm.com/research/cognitive-technologies/immersive-experiences/augmented-reality
* https://www.qualcomm.com/news/onq/2021/08/16/how-snapdragon-xr1-powers-lenovo-thinkreality-a3-smart-glasses-and-moto-g100
