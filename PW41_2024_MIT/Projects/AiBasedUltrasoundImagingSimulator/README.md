---
layout: pw41-project

permalink: /:path/

project_title: AI-based ultrasound imaging simulator
category: IGT and Training
presenter_location: In-person

key_investigators:

- name: Junichi Tokuda
  affiliation: BWH

- name: Xihan Ma
  affiliation: WPI

- name: Simon Leonard
  affiliation: JHU

- name: Laura Connolly
  affiliation: Queen's

- name: Haichong
  affiliation: Kai) Zhang (WPI

---

# Project Description

<!-- Add a short paragraph describing the project. -->


We will discuss strategies to integrate AI-based ultrasound imaging simulators in multiple platforms for medical robotics and IGT, including the Gazebo dynamic simulator and PLUS.

Demo video is available at [GitHub](https://github.com/MXHsj/rus_sim_visuals/)

![2024-03-18_rus_sim1 0_beta](https://github.com/MXHsj/ProjectWeek/assets/31639301/7be20c1a-608b-4207-8e63-44429c663118)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. **Model** Improve the model - make the simulated ultrasound image more realistic
2. **Architecture** Explore the fast way to package the model into applications.


## Approach and Plan

1. Model improvement
   - The current model doesn't take account of tissue attenuation properties. Explore the use of CT segmentation data (or total segmentator).
   - To use the neuron network to accelerate the computation speed.
2. Architecture
   - Create an independent library for CT-ultrasound conversion. This library takes a 2D resampled CT data that is aligned to the (virtual) ultrasound probe, and generate a corresponding simulated ultrasound image.
   - Integration with existing platforms, including Gazebo, Slicer, PLUS (to be discussed with the community)
   - 



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


- Progress
    1. Built pipeline to generate ```sound speed map``` and ```density map``` from CT total segmentation.

        ![fig1](https://github.com/MXHsj/ProjectWeek/assets/31639301/378084c3-90fe-48ca-bdb5-bb0299c05800=x200)

    2. Built pipeline using k-wave to simulate B-mode ultrasound in 3-dimensional, i.e., the ultrasound beam thickness is taken into account. Tissue speed of sound and density are taken into acount in the simulation.

- Next steps
    1. Debug simulation settings, including transducer properties, beam transmit/receive pattern, etc.
    2. Generate sufficient CT(segmented)-to-simulated ultrasound pairs for neural network training. The network will learn the mapping from CT to ultrasound and achieve real-time processing speed




# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


_No response_



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


_No response_

