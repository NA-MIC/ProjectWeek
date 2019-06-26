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
  * Possible solutions:
    * paging data to GPU
    * virtual memory
    * remote rendering / clusters
1. Generating animations
  * Goals:
    * illustrate complex volume data by changing camera, cropping, transfer functions
    * visualize processes (time series, procedure plans, etc)
  * Approaches:
    * generalize sequences with interpolation
    * create 'canned' scripts like rock and rotate modes
    * create keyframe animation system and GUI
1. Other topics as they come up


# Background and References

<!-- Anything people should review to prepare for the discussion -->


# Results of Discussion

<!-- To be filled out after the event. -->


