Back to [Projects List](../../README.md#ProjectsList)

# Remote Control for Plus Server Launcher

## Key Investigators

- Kyle Sunderland (Queen's University, Canada)
- Andras Lasso (Queen's University, Canada)

# Project Description

## Objective

1. Develop a framework to send commands to the Plus Server Launcher using OpenIGTLink
1. Should be able to start and stop servers, as well as pass config files
1. Store server states and config files in Slicer so that servers can be started remotely when the scene is loaded

## Approach and Plan

1. Use the updated version of OpenIGTLInkIF using OpenIGTLinkIO to send commands to the Plus Server Launcher
1. Add an interface to control servers to PlusRemote in SlicerIGT
1. Implement MRML nodes within SlicerIGT to save server launcher connections, and to start servers automatically when the scene is loaded

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [Source code](https://github.com/Sunderlandkyl/PlusApp)
