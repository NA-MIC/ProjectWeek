Back to [Projects List](../../README.md#ProjectsList)

# Whitematteranalysis To Python3

## Key Investigators

* Scott Lill (Univestiy of Sydney, Harvard Medical School)
* Steve Pieper (Harvard Medical School)
* Sandy Wells (Harvard Medical School)
* Yang Song (University of New South Wales)
* Tom Cai (University of Sydney)
* Fan Zhang (Harvard Medical School)
* Lauren O'Donnell (Harvard Medical School)

# Project Description

Whitematteranalysis is a python pipeline for peforming fibre processing and clustering. The project aims to upgrade this package, porting it to python3, adding a comprehensive suite of regression tests and porting it into 3D Slicer. This will make the pipeline easier to use, maintain and extend, all of which are beneficial for applicaple dMRI workflows.

## Objective

1. Objective A. Port the codebase to python3, adding regression tests to ensure consistancy.
1. Objective B. Bundle the pipleine into 3D Slicer, adding a qt based GUI as an alternative to the CLI interface
1. Objective C. Add regression tests for existing and added functionality.

## Approach and Plan

1. Test and iterate the python version conversion
1. Explore options for running python externally to 3D slicer to allow the porting of required dependenceis.
1. Document functionality to ensure coverage for the testing suite

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Transisted codebase into python3 syntactically with automatred upgrading
2. Manual review of codebase to fix error in the automatic review
3. Sanity testing of entire pipeline - running through with both python 2 and 3 for consistancy within a certain tolerance, due to stochasitic functionality.
4. Fixing errors caused by library changes, revealed by sanity testing.
4. Testing with controlled stochasticity via a python testing environment. Changes also applied to python2, to comparisions.
5. Ensuring protability in serilization format. Settled on providing backwards compatability of files serialized under python2
by making the python3 code able to read python2 or python3 objects, but only support writing python3. This will shift serilaised objects towards python3 standards and facilitate eventually dropping python2 support.
6. Wrote a script for bundling whitematteranalysis (WMA) in it's own python environment, seperate from the system python or Slicer python. This is necessary for porting WMA to Slicer, as it uses dependancies unsupported by Slicer's python and the system python not under the control of Slicer and therefore unreliable. The next step of writing a GUI extension in Slicer was not completed.

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Some more images](Example2.jpg)
-->

[Clustering done under python3](view_left.jpg)

# Background and References

Github Links
Upgrade to python3 branch - https://github.com/ScLill/whitematteranalysis/tree/2to3
Testing branch - https://github.com/ScLill/whitematteranalysis/tree/2test

Reference
Documentation for original project - https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md
