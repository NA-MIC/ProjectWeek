Back to [Projects List](../../README.md#ProjectsList)

# GPU Rigid Registration

## Key Investigators
- Gelel Rezig (Ecole de technologie supérieur, Montréal, Canada)
- Houssem Eddine Gueziri (Montreal Neurological Institute and Hopital, Canada)
- Simon Drouin (Ecole de technologie supérieur, Montréal, Canada)

# Project Description
<!-- Add a short paragraph describing the project. -->
With this project, we would like to add a new feature to Slicer.
The goal of this project is to extract code from an opensource software for image-based neurosurgery guidance: IBIS Neuronav.
This code in C++ aims to perform registration between different images using the GPU. It is located in an IBIS Neuronav 
plugin. Then, it will be implemented in Slicer to be available for all users. 

## Long-term Objective
1. Extract GPU registration code from IBIS Neuronav to an independent library (done in PW35, see extracted lib [here](https://github.com/IbisNeuronav/GPURigidRegistrationLib) )
2. Create a standalone command-line application to register images (partly done in PW35)
3. Create a Slicer module that replicates the functionality of Ibis using the independent library (TODO)

## Approach and Plan
1. Implement command-line parameters in the standalone app to support all options available in the Ibis GUI for the registration plugin
2. Write a test suite using the command-line application.
3. Build a prototype for the Slicer registration module. Some questions remain:
  * Should the first iteration use the CLI interface?
  * How to build and distribute Slicer modules with OpenCL support?

## Progress and Next Steps

# Illustrations
![Registration on real time with GPU](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/GPURigidRegistration/gpu-rigid-reg.gif)

# Background and References
Webpage and GitHub repositories with relevant code:
- [Ibis Neuronav](http://ibisneuronav.org)
- [Ibis Neuronav on GitHub](https://github.com/IbisNeuronav/Ibis)
- [New GPURigidRegistration lib](https://github.com/IbisNeuronav/GPURigidRegistrationLib)
