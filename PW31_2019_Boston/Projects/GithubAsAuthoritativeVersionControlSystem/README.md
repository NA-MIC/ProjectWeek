Back to [Projects List](../../README.md#ProjectsList)

# Transition to GitHub as authoritative version control system

## Key Investigators

- Jean-Christophe Fillion-Robin (Kitware, Inc.)
- Andras Lasso (Queen's University)
- Steve Pieper (Isomics, Inc.)

# Project Description

<!-- Add a short paragraph describing the project. -->

Work toward finalizing the conversion from

`Slicer SVN repository mirror mirrored on GitHub`

to

`GitHub only repository`

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Remove all large binary data from current Slicer source version and filter history removing large data from past commits and restore authorship
1. Objective B. Document how developers can upload binary data, and update release process as needed. (based on ITK great documentation)
1. Objective C. Publish updated repository

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. See plan documented on the wiki Labs page. See https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Describe specific steps you **have actually done**.
1. ...
1. ...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

* ITK documentation
  * [ITK Data](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/Data.md)
  * [Uploading binary data in ITK](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/UploadBinaryData.md)
* [CMake ExternalData: Using Large Files with Distributed Version Control](https://blog.kitware.com/cmake-externaldata-using-large-files-with-distributed-version-control/)
* [PR #1158: Reduce source tree size downloading test data from 114MB to 74MB (35% decrease)](https://github.com/Slicer/Slicer/pull/1158)
* [Slicer Wiki: Labs](https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit)
* git_list_largest_file_from_history
  * [git_list_largest_file_from_history.sh](https://gist.github.com/jcfr/4348af13d2c8931daeab4ff9ab73e14b)
  * [slicer_git_history_350_largest_files.txt](https://gist.github.com/jcfr/93fe51974d9db8ef55a6d3172c1de68d)
* [02_Update_Slicer_CLI_buildsystem_to_download_test_data_from_midas.ipynb](https://github.com/jcfr/jupyter-notebooks/blob/master/02_Update_Slicer_CLI_buildsystem_to_download_test_data_from_midas.ipynb)
