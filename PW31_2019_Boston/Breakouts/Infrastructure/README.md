Back to [Project Week](../../README.md)

# Slicer Infrastructure Brainstorming

* 4-5 pm Wednesday Jun 26, 2019
* Room 32D-407

## Organizers

- Steve Pieper (Isomics)
- Andras Lasso (Queens)
- Jean-Christophe Fillion-Robin (Kitware)
- Murat Maga (University of Washington (remote)

# Breakout Description

As we continue to work on Slicer version 5, there is an opportunity to make somewhat major changes and to add features
to address new use cases and user communities.

## Agenda

<!-- Describe topics and schedule. -->

1. Rendering of large volumes
  * Goals:
    * data too big for GPU memory
    * data too big for CPU memory
    * better rendering
      * multiple volumes
      * nonlinear transforms
      * photorealistic effects
  * Possible solutions:
    * paging data to GPU
    * virtual memory
    * remote rendering / clusters
2. Generating animations
  * Goals:
    * illustrate complex volume data by changing camera, cropping, transfer functions
    * visualize processes (time series, procedure plans, etc)
  * Approaches:
    * generalize sequences with interpolation
    * create 'canned' scripts like rock and rotate modes
    * create keyframe animation system and GUI
3. Other topics as they come up


# Background and References

<!-- Anything people should review to prepare for the discussion -->


# Results of Discussion

<!-- To be filled out after the event. -->

## Volume Rendering

* Need to fix GPU use cases first
  - better error / warning messages
  - on-the-fly resampling to fit in memory
* Sweet spot seems to be looking at pyramid encoding options
  - file formats like HDF 5
  - servers like dicomweb for larger data
  - there's some precedent but nothing completely standard at the moment

## Keyframing

* Good to build on ScreenCapture and Sequences
* See if we can build something 'simple' something like powerpoint build effects in ScreenCapture
* Longer term project to build a nice keyframe/timeline slider (Kitware will follow up with Murat on that)
