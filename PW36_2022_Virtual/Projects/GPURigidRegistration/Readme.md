Back to [Projects List](../../README.md#ProjectsList)

# GPU Rigid Registration for Neuronavigation (from Ibis)

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
The objective of the second project is to recover another functionality in the same way: the conversion of a minc file into mha ([SequenceIO](https://github.com/IbisNeuronav/Ibis/tree/master/IbisPlugins/SequenceIO)).

## Long-term Objective
1. Extract GPU registration code from IBIS Neuronav to an independent library (done in PW35, see extracted lib [here](https://github.com/IbisNeuronav/GPURigidRegistrationLib) )
2. Create a standalone command-line application to register images (partly done in PW35)
3. Create a Slicer module that replicates the functionality of Ibis using the independent library (TODO)

2nd project (New)
1. Extract the converter minc/mha (SequenceIO) code from IBIS Neuronav to an independent library 
2. Create a standalone command-line application to convert
3. Create a Slicer module that replicates the functionality of Ibis using the independent library

## Approach and Plan
1. Implement command-line parameters in the standalone app to support all options available in the Ibis GUI for the registration plugin
2. Write a test suite using the command-line application.
3. Build a prototype for the Slicer registration module. Some questions remain:
  * Should the first iteration use the CLI interface?
  * How to build and distribute Slicer modules with OpenCL support?

2nd project
1. Implement command-line parameters in the standalone app to support all options available in the Ibis GUI for the convertor plugin
2. Write a test suite using the command-line application.

## Progress and Next Steps

1. The GPU RegidRegistration Lib is available to be used by command line [here](https://github.com/IbisNeuronav/GPURigidRegistrationLib) . (DONE)
2. Make modifications for Ibis neuro uses this library to avoid code duplication. (In progress)
3. Implementation of the solution in slicer. (Next Step)

 The second project
1. Extract the converter minc/mha (SequenceIO) code from IBIS Neuronav to an independent library (in progress) [here](https://github.com/rggelel/SequenceIo) 
2. Make modifications for Ibis neuro uses this library to avoid code duplication. (Next step)
3. Implementation of the solution in slicer. (Next Step)

# Illustrations
![Registration on real time with GPU](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/GPURigidRegistration/gpu-rigid-reg.gif)

# Background and References
Webpage and GitHub repositories with relevant code:
- [Ibis Neuronav](http://ibisneuronav.org)
- [Ibis Neuronav on GitHub](https://github.com/IbisNeuronav/Ibis)
- [New GPURigidRegistration lib](https://github.com/IbisNeuronav/GPURigidRegistrationLib)
- [SequenceIO on Ibis Neuronav](https://github.com/IbisNeuronav/Ibis/tree/master/IbisPlugins/SequenceIO)
