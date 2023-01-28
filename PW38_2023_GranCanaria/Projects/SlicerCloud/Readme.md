Back to [Projects List](../../README.md#ProjectsList)

# How-to setup and run 3D Slicer on an AWS cloud server


## Key Investigators

- Rudolf Bumm (KSGR)
- Steve Pieper (Isomics) 
- Gang Fu (AWS)
- Qing Liu (AWS)

# Project Description

How-to setup and run 3D Slicer on an AWS cloud server

## Objective

For this workshop, we want to set up a 3D Slicer EC2 AWS cloud instance that can be scaled based on hardware needs.  

[All necessary steps are documented here](./HowToSetupAWSEC2Server.md).  

## Approach and Plan

A CloudFormation template was developled to

Install the latest NVIDIA drivers
Install git
Install MONAILabel
Install TotalSegmentator
Install lungmask
Download the 3D Slicer stable installer
Install Firefox
Install and connect an S3 bucket

A mechanism how to share result data between a working group will be discussed, with the option to install a 3dviewer.net server instance or using a S3 bucket. 

The speed of general system setup, up- and downscaling as well as running costs will be evaluated.

## Progress and Next Steps

# Illustrations

![image](https://user-images.githubusercontent.com/18140094/211152360-f6e0d66b-aa84-4109-86d5-eedf404fd528.png)

Fig. 1 Raspberry 4 Model B running 3D Slicer on EC2 instance in Chromium browser


# Background and References

