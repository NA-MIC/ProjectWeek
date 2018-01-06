Back to [Projects List](../../README.md#ProjectsList)

# PyRadiomics Models

## Key Investigators

 - [Joost van Griethuysen](https://github.com/JoostJM) <sup>1, 3, 4</sup>
 - [Andriy Fedorov](https://github.com/fedorov) <sup>2</sup>
 - [Nicole Aucoin](https://github.com/naucoin) <sup>2</sup>
 - [Jean-Christophe Fillion-Robin](https://github.com/jcfr) <sup>5</sup>
 - [Ahmed Hosny](https://github.com/ahmedhosny) <sup>1</sup>
 - [Steve Pieper](https://github.com/pieper) <sup>6</sup>
 - [Hugo Aerts (PI)](https://github.com/hugoaerts) <sup>1, 2</sup>
 
<sup>1</sup> Department of Radiation Oncology, Dana-Farber Cancer Institute, Brigham and Women's Hospital, Harvard Medical -School, Boston, MA,USA.<br>
<sup>2</sup> Department of Radiology, Brigham and Women's Hospital, Harvard Medical School, Boston, MA, USA.
<sup>3</sup> Department of Radiology, Netherlands Cancer Institute, Amsterdam, The Netherlands 
<sup>4</sup >GROW-School for Oncology and Developmental Biology, Maastricht University Medical Center, Maastricht, The Netherlands.
<sup>5</sup> Kitware, Inc.
<sup>6</sup> Isomics, Inc.

# Project Description

## Objective

1. Develop framework to easily apply and share radiomic models using PyRadiomics and it's 3D slicer extension SlicerRadiomics.
2. In addition to the current lesion-based extraction, add a voxel-based extraction.

## Approach and Plan

Objective #1

1. Develop configuration file to store a radiomic model.
2. Add a pyradiomics module or a separate github python repository that can read/write the config file and use radiomics to apply it.
3. Add commandline interface to use new functionality.
4. Develop new Slicer module to interface with this new pyradiomics module to make this new functionality directly available in slicer.

Objective #2

4. Update radiomics base module to allow voxel-based extraction
5. Add new feature extractor module to provide interface for voxel-based extraction
6. Add Commandline interface for voxel based extraction
7. Add examples (settings, usage) to show new functionality

## Progress and Next Steps

<!--Describe progress and next steps in a few bullet points as you are making progress.-->

# Illustrations

<!--Add pictures and links to videos that demonstrate what has been accomplished.-->

![Description of picture](Example2.jpg)

![Some more images](Example2.jpg)

# Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data.-->

- [PyRadiomics Source Code](https://github.com/Radiomics/pyradiomics)
- [SlicerRadiomics Source Code](https://github.com/Radiomics/SlicerRadiomics)
- [Documentation](http://pyradiomics.readthedocs.io)
- PyRadiomics Article: [Computational Radiomics System to Decode the Radiographic Phenotype](http://cancerres.aacrjournals.org/content/77/21/e104)
