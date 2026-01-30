---
layout: pw44-project

permalink: /:path/

project_title: Gradient waveform optimisation for microstructure mapping with diffusion MRI
category: Quantification and Computation
presenter_location: 

key_investigators:

- name: Arthur Chakwizira
  affiliation: Brigham and Women's Hospital
  country: Harvard Medical School, USA

---

# Project Description

<!-- Add a short paragraph describing the project. -->


Time-dependent diffusion MRI offers sensitivity to brain tissue microstructure, but has limited specificity. Multiple features of the tissue microstructure tend to map onto the same signal contrast. Multi-dimensional experiment designs using freely modulated gradient waveforms have been proposed as a remedy, with previous work demonstrating the ability to disentangle features such as cell size, cell shape and membrane permeability. However, the waveforms used in previous studies were stochastically generated and a rigorous optimiser remains an unmet need. 



## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->


Develop a gradient waveform optimiser that allows targeting specific tissue characteristics (such as cell size) while respecting hardware constraints and maximising diffusion encoding efficiency




## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->


1. Parameterise gradient waveforms using a set of control points in the Cartesian plane, together with cubic spline interpolation
2. Define a cost function predicting sensitivity to various microstructural properties, using the gradient waveform and analytical microstructure models
3. Set up constraints to account for hardware and time limitations. Enforce a minimum b-value.
4. Choose an appropriate solver



## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->


1. Parameterised waveforms using control points and cubic spline interpolation
2. Defined a cost function evaluating sensitivity using the gradient waveform and microstructure models
3. Imposed constraints to account for hardware (slew rate, gradient amplitude) and echo time. Enforced a minimum b-value of 4000 s/mm2.
4. Chose the patternsearch solver with randomised initial conditions



# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished. -->


Stochastically generated waveforms from previous work, designed for the MAGNUS MRI scanner.
<img width="858" height="293" alt="Image" src="https://github.com/user-attachments/assets/61e1977f-4604-4df5-8c96-921b1cdec0bd" />




Example waveforms from the new optimiser, illustrating both the gradient in time and the encoding power spectrum. These waveforms are optimised for specificity to restricted diffusion (cell size).





<img width="700" height="901" alt="Image" src="https://github.com/user-attachments/assets/7c066a36-402e-43ff-84d0-3db6ee172348" />



# Background and References

<!-- If you developed any software, include link to the source code repository.
     If possible, also add links to sample data, and to any relevant publications. -->


[GitHub repository](https://github.com/arthur-chakwizira/waveform-optimisation)



Previous work presenting the idea of time-dependent diffusion MRI with non-standard waveforms:

- Chakwizira, A., Zhu, A., Foo, T., Westin, C.-F., Szczepankiewicz, F. & Nilsson, M. 2023. Diffusion MRI with free gradient waveforms on a high-performance gradient system: Probing restriction and exchange in the human brain. NeuroImage. 283: 120409

- Chakwizira, A., Westin, C.-F., Brabec, J., Lasič, S., Knutsson, L., Szczepankiewicz, F. & Nilsson, M. 2022. Diffusion MRI with pulsed and free gradient waveforms: Effects of restricted diffusion and exchange. NMR in Biomedicine. n/a(n/a): e4827.

