Back to [Projects List](../../README.md#ProjectsList)

# Compressed Video Saving and Loading for Sequences

## Key Investigators

- Longquan Chen (Brigham and Women's Hospital)
- Kyle Sunderland (Perk Lab)
- Andras Lasso (Perk Lab)
- Étienne Léger (Concordia University)
- Junichi	Tokuda (Brigham and Women's Hospital)

# Project Description
The Video streaming saving module Sequence. [Video Streaming in Sequence](https://drive.google.com/open?id=1gCdVS6aRlg__4KuaoDLK4HqSbAFGoZ4d)

A 5 minutes HD video without compression will be around 10GB. VP9, H264, HEVC codecs are available for video compression and video streaming.

## Objective

1. Implement and test the saving and loading of compressed video files using the Sequences module.
2. Should be able to:
    - Store video Sequences in memory using a compressed video format
    - Save video Sequences to files in a compressed video format
    - Load compressed video files into Sequences

## Approach and Plan

1. Test the currently implemented version.
1. Fix bugs and implement features as necessary.
1. Integrate these changes into the master branch of Sequences.

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

- An existing version of this feature has already been implemented [here](https://github.com/leochan2009/Sequences/tree/BitStreamForVideo).
- Need to test the existing method to see if it still works, and determine if any changes need to be made.

The work finished in the project week
- A new vtkBitStreamMRMLNode is created for displaying video data, the most recent key frame and current frame are stored in this node.
- A new vtkMRMLBitStreamSequenceStorageNode is created for write and read bitstream sequence data in Slicer.
- Video can be replayed at any time point in the Sequence browsing widget. The related key frame will be found and decoded So the current frame can be showed correctly.
- Compressed video data are saved in a binary file, and can be reloaded into Slicer correctly.
- Demo Video [IPad real time video](https://drive.google.com/open?id=1WUel7oUq8ndm2i-7pMZGIdSIh0Qak9XY), lossy compression, frame rate 30 FPS, compressed data only 1.7% of the original data.
- Added support for AV1 codec in OpenIGTLink

Next steps
- Clean the code, merge branch into upstream, make the new feature in Slicer nightly build

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

<!-- ![Description of picture](Example2.jpg) -->
<!-- ![Some more images](Example2.jpg) -->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [OpenIGTLinkIF module Source Code](https://github.com/openigtlink/OpenIGTLinkIF/tree/IGTLIOFullIntegration)
- [Sequence module Source Code](https://github.com/leochan2009/Sequences/tree/BitStreamForVideo)
- [Ipad for image-guided neurosurgery](http://digital-library.theiet.org/content/journals/10.1049/htl.2017.0062?crawler=true&mimetype=application/pdf&tags=noindex)
<!-- Documentation: https://link.to.docs -->
<!-- Test data: https://link.to.test.data -->
