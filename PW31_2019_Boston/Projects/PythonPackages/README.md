Back to [Projects List](../../README.md#ProjectsList)

# Python Package Management for Slicer Extensions

## Key Investigators

- Sam Horvath (Kitware)
- Jean Christophe Fillion-Robin (Kitware)
- Steve Pieper (Isomics)
- Andras Lasso (Queen's University)

# Project Description

This project will focus on improving the python package management in Slicer (i.e. pip install)

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

The objective is to have a consistent interface / process for installing patyhon packages across Slicer (extensions and in the python interactor)



## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->
1. Create a slicer.util.pip function (or equivalent architecture) for accessing pip install from scripts or the interactor
  * Investigate use of virtual environments in Slicer
2. Extension python package automatic install
  * Post-install packages using a hook for requirements.txt
3. Document experience installing and using various python packages in Slicer
  * which ones work well with no problems
  * what properties of some packages lead to problems (e.g. conflicting dependencies)


## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1.  Andras has already implemented the slicer.util.pip_install()
2.  Discussed plans for python package management during a dedicated breakout session
3.  We will be continuing with the plan to pip install packages after extension install, not during the build process
4.  We need to look into blacklisting packages though pip


# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

### Discourse Dicussions
  * [Automatic Install of Python Packages](https://discourse.slicer.org/t/automatic-install-of-python-packages/7078)
  * [Python3 Switch and Package Install](https://discourse.slicer.org/t/python3-switch-and-python-package-install/6534)
  * [Proper way to install Python Packages](https://discourse.slicer.org/t/proper-way-to-automatically-install-external-python-modules/2559)
