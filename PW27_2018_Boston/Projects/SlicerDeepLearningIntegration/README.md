Back to [Projects List](../../README.md#ProjectsList)

# Deep Learning Integration in Slicer

## Key Investigators

- Jorge Onieva (BWH)
- Raúl San José (BWH)
- Roya Khajavi
- Alireza Mehrtash
- Andrey Fedorov

# Project Description

Integrate a lung segmentation algorithm based on Deep Learning in Slicer.

## Objective

1. Develop a proof of concept to test the integration of Keras+Tensorflow tools in Slicer
1. Create a Slicer package that can be distributed with these features


## Approach and Plan

1. Integrate the algorithm+pretrained models in CIP (see CIPDeepLearningLungSegmentation).
1. Compile Slicer against a customized Python that includes all the CIP required components
1. Pack Slicer with that Python version

## Progress and Next Steps

1. This integration was done through the CustomSlicerGenerator in MacOS and Linux.
1. Luckily, it would be obsolete in Slicer 5!! A template with a Python distribution based on Anaconda or others may be used
1. Also, we found out other extensions like DeepInfer and TOOMCAT that may be useful in the meantime
