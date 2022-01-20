Back to [Projects List](../../README.md#ProjectsList)

# Spine Segmentation

## Key Investigators

- Ron Alkalay (Beth Isreal Deaconess, Boston)
- Steve Pieper (Isomics)
- Andres Diaz-Pinto (KCL)
- Juan Ruiz (Ebatinca, ULPGC)
- YOU

# Project Description

Investigate and implement methods to segment the human spine from CT scans.  See [last Project Week's page for background](https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SpineSegmentation/).

## Objective

1. Ideal segmentation will independently segment and label the vertebral bodies.
2. We want the system to integrate with Slicer's segmentation infrastructure.
3. We think a deep learning approach using MONAILabel will be useful for this.

## Approach and Plan

1. Learn as much as possible about MONAILabel
2. Investigate [VerSe](https://arxiv.org/abs/2001.09193) and if possible port it to Slicer/MONAI
3. Figure out if/how we can use spine CTs from IDC for training.

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Held many productive discussions and worked on training with the VerSe public data
1. Exchanged notes with the other MONAI Label projects
1. Installing MONAI Label at BIDMC machines to train on cadeveric and patient spine scans
2. Plan to make single-vertebra models for faster training of high resolution models (tractable on smaller GPU memory footprint)

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
# Current effort
![image](https://user-images.githubusercontent.com/126077/150421004-2185ad15-02a1-47ba-be09-45f4921e6741.png)
![image](https://user-images.githubusercontent.com/126077/150421056-48c5cb5b-a328-4142-823a-8d8831efccd8.png)



# Initial effort
![image](https://user-images.githubusercontent.com/126077/149805728-25491bc0-f2ea-4799-84b3-3289f58e4f8f.png)
![image](https://user-images.githubusercontent.com/126077/149805758-ed6f30da-2817-47fa-ad04-eedb10c5a9e8.png)


# Background and References

* https://github.com/anjany/verse
* https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SpineSegmentation/
