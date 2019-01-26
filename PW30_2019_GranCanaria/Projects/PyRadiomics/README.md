Back to [Projects List](../../README.md#ProjectsList)

# PyRadiomics update and revision of C extensions

## Key Investigators

- Joost van Griethuysen (The Netherlands Cancer Institute)
- Steve Pieper (Isomics)
- Andrey Fedorov (BWH)
- Hugo Aerts (Dana Farber)

# Project Description

This project aims to develop and maintain the open source software PyRadiomics, which provides easy to use Radiomic feature extraction tools coded in Python.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Update the C-Extensions to allow for N-dimensional input (image/mask). Together with updates to the python code, this is to make PyRadiomics more suitable to work with e.g. 2D input (instead of forced 3D input)
1. Investigate possibility of integration with ITK. 
1. Update documentation and command line interface for voxel-based extraction. Though already part of the PyRadiomics code, voxel based extraction can currently only be used via Python scripts.

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Replace nested loop per dimension by a dimension less single iterator over voxels. Update input checks to allow N-dimensional input.
1. Talk to developers who have worked with ITK. Review the overlap between PyRadiomics and [ITK Texture Features](https://github.com/InsightSoftwareConsortium/ITKTextureFeatures)
1. Write a command line interface similar to the interface for segment-based extraction. Use output folder instead of file to store results (each feature will be a image file (e.g. .nrrd or .nii.gz))

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE. If there are specific steps that you could not complete then you can describe them here, too. -->

1. Nothing yet...

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

<!-- If you developed any software, include link to the source code repository. If possible, also add links to sample data, and to any relevant publications. -->

- [PyRadiomics Source Code](https://github.com/Radiomics/pyradiomics)
- [SlicerRadiomics Source Code](https://github.com/Radiomics/SlicerRadiomics)
- [Documentation](http://pyradiomics.readthedocs.io)
- PyRadiomics Article: [Computational Radiomics System to Decode the Radiographic Phenotype](http://cancerres.aacrjournals.org/content/77/21/e104)

Other related references:
* Image biomarker standardisation initiative: https://arxiv.org/abs/1612.07003
* Radiomics Ontology: http://www.radiomics.org/RO/01000, http://bioportal.bioontology.org/ontologies/RO
