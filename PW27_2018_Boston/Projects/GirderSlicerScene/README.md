Back to [Projects List](../../README.md#ProjectsList)

# Uploading and Downloading a Scene from Slicer to Girder

## Key Investigators

- Michael Grauer - (Kitware, Inc. @mgrauer)
- Tamas Ungi - (Perk Lab @ungi)
- Jean-Christophe Fillion-Robin - (Kitware, Inc. @jcfr)
- Pierre Assemat - (Kitware, Inc. @pierre.assemat@kitware.com)

# Project Description

This will be a mini-project to upload and download a scene from Slicer to a Girder instance using the Girder API.

As mgrauer will only be at project week Monday and Tuesday, this will have to start on those days.

## Objective

1. Provide an example of calling the Girder API from Slicer

## Approach and Plan

1. Use the Girder server created as an example for the project week
2. Install girder-client package for Slicer Python
3. Add a Slicer module that saves the scene and uploads the scene file to the Girder server

## Progress and Next Steps

1. girder-client is currently not part of Slicer's Python, but can be installed, see [this guide](https://github.com/ungi/SlicerGirderExample/wiki)
2. [This module](https://github.com/ungi/SlicerGirderExample) saves current Slicer scene and uploads it to the example Girder (ask API key from @mgrauer or [install your own Girder](https://girder.readthedocs.io/en/latest/installation.html))

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->
![image](https://raw.githubusercontent.com/Pierre-Assemat/Slicer-Project-Week-2018/b48b5047d849c9582b170ec53cf0f905a838853d/Screenshot-2018-1-11%20Girder%20-%20REST%20API%20Documentation.png)

# Background and References

- [Girder documentation](https://girder.readthedocs.io/en/latest/index.html)
