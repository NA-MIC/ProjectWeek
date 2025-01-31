Back to [Projects List](../../README.md#ProjectsList)

# Gynecological Brachytherapy Needle Segmentation Deployment

## Key Investigators

- Paolo Zaffino (Magna Graecia University, Catanzaro, Italy)
- Tina Kapur (Brigham and Women’s Hospital and Harvard Medical School, USA)
- Maria Francesca Spadea (Magna Graecia University, Catanzaro, Italy)

## Participating remotely
- Guillaume Pernelle
- Alireza Mehrtash

# Project Description

We developed a fully automatic, AI based algorithm to segment brachyterapy neeedles from intraoperative MRI images.
Since, we want to make it usable from the 3D Slicer users in a simple and efficient manner, we would like to deploy our algorithm by using DeepInfer plugin.

## Objective

1. Deploy the developed algorithm


## Approach and Plan

1. Learn about DeepInfer plugin and Docker system
1. Deploy the entire workflow

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->
1. A docker container containing the code and the models has been created for a GPU based prediction.
1. The docker has been exposed via DeepInfer Slicer extension
1. We are evaluating the possibility to expose the service also via Tomaat extension

1. Next step is to upload the container into the cloud

# Illustrations

Automatic segmentation example:

<p align="center">
  <img src="https://raw.githubusercontent.com/NA-MIC/ProjectWeek/master/PW28_2018_GranCanaria/Projects/NeedleSegmentationDeployment/GYN%20needles%20example.jpg"/>
</p>

<p align="center">
  <img src="https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/NeedleSegmentationDeployment/all30_s.gif?raw=true"/>
</p>

The docker exposed via DeepInfer extension
<p align="center">
  <img src="https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/NeedleSegmentationDeployment/local%20docker%20GYN%20needles.png?raw=true"/>
</p>

# Background and References

- [Needle finder website](http://needlefinder.org)
- [Model-based Catheter Segmentation in MRI-images](https://arxiv.org/abs/1705.06712)
- [PW 25](https://na-mic.org/wiki/Project_Week_25/NeedleSegmentation)
- [2017 Winter PW](https://na-mic.org/wiki/2017_Winter_Project_Week/Needle_Segmentation_from_MRI)
