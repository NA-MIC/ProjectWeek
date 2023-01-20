Back to [Projects List](../../README.md#ProjectsList)

# DICOM Segmentation Optimization

## Key Investigators

- Steve Pieper (Isomics, Inc)
- Andrey Fedorov (BWH)
- Andras Lasso (Queens)
- Marco Nolden (DKFZ)
- Hans Meine (MeVis)
- Alireza Sedghi (Radical)
- Erik Ziegler (Yunu)
- Markus Hermann (Roche)
- Chris Bridge (MGH)
- David Clunie (PixelMed Publishing)

# Project Description

Discuss our experiences and thoughts on the DICOM SEG standard.

## Objective

Compare notes, benchmarks, and experience with interoperability and performance of DICOM SEG instances across platforms.
Evaluate the extent to which any observed performance issues are inherent in the format or simply inefficient implementations.
Consider proposals to improve the standard to address any inherent issues.

## Approach and Plan

1. Collate experiences from any investigations and benchmarks to date
2. Meet at project week with those on site involving remote participants as possible
3. Add notes here about results and plans for any follow up proposals to add representations to the standard

## Progress and Next Steps


# Illustrations

# Background and References

The DICOM SEG standard has been around for several years and has been implemented as part of several tools in various languages:
* [dcmqi](https://github.com/QIICR/dcmqi) in C++ uses [DCMTK]([url](https://dicom.offis.de/dcmtk.php.en)) and provides support for SEG read/write through [the Quantitative Reporting extension](https://github.com/QIICR/QuantitativeReporting) to 3D Slicer
* [dcmjs](https://github.com/dcmjs-org/dcmjs) supports read/write of SEG in javascript for use in [OHIF](https://ohif.org/)
* [highdicom](https://github.com/ImagingDataCommons/highdicom) supports read/write of SEG in python
* (others - please add to this list)

While interoperability has generally been good, performance of these SEG implementation has in general been orders of magnitude slower
than research formats (e.g. nii.gz, nrrd, or seg.nrrd) at supporting segmentation use cases such as using segmentation data for machine
learning.  For example, [this notebook](https://colab.research.google.com/drive/1ZLqJwDIO1XKnnjOzClkSq8RIawm3sp9M) shows that decoding a
TotalSegmentator result from DICOM SEG with approximately 100 segments can take several minutes and consume very large amounts of memory
for a segmentation that takes less than a second to read from a research format.

We are interested in how the benefits of DICOM (standardized encoding, rich metadata, coded concepts, etc) can coexist with efficient
read-write performance for real-world use cases.
