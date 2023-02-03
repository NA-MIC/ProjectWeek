Back to [Projects List](../../README.md#ProjectsList)

# How to setup and run 3D Slicer on an AWS cloud server

## Key Investigators

*   Rudolf Bumm (KSGR)
*   Steve Pieper (Isomics)
*   Gang Fu (AWS)
*   Qing Liu (AWS)

# Project Description

How to setup and run 3D Slicer on an AWS cloud server

## Objective

For this workshop, we want to set up a 3D Slicer EC2 AWS cloud instance that can be scaled based on hardware needs and can be used for deep learning. 

The EC2 Windows Cloud server instance should natively run 3D Slicer and have NVIDIA GPU and CUDA support. 

[The necessary steps are documented here](./HowToSetupAWSEC2Server.md).

## Approach and Plan

An AWS [CloudFormation template](https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/WindowsServer2019-NICE-DCV.yaml) was designed to install 

*   3D Slicer stable
*   Firefox
*   latest NVIDIA drivers
*   git
*   MONAILabel
*   TotalSegmentator
*   lungmask 
*   S3 bucket

A mechanism how to share result data between a working group will be discussed, with the option to install a 3dviewer.net server instance or use a S3 bucket.

The speed of general system setup, up- and downscaling as well as running costs will be evaluated.

## Progress and Next Steps

The use of the EC2 instances was comfortable and reliable during the Project week. The performance of the g5x4large instance was a bit slower than the reference GTX 3070 Ti, although the GPU load never was on the upper limits. Up and downgrading the EC2 instance was comfortable and did not touch any component of the installed programs. The cost of running a g5.x4large GPU instance is around 2 $ per hour. The Cloudformation template proved very helpful. 

Setting up the EC2 instance for interactive 3D purposes makes only sense if connection speeds to and from the server are around 50 Mbps. 

# Illustrations

![image](https://user-images.githubusercontent.com/18140094/211152360-f6e0d66b-aa84-4109-86d5-eedf404fd528.png)

Fig. 1 Raspberry 4 Model B running 3D Slicer on an EC2 instance in Chromium browser

# Background and References

[Recommended GPU instances for deep learning purposes](https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html)
