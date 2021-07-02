Back to [Projects List](../../README.md#ProjectsList)

Loading Large Microscopy Data in Slicer

## Key Investigators

- Sindhura Thirumal (Queen's University)
- Steve Pieper (Isomics)
- Tina Kapur (BWH)

# Project Description

We've developed a module in Slicer - TITAN - that is meant to be an end-to-end pipeline of processing and analyzing imaging mass cytometry data. TITAN allows the user to
visualize the different protein channels in the tissue, segment the individual cells in the tissue, and create some simple analysis plots of the data. Currently, user has to export
the raw file from the cytometer into TIFF files using an external software in order to use TITAN. However, we would like to use the raw text files directly with Slicer instead,
in order to eliminate the need for any external software.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Be able to import large text files into Slicer without causing Slicer to become unresponsive
2. Update functions in TITAN to work with the text file rather than TIFF images

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Implement a custom reader to deal with these text files


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Added button to module that opens the user's file explorer for them to select the text file(s) to be imported
1. Doing this just points to the file's location on the computer rather than opening the file in Slicer (which is what slows it down)
1. Data from the files are obtained by parsing through each line and generating the corresponding image arrays, which are then used to create new volume nodes

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->
Loading text files
![load text files box](https://user-images.githubusercontent.com/21988487/124183446-3daaab00-da86-11eb-9de0-05010474ebe1.PNG)

Result of generated image from text file
![load text files p2](https://user-images.githubusercontent.com/21988487/124183494-4ef3b780-da86-11eb-81ea-cef6eb9ae278.PNG)

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->
